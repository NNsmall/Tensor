from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import logging
import os


def start_webdriver():
    logging.basicConfig(level=logging.DEBUG, filename="log_task_3.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd(), 'safebrowsing.enabled': True}
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--start-maximized')
    options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=options)


driver = start_webdriver()
try:
    # 1) Перейти на https://sbis.ru/
    # 2) В Footer'e найти и перейти "Скачать СБИС"
    driver.get("https://sbis.ru/")
    driver.find_element(By.XPATH,"//div[@class='sbis_ru-CookieAgreement__close']").click()
    target = driver.find_element(By.LINK_TEXT, "Демо")
    ActionChains(driver).move_to_element(target).perform()
    driver.find_element(By.LINK_TEXT, "Скачать СБИС").click()
    sleep(2)

    # # 3) Скачать СБИС Плагин для вашей для windows, веб-установщик в папку с данным тестом
    driver.find_element(By.XPATH, "//div[@data-id='plugin']").click()
    driver.implicitly_wait(5)
    load = driver.find_element(By.XPATH, "//div[@class='ws-SwitchableArea sbis_ru-VerticalTabs__area ws-enabled ws-component ws-has-focus']/div[2]/div/div/div[2]/div/div[2]//a")
    file = load.get_attribute("href").split("/")[-1]
    load.click()
    sleep(10)

    # 4) Убедиться, что плагин скачался
    check_for_file_existence = os.path.isfile(file)

    # 5) Сравнить размер скачанного файла в мегабайтах. Он должен совпадать с указанным на сайте
    size_link_file = float(load.text.split(" ")[2])
    size_load_file = round((os.path.getsize(file) / pow(1024, 2)), 2)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()