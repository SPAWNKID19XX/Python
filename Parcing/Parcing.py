import requests
from bs4 import BeautifulSoup

for i in range(7):
    URL = "https://scrapingclub.com/exercise/list_basic/?page={i+1}"

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "lxml")
    data = soup.findAll("div",class_="col-lg-4 col-md-6 mb-4")


    for obj in data:
        name = obj.find("h4", class_="card-title").text.replace("\n", "")
        price = obj.find("h5").text
        urlImg = "https://scrapingclub.com" + obj.find("img").get("src")
        print(name, "\n\t",price, urlImg)



        