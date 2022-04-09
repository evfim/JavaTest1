import socket, os

hostname = socket.gethostname()
url_name = "http://" + socket.gethostbyname(hostname) + ":8080/CRMMVC/"
print(url_name)
url_name = "docker run -t owasp/zap2docker-stable zap-baseline.py -t " + url_name

os.system(url_name)
