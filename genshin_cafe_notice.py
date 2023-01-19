from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

n_cafe_url = "https://cafe.naver.com/genshin"

driver = webdriver.Chrome(options=options)

def start():
    # notice_list_copy = []
    notice_list = []
    link_list = []

    driver.get(n_cafe_url)
    time.sleep(1)
    driver.switch_to.frame("cafe_main")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    notice_dats = soup.find_all("a", "article")
        
    for notice_data in notice_dats:
        notice: str = notice_data.attrs["title"]
        link: str = notice_data.attrs["href"]
        notice_list.append(notice)
        link_list.append("https://cafe.naver.com"+link)
        
    print("최근 원신 공식카페 공지\n")
    for i in range(10):
        print(f"{notice_list[i]}\n{link_list[i]}\n")

start()