'''
원하는 웹 페이지에 접속하여 HTML 데이터를 받아온다 
받아온 HTMl 데이터를 분석가능한 형태로 가공한다
원하는 데이터를 추출한다
'''
#1
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
session = HTMLSession()
response = session.get("https://www.naver.com")
print(response.html.links)

# response = requests.get("https://www.naver.com")
# bs = BeautifulSoup(response.text, "html.parser") #html을 파싱 문자열 데이터 사이에서 원하는 데이터 추출
# for img in bs.select("img"):
#     print(img)




#print(response.status_code)
#print(response.headers)
#print(response.text) #decoding된 상태