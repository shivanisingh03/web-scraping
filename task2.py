import json
import pprint
from task1 import top_movie_list 
scrapped1=top_movie_list()
def group_by_year(movies):
    years=[]
    for i in movies:
        # print(i)
        year=i["year"]
        # print(year)
        if year not in years:
            years.append(year)
    # print(years)
    movies_dic={i:[] for i in years}
    # print(movies_dic)
    for i in movies:
        # print(i)
        year=i["year"]
        movies_dic[year].append(i)
        # for x in movies_dic:
        #     # print(x)
        #     if str(x)==str(year):
        #         # print(x,year)
        #         # print(year)
        #         movies_dic[x].append(i)
    # pprint.pprint(movies_dic)
    with open("tast2.json","w") as file:
        json.dump(movies_dic,file,indent=4)  
        return movies_dic         
group_by_year(scrapped1)


    
        
        


















