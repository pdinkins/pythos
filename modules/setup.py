
'''
# setup.py 
# sniffs current build and generates current config file
# import setup
# 
# user = setup.UserBuild()
'''
import hashlib
from _log import log
from writer import FileObject, Write2file

class UserBuild:
    '''
        # for testing the current local build
               #### current cpu system configuration 
                           #### file system analyze 
            ## checks for corrupted or out of date software
    '''

    def __init__(self):
        self.operating_sys = self.os_sys()
        self.node_ip = self.get_ip()
        self.build = self.user_build()
        self._hash_value = self.__hash(self.build, self.node_ip)
        self.config_file = self._config_file()

    def __hash(self, val1, val2):
        # reutrn hash value
        return 0

    def os_sys(self):
        import platform
        return platform.system()
    
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
        log('user_build')
        # initial import
        log('Initial Imports')
        try:
            import os, sys
            log('import: os, sys') 
            from platform import platform, python_branch, python_compiler, machine, python_build
            log('import: platform')
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
            #self._python_build = python_build()
            #log(self._python_build)
            self._python_compiler = python_compiler()
            log(self._python_compiler)
            self.pmachine = machine()
            log(self.pmachine)
            log('0_SYSTEM_CONFIGFILE')
            self.n0osd = [
                self.node,
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
    
    def _config_file(self):
        self.__config_file = FileObject('cfg', 'txt')
        




