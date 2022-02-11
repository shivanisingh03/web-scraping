from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint
from task1 import top_rated_movies
data=top_rated_movies()
# print(data)

def Main_fun(data):
    Scrap_data_list=[]
    def Scrap_movie_details(link,MovieName):
        d1={}
        link_data=requests.get(link)

        soup=BeautifulSoup(link_data.text,'html.parser')     
        d1["Name"]=MovieName
        movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()     
        d1["Bio"]=movie_bio
        alltitle=soup.find_all("div",class_="meta-label subtle")
        allvalue=soup.find_all("div",class_="meta-value")
        

        for i in range(len(alltitle)):
            d1[alltitle[i].get_text().strip()]=allvalue[i].get_text().strip()
        # pprint(d1)
        return d1

    movie_details_list=[]
    # # print(data)

    
        # print(data[i]["link"])
    for i in data:
        for j in i:
            MovieName=i["Name"]
            if j=="link":
                # print(i[j])
                movie_details_dic=Scrap_movie_details(i[j],MovieName)
                # print(movie_details_dic)
                
                movie_details_list.append(movie_details_dic)

    print(movie_details_list)

    with open("2Scrap_Movie_details4.json","w") as f:
        json.dump(movie_details_list,f,indent=4)
        
data4=Main_fun(data)