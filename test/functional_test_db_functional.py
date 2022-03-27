import requests
from bs4 import BeautifulSoup

# login test cases

def server_pass():
    session = requests.session()
    server = session.post("http://localhost:8080/CRMMVC_war").text
    soup = BeautifulSoup(server, "html.parser")
    print(soup.title.string)
    fault_text = soup.title.string
    assert fault_text == "Hello NUS!"


if __name__ == '__main__':
    server_pass()