import requests
from bs4 import BeautifulSoup
import re

# res = requests.get("http://127.0.0.1:5500/REQUEST/b.html")
# soup = BeautifulSoup(res.text,'html.parser')
# metas = soup.find_all('meta')
# for meta in metas:
#     print(meta)

# res = requests.get("http://127.0.0.1:5500/REQUEST/some.html")

# soup = BeautifulSoup(res.text,"html.parser")
# forms = soup.find_all('input')
# for form in forms:
#     print(form)


# res = requests.get('http://127.0.0.1:5500/REQUEST/d.html')
# soup = BeautifulSoup(res.text,'html.parser')

# script = soup.find('script')
# re = r'FLAG\{.*?\}'
# print(script)
# flag = script.find("FLAG")
# print(flag)

html_txt = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
</head>
<body>
    <h1>Foydalanuvchi paneli</h1>
    <p>Hisobingiz muvaffaqiyatli faollashtirildi.</p>

    <script>
        const username = "guest";
        const role = "viewer";
        const secretKey = "FLAG{j4v4scr1pt_v4r_1s_h1dd3n}";
        console.log("Dashboard loaded");
    </script>
</body>
</html>"""

regex = r"FLAG\{.*?\}"
request = re.findall(regex,html_txt)
print(request)