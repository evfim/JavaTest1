import requests
from bs4 import BeautifulSoup

# login test cases
def test_login_1():

    POST_LOGIN_URL = 'http://127.0.0.1:8080/CRMMVC/login'
    REQUEST_URL = 'http://127.0.0.1:8080/CRMMVC/posts'


    r = requests.session()
    data = {

    'username': 'admin',
    'password': '1234'
    }
    opens = r.post(url=POST_LOGIN_URL, data=data)
    soup = BeautifulSoup(opens.text, 'lxml')
    print(soup)

    #r = session.get(REQUEST_URL)
    #print(r.text)   

    #session = requests.session()
    #login = session.post("http://127.0.0.1:8080/CRMMVC/login", {"username": "admin", "password": "1234"}).text
    #soup = BeautifulSoup(login, "html.parser")
    #print(soup.title.string)
    #fault_text = soup.find_all(text=True)
    #print(fault_text)
    #str_match = [s for s in fault_text if s.__contains__("Posts")]  
    #str_match=' '.join(map(str,str_match))
    #print(str_match)
    assert "Posts" in r.text

def test_login_2():
    session = requests.session()
    login = session.post("http://127.0.0.1/CRMMVC/login", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    #print(soup.title.string)
    fault_text = soup.find_all(text=True)
    str_match = [s for s in fault_text if s.__contains__("Posts")]  
    str_match=' '.join(map(str,str_match))
    assert "Wrong Login!" in str_match
    


def test_login_3():
    session = requests.session()
    login = session.post("http://127.0.0.1:8080/CRMMVC/login", {"username": "admin", "password": "1234"}).text
    soup = BeautifulSoup(login, "html.parser")
    #print(soup.title.string)
    fault_text = soup.find_all(text=True)
    str_match = [s for s in fault_text if s.__contains__("Posts")]  
    str_match=' '.join(map(str,str_match))
    assert "Wrong Login!" in str_match

if __name__ == '__main__':
    test_login_1()
    test_login_2()
    test_login_3()
