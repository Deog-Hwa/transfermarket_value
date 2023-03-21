import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# requsts.get()으로 url정보 요청하기 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

number=[]
name=[]
position=[]
age=[]
nation=[]
team=[]
value=[]

# 두번째 페이지까지 크롤링하기 
for i in range(1, 3):

    url = f"https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop/plus/ajax/yw1/0//page/{i}"

    r= requests.get(url, headers=headers)
    r.status_code  #200이 나오면 정상

    soup = BeautifulSoup(r.text, 'html.parser')  # r.content 대신 r.text도 가능

    player_info= soup.find_all('tr', class_=['odd', 'even'])

    # player_info에서 'td'태그만 모두 찾기
    for info in player_info:
        player = info.find_all("td")

        number.append(player[0].text)
        name.append(player[3].text)
        position.append(player[4].text)
        age.append(player[5].text)
        nation.append(player[6].img['alt'])
        team.append(player[7].img['alt'])
        value.append(player[8].text.strip())
        # value.value[1:-1] 특수 기호 지우기
    
    time.sleep(1)

    # pd.DataFrame()으로 저장하기

df = pd.DataFrame(
        {"number":number,
         "name":name,
         "position":position,
         "age":age,
         "nation":nation,
         "team":team,
         "value":value}
)

