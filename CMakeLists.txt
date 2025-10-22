#
# NrrdIO: stand-alone code for basic nrrd functionality
# Copyright (C) 2009--2025  University of Chicago
# Copyright (C) 2005--2008  Gordon Kindlmann
# Copyright (C) 1998--2004  University of Utah
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any
# damages arising from the use of this software.
#
# Permission is granted to anyone to use this software for any
# purpose, including commercial applications, and to alter it and
# redistribute it freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must
#    not claim that you wrote the original software. If you use this
#    software in a product, an acknowledgment in the product
#    documentation would be appreciated but is not required.
#
#   2. Altered source versions must be plainly marked as such, and must
#    not be misrepresented as being the original software.
#
# 3. This notice may not be removed or altered from any source distribution.
#
# CMake Version 3.25 came out November 16, 2022
# https://www.kitware.com/cmake-3-25-0-available-for-download/
# why use 3.25: has nicer syntax for try_compile
cmake_minimum_required(VERSION 3.25...3.31)
project(NrrdIO)
include_regular_expression("^.*.h$")

#
# This CMake file configures the NrrdIO library build.  NrrdIO
# is used by Insight/Code/IO/itkNrrdIO for reading/writing
# "Nearly Raw Raster Data" within the open-source Teem software
# package. See http://teem.sourceforge.net for more information.
#

set(nrrdio_SRCS
    754.c
    accessors.c
    array.c
    arraysNrrd.c
    axis.c
    biffbiff.c
    biffmsg.c
    comment.c
    defaultsNrrd.c
    encoding.c
    encodingAscii.c
    encodingBzip2.c
    encodingGzip.c
    encodingHex.c
    encodingRaw.c
    encodingZRL.c
    endianAir.c
    endianNrrd.c
    enum.c
    enumsNrrd.c
    format.c
    formatEPS.c
    formatNRRD.c
    formatPNG.c
    formatPNM.c
    formatText.c
    formatVTK.c
    gzio.c
    keyvalue.c
    methodsNrrd.c
    miscAir.c
    mop.c
    parseAir.c
    parseNrrd.c
    preamble.c
    read.c
    reorder.c
    sampleIO.c
    sane.c
    simple.c
    string.c
    subset.c
    write.c
)

# Turn on TEEM_BUILD so that the proper dll export def's are
# used on windows builds.
add_definitions(-DTEEM_BUILD=1)

# (TeemV2: TEEM_QNANHIBIT is gone)

# (TeemV2: TEEM_DIO (and dio.c) is gone)

# Possibly turn on usage of zlib compression (requires linking with libz)
# (i.e., programs compiled with ITKNrrdIO must also be compiled with zlib)
add_definitions(-DTEEM_ZLIB=1)

add_library(NrrdIO ${nrrdio_SRCS} )

## These are ITK-specific
#target_link_libraries(NrrdIO ${ITK_ZLIB_LIBRARIES} )
#install_targets(/lib/InsightToolkit ITKNrrdIO)
#install_files(/include/InsightToolkit/Utilities/NrrdIO "(\\.h)$")

