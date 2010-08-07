from fetcher import Fetcher
from customexceptions import ArgsException
import sys
#Arguments: path/web.config path/dump.sql path/mysqldump.exe

def main():
    args = sys.argv[1:]
    validateArgsLen(sys.argv, 15)

def validateArgsLen(args, length):
    if len(args) != length:
        exceptionMsg = 'Was expecting {0} arguments but got {1}'.format( length, len(args) )
        raise ArgsException, exceptionMsg

def getWebConfig(args):
    webConfigPath = ''
    for a in args:
        if 'web.config' in a:
            webConfigPath = a 

    if not webConfigPath:
        raise ArgsException, 'No web.config path found'

    return webConfigPath

def getDumpFile(args):
    dumpFilePath = ''
    for a in args:
        if not 'web.config' in a:
            dumpFilePath = a

    if not dumpFilePath:
        raise ArgsException, 'No dump files path found'

    return dumpFilePath
if __name__ == '__main__':
    main()
