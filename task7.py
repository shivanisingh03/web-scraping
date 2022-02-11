# import json

# def final(text):
#     return "".join(text.split())

# def get_lang_count():
#     file=open("task5.json","r")
#     var=json.load(file)
#     list=[]
#     for i in var:
#         f=final(i["Director:"])
#         temp=f.split(",")
#         for j in temp:
#             if j not in list:
#                 list.append(j)
#                 # print(list)
#     print(list)
#     dict={}
#     for j in list:
#         # print(j)
#         i=0
#         count=0
#         while i<len(var):
#             # print(i)
#             if j in final(var[i]["Director:"]).split(","):
#                 count+=1
#             i+=1
#         dict[j]=count

#     with open("task7.json","w") as f:
#         json.dump(dict,f,indent=4)

# get_lang_count()


import json

def final(text):
    return "".join(text.split())

def get_lang_count():
    file=open("task5.json","r")
    var=json.load(file)
    print(var)
    list=[]
    for i in var:
        f=final(i["Director:"])
        if f not in list:
            list.append(f)
            # print(list)
    dict={}
    for j in list:
        # print(j)
        i=0
        count=0
        while i<len(var):
            # print(i)
            if j==final(var[i]["Director:"]):
                count+=1
            i+=1
        dict[j]=count

    with open("task7.json","w") as f:
        json.dump(dict,f,indent=4)

get_lang_count()