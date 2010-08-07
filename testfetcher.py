import unittest
from fetcher import ArgsException, Fetcher
from libs.mock import Mock

class testFetcher(unittest.TestCase):
    def testvalidateArgLen(self):
        """
            Args length should match expected length
        """
        args = ['1','2', '3']
        v = Fetcher().validateArgsLen
        self.assertRaises(ArgsException, v, args, 2)
    
    def testGetWebConfig(self):
        """
            Should return web.config path
        """
        args = ['/test/web.config']
        badargs = ['/test/dump.sql']

        g = Fetcher().getWebConfig
        self.assertEqual(g(args), '/test/web.config')
        self.assertRaises(ArgsException, g, badargs)

    def testGetDumpFile(self):
        """
            Should return dump file path
        """
        args = ['/test/dump.sql']
        badargs = ['/test/web.config']

        g = Fetcher().getDumpFile
        self.assertEqual(g(args), '/test/dump.sql')
        self.assertRaises(ArgsException, g, badargs)

    def testMatchConStr(self):
        """
            Extract the connectionstring from the xmlnode
        """

        xmlline = '<add key="umbracoDbDSN" value="server=localhost;database=projects;user id=projects;password=1234;datalayer=MySql" />'
        #Find out how to makes this work. Need to adjust regex
        #xmlline2 = '<add value="server=localhost;database=projects;user id=projects;password=1234;datalayer=MySql" key="umbracoDbDSN" />'
                  
        badXmlline = '<add key="umbracoPath" value="~/umbraco" />'
        connStrResult = "server=localhost;database=projects;user id=projects;password=1234;datalayer=MySql"
        m = Fetcher().matchConStr
        self.assertEqual( m(xmlline), connStrResult ) 
        #self.assertEqual( m(xmlline2), connStrResult ) 

    def testFindConStr(self):
        """
            For this test to pass you need the web.config file in
            ../Externals/web.config
        """
        f = Fetcher().findConStr
        connStrResult = "server=localhost;database=projects;user id=projects;password=1234;datalayer=MySql"

        self.assertRaises(IOError, f, 'test')
        self.assertEqual(f('../Externals/web.config'), connStrResult)
    
    def testBuildConSettings(self):
        """
            turns the connectionstring into a dictionary
        """
        constr = 'name=geert;Age=28;sex=ohyeah'
        result = Fetcher().buildConSettings(constr)

        self.assertEqual(result['name'], 'geert')
        self.assertEqual(result['age'], '28')
        self.assertEqual(result['sex'], 'ohyeah')

    def testBuildCommand(self):
        conSettings = { 'datalayer': 'mysql' }

        sf = Fetcher()
        sfb = sf.buildCommand
        bMySql = sf.buildMySqlCommand = Mock()

        result = sfb(conSettings, 'dumpfile.sql')
        self.assertEqual(1, bMySql.call_count)
    
    def testBuildMySqlCommand(self):
        conSettings = { 'server'   : 'localhost', 
                        'database' : 'projects', 
                        'user id'  : 'projects', 
                        'password' : '1234', 
                        'datalayer': 'MySql' }
        dumpFile = 'dump.sql'

        b        = Fetcher().buildMySqlCommand
        result   = b(conSettings, dumpFile)
        expected = '-uprojects -p1234 -hlocalhost projects > dump.sql'

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
