import time
import os
import urllib.request
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 1. Proxy not handled -> env set && webdriver set
# 2. Thread not handled

# Proxy set
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
os.environ["all_proxy"] = "socks5://127.0.0.1:7890"

url = "https://www.mangacopy.com/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}


def enter_load_page_x(driver, manga_name, page_x):
    return

def get_default_page_list(driver: webdriver, manga_name):
    try:
        driver.get(url + "comic/" + manga_name)
        div = driver.find_element(By.ID, "default全部")
        a_tags = div.find_elements(By.TAG_NAME, "a")
        href_list = [a.get_attribute("href") for a in  a_tags if a.get_attribute("target") == "_blank"]
    except Exception as e:
        logger.error(f"PageList_Error: {e}")
    
    return href_list

def get_img_list(driver: webdriver, cookie, href):
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
    except Exception as oo:
        logger.error(f"Download_Error " + str(oo))
        return "failed"

if __name__ == "__main__":

    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    # 启用无痕模式（关闭后自动清理临时数据）
    chrome_options.add_argument("--incognito")
    # 禁用缓存
    chrome_options.add_argument("--disk-cache-size=0")
    chrome_options.add_argument("--disable-application-cache")
    # 禁用 GPU 和沙盒（减少临时文件）
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    # Proxy set
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:7890')
    driver = webdriver.Chrome(options = chrome_options)
    # driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    manga_name = "shengxiadebangxiong"
    cookie = {'name': 'token', 'value': '1db18e80eb4755c6e4cf335c451c7956ceccd235'}
    loading_string = "https://hi77-overseas.mangafuna.xyz/static/websitefree/jpg/loading.jpg"
    
    href_list = get_default_page_list(driver, manga_name)


    for i in range(len(href_list)):
        logger.info("Enter every manga_list's getting process")
        manga_list = get_img_list(driver, cookie, href_list[i])

        # As for each href, create download folder by order
        logger.info("Creating download folder")
        try:
            os.makedirs(f"./img/sxdbx/_{ i + 1 }", exist_ok = True)
        except Exception as e:
            logger.error(f"Creating download folder_Error: {e}")

        # get all imgs for each manga_list
        for j in range(len(manga_list)):
            try:
                download_img(manga_list[j], f"./img/sxdbx/_{ i + 1 }/{j}" + ".jpg")
            except Exception as e:
                logger.error(f"Whole Download_Error: {e}")
    
    driver.quit()