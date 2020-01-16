import os
import sys
import unittest

# Bob Ippolito:
#
# Ok.. the code to find the filename for __getattr__ should look
# something like:
#
# import os
# from macholib.dyld import dyld_find
#
# def find_lib(name):
#      possible = ['Lib'+name+'.dylib', name+'.dylib',
#      name+'.framework/'+name]
#      for dylib in possible:
#          try:
#              return os.path.realpath(dyld_find(dylib))
#          except ValueError:
#              pass
#      raise ValueError, "%s not found" % (name,)
#
# It'll have output like this:
#
#  >>> find_lib('pthread')
# '/usr/Lib/libSystem.B.dylib'
#  >>> find_lib('z')
# '/usr/Lib/libz.1.dylib'
#  >>> find_lib('IOKit')
# '/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit'
#
# -bob

from ctypes.macholib.dyld import dyld_find

def find_lib(name):
    possible = ['Lib'+name+'.dylib', name+'.dylib', name+'.framework/'+name]
    for dylib in possible:
        try:
            return os.path.realpath(dyld_find(dylib))
        except ValueError:
            pass
    raise ValueError("%s not found" % (name,))

class MachOTest(unittest.TestCase):
    @unittest.skipUnless(sys.platform == "darwin", 'OSX-specific test')
    def test_find(self):

        self.assertEqual(find_lib('pthread'),
                             '/usr/Lib/libSystem.B.dylib')

        result = find_lib('z')
        # Issue #21093: dyld default search path includes $HOME/Lib and
        # /usr/local/Lib before /usr/Lib, which caused test failures if
        # a local copy of libz exists in one of them. Now ignore the head
        # of the path.
        self.assertRegex(result, r".*/Lib/libz\..*.*\.dylib")

        self.assertEqual(find_lib('IOKit'),
                             '/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit')

if __name__ == "__main__":
    unittest.main()
