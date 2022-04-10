import requests
from bs4 import BeautifulSoup

# login test cases
def test_login_1():

    POST_LOGIN_URL = 'http://127.0.0.1:8080/CRMMVC/login2'
    REQUEST_URL = 'http://127.0.0.1:8080/CRMMVC/posts'


    payload = {
    'username': 'admin',
    'password': '1234'
    }
    
    with requests.Session() as session:
         post = session.post(POST_LOGIN_URL, data=payload)
         soup = BeautifulSoup(post.text, "html.parser")

    fault_text = soup.find_all(text=True)
    assert "Posts" in fault_text

def test_login_2():
#    session = requests.session()
#    login = session.post("http://127.0.0.1/CRMMVC/login", {"username": "admin", "password": "1234"}).text
#    soup = BeautifulSoup(login, "html.parser")
#    #print(soup.title.string)
#    fault_text = soup.find_all(text=True)
#    str_match = [s for s in fault_text if s.__contains__("Posts")]  
#    str_match=' '.join(map(str,str_match))
    POST_LOGIN_URL = 'http://127.0.0.1:8080/CRMMVC/login2'
    REQUEST_URL = 'http://127.0.0.1:8080/CRMMVC/posts'

    payload = {
    'username': 'admin',
    'password': '12345'
    }

    with requests.Session() as session:
         post = session.post(POST_LOGIN_URL, data=payload)
         soup = BeautifulSoup(post.text, "html.parser")

    fault_text = soup.find_all(text=True)
    str_match = [s for s in fault_text if s.__contains__("Wrong Login!")]
    str_match=' '.join(map(str,str_match))
    assert "Wrong Login!" in str_match

    


def test_login_3():
#    session = requests.session()
#    login = session.post("http://127.0.0.1/CRMMVC/login", {"username": "admin", "password": "1234"}).text
#    soup = BeautifulSoup(login, "html.parser")
#    #print(soup.title.string)
#    fault_text = soup.find_all(text=True)
#    str_match = [s for s in fault_text if s.__contains__("Posts")]
#    str_match=' '.join(map(str,str_match))
    POST_LOGIN_URL = 'http://127.0.0.1:8080/CRMMVC/login2'
    REQUEST_URL = 'http://127.0.0.1:8080/CRMMVC/posts'

    payload = {
    'username': 'root',
    'password': '1234'
    }

    with requests.Session() as session:
         post = session.post(POST_LOGIN_URL, data=payload)
         soup = BeautifulSoup(post.text, "html.parser")

    fault_text = soup.find_all(text=True)
    str_match = [s for s in fault_text if s.__contains__("Wrong Login!")]
    str_match=' '.join(map(str,str_match))
    assert "Wrong Login!" in str_match


if __name__ == '__main__':
    test_login_1()
    test_login_2()
    test_login_3()
