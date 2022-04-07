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
    print("Fault text value:")
    print(fault_text)
    str_match = [s for s in fault_text if s.__contains__("Hello")]
    print (str_match)
    str_match=' '.join(map(str,str_match))
    assert str_match == "Hello NUS!"
    #assert "Hello" in str_match

def test_login_1():
    session = requests.session()
    login = session.post("http://127.0.0.1:8080/CRMMVC/login", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    #print(soup.title.string)
    fault_text = soup.find_all(text=True)
    assert "Posts" in fault_text

def test_login_2():
    session = requests.session()
    login = session.post("http://127.0.0.1/CRMMVC/login", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    #print(soup.title.string)
    fault_text = soup.find_all(text=True)
    assert "Wrong Login!" in fault_text


def test_login_3():
    session = requests.session()
    login = session.post("http://127.0.0.1:8080/CRMMVC/login", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    #print(soup.title.string)
    fault_text = soup.find_all(text=True)
    assert "Wrong Login!" in fault_text

if __name__ == '__main__':
    test_static()
    test_login_1()
    test_login_2()
    test_login_3()
