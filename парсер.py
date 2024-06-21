import requests
from bs4 import BeautifulSoup #импортируем библиотеки
from time import sleep

list_card_url = [] #создали список куда будем ложить ссылки на описание товара

headers = {
    "User-Agent":
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0" #заведем словарь с заголовками, запросами headers
}

def get_url():
    for count in range(1, 7): #создаем цикл что бы пройтись по всем страницам сайта 
        
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}" #переменная с ссылкой на сайт, f строка что бы count счетчик

        response = requests.get(url, headers=headers) #отправляем get запрос

        soup = BeautifulSoup(response.text, "lxml") #получаем код страницы в норм виде, lxml - это парсер, разбираем ее парсером

        data = soup.find_all("div", class_="w-full rounded border") #метод find находит первый тег или класс в коде сайта, находим карточку товара
                                                                        #метод find_all находит все теги и классы в коде сайта

        for i in data: #создаем цикл for что бы пройтись по всем карточкам сайта 
            card_url = "https://scrapingclub.com" + i.find("a").get("href") #получаем ссылку на описание товара
            yield card_url
def array():
    for card_url in get_url(): #проходимся по списку 

        response = requests.get(card_url, headers=headers) #отправляем get запрос
        sleep(2)#выставляем таймер в 2 сек, что бы была задержка
        soup = BeautifulSoup(response.text, "lxml") #получаем код страницы в норм виде, lxml - это парсер

        data = soup.find("div", class_="my-8 w-full rounded border")
        name = soup.find("h3", class_="card-title").text #получаем название товара 
        price = soup.find("h4").text #цена на товар
        text = soup.find("p", class_="card-description").text #получаем описание товара
        url_img = "https://scrapingclub.com" + soup.find("img", class_="card-img-top").get("src") #получаем ссылку на картинку
        yield name, price, text, url_img