from customexceptions import ArgsException
class Helpers(object):
    def validateArgsLen(self, args, length):
        if len(args) != length:
            exceptionMsg = 'Was expecting {0} arguments but got {1}'.format( length, len(args) )
            raise ArgsException, exceptionMsg
    
    def getWebConfigPath(self, args):
        """1st argument should be the path to the web.config"""

        try:
            path = args[0]
        except:
            raise ArgsException, 'Web.config argument was missing'
        
        if not 'web.config' in path.lower():
            raise ArgsException, 'First argument should be the path to the web.config'
    
        return path 
    
    def getDumpFilePath(self, args):
        """2nd argument should be the path to the dump file."""
    
        try:
             path = args[1]
        except:
            raise ArgsException, 'Second argument (dump file) was not found'
        
        return path 
    
    def getApp(self, args):
        """3rd argument should be the application to create the dump file. Don't
        check for mysqldump cause might support other applications in future."""
    
        try:
             return args[2]
        except:
            raise ArgsException, '3rd argument should be the application(path) for creating the sql backup'
    
