import glob
import os

CONST_STRING = lambda *args: "_".join(args).upper()


class Basic:

    def __init__(self, path):
        self.path = os.path.abspath(path)
        print("Will construct", self.__class__.__name__.upper(), "in", self.path)


class Library(Basic):

    def __construct_cmakelists(self, folder, sub_folder):
        print(folder, sub_folder)
        return "\n".join([
            # "aux_source_directory(. {})".format(CONST_STRING(folder, "src_list")),
            # "add_library({} ${{{}}})\n".format(folder, CONST_STRING(folder, "src_list")),
            # "if (${{{}}})".format(CONST_STRING(folder, "src_list")),
            # "\tadd_library({} ${{{}}})".format(folder, CONST_STRING(folder, "src_list")),
            # "endif()\n",
            "set(",
            "\t{}".format(CONST_STRING(folder, "include_dir")),
            "\t${CMAKE_CURRENT_SOURCE_DIR}",
            *["\t${{{}}}".format(CONST_STRING(f, "include_dir")) for f in sub_folder],
            "\tCACHE INTERNAL \"{}\"".format(CONST_STRING(folder, "include_dir")),
            ")\n",
            *["add_subdirectory({})".format(f) for f in sub_folder],
        ])

    def construct(self, folder=None):
        if folder is None:
            folder = self.path
        with open(os.path.join(folder, "CMakeLists.txt"), 'w') as f:
            f.write(self.__construct_cmakelists(
                os.path.basename(folder),
                [self.construct(file) for file in glob.glob(os.path.join(folder, "*")) if os.path.isdir(file)]
            ))
        return os.path.basename(folder)


class Test(Basic):
    def construct(self):
        with open(os.path.join(self.path, "CMakeLists.txt"), 'w') as f:
            f.write(r"""include_directories(${LIBRARY_INCLUDE_DIR} .)

set(special_chars "[:\\+\\./]")
set(delimiter "_")
string(REGEX REPLACE ${special_chars} ${delimiter} pre ${CMAKE_CURRENT_SOURCE_DIR}/)

file (GLOB_RECURSE files ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)
foreach (file ${files})
    string(REGEX REPLACE ${special_chars} ${delimiter} exe ${file})
    string(REGEX REPLACE "^${pre}(.*)_cpp$" "\\1" exe ${exe})
    add_executable (${exe} ${file})
#    target_link_libraries(${exe} library)
endforeach ()
""")


class Project(Basic):
    def construct(self):
        with open(os.path.join(self.path, "CMakeLists.txt"), 'w') as f:
            f.write(r"""cmake_minimum_required(VERSION 3.23)
set(CMAKE_CXX_STANDARD 11)

project(MY-STL)


add_subdirectory(library)
add_subdirectory(test)
""")


if __name__ == "__main__":
    for Constructor in [Library('library'), Test("test"), Project('.')]:
        Constructor.construct()
