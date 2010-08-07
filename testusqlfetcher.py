from customexceptions import ArgsException
from libs.mock import Mock
from helpers import Helpers
from extractor import Extractor
from commander import Commander

import usqlfetcher
import unittest

class Testusqlfetcher(unittest.TestCase):
    def testSuperCreateDumpCommand(self):
        helpers = Helpers()
        commander = Commander()
        extractor = Extractor()

        helpers.getWebConfigPath = Mock()
        helpers.getDumpFilesPath = Mock()
        helpers.getApp = Mock()

        helpers.getWebConfigPath.return_value = 'testfiles/web.config'
        helpers.getDumpFilesPath.return_value = 'db.sql'
        helpers.getApp.return_value = 'mysql.exe'
        
        extractor.getConSettings = Mock()
        extractor.getConSettings.return_value = { 'server': 'localhost',
                                                  'user id' :  'geert',
                                                  'database' : 'projects',
                                                  'datalayer' : 'mysql',
                                                  'password': 'neverfails' }

        args = ['path/web.config', 'path/.sql', 'path/mysql.exe']
        result = usqlfetcher.superCreateDumpCommand(args, commander, helpers, extractor) 
        
        self.assertEqual(result, 'mysql.exe -ugeert -pneverfails -hlocalhost projects')

if __name__ == '__main__':
    unittest.main()
