import csv
from scrapper import search_incruit, search_hrd24

def save_to_csv(jobs):

    with open("./downloads.csv", "w", encoding="cp949") as file:

        try:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["No", "회사", "제목", "지역", "상세보기"])

            for i, job in enumerate(jobs):
                csv_writer.writerow([i+1, job["company"], job["title"], job["location"], job["link"]])
        
        except:
            pass

    return 