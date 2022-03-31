import requests
from bs4 import BeautifulSoup

# login test cases

def test_static():
    session = requests.session()
    login = session.get("http://127.0.0.1:8080/CRMMVC/").text
    soup = BeautifulSoup(login, "html.parser")
    print(soup.title.string)
    fault_text = soup.title.string
    assert fault_text == "Hello"

def test_login_1():
    session = requests.session()
    login = session.post("http://127.0.0.1:8080/CRMMVC_war/login.jsp", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    print(soup.title.string)
    fault_text = soup.title.string
    assert fault_text == "Posts"

def test_login_2():
    session = requests.session()
    login = session.post("http://127.0.0.1/CRMMVC_war/login", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    print(soup.title.string)
    fault_text = soup.title.string
    assert fault_text == "Wrong Login!"


def test_login_3():
    session = requests.session()
    login = session.post("http://127.0.0.1:8080/CRMMVC_war/login", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    print(soup.title.string)
    fault_text = soup.title.string
    assert fault_text == "Wrong Login!"

if __name__ == '__main__':
    test_login_1()
    test_login_2()
    test_login_3()