#!/usr/bin/env python

import sys
from os import path

if __name__ == '__main__':

    # This is a little gross but we need the directory containing the brew_view package on the sys path
    sys.path.append(path.abspath(path.join(path.abspath(__file__), '..', '..')))

    from beer_garden.brew_view.__main__ import main
    sys.exit(main())
