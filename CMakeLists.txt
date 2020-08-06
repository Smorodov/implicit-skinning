cmake_minimum_required(VERSION 2.8)
set (CMAKE_CXX_STANDARD 14)
project(minimal_hand)

set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/build)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})

set(CMAKE_C_FLAGS "/EHsc")
set(CMAKE_CXX_FLAGS "/EHsc")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /bigobj")
add_subdirectory(glfw)
add_subdirectory(glew)

SET(CMAKE_CXX_FLAGS_DEBUG  "-MDd -Zi -Ob0 -Od -RTC1  -_Debug") 

FIND_PACKAGE(OpenGL)
INCLUDE_DIRECTORIES("glm")
INCLUDE_DIRECTORIES("OpenMesh-8.1/src/OpenMesh/Core")
IF ( MSVC )
  SET(M_LIB)
ELSE ( MSVC )
  find_library(M_LIB m)
ENDIF ( MSVC )

INCLUDE_DIRECTORIES("glew/include")
INCLUDE_DIRECTORIES("glfw/include")
INCLUDE_DIRECTORIES("glm")

INCLUDE_DIRECTORIES("OpenMesh/Core")
INCLUDE_DIRECTORIES("OpenMesh/Core/Mesh")
INCLUDE_DIRECTORIES("OpenMesh/Core/Utils")
INCLUDE_DIRECTORIES("OpenMesh/Core/Templates")
INCLUDE_DIRECTORIES("OpenMesh/Core/IO/reader")
INCLUDE_DIRECTORIES("OpenMesh/Core/IO/importer")
INCLUDE_DIRECTORIES("OpenMesh/Core/Geometry")
INCLUDE_DIRECTORIES("OpenMesh/Core/Mesh/gen")
INCLUDE_DIRECTORIES("OpenMesh/Core/System")
INCLUDE_DIRECTORIES("OpenMesh/Core/IO/exporter")
INCLUDE_DIRECTORIES("OpenMesh/Core/IO")
INCLUDE_DIRECTORIES("OpenMesh/Core/IO/writer")

set( open_mesh_headers 
"OpenMesh/Core/Utils/vector_traits.hh"
"OpenMesh/Core/System/compiler.hh"
"OpenMesh/Core/IO/reader/OFFReader.hh"
"OpenMesh/Core/IO/importer/BaseImporter.hh"
"OpenMesh/Core/IO/writer/OBJWriter.hh"
"OpenMesh/Core/Mesh/BaseKernel.hh"
"OpenMesh/Core/IO/reader/OMReader.hh"
"OpenMesh/Core/Mesh/Handles.hh"
"OpenMesh/Core/IO/IOManager.hh"
"OpenMesh/Core/Mesh/TriConnectivity.hh"
"OpenMesh/Core/IO/reader/BaseReader.hh"
"OpenMesh/Core/Mesh/TriMeshT_impl.hh"
"OpenMesh/Core/Mesh/gen/iterators_template.hh"
"OpenMesh/Core/IO/OMFormatT_impl.hh"
"OpenMesh/Core/Utils/BaseProperty.hh"
"OpenMesh/Core/Mesh/Status.hh"
"OpenMesh/Core/Utils/Property.hh"
"OpenMesh/Core/Utils/RandomNumberGenerator.hh"
"OpenMesh/Core/IO/OFFFormat.hh"
"OpenMesh/Core/Templates/bla.hh"
"OpenMesh/Core/Mesh/Attributes.hh"
"OpenMesh/Core/Mesh/PolyConnectivity_inline_impl.hh"
"OpenMesh/Core/IO/writer/OFFWriter.hh"
"OpenMesh/Core/Geometry/NormalConeT_impl.hh"
"OpenMesh/Core/Utils/SingletonT.hh"
"OpenMesh/Core/IO/writer/BaseWriter.hh"
"OpenMesh/Core/Mesh/gen/footer.hh"
"OpenMesh/Core/Utils/PropertyContainer.hh"
"OpenMesh/Core/Utils/SingletonT_impl.hh"
"OpenMesh/Core/IO/SR_binary_spec.hh"
"OpenMesh/Core/Mesh/SmartRange.hh"
"OpenMesh/Core/Utils/typename.hh"
"OpenMesh/Core/Mesh/PolyMesh_ArrayKernelT.hh"
"OpenMesh/Core/Mesh/Tags.hh"
"OpenMesh/Core/Utils/color_cast.hh"
"OpenMesh/Core/Mesh/BaseMesh.hh"
"OpenMesh/Core/Mesh/TriMesh_ArrayKernelT.hh"
"OpenMesh/Core/System/omstream.hh"
"OpenMesh/Core/IO/writer/PLYWriter.hh"
"OpenMesh/Core/Mesh/Casts.hh"
"OpenMesh/Core/Geometry/VectorT.hh"
"OpenMesh/Core/IO/MeshIO.hh"
"OpenMesh/Core/Mesh/ArrayItems.hh"
"OpenMesh/Core/Mesh/TriMeshT.hh"
"OpenMesh/Core/Utils/PropertyManager.hh"
"OpenMesh/Core/Mesh/PolyMeshT_impl.hh"
"OpenMesh/Core/IO/reader/STLReader.hh"
"OpenMesh/Core/System/config.hh"
"OpenMesh/Core/IO/SR_rbo.hh"
"OpenMesh/Core/IO/SR_types.hh"
"OpenMesh/Core/Utils/vector_cast.hh"
"OpenMesh/Core/IO/BinaryHelper.hh"
"OpenMesh/Core/Mesh/Traits.hh"
"OpenMesh/Core/Mesh/ArrayKernel.hh"
"OpenMesh/Core/Mesh/SmartHandles.hh"
"OpenMesh/Core/System/OpenMeshDLLMacros.hh"
"OpenMesh/Core/Mesh/FinalMeshItemsT.hh"
"OpenMesh/Core/Mesh/DefaultPolyMesh.hh"
"OpenMesh/Core/Geometry/LoopSchemeMaskT.hh"
"OpenMesh/Core/IO/writer/VTKWriter.hh"
"OpenMesh/Core/IO/SR_store.hh"
"OpenMesh/Core/Geometry/Vector11T.hh"
"OpenMesh/Core/Utils/Noncopyable.hh"
"OpenMesh/Core/Geometry/EigenVectorT.hh"
"OpenMesh/Core/Geometry/MathDefs.hh"
"OpenMesh/Core/IO/reader/PLYReader.hh"
"OpenMesh/Core/Mesh/PolyConnectivity.hh"
"OpenMesh/Core/Mesh/gen/circulators_header.hh"
"OpenMesh/Core/Utils/GenProg.hh"
"OpenMesh/Core/IO/Options.hh"
"OpenMesh/Core/IO/OMFormat.hh"
"OpenMesh/Core/Mesh/gen/iterators_header.hh"
"OpenMesh/Core/Mesh/CirculatorsT.hh"
"OpenMesh/Core/Templates/blaT_impl.hh"
"OpenMesh/Core/Mesh/IteratorsT.hh"
"OpenMesh/Core/IO/importer/ImporterT.hh"
"OpenMesh/Core/Geometry/QuadricT.hh"
"OpenMesh/Core/Mesh/gen/circulators_template.hh"
"OpenMesh/Core/Mesh/PolyMeshT.hh"
"OpenMesh/Core/Geometry/Plane3d.hh"
"OpenMesh/Core/Geometry/NormalConeT.hh"
"OpenMesh/Core/Geometry/Config.hh"
"OpenMesh/Core/IO/writer/OMWriter.hh"
"OpenMesh/Core/Utils/AutoPropertyHandleT.hh"
"OpenMesh/Core/Utils/Endian.hh"
"OpenMesh/Core/IO/writer/STLWriter.hh"
"OpenMesh/Core/IO/exporter/BaseExporter.hh"
"OpenMesh/Core/Mesh/ArrayKernelT_impl.hh"
"OpenMesh/Core/Utils/HandleToPropHandle.hh"
"OpenMesh/Core/IO/exporter/ExporterT.hh"
"OpenMesh/Core/IO/reader/OBJReader.hh"
"OpenMesh/Core/IO/SR_binary.hh"
"OpenMesh/Core/IO/StoreRestore.hh"
"OpenMesh/Core/Mesh/DefaultTriMesh.hh"
"OpenMesh/Core/IO/IOInstances.hh"
"OpenMesh/Core/Mesh/AttribKernelT.hh"
"OpenMesh/Core/Geometry/VectorT_inc.hh"
"OpenMesh/Core/System/mostream.hh"
)

