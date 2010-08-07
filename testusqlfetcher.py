from customexceptions import ArgsException
import usqlfetcher
import unittest

class Testusqlfetcher(unittest.TestCase):
    def setUp(self):
        self.Args = [
                     '../externals/web.conFig',
                     '../output/dump.sqL',
                     '../externals/mySqldump.exe'
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
        v = usqlfetcher.validateArgsLen
        self.assertRaises(ArgsException, v, args, 2)
    
    def testGetWebConfig(self):
        g = usqlfetcher.getWebConfigPath
        self.assertEqual( g(self.Args), '../externals/web.config' )
        self.assertRaises( ArgsException, g, self.BadArgs )

    def testGetDumpFilePath(self):
        g = usqlfetcher.getDumpFilePath
        self.assertEqual( g(self.Args), '../output/dump.sql' )
        self.assertRaises( ArgsException, g, self.BadArgs )
    
    def testGetCommandArgument(self):
        g = usqlfetcher.getApp
        self.assertEqual( g(self.Args), '../externals/mysqldump.exe' )
        self.assertRaises( ArgsException, g, ['hihi', 'haha'] )

if __name__ == '__main__':
    unittest.main()
