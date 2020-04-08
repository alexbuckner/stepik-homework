from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text

input1 = browser.find_element_by_id("answer")
input1.send_keys(calc(x))

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radiobutton = browser.find_element_by_id("robotsRule")
radiobutton.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
