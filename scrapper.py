import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Whale/4.38.386.14 Safari/537.36"
}

# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# print(r.status_code)

def search_incruit(keyword):

    # 인크루트
    url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"
    r = requests.get(url)
    # print(r.text)

    soup = BeautifulSoup(r.text, "html.parser")
    lis = soup.find_all("li", class_ = "c_col")

    incruit_jobs = []

    for li in lis:
        company = li.find("a", class_ = "cpname").text
        title = li.find("div", class_ = "cell_mid").find("div", class_ = 'cl_top').find("a").text
        location = li.find("div", class_ = "cl_md").find_all("span")[0].text
        link = li.find("div", class_ = "cell_mid").find("div", class_ = 'cl_top').find("a").get("href")

        job_data = {
            "company": company,
            "title": title,
            "location": location,
            "link": link
        }

        incruit_jobs.append(job_data)

    return incruit_jobs

def search_hrd24(keyword):

    # 고용24
    url = f"https://www.work24.go.kr/cm/f/c/0100/selectUnifySearch.do?topQuerySearchArea=tb_workinfo&topQueryData={keyword}"
    r = requests.get(url)
    # print(r.text)

    soup = BeautifulSoup(r.text, "html.parser")
    lis = soup.find("ul", class_ = "srch_list_default").find_all("li")

    hrd24_jobs = []

    for li in lis:
        company = li.find("dl", class_ = "dl_list").find("strong", class_ = "b1_sb").text
        title = li.find("dd").find("a").text.strip()
        location = li.find("div", class_ = "vline_group type2 small").find_all("span", class_ = "item")[4].text
        link = li.find("dd").find("a").get("href")

        job_data = {
            "company": company,
            "title": title,
            "location": location,
            "link": link
        }

        hrd24_jobs.append(job_data)

    return hrd24_jobs