import os, sys, re
from customexceptions import ArgsException

class Fetcher(object):
    """
        this class is used to create a MySql dump command
        based on the connection string in your web.config
    """

    def Command(self, args):
        """
            return MySql dump command
        """
        self.validateArgsLen(args, 2)
        webconfigpath = self.getWebConfig(args)
        constr = self.findConStr(webconfigpath)
        constrsettings = self.buildConSettings(constr)
        dumpfile = self.getDumpFile(args)

        return self.buildCommand(constrsettings, dumpfile)

    def findConStr(self, webConfig ):
        w = open( webConfig, 'r' )
        constr = ''
        for l in w.readlines():
            if self.matchConStr(l):
                constr = self.matchConStr(l)
    
        return constr
    
    def matchConStr(self, xmlline):
        regex = r'<add.*key=\"umbracoDbDSN\".*value=\"(.*)\".*/>'
        m = re.search(regex, xmlline)
        if m:
            return m.group(1) 
    
    def buildConSettings(self, constr):
        return dict( [ tuple( s.lower().split('=') ) for s in constr.split(';') if
        '=' in s ] )
    
    def buildCommand(self, conSettings, dumpFile):
        if conSettings['datalayer'] == 'mysql':
            return self.buildMySqlCommand(conSettings, dumpFile) 
    
    def buildMySqlCommand(self, cs, dumpFile):
        return '-u{0} -p{1} -h{2} {3} > {4}'.format(cs['user id'], 
                                              cs['password'], 
                                              cs['server'], 
                                              cs['database'],
                                              dumpFile)
