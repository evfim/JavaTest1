import socket

hostname = socket.gethostname()
url_name = "http://" + socket.gethostbyname(hostname) + ":8080/CRMMVC/"
print(url_name)
