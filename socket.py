# Echo Server
import socket

HOST = '127.0.0.1' #Localhost
PORT = 8000 # non privileged hsots(used for testing)

# using with statement 
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  connn , addr = s.accept()
  with connn:  #i assue that accpet received an context managed protocol
    print(f"Connected by {addr}")
    while True:
      data =connn.recv(1024)
      if not data:
        break
      connn.sendall(data)