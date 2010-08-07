import re
class Extractor(object):
    """
        extract the connection string from your umbraco web.config
    """
    def findConStr(self, webconfigpath ):
        w = open( webconfigpath, 'r' )
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
        return dict( [ tuple( s.lower().split('=') ) for s in constr.split(';') if '=' in s ] )


    def getConSettings(self, webconfigpath):
        constr = self.findConStr(webconfigpath)
        return self.buildConSettings(constr)

