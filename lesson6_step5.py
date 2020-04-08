from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/find_link_text"
a = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_partial_link_text(a)
    button.click()
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("firstname")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(70)
    # закрываем браузер после всех манипуляций
    #browser.quit()

# не забываем оставить пустую строку в конце файла