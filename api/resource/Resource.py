import requests
from bs4 import BeautifulSoup

class Resource:
    def __init__(self):
        pass

    @staticmethod
    async def searchGoogle(search):
        page = requests.get("https://www.google.com/search?q="+search)
        soup = BeautifulSoup(page.text, "html.parser")

        search = soup.find("div", {"id": "main"})
        firstParameter = "/url?q="
        endParameter = "/&sa="
        links = []
        
        if search != None:
            tags = search.findAll("a")
            for tag in tags:
                href = tag["href"]
                if firstParameter in href and endParameter in href:
                    links.append(href.split(firstParameter)[1].split(endParameter)[0])
        
        
        return  links