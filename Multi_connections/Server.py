import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()

host , port  = sys.argv[1], int(sys.argv[2])
# sys module is used to interact with the python niterpreter deeply
lsock= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
lsock.bind((host,port))
lsock.listen()
print(f"Listinng on {(host
  , port)}")
lsock.setblocking(False)
