import pytest
import sys

from ctypes import util

# this problem was supposedly fixed in a newer Python 3.8 release, but after binary installer support expired
# https://github.com/python/cpython/pull/28054
if sys.platform == 'darwin' and sys.version_info[:2] == (3, 8):
    orig_find_library = util.find_library

    def hacked_find_library(*args, **kwargs):
        res = orig_find_library(*args, **kwargs)

        if res is None:
            pytest.xfail("busted find_library on MacOS Python 3.8")

        return res

    util.find_library = hacked_find_library
