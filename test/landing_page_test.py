import requests
from bs4 import BeautifulSoup

# test that page is main page rendered properly after being deployed from war file

def test_landing_page():
    session = requests.session()
    login = session.get("http://127.0.0.1:8080/CRMMVC/").text
    soup = BeautifulSoup(login, "html.parser")
    fault_text = soup.find_all(text=True)
    str_match = [s for s in fault_text if s.__contains__("Hello")]  
    str_match=' '.join(map(str,str_match))
    #assert str_match == "Hello NUS!"
    assert "Hello NUS!" in str_match
    print("Landing Page exist and successfully rendered")





if __name__ == '__main__':
    test_landing_page()
