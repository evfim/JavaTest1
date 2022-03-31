import requests
from bs4 import BeautifulSoup

# login test cases

def test_static():
    session = requests.session()
    login = session.get("http://127.0.0.1:8080/CRMMVC/").text
    soup = BeautifulSoup(login, "html.parser")
    #print("=========")
    #print(soup)
    #print("=========")
    fault_text = soup.find_all(text=True)
    assert fault_text in "Hello"

def test_login_1():
    session = requests.session()
    login = session.post("http://127.0.0.1:8080/CRMMVC/login", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    #print(soup.title.string)
    fault_text = soup.find_all(text=True)
    assert fault_text in "Posts"

def test_login_2():
    session = requests.session()
    login = session.post("http://127.0.0.1/CRMMVC/login", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    #print(soup.title.string)
    fault_text = soup.find_all(text=True)
    assert fault_text in "Wrong Login!"


def test_login_3():
    session = requests.session()
    login = session.post("http://127.0.0.1:8080/CRMMVC/login", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    #print(soup.title.string)
    fault_text = soup.find_all(text=True)
    assert fault_text in "Wrong Login!"

if __name__ == '__main__':
    test_static()
    test_login_1()
    test_login_2()
    test_login_3()
