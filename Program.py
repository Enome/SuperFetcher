import os, sys, re

#Arguments should be: webConfigLocation, mysqldumpLocation, dumpLocation
#../Externals/mysqldump.exe ../Externals/web.config ../Output/dumpster.sql

def main():
    #First one is always the current filename
    args = sys.argv[1:]    
    
    if not len(args) == 3:
        raise Exception('You need to specify 3 arguments: MySqldump location, web.config path, path to dump file')
    
    #mysqldump validation
    if not 'mysqldump' in args[0]:
        raise Exception('First argument should be the mysqldump cmd or path to mysqldump.exe')
    
    if not os.path.exists( args[0] ):
        raise Exception('MySqlDump was not found')
    
    #web.config validation
    if not 'web.config' in args[1]:
        raise Exception('Second argument should be the path to the web.config file')
        
    if not os.path.exists( args[1] ):
        raise Exception('web.config was not found')
        
    if not os.path.exists( os.path.dirname(args[2] ) ):
        raise Exception('Could not find the directory for the dump file')
        
    mysqldumppath = args[0]
    webconfigpath = args[1]
    dumpfilepath  = args[2]
    
    #WEBCONFIG STUFF BUILD SETTINGS
    webconfig = open(webconfigpath, 'r')
    
    regex = r'<add.*key=\"umbracoDbDSN\".*value=\"(.*)\".*/>'
    connectionString = ''
    try:
        connectionstring = [ re.search(regex, l) for l in webconfig.readlines() if re.search(regex, l) ][0].group(1).lower()
    except:
        raise Exception('There was a problem with retrieving the connection string from the web.config file')
        
    if not connectionstring:
        raise Exception('The connection string turned up empty')
        
    #connectionsettings
    cs = dict( [ tuple( s.lower().split('=') ) for s in connectionstring.split(';') ] )
        
    if not len(cs) == 5:
        raise Exception('The connection string is missing some values')
        
    #If ony the keys is missing it will explode
    for m in [ k for k in ['server', 'database', 'user id', 'password', 'datalayer' ] if not k in cs ]:
        raise Exception('The following key was missin in the connection string:{0}'.format(m))
        
    if cs['datalayer'] != 'mysql':
        raise Exception('Sorry we only support MySql')
  

    #CREATE ARGUMENTS
    arguments = '-u{0} -p{1} -h{2} {3}'.format(cs['user id'], cs['password'], cs['server'], cs['database'])
    cmd =  '{0} {1}'.format(mysqldumppath, arguments)
    
    try:
        #Process Open = popen
        pipe = os.popen(cmd)
        text = pipe.read()
        sts = pipe.close()
    except:
        raise Exception('Something went wrong with executing the dump commands')
        
    if not text:
        raise Exception('The dump file is empty')
    
    try:
        dumpFile = open(dumpfilepath, 'w')
        dumpFile.write(text)
        dumpFile.close()
    except:
        raise Exception('something went wrong with writing the dump files')
        
    print 'Done superFetching'
        
if __name__ == '__main__':
    main()
