import requests
from bs4 import BeautifulSoup

# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# print(r.status_code)

keyword = "python"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
result = soup.find_all("li", class_="c_col")

print(len(result))
