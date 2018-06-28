"""
###### 0_NODE_SERVER ######

This is a level 0 node server. This node contains the entire software
stack and can execute every network function. Gate keeper for private
networks. Facilitates custom user functions. 

IPFS Daemon must be running 
IPFSAPI_IP: 127.0.0.1:5001/5002

Config file is required
    > network config
    > ipfs id
    > node wallet
        > trusted peers
        > data store hashes

> Node
    -client interface
        -user input

    -httpserver
        -filehosting
        -filestorage

    -ipfs node(daemon)
        -read
        -write

    -tpls_server
        -config security settings

"""

class NodeServer:
    '''
    
    '''
    def __init__(self, config_file):
        self._configFile = config_file
        self._httpServer = self.__http_server()
        self._ipfsNode = self.__ipfs_node()
        self.