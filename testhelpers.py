import unittest
from customexceptions import ArgsException
from helpers import Helpers

class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.Args = [
                     '../externals/web.config',
                     '../output/dump.sql',
                     '../externals/mysqldump.exe'
                    ]

        self.BadArgs = [
                        '../output/dump.sql',
                        '../externals/mysqldump.exe',
                        '../externals/web.config'
                       ]
        
    def testvalidateArgLen(self):
        """
            Args length should match expected length
        """
        args = ['1','2', '3']
        v = Helpers().validateArgsLen
        self.assertRaises(ArgsException, v, args, 2)
    
    def testGetWebConfig(self):
        g = Helpers().getWebConfigPath
        self.assertEqual( g(self.Args), '../externals/web.config' )
        self.assertRaises( ArgsException, g, self.BadArgs )

    def testGetDumpFilePath(self):
        g = Helpers().getDumpFilePath
        self.assertEqual( g(self.Args), '../output/dump.sql' )
    
    def testGetCommandArgument(self):
        g = Helpers().getApp
        self.assertEqual( g(self.Args), '../externals/mysqldump.exe' )
        self.assertRaises( ArgsException, g, ['hihi', 'haha'] )

if __name__ == '__main__':
    unittest.main()
