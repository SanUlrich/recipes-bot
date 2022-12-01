import random
import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

time_for_eat = {
    'Завтрак': '926',
    'Обед': '927',
    'Ужин': '928'
}
max_pages = 9999
ua = UserAgent()
headers = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "user-agent": ua.random
}


# Цикл для обхода всех страниц
for p in range(max_pages):
    base_url = f'https://www.russianfood.com/recipes/bytype/?fid=928&page={p + 1}#rcp_list'
    print(f'Собираю данные со страницы {base_url}')
    req = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    next_button = len(soup.find('div', class_='page_selector_o').find('td').find_all('a'))
    time.sleep(int(random.random() * 3 + 2))

    # Собираю список из id рецептов завтраков
    lnk = soup.find('div', class_='recipe_list_new').find_all(class_='title')

    with open('../data/dinner.py', 'a') as file:
        for item in lnk:
            file.write(item.a.get('href')[24:] + ', ')
        file.close()
    # Проверка на последнюю страницу
    if p > 2 and next_button == 1:
        print(f'Всего страниц {p+1}')
        break

# with open(f'test.html', 'r') as file:
# #     file.write(r.text)
#     src = file.read()

#

#
# current_pagination = int(soup.find('div', class_='pages').find('span').string)
# next_button = soup.find('div', class_='page_selector_o').find_all('a')[0]
#
# print(next_button)
# print(current_pagination)


#
# print(breakfast_id)


# for i in l.find_all('a'):
#     print(i.get('href'))




# def get_recipe_text():
#
#
# def get_breakfast_list():
#
#
#     r = requests.get(url=url, headers=headers)
#
#
#
#
#     soup = BeautifulSoup(src, 'lxml')
#     p = 1
#     while url:
#
#     print(qty_pages)



    # qty_pages = soup.find('div', class_='pages').find_all('a')[-1]
    # recipe_title = soup.find("h1", class_="title").text
    # recipe_desc = soup.find("td", class_="padding_l padding_r").find("p").text
    # recipe_id = URL.split('rid=')[-1]
    # ing_table = soup.find("table", class_="ingr").find_all("span", class_="")
    #
    # ingredients = []
    # for item in ing_table:
    #     ingredients.append(item.text)
    #
    # print(f'{recipe_title} | {recipe_desc} | {ingredients} | {recipe_id}')


# def main():
#     get_breakfast_list()
#
#
# if __name__ == '__main__':
#     main()