set( open_mesh_sources 
"OpenMesh/Core/Utils/Endian.cc"
"OpenMesh/Core/IO/writer/STLWriter.cc"
"OpenMesh/Core/IO/writer/OBJWriter.cc"
"OpenMesh/Core/Utils/RandomNumberGenerator.cc"
"OpenMesh/Core/IO/reader/OFFReader.cc"
"OpenMesh/Core/IO/writer/OFFWriter.cc"
"OpenMesh/Core/Mesh/ArrayKernel.cc"
"OpenMesh/Core/IO/BinaryHelper.cc"
"OpenMesh/Core/Mesh/TriConnectivity.cc"
"OpenMesh/Core/IO/IOManager.cc"
"OpenMesh/Core/IO/writer/VTKWriter.cc"
"OpenMesh/Core/Mesh/SmartHandles.cc"
"OpenMesh/Core/IO/writer/BaseWriter.cc"
"OpenMesh/Core/IO/OMFormat.cc"
"OpenMesh/Core/Utils/BaseProperty.cc"
"OpenMesh/Core/IO/reader/OBJReader.cc"
"OpenMesh/Core/IO/reader/OMReader.cc"
"OpenMesh/Core/IO/reader/BaseReader.cc"
"OpenMesh/Core/IO/reader/STLReader.cc"
"OpenMesh/Core/System/omstream.cc"
"OpenMesh/Core/IO/reader/PLYReader.cc"
"OpenMesh/Core/IO/writer/PLYWriter.cc"
"OpenMesh/Core/Mesh/BaseKernel.cc"
"OpenMesh/Core/IO/writer/OMWriter.cc"
"OpenMesh/Core/Mesh/PolyConnectivity.cc"
)

  add_definitions(
      -D_USE_MATH_DEFINES -DNOMINMAX
      -D_CRT_SECURE_NO_WARNINGS
  )

include_directories("${CMAKE_SOURCE_DIR}")
set(SOURCES
    main/main.cpp
    glew/src/glew.c
    ${open_mesh_sources}
    )

set(HEADERS
	${open_mesh_headers}
    )
SOURCE_GROUP("Source Files" FILES ${SOURCES})
SOURCE_GROUP("Header Files" FILES ${HEADERS})

add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})
target_link_libraries(${PROJECT_NAME} glew glfw opengl32 )
set_target_properties( ${PROJECT_NAME} PROPERTIES  VS_DEBUGGER_WORKING_DIRECTORY "$<TARGET_FILE_DIR:${PROJECT_NAME}>")
set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT ${PROJECT_NAME})
#target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS} zlib freeglut )

#file(COPY ${PROJECT_SOURCE_DIR}/scripts/model DESTINATION ${CMAKE_SOURCE_DIR}/build/Debug)
#file(COPY ${PROJECT_SOURCE_DIR}/scripts/model DESTINATION ${CMAKE_SOURCE_DIR}/build/Release)