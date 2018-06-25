
'''
# setup.py 
# sniffs current build and generates current config file
# import setup
# 
# user = setup.UserBuild()
'''


class UserBuild:
    '''
        # for testing the current local build
               #### current cpu system configuration 
                           #### file system analyze 
            ## checks for corrupted or out of date software
    '''

    def __init__(self):
        self.node_ip = self.get_ip()
        self.build = self.user_build()
      
    def get_ip(self):
        from requests import get
        try:
            log('Pinging 3rd party for public IP')
            self._0_node_ip = get('http://ip.42.pl/raw').text
            log(self._0_node_ip)  
        except:
            self._0_node_ip = 'No network connection'
            log('REQUESTS_ERROR')
        return self._0_node_ip

    def user_build(self):

        # initial import
        log('Initial Import Tests')
        try:
            import os, sys
            log('os, sys') 

            from platform import platform, python_branch, python_compiler, machine, python_build
            log('platform')

            import datetime
            log('datetime') 

            from subprocess import Popen, PIPE
            log('subprocess') 

            from requests import get
            log('requests') 

            import time
            log('time') 
        
        except:
            print('FATAL_PYTHON_BUILD_ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
        


        try:
            log('0_SYSTEM_PYTHON_CONFIG')

                
            self.node = platform()
            log(self.node)
                
            self._python_build = python_build()
            log(self._python_build)
                
            self._python_compiler = python_compiler()
            log(self._python_compiler)

            self.pmachine = machine()
            log(self.pmachine)
            


            log('0_SYSTEM_CONFIGFILE')
            self.n0osd = [
                self.node,
                self._python_build,
                self._python_compiler,
                self.pmachine]
            log("USER_BUILD_COMPLETE")
            return self.n0osd

        except:
            log('USER_BUILD_FAILED')
            log('something went horribly wrong')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise


def log(message):
    import inspect, logging
    import datetime as dt
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    func = inspect.currentframe().f_back.f_code
    logging.debug("{}\t{}\t{}\t{}".format(
        dt.datetime.now(),
        func.co_filename,
        func.co_name,
        message))




