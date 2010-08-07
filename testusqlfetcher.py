from customexceptions import ArgsException
import usqlfetcher
import unittest
class Testusqlfetcher(unittest.TestCase):
    def testvalidateArgLen(self):
        """
            Args length should match expected length
        """
        args = ['1','2', '3']
        v = usqlfetcher.validateArgsLen
        self.assertRaises(ArgsException, v, args, 2)
    
    def testGetWebConfig(self):
        """
            Should return web.config path
        """
        args = ['/test/web.config']
        badargs = ['/test/dump.sql']
    
        g = usqlfetcher.getWebConfig
        self.assertEqual(g(args), '/test/web.config')
        self.assertRaises(ArgsException, g, badargs)
    
    def testGetDumpFile(self):
        """
            Should return dump file path
        """
        args = ['/test/dump.sql']
        badargs = ['/test/web.config']
    
        g = usqlfetcher.getDumpFile
        self.assertEqual(g(args), '/test/dump.sql')
        self.assertRaises(ArgsException, g, badargs)

if __name__ == '__main__':
    unittest.main()
