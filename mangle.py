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
#
#  2. Altered source versions must be plainly marked as such, and must
#     not be misrepresented as being the original software.
#
#  3. This notice may not be removed or altered from any source distribution.
#

"""
This prints (to stdout) a header file intended to be included into
source files where there is a concern of name-space collision induced
by linking to two different version of NrrdIO (or NrrdIO and Teem)
"""

import re
import subprocess
import sys

import textwrap


def main():
    """Filters outout of `nm libNrrdIO.a` to produce #define renames"""
    if len(sys.argv) != 2:
        sys.exit('usage: python mangle.py <prefix>')
    prefix = sys.argv[1]

    mac = sys.platform == 'darwin'

    print(
        textwrap.dedent(
            f"""\
        #ifndef __{prefix}_NrrdIO_mangle_h
        #define __{prefix}_NrrdIO_mangle_h

        /*
        This header file mangles all symbols exported from the
        NrrdIO library. It is included in all files while building
        the NrrdIO library.  Due to namespace pollution, no NrrdIO
        headers should be included in .h files in ITK.

        This file was created via the mangle.py script in the
        NrrdIO distribution:

          python mangle.py {prefix} > {prefix}_NrrdIO_mangle.h

        This uses nm to list all text (T), data (D) symbols, as well
        read-only (R) things (seen on Linux) and "other" (S) things
        (seen on Mac).  On Macs, the preceding underscore is removed.

        Also ensures that a few others starting with nrrd are included, and
        prevents variables ending with .N* where N is some number, from inclusion.
        */
        """
        )
    )

    try:
        nm_proc = subprocess.Popen(['nm', 'libNrrdIO.a'], stdout=subprocess.PIPE, text=True)
    except FileNotFoundError:
        sys.exit('Error: `nm` not found in PATH')

    for line in nm_proc.stdout:
        # Skip local numbered variants (e.g. foo.1) or .eh symbols
        if re.search(r'.*\s.*\.[0-9]', line):
            continue
        if line.strip().endswith('.eh'):
            continue

        # Match lines with symbol types of interest
        match = re.search(r'\s[TBDSR]\s', line)
        if match:
            symbol = re.sub(r'.*\s[TBDSR]\s(.*)', r'\1', line).strip()
            if mac and symbol.startswith('_'):
                symbol = symbol[1:]
            print(f'#define {symbol} {prefix}_{symbol}')

    nm_proc.stdout.close()
    nm_proc.wait()

    print(f'#endif  /* __{prefix}_NrrdIO_mangle_h */')


if __name__ == '__main__':
    main()
