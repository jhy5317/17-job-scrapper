import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Whale/4.38.386.14 Safari/537.36"
}

# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# print(r.status_code)


def search_incruit(keyword, page = 1):

    incruit_jobs = []

    for i in range(page):
    # 인크루트
        page = 30 * i
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"
        r = requests.get(url, headers = headers)
        # print(r.text)

        soup = BeautifulSoup(r.text, "html.parser")
        lis = soup.find_all("li", class_ = "c_col")

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
# incruit_jobs = [
#     {
#         "company": company,
#         "title": title,
#         "location": location,
#         "link": link
#      }
# ]

def search_hrd24(keyword, page = 1):

    hrd24_jobs = []

    for i in range(1, page + 1):
        # 고용24
        url = f"https://www.work24.go.kr/cm/f/c/0100/selectUnifySearch.do?topQuerySearchArea=tb_workinfo&topQueryData={keyword}&startCount={i}"
        r = requests.get(url, headers = headers)
        # print(r.text)

        soup = BeautifulSoup(r.text, "html.parser")
        lis = soup.find("ul", class_ = "srch_list_default").find_all("li")
        try:

            for li in lis:
                company = li.find("dl", class_ = "dl_list").find("strong", class_ = "b1_sb").text
                title = li.find("dd").find("a").text.strip()
                location = li.find("div", class_ = "vline_group type2 small").find_all("span", class_ = "item")[4].text.strip("근무지 ")
                link = li.find("dd").find("a").get("href")

                job_data = {
                    "company": company,
                    "title": title,
                    "location": location,
                    "link": link
                }
                hrd24_jobs.append(job_data)

        except:
            pass

    print(location)
    print(lis)

    return hrd24_jobs


# hrd_jobs = [
#     {
#         "company": company,
#         "title": title,
#         "location": location,
#         "link": link
#      }
# ]

def search_saramin(keyword, page = 1):

    saramin_jobs = []

    url = f"https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={keyword}&recruitPage={page}&recruitSort=relation&recruitPageCount=40"
    r = requests.get(url, headers = headers)
    print(r)

    soup = BeautifulSoup(r.text, "html.parser")
    lis = soup.find_all("div", class_ = "item_recruit")

    for li in lis:
        company = li.find("strong", class_ = "corp_name").text.strip("\n ")
        title = li.find("a", class_ = "data_layer").find("span").text
        location = li.find("div", class_ = "job_condition").find("span").text
        link = li.find("a", class_ = "data_layer").get("href")

        job_data = {
            "company": company,
            "title": title,
            "location": location,
            "link": link
        }

        saramin_jobs.append(job_data)

    return saramin_jobs
