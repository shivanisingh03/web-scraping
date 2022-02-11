# import json


# with open ("task13.json","r") as f:
#     movie_cast_list=json.load(f)
# # print(movie_cast_list)

# cast_name_list=[]
# for i in range(len(movie_cast_list)):
#     # print(i)
#     for j in movie_cast_list [i].values():
#         # print(j)
#         for k in j.values():
        
#             # print(k)
#             if k not in cast_name_list:
#                 cast_name_list.append(k)        
# # print(cast_name_list)




# cast_id_list=[]
# for i in range(len(movie_cast_list)):
#     # print(i)
#     for j in movie_cast_list [i].values():
#         # print(j)
#         for k in j:
        
#             # print(k)
#             if k not in cast_id_list:
#                 cast_id_list.append(k)        
# # print(cast_id_list)
# # for i in cast_name_list:

# cast_item_count=[]
# for i in cast_name_list:
#     c=0
#     for m in range(len(movie_cast_list)):
#         for j in movie_cast_list [m].values():
#             for k in j.values():  
#                 # print(k)         
#                 if k ==i:
#                     # print(i)
#                     c=c+1
#     cast_item_count.append(c)     
# print(cast_item_count)


# dic={}
# for i in range(len(cast_id_list)):
#     d1={}
#     # dic[i]=d1
#     # for j in range(len(cast_name_list)):
#     d1["Name"]=cast_name_list[i]
#     d1["Num Of Movies"]=cast_item_count[i]
#     dic[cast_id_list[i]]=d1
# print(dic)


# with open("Task15.json","w") as f:
#     json.dump(dic,f,indent=4)






from bs4 import BeautifulSoup
import json
import requests
from task13 import scrape_movie_details

def actor():
    with open("task1.json", 'r') as file:
        data=json.load(file)
    movie_url_list=[]
    for i in data:
        movie_url_list.append(i['movie URL'])
    # print(movie_url_list)
    lis=[]
    for i in range(5):
        lis.append(scrape_movie_details(movie_url_list[i]))
        # print(lis)
    dict={}
    for i in lis:
        for j in i["cast"]:
            if j  not in dict:
                dict.update({j:[]})
    # print(dict)
    
    for i in dict:
        for j in lis:
            if i in j["cast"]:
                for k in j["cast"]:
                    if i==k:
                        continue
                    dict[i].append(k)
                    print(dict)
        
    with open('task14.json',  'w') as file:
        json.dump(dict, file, indent=4)
actor()

