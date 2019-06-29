import socket 
def echo(event, context):
  return socket.gethostname()
