import socket
if hasattr(socket, "TCP_KEEPCNT"):
    del socket.TCP_KEEPCNT
if hasattr(socket, "TCP_KEEPIDLE"):
    del socket.TCP_KEEPIDLE
if hasattr(socket, "TCP_KEEPINTVL"):
    del socket.TCP_KEEPINTVL
