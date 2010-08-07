import unittest
from extractor import Extractor 
from libs.mock import Mock

class testExtractor(unittest.TestCase):
    def testMatchConStr(self):
        """
            Extract the connectionstring from the xmlnode
        """

        xmlline = '<add key="umbracoDbDSN" value="server=localhost;database=projects;user id=projects;password=1234;datalayer=MySql" />'
        #Find out how to makes this work. Need to adjust regex
        #xmlline2 = '<add value="server=localhost;database=projects;user id=projects;password=1234;datalayer=MySql" key="umbracoDbDSN" />'
                  
        badXmlline = '<add key="umbracoPath" value="~/umbraco" />'
        connStrResult = "server=localhost;database=projects;user id=projects;password=1234;datalayer=MySql"
        m = Extractor().matchConStr
        self.assertEqual( m(xmlline), connStrResult ) 
        #self.assertEqual( m(xmlline2), connStrResult ) 

    def testFindConStr(self):
        """
            For this test to pass you need the web.config file in
            testfiles/web.config
        """
        f = Extractor().findConStr
        connStrResult = "server=localhost;database=projects;user id=projects;password=1234;datalayer=MySql"

        self.assertRaises(IOError, f, 'test')
        self.assertEqual(f('testfiles/web.config'), connStrResult)
    
    def testBuildConSettings(self):
        """
            turns the connectionstring into a dictionary
        """
        constr = 'name=geert;Age=28;sex=ohyeah'
        result = Extractor().buildConSettings(constr)

        self.assertEqual(result['name'], 'geert')
        self.assertEqual(result['age'], '28')
        self.assertEqual(result['sex'], 'ohyeah')

if __name__ == '__main__':
    unittest.main()
