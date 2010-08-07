from commander import Commander
from customexceptions import ArgsException
from extractor import Extractor
from subprocess import Popen, PIPE
from helpers import Helpers
import sys
import os

#Arguments: path/web.config path/.sql path/mysql.exe
#cmd: mysql --verbose --user=XXXXXXXX --password=XXXXXXXX DB_NAME < /PATH/TO/DUMPFILE.SQL

def main(args):
    commander = Commander()
    helpers = Helpers()
    extractor = Extractor()

    commandandarguments = superCreatePushCommand(args, commander, helpers, extractor)

    dumpfilepath = helpers.getDumpFilePath(args)
    executeCommandAndArguments(commandandarguments, dumpfilepath);

def superCreatePushCommand(args, commander, helpers, extractor):
    """
    this function is super because it combines everything in this project
    to create a command and arguments. Awesome eh?
    """
    webconfigpath = helpers.getWebConfigPath(args)
    dumpfilepath = helpers.getDumpFilePath(args)
    app = helpers.getApp(args)

    connectionsettings = extractor.getConSettings(webconfigpath)

    return commander.buildCommand(connectionsettings, app)

def executeCommandAndArguments(caa, dumpfilepath):
    print '---------------------------------------------'
    print caa + ' < ' + dumpfilepath
    result = Popen(caa + ' < ' + dumpfilepath, shell=True)
    print '---------------------------------------------'

    print '---------------------------------------------'
    print 'done pushing: everything went well (I think)'
    print '---------------------------------------------'

if __name__ == '__main__':
    main(sys.argv[1:])
