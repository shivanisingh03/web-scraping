from task1 import top_movie_list 
import json
from bs4 import BeautifulSoup
import requests
import os
import pprint

screaped=top_movie_list()

def get_movie_list_details(movies):
    if os.path.exists("/home/shivani/Desktop/web scraping/task5.json") ==True:
        with open("/home/shivani/Desktop/web scraping/task5.json","r")as file:
            data=file.read()
            dic=json.loads(data)
        return dic
    else:
        j=0
        list4=[]
        while j<len(movies):
            url=movies[j]["movie URL"]
            x=requests.get(url)
            soup=BeautifulSoup(x.text,"html.parser")
            main=soup.find("ul",class_="content-meta info")
            all=main.find_all("li",class_="meta-row clearfix")
            my_dict={}

            for i in all:
                my_dict[i.find("div",class_="meta-label subtle").get_text().strip()]=i.find("div",class_="meta-value").get_text().strip().replace("\n",'')
                
            my_dict["name"]=soup.find("h1").text
            list4.append(my_dict)
            j+=1
            
            # print(list4)
        # print(list4)
        with open("task5.json","w")as f:
            json.dump(list4,f,indent=4)
        return list4


# print(get_movie_list_details(screaped[:10]))

task5=get_movie_list_details(screaped)

