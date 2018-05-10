# 네이버 실시간 급상승 검색어 랭킹 크롤러

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
from bs4 import BeautifulSoup
from os import system
from time import sleep
from datetime import datetime

def time_check():
    now = datetime.now()
    now_time = f"{now.year}.{now.month}.{now.day} - {now.hour}:{now.minute}"

    return now_time

while True:
    html = requests.get('https://www.naver.com/').text
    soup = BeautifulSoup(html, 'lxml')
    rank_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
    # PM_CL_realtimeKeyword_rolling 라는 class에서 class명이 ah_k인 span 태그 형식의 내용만 select로 저장

    print(time_check() + "\n")
    for rank, title in enumerate(rank_list, 1):  # enumerate를 이용하여 반복문 실행
        print(rank, title.text)
        sleep(0.5)  # 0.75초를 간격으로 1위부터 20위까지 순차적으로 출력
    sleep(10)  # 10초 경과 시 실시간 검색어 순위 정보를 업데이트 하기 위해 sleep 사용
    system('cls')
    print("\n")
