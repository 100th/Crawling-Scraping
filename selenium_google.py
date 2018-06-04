from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# PhantomJS 모듈의 WebDriver 객체 생성
# 다른 브라우저를 조작하고 싶을 때는 webdriver.Firefox() 등으로도 가능
# http://www.seleniumhq.org/about/platforms.jsp
driver = webdriver.PhantomJS

# Google 메인 페이지 열기
driver.get('https://www.google.co.kr/')

#타이틀에 'Google'이 포함돼 있는지 확인
assert 'Google' in driver.title

# 검색어를 입력하고 검색
# send_keys 메서드로 키보드 입력을 한다
# "내용을 입력하고 Enter 키를 누른다" 등
input_element = driver.find_element_by_name('q')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

# 타이틀에 'Python'이 포함돼 있는지 확인
assert 'Python' in driver.title

# 스크린샷 찍기
# 화면 크기 변환 가능
# driver.set_window_size(320, 600)
driver.save_screenshot('search_results.png')

# 검색 결과 출력
for a in driver.find_elements_by_css_selector('h3 > a'):
    print(a.text)
    print(a.get_attribute('href'))
    print()
