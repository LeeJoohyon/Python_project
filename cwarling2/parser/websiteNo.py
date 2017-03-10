import requests
from bs4 import BeautifulSoup


# 사이트 정보 긁어오기

def get_soup_from_url(url, params=None):
    '''
    url과  parameter 사용해서 해당 url에 get요청을 보낸 결과 (html,text)로
    BeautifulSoup객체를 생성해 반환
    :param url: get요청을 보낼 url string
    :param params: get요청 매개변수
    :return: BerutifulSoup object
    '''

    # request.get요청을 보낸 결과값(response객체)을 r변수에 할당
    r = requests.get(url, params=params)

    html_doc = r.text

    soup = BeautifulSoup(html_doc,'lxml')
    return soup
