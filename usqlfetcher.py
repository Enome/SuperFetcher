from fetcher import Fetcher
from customexceptions import ArgsException
import sys
#Arguments: path/web.config path/dump.sql path/mysqldump.exe

def main():
    args = sys.argv[1:]
    commandandarguments = Fetcher().CommandAndArguments(getWebConfigPath(args), 
                                                        getDumpFilePath(args),
                                                        getApp(args))

    print commandandarguments

def validateArgsLen(args, length):
    if len(args) != length:
        exceptionMsg = 'Was expecting {0} arguments but got {1}'.format( length, len(args) )
        raise ArgsException, exceptionMsg

def getWebConfigPath(args):
    """1st argument should be the path to the web.config"""

    try:
        path = args[0].lower()
    except:
        raise ArgsException, 'Web.config argument was missing'
    
    if not 'web.config' in path:
        raise ArgsException, 'First argument should be the path to the web.config'

    return path 

def getDumpFilePath(args):
    """2nd argument should be the path to the dump file. It should end in .sql
    so it's easier to validate"""

    try:
         path = args[1].lower()
    except:
        raise ArgsException, 'Dump file argument was missing'
    
    if not path.endswith('.sql'):
        raise ArgsException, 'Second argument should be the path to the dump file. Please give it the extension .sql.'

    return path 

def getApp(args):
    """3rd argument should be the application to create the dump file. Don't
    check for mysqldump cause might support other applications in future."""

    try:
         return args[2].lower()
    except:
        raise ArgsException, '3rd argument should be the application(path) for creating the sql backup'
    

def findArgument(match, args):
    arg = ''
    
    for a in args:
        if match in args:
            return a


if __name__ == '__main__':
    main()
