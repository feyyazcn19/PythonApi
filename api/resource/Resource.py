import requests
from bs4 import BeautifulSoup
import json
from decouple import config
from .Response import Response
import os


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
                    links.append(href.split(firstParameter)
                                 [1].split(endParameter)[0])

        return links

    @staticmethod
    async def serperSearch(serach):
        res = Response()
        
        try:
            url = "https://google.serper.dev/search"
            payload = json.dumps({
                "q": serach,
                "gl": "tr",
                "hl": "tr",
                "autocorrect": True
            })
            headers = {
                'X-API-KEY': os.getenv("API_SERPER_KEY"),
                'Content-Type': 'application/json'
            }

            response = requests.post(url=url, data=payload, headers=headers)
            
            res.response=json.loads(response.text)["organic"]
            res.responseCode=200
        except:
            res.response=await Resource.searchGoogle(serach)
            res.responseCode=201

        return res

