from task1 import top_movie_list 
import json
from bs4 import BeautifulSoup
import requests
import os
import time
import pprint
import random


screaped=top_movie_list()
url_list=[]
for i in screaped:
    url_list.append(i["movie URL"])

def get_movie_list_details(movies_list):
    time_sleep=random.randint(1,3)
    list4=[]
    for movies in movies_list:
        movie_name=movies[33:]
        if os.path.exists(movie_name+".json") ==True:
            with open(movie_name+".json","r")as file:
                data=file.read()
                dic=json.loads(data)
            list4.append(dic)
        else:
            time.sleep(time_sleep)
            x=requests.get(movies)
            soup=BeautifulSoup(x.text,"html.parser")
            main=soup.find("ul",class_="content-meta info")
            all=main.find_all("li",class_="meta-row clearfix")
            my_dict={}
            for i in all:
                my_dict[i.find("div",class_="meta-label subtle").get_text().strip()]=i.find("div",class_="meta-value").get_text().strip().replace("\n",'')
                    
            my_dict["name"]=soup.find("h1").text
            list4.append(my_dict)
            with open(movie_name+".json","w")as f:
                json.dump(my_dict,f,indent=4)
                
    return list4
pprint.pprint(get_movie_list_details(url_list))


