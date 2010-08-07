import unittest
from commander import Commander
from customexceptions import ArgsException
from libs.mock import Mock

class testFetcher(unittest.TestCase):
    def testBuildCommand(self):
        conSettings = { 'datalayer': 'mysql' }

        sf = Commander()
        sfb = sf.buildCommand
        bMySql = sf.buildMySqlCommand = Mock()

        result = sfb(conSettings, 'dumpapp.exe')
        self.assertEqual(1, bMySql.call_count)
    
    def testBuildMySqlCommand(self):
        conSettings = { 'server'   : 'localhost', 
                        'database' : 'projects', 
                        'user id'  : 'projects', 
                        'password' : '1234', 
                        'datalayer': 'MySql' }
        dumpFile = 'dump.sql'
        command = 'dumpapp.exe'

        b        = Commander().buildMySqlCommand
        result   = b(conSettings, command)
        expected = 'dumpapp.exe -uprojects -p1234 -hlocalhost projects'

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
