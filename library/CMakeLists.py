import os
import glob

CONST_STRING = lambda *args: "_".join(args).upper()


def construct_cmakelists(folder, sub_folder):
    print(folder,sub_folder)
    return "\n".join([
        "aux_source_directory(. {})".format(CONST_STRING(folder, "src_list")),
        "add_library({} ${{{}}})\n".format(folder, CONST_STRING(folder, "src_list")),
        "set(",
        "\t{}".format(CONST_STRING(folder, "include_dir")),
        "\t${CMAKE_CURRENT_SOURCE_DIR}",
        *["\t${{{}}}".format(CONST_STRING(f, "include_dir")) for f in sub_folder],
        "\tCACHE INTERNAL \"{}\"".format(CONST_STRING(folder, "include_dir")),
        ")\n",
        *["add_subdirectory({})".format(f) for f in sub_folder],
    ])


def view(folder):
    with open(os.path.join(folder, "CMakeLists.txt"), 'w') as f:
        f.write(construct_cmakelists(
            os.path.basename(folder),
            [view(file) for file in glob.glob(os.path.join(folder, "*")) if os.path.isdir(file)]
        ))
    return os.path.basename(folder)


if __name__ == "__main__":
    view(os.path.abspath('.'))
