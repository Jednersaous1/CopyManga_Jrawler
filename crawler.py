import time
import os
from threading import Thread
import argparse
import urllib.request
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import check

# 1. Proxy not handled -> env set && webdriver set
# 2. Thread not handled -> threading
# 3. Collect user input and parse for variables -> use argparse
# 4. specify wanted manga chapter
# 5. replace cookie set of logining (no captcha)
# 6. replace index of crawl specific chapter name
# done

# Proxy set(Clash)
# Make sure you started clash's allow LAN connect!
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
os.environ["all_proxy"] = "socks5://127.0.0.1:7890"


loading_string = "https://hi77-overseas.mangafuna.xyz/static/websitefree/jpg/loading.jpg"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}


def initialize_driver():
    chrome_options = Options()
    # headless mode
    chrome_options.add_argument("--headless=new") 
    # incognito mode
    chrome_options.add_argument("--incognito")
    # disable cache
    chrome_options.add_argument("--disk-cache-size=0")
    chrome_options.add_argument("--disable-application-cache")
    # disable gpu and sandbox to save space
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    # Proxy set manually
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:7890')
    driver = webdriver.Chrome(options = chrome_options, keep_alive = False)
    driver.implicitly_wait(10)
    driver.maximize_window()

    return driver

def login(driver: webdriver, username, password, login_url):
    try:
        logger.info("Start simulating login")
        driver.get(login_url)
        username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'].el-input__inner")))
        username_input.send_keys(username)

        password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password'].el-input__inner")))
        password_input.send_keys(password)

        login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.el-button--primary")))
        login_button.click()

        WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.username")))
        logger.info("Login success!")
        return True
    except Exception as e:
        logger.error(f"Login_Error: {e}")
        return False


def get_default_page_list(driver: webdriver, manga_name, url):
    try:
        driver.get(url + "comic/" + manga_name)
        div = driver.find_element(By.ID, "default全部")
        a_tags = div.find_elements(By.TAG_NAME, "a")
        li_tags = div.find_elements(By.TAG_NAME, "li")
        href_list = [a.get_attribute("href") for a in  a_tags if a.get_attribute("target") == "_blank"]
        name_list = [li.get_attribute("innerHTML") for li in li_tags if li.get_attribute("class") == '']
        # remove unneed <li> content
        name_list.pop()
    except Exception as e:
        logger.error(f"PageList_Error: {e}")
        quit()
    
    return href_list, name_list

def get_img_list(driver: webdriver, href, cookie):
    if cookie:
        driver.add_cookie(cookie)
    driver.get(href)
    page_number = driver.find_element(By.CSS_SELECTOR, "span.comicCount").text.strip()
    ul = driver.find_element(By.CSS_SELECTOR, "ul.comicContent-list.comic-size-1")
    try:
        while True:
            driver.execute_script(f"window.scrollBy(0, {500});")
            time.sleep(0.5)
            img_tags = ul.find_elements(By.TAG_NAME, "img")
            img_list = [img.get_attribute("src") for img in img_tags if img.get_attribute("src")]
            if len(img_tags) == int(page_number) and loading_string not in img_list:
                break
        return img_list
    except Exception as e:
        logger.error(f"GetMangaList_Error: {e}")

def download_img(img_url,filnem):
    request = urllib.request.Request(img_url, headers=headers)
    logger.info("Start downloading: " + str(filnem))
    try:
        response = urllib.request.urlopen(request)
        filename = filnem
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read()) 
            logger.info(str(filnem) + " Downloaded success! ")
            return filename
        elif (response.getcode() == 429):
            logger.info(f"Too many requests! Status code: {response.getcode()}")
    except Exception as oo:
        logger.error(f"Download_Error: {oo}")
        return "failed"
    
def parse_main():
    # Parse main arguments
    parser = argparse.ArgumentParser(description = "CopyManga_Jrawler Help Manual")
    parser.add_argument("-m", "--manga", required = True, help = "Enter wanted manga's name with pinyin format")
    parser.add_argument("-c", "--cookie", help = "Enter your copymanga website's cookie(token)")
    parser.add_argument("-u", "--username", help = "Enter your username")
    parser.add_argument("-p", "--password", help = "Enter your password")
    parser.add_argument("-ch", "--chapter",nargs = "*", help = "Enter specific chapter that you want download from the manga")
    args = parser.parse_args()
    return args


if __name__ == "__main__":

    # Get manga's arguments
    arguments = parse_main()
    # Set cookie
    cookie = None
    if arguments.cookie:
        cookie = {'name': 'token', 'value': arguments.cookie}
    # Set credential
    login_res = None
    login_username = arguments.username
    login_password = arguments.password
    # Set Manga name
    manga_name = arguments.manga

    # Get accessiable copymanga website (But token has some problem)
    url_dict = check.check_main()
    if url := check.check_every_url(url_dict):
        logger.info(f"Found accessiable webiste {url}")
    login_url = url + "web/login/loginByAccount?url=person%2Fhome"

    # Initialize webdriver
    driver = initialize_driver()

    if login_username and login_password:
        login_res = login(driver, login_username, login_password, login_url)

    if login_res or cookie != None:
        href_list, name_list = get_default_page_list(driver, manga_name, url)
    else:
        logger.error("You don't provide cookie or username/password, please check your arguments!")
        quit()

    # Set specific manga chapter
    if arguments.chapter:
        chapters = [int(c) - 1 for c in arguments.chapter]
    else:
        chapters = [c for c in range(len(href_list))]

    for i in chapters:
        logger.info("Enter every manga_list's getting process")
        manga_list = get_img_list(driver, href_list[i], cookie)

        # As for each href, try create download folder by order
        logger.info("Creating download folder")
        try:
            os.makedirs(f"./img/{manga_name}/{name_list[i]}", exist_ok = True)
        except Exception as e:
            logger.error(f"Creating download folder_Error: {e}")


        thread_list = []

        # get all imgs for each manga_list using thread list
        for j in range(len(manga_list)):
            t1 = Thread(target = download_img, args = (manga_list[j], f"./img/{manga_name}/{name_list[i]}/{ j + 1 }" + ".jpg"))
            thread_list.append(t1)
            time.sleep(0.5)
        
        for t in thread_list:
            t.daemon = True
            t.start()
        for t in thread_list:
            t.join()
        logger.info(f"Manga {manga_name} {name_list[i]} Downloaded success!")
    
    driver.quit()