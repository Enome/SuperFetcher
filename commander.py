import os, sys

class Commander(object):
    """
        this class is used to create a MySql dump command
        based on the connection string in your web.config
    """
    
    def buildCommand(self, conSettings, app):
        if conSettings['datalayer'] == 'mysql':
            return self.buildMySqlCommand(conSettings, app) 
        else:
            raise Exception, 'Sorry but we only support MySql. Might change in the future'
    
    def buildMySqlCommand(self, cs, app):
        return '{0} -u{1} -p{2} -h{3} {4}'.format(
                                                   app,
                                                   cs['user id'], 
                                                   cs['password'], 
                                                   cs['server'], 
                                                   cs['database'])
