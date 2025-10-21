#!/usr/bin/env python3
#
#  NrrdIO: stand-alone code for basic nrrd functionality
#  Copyright (C) 2009--2025  University of Chicago
#  Copyright (C) 2005--2008  Gordon Kindlmann
#  Copyright (C) 1998--2004  University of Utah
#
#  This software is provided 'as-is', without any express or implied
#  warranty.  In no event will the authors be held liable for any
#  damages arising from the use of this software.
#
#  Permission is granted to anyone to use this software for any
#  purpose, including commercial applications, and to alter it and
#  redistribute it freely, subject to the following restrictions:
#
#  1. The origin of this software must not be misrepresented; you must
#     not claim that you wrote the original software. If you use this
#     software in a product, an acknowledgment in the product
#     documentation would be appreciated but is not required.

"""
This removes a large comment-block at the top of a Teem .c or .h file, by
eliding the lines up to and including a line containing nothing but '*/'
"""

import sys
import re

PRINTING = False
for line in sys.stdin:
    if PRINTING:
        sys.stdout.write(line)
    elif re.match(r'^\*/\s*$', line):
        PRINTING = True
