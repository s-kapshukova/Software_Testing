from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
#driver.get("https://calcus.ru/random-number")

# Проверка наличия заголовка
#title = driver.title
#assert title == "Рандомайзер. Генератор случайных чисел", "Тест 'Наличие заголовка' - не пройден"
#print("Тест 'Наличие заголовка' - пройден")
#
## Проверка наличия поля ввода "Количество чисел"
#count_numbers = driver.find_element(By.NAME, "qty")
#assert count_numbers.is_displayed(), "Тест 'Наличие поля ввода количества чисел' - не пройден"
#print("Тест 'Наличие поля ввода количества чисел' - пройден")
#
## Проверка на заполнимость полей из диапазона
#is_selected_start = driver.find_element(By.NAME, "range_start").is_selected()
#is_selected_end = driver.find_element (By.NAME, "range_end").is_selected()
#assert ((is_selected_start == False) | (is_selected_end == False)), "Тест 'Заполнимость полей из диапазона'  - не пройден" 
#print ("Тест 'Заполнимость полей из диапазона'  - пройден")

# Переход по ссылке на другой калькулятор
#driver.execute_script("window.scrollTo(0, 300);")
#link = WebDriverWait(driver, 10).until(
#        EC.element_to_be_clickable((By.LINK_TEXT, "Генератор QR кодов"))
#    )
#link.click()
#
## Проверка перехода на нужную страницу
#assert "Генератор QR кодов" in driver.title, "Тест 'Переход по ссылке Генератоp QR кодов' - не пройден"
#print("Тест 'Переход по ссылке Генератоp QR кодов' - пройден")

#Проверка генерации чисел по позитивному сценарию
driver.get("https://calcus.ru")
search_icon = driver.find_element(By.CSS_SELECTOR, ".search-icon > svg:nth-child(1) > use:nth-child(1)")
search_icon.click() #Переход по иконке поиска

search_field = driver.find_element(By.CSS_SELECTOR, ".d-block")
search_field.send_keys("Генератор случайных чисел")
link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Генератор случайных чисел"))
    )
link.click() 

count = driver.find_element(By.NAME, "qty") #Ввод количества чисел
count.clear()
count.send_keys("5")

min = driver.find_element(By.NAME, "range_start") #Ввод нижней границы диапазона
min.clear()
min.send_keys("-10")

max = driver.find_element(By.NAME, "range_end") #Ввод верхней границы диапазона
max.clear()
max.send_keys("10")

wait = WebDriverWait(driver, 10) #Галочка на повторы
repeats = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "align-middle"))
    )
repeats.click()

generation = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class *= 'calc-submit me-3']"))
    ) 
generation.click() #Поиск и клик по кнопке "Генерировать"

try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[class *= 'result-placeholder-result']"))
    )
    print ("Генерация завершена") #Поиск блока с результатом
    
    elements = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.calc-result-big"))
    )
    print(f"Элементов найдено: {len(elements)}") #Создание списка с результатами
    
    results = []
    for element in elements:
        text = element.text.strip() #Вычленение значения из каждой ячейки
        if ((int(text) < -10) | (int(text) > 10)): 
            print ("Ошибка: Число находится вне диапазона")
            break
        #print (text)
        results.append(text)

    if (len(results) == len(elements)):
        print ("Все числа находятся внутри заданного диапазона") #Сравнение фактического количества чисел и заданного
    else:
        print ("Тест 'Генерация чисел' - не пройден")

        
except Exception:
    print("Ошибка генерации результата")

driver.quit()