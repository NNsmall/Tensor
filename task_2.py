from selenium import webdriver
from time import sleep
import logging


def start_webdriver():
    logging.basicConfig(level=logging.DEBUG, filename="log_task_2.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--start-maximized')
    return webdriver.Chrome(options=options)


driver = start_webdriver()
try:
    # 1) Перейти на https://sbis.ru/ в раздел "Контакты"
    driver.get("https://sbis.ru/")
    driver.find_element("xpath",
                "//li[@class='sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm']").click()

    # 2) Проверить, что определился ваш регион (в нашем примере Ярославская обл.) и есть список партнеров.
    region = driver.find_element("xpath", "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    partners = driver.find_elements("xpath", "//div[@class='sbisru-Contacts-List__col-1']")
    list_partners = []
    for i in partners:
        list_partners.append(i.text.replace("\n", " "))
    region_yar, list_partners_yar = region.text, list_partners

    # 3) Изменить регион на Камчатский край
    region.click()
    driver.implicitly_wait(2)
    select_region = 'Камчатский край'
    driver.find_element("xpath", f"//span[@title='{select_region}']").click()
    sleep(3)

    # 4) Проверить, что подставился выбранный регион,
    # список партнеров изменился, url и title содержат информацию выбранного региона
    region = driver.find_element("xpath", "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    partners = driver.find_elements("xpath", "//div[@class='sbisru-Contacts-List__col-1']")
    list_partners = []
    for i in partners:
        list_partners.append(i.text.replace("\n", " "))
    region_kam, list_partners_kam = region.text, list_partners
    url, title = driver.current_url, driver.title
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()