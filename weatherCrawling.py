import requests

from bs4 import BeautifulSoup

#weather_area = input('날씨를 알고 싶은 지역을 입력하세요:')
#
#weather_html = requests.get(f"http://search.naver.com/search.naver?&query={weather_area}날씨")
weather_html = requests.get(f"http://search.naver.com/search.naver?&query=한남동날씨")
#print(weather_html.text)

weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

area_text = weather_soup.find('h2',{'class':'title'}).text #검색된 날씨 지역명
print(area_text)

today_temper = weather_soup.find('div', {'class':'temperature_text'}).text #현재온도

today_temper = today_temper[6:10]

print(today_temper)