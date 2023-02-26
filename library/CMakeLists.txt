aux_source_directory(. LIBRARY_SRC_LIST)
add_library(library ${LIBRARY_SRC_LIST})

set(
	LIBRARY_INCLUDE_DIR
	${CMAKE_CURRENT_SOURCE_DIR}
	${ALLOCATOR_INCLUDE_DIR}
	CACHE INTERNAL "LIBRARY_INCLUDE_DIR"
)

add_subdirectory(allocator)