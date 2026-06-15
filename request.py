# import requests

# user = int(input("nechta fakt hohlaysiz:"))

# for i in range(1,user + 1):
#     response = requests.get('https://app.exchangerate-api.com/')

#     print(response.status_code)
#     print(response.json())  

# url = requests.get('https://v6.exchangerate-api.com/v6/6e03a237ba410e1a818e59dc/latest/USD')


# import requests

# # Valyutalarni kiritish
# from_currency = input("Qaysi valyutadan: ").upper()
# to_currency = input("Qaysi valyutaga: ").upper()
# amount = float(input("Miqdor: "))

# # API so'rovi
# import requests

# res = requests.get('https://v6.exchangerate-api.com/v6/6e03a237ba410e1a818e59dc/latest/USD')

# input_ = input("Qaysi valyuta: ").upper()
# input2_ = input("Qaysi valyuta ga ogirmoqchisiz: ").upper()
# amount = int(input("Qancha miqdorda ogirmoqchisiz: "))

# data = res.json()
# try:
#     if res.status_code == 200:
#         val1 = data["conversion_rates"][f"{input_}"]
#         val2 = data["conversion_rates"][f"{input2_}"]
#         miqdor = amount * val2
#         print(f"miqdor {miqdor:.2f}")
# except KeyError:
#     print("Iltimos son orniga valyuta kirgizing")

# # import requests


# data = {
#     "name":"ALI",
#     "age":0
# }

# res = requests.patch('https://jsonplaceholder.typicode.com/posts/3',json=data)

# print(res.status_code)
# print(res.json())


# from bs4 import BeautifulSoup
# import requests

# res = requests.get("https://uzmovi.net/")
# sup = BeautifulSoup(res.text,'html.parser')
# for comment in sup.find_all(""):
#     print(comment.text)


# import requests
# from bs4 import BeautifulSoup,Comment

# res = requests.get("http://127.0.0.1:5500/REQUEST/html.html")
# sup = BeautifulSoup(res.text,'html.parser')

# comments = sup.find_all(string=lambda text: isinstance(text, Comment))

# for i in comments:
#     print(i)

# import requests
# from bs4 import BeautifulSoup

# res = requests.get("http://127.0.0.1:5500/REQUEST/v.html")
# sup = BeautifulSoup(res.text,'html.parser')
# founded = sup.select('a[href][data-secret]')
# print(founded)
# print(res.status_code)
# for i in founded:
#     print(i.get("data-secret"))


# import requests
# from bs4 import BeautifulSoup

# res = requests.get('http://127.0.0.1:5500/REQUEST/b.html')
# sup = BeautifulSoup(res.text,"html.parcer")

# print(res.status_code)

