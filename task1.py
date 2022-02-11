import pprint
from bs4 import BeautifulSoup             
import requests                              
import json                                     
def top_movie_list():

    adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"     
    adventure_api=requests.get(adventure_url)                                                        
    soup=BeautifulSoup(adventure_api.text,"html.parser") 
    table_tag=soup.find("table",class_="table")  
    tr=table_tag.find_all("tr")      
    top_movie=[]
    for i in tr[1:]:
        rank1=i.find("td",class_="bold").get_text().strip()
        rank=rank1[:0]+rank1[:-1]
        rating=i.find("span",class_="tMeterScore").get_text().strip()
        names=i.find("a",class_="unstyled articleLink").get_text().strip()
        list=names.split()
        year=list[-1][1:5]
        movie_name=names[:0]+names[:-6]
        reviews=i.find("td",class_="right hidden-xs").get_text()
        url=i.find("a",class_="unstyled articleLink")["href"]
        movie_link="https://www.rottentomatoes.com"+url
        details={"movie_rank":rank,"movie_rating":rating,"movie_name":movie_name,"movie_reviews":reviews,"movie URL":movie_link,"year":year}
        top_movie.append(details)
    with open("task1.json","w")as file:
        json.dump(top_movie,file,indent=4)
        return top_movie
movie=top_movie_list()

        















