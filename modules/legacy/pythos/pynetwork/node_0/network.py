# Network
# contains network related functions

#==============================================================================================#
###### 0_NODE_SERVER ######
'''
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


'''
#==============================================================================================#


class CreateSocket:
    '''
    This class will create a socket server with the handshake 
    interface from the tpls_server module. This replaces the tpls server and 
    the node_server. 
    '''

    import sys
    import socket as soc
    from threading import Thread

    def __init__(self):
        self._ip = '192.168.1.4'
        self._port = 1234
        self._socket_tup = (self._ip, self._port)
        self.chash = self.make_internet()

    def _decode(self, arg):
        return arg.decode('utf-8')
    
    def _encode(self, arg):
        return arg.encode('utf-8')
    
    def __check_size(self, bytes_object, MAX_BUFFER_SIZE = 4096):
        return self.sys.getsizeof(bytes_object)

    def make_internet(self):
        self._socket = self.soc.socket(self.soc.AF_INET, self.soc.SOCK_STREAM)
        self._socket.setsockopt(self.soc.SOL_SOCKET, self.soc.SO_REUSEADDR, 1)
        self._socket.bind(self._socket_tup)
        self._socket.listen(10)
        self.conn , self.addr = self._socket.accept()
        self.__ip , self.__port = str(self.addr[0]), str(self.addr[1])
        self.Thread(target=self.client_thread, args=(self.conn, self.__ip, self.__port)).start()
        
    def client_thread(self, conn, ip, port, MAX_BUFFER_SIZE = 4096):
        self.incoming_client_hash = self.conn.recv(MAX_BUFFER_SIZE)
        self.incoming_client_hash_size = self.__check_size(self.incoming_client_hash)
        self.client_hash = self._decode(self.incoming_client_hash)
        return self.client_hash

    def _client_hash_analyzer(self):
        pass