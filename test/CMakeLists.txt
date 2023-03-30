include_directories(${LIBRARY_INCLUDE_DIR} .)

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
