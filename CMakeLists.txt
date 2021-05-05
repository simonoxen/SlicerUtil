cmake_minimum_required(VERSION 3.13.4)

project(SlicerUtil)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerUtil")
set(EXTENSION_CATEGORY "Examples")
set(EXTENSION_CONTRIBUTORS "Simon Oxenford (Netstim Berlin)")
set(EXTENSION_DESCRIPTION "Extension used for testing modules")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/SlicerUtil.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/SlicerUtil/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a list or "NA" if no dependencies

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(RootMeanSquare)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
