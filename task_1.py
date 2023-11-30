from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging


def start_webdriver():
    logging.basicConfig(level=logging.DEBUG, filename="log_task_1.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--start-maximized')
    return webdriver.Chrome(options=options)


driver = start_webdriver()
try:
    # 1) Перейти на https://sbis.ru/ в раздел "Контакты"
    # 2) Найти баннер Тензор, кликнуть по нему
    driver.get("https://sbis.ru/")
    driver.find_element(By.XPATH,"//li[@class='sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm']").click()

    # 3) Перейти на https://tensor.ru/
    driver.find_element(By.XPATH,"//div[@class='sbisru-Contacts__border-left sbisru-Contacts__border-left--border-xm pl-20 pv-12 pl-xm-0 mt-xm-12']/a").click()

    # 4) Проверить, что есть блок "Сила в людях"
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    force_in_people = driver.find_element(By.XPATH, "//div[@class='s-Grid-col s-Grid-col--6 s-Grid-col--sm12']//p").text
    driver.implicitly_wait(5)

    # 5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    target = driver.find_element(By.XPATH,"//div[@class='nl-LastCovers__header_title']")
    ActionChains(driver).move_to_element(target).perform()
    driver.find_element(By.XPATH,"//div[@class='controls-Scroll-containerBase_userContent']//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']//a").click()
    url = driver.current_url

    # 6) Находим раздел Работаем и проверяем, что у всех фотографий хронологии одинаковые высота (height) и ширина (width)
    images = driver.find_elements(By.XPATH, "//div[@class='tensor_ru-About__block3-image-wrapper']")
    list_images = []
    for img in images:
        width = img.find_element("tag name", "img").get_attribute("width")
        height = img.find_element("tag name", "img").get_attribute("height")
        list_images.append([width, height])

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()