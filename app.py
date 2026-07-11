from flask import Flask, render_template, request, send_file, redirect
from scrapper import search_incruit, search_hrd24, search_saramin
from file import save_to_csv

app = Flask(__name__)

db = {

}

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/search')
def search():
    keyword = request.args.get("keyword")
    print(keyword)

    if keyword == "":
        return redirect('/')

    incruit = search_incruit(keyword, 2)
    hrd24 = search_hrd24(keyword, 2)
    saramin = search_saramin(keyword, 2)

    return render_template("search.html", jobs1 = enumerate(incruit), jobs2 = enumerate(hrd24), jobs3 = enumerate(saramin), keyword = keyword, count = (len(incruit) + len(hrd24) + len(saramin))) # html에서 enumerate를 사용할 수 없어서 미리 묶어서 보내기

@app.route("/file")
def download_csv():
    
    keyword = request.args.get("keyword")
    incruit = search_incruit(keyword, 2)
    hrd24 = search_hrd24(keyword, 2)
    saramin = search_saramin(keyword, 2)
    jobs = incruit + hrd24 + saramin
    save_to_csv(jobs)

    return send_file("./downloads.csv", as_attachment=True)


# @app.route('/hello')
# def hello():
#     return "안녕하세요"

if __name__ == "__main__":
    app.run(debug=True)