import pprint
from bs4 import BeautifulSoup               #for importing beautifulsoup 
import requests                                  #importing requeats module
import json                                       #importing json

# def  top_rated_movies():                                        
#     if os.path.exists("/home/shivani/Desktop/web scraping/task1.json")==True:        #for checking the json file is exists or not 
#         with open("/home/shivani/Desktop/web scraping/task1.json","r")as file:
#             data=file.read()
#             dic=json.loads(data)
#         return dic
#     else:                                                                                 #if the file not exists that that code will be run
#         adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"     # side link
#         adventure_api=requests.get(adventure_url)                                                        #for getting 
#         htmlcontent=adventure_api.content
#         # print(htmlcontent)
#         soup=BeautifulSoup(htmlcontent,"html.parser")                         #for changing data in html text
#         table_tag=soup.find("table",class_="table")                          #ye puri table 
#         tr=table_tag.find_all("tr")                                         # table ke under tr h jo us ke under sari chize h 
#         top_movie=[]                                                        #empty list
#         for i in tr:                                                        #tr pr loop chalaya hai
#             movie_rank=i.find_all("td",class_="bold")                       #it's rank area 
#             for j in movie_rank:                                             # rank pr loop chalaya hai 
#                 rank=j.get_text()                                            # rank serial ko get kiya hai
#                 # print(rank)
#             movie_rating=i.find_all("span",class_="tMeterScore")            # ratting area
#             for rate in  movie_rating:                                        #
#                 rating=rate.get_text().strip()
#                 # print(rating)
#             movie_name=i.find_all("a",class_="unstyled articleLink")
#             for name in movie_name:
#                 title=name.get_text().strip()
#                 list=title.split()
#                 # print(title)
#                 # print(list)
                
#                 year=list[-1][1:5]
#                 # print(year)
                
#                 year1=int(year)
#                 # print(year1)
                
#                 name_lenght=len(list)-1
#                 name=""
#                 for l in range(name_lenght):
#                     name+=""
#                     name+=list[l]
#                 movie_name=name
#                 # print(movie_name)
                
#             movie_reviews=i.find_all("td",class_="right hidden-xs")
#             for rev in movie_reviews:
#                 reviews=rev.get_text()
#                 # print(reviews)
#             url=i.find("a",class_="unstyled articleLink")
#             for i in url:
#                 link=i["href"]
#                 movie_link="https://www.rottentomatoes.com"+link
#                 # print(movie_link)
#                 details={"movie_rank":rank,"movie_rating":rating,"movie_name":movie_name,"movie_reviews":reviews,"movie URL":movie_link,"year":year1}
#                 top_movie.append(details.copy())
#                 # print(top_movie)
                
#                 # print(rank,movie_name,rating)
#         with open("task1.json","w")as file:
#             json.dump(top_movie,file,indent=4)
#         return top_movie
            
        
        
# screaped=top_rated_movies()        
      