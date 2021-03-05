"""Este chunk tiene como prop�sito explorar la posibilidad de hacer test de una
funci�n qu eposee una libreer�a como request."""

import requests as rq



def request(url):
    response =rq.get(url)
    return response.status_code 

def test_request_status():
    assert request('http://www.google.com') == 200


if __name__ == "__main__":
    test_request_status()
    print("Everything fine")