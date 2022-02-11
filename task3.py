import json
def group_by_decade():
    declist=[]
    with open("/home/shivani/Desktop/web scraping/tast2.json") as jsfile:
        data=jsfile.read()
        dic=json.loads(data)
        for i in dic.keys():
            mod=int(i)%10
            dec=int(i)-mod
            if dec not in declist:
                declist.append(dec)
    with open("/home/shivani/Desktop/web scraping/task1.json") as jsfile:
        data=jsfile.read()
        dic=json.loads(data)
    declist.sort()
    moviedec={}
    for i in declist:
        moviedec[i]=[]
        range=i+9
        for index in dic:
            if int(index["year"])>=i and int(index["year"])<=range:
                moviedec[i].append(index)
    with open("task3.json","w")as file2:
        json.dump(moviedec,file2,indent=4)      
group_by_decade()




