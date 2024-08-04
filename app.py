from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/getlink", methods=["GET"])
def getlink():
    url = "https://bingotingo.com/best-social-media-platforms/"
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html, "html.parser")
    job_desc = soup.find('a', class_='su-button su-button-style-soft su-button-wide')
    
    l = str(job_desc)
    list = l.split()
    for i in list:
        if "href" in i:
            j = i.lstrip('href=')
            job_desc = j.replace('"', '')
    
    url2 = job_desc
    page2 = requests.get(str(url2))
    html2 = page2.content
    soup2 = BeautifulSoup(html2, "html.parser")
    divv = soup2.find('div', class_="col-md-8")
    div = BeautifulSoup(str(divv), "html.parser")
    div22 = div.find('div', class_='min-vh-100 d-flex justify-content-center align-items-center')
    div2 = BeautifulSoup(str(div22), "html.parser")
    a = div2.find('a', class_="item-wrapper bg-white -outlined text-dark-1 shadow-3")
    
    hi = str(a)
    li = hi.split()
    b = ''
    for i in li:
        if "href" in i:
            b = i.lstrip('href=')
    
    g = b.replace('"', '')
    finallink = f'{g}'
    
    def remove(string):
        return string.replace(" ", "")
    
    if "canva" in finallink:
        return jsonify({"link": remove(finallink)})
    else:
        return jsonify({"link": "No"})

if __name__ == "__main__":
    app.run()
