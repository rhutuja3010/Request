import requests
import json
r=requests.get('https://api.merakilearn.org/courses')
info=json.loads(r.text)
# print(r)
# info=r.json()
with open ("course_name.json","w") as f:                                                                                                                               
    json.dump(info,f,indent=4)
print("course_name :")

for i in range(len(info)):
    for k,v in info[i].items():
        if k=="name":
            print(i+1,v," :",info[i]["id"])
choose_cource=int(input("which course you want :"))
choose_cource1=choose_cource-1
print(info[choose_cource1]["name"])                                                                                                                 
print(info[choose_cource1]["id"])

p=requests.get("https://api.merakilearn.org/courses/"+ info[choose_cource1]["id"]+" "+ "/exercises")
parent_id_data=json.loads(p.text)
# parent_id_data=p.json()
with open("parentid_file.json","w") as file:
    json.dump(parent_id_data,file,indent=4)

s1=1
s2=1
l1=[]
l2=[]  
for k in parent_id_data['course']['exercises']:
    if k["parent_exercise_id"]==None:
        print(s1,k["name"])
        print("  ",s2,"  ",k["slug"])
        s1+=1
        # new_num=1
        l1.append(k)
        l2.append(k)
        # print(l1)
        # print(l2)
    elif k["parent_exercise_id"]==k["id"]:
        print(s1,k["name"])
        s1+=1
        l1.append(k)
        new_num=1
    elif k["parent_exercise_id"]!=k["id"]:
        print(" ",new_num,k["name"])
        new_num+=1
        l2.append(k)
        # new_num+=1

user=input("what do you what previous or next(n/p) :")
if user=="p":
    print("cources name :")
    for j in range(len(parent_id_data)):
        for k,v in info[j].items():
            if k=="name":
                print(j+1,v," :",info[j]["id"])

    choose_parent_id=int(input("which cource you want :"))
    choose_parent_id1=choose_parent_id-1
    print(info[choose_parent_id1]["name"])
    print(info[choose_parent_id1]["id"])

    h=requests.get("https://api.merakilearn.org/courses/"+info[choose_parent_id1]["id"]+" "+ "/exercises")
    parent_id_data=h.json()
    with open("courses_exercise.json","w")as n:
        json.dump(parent_id_data,n,indent=4)
    s1=1
    s2=1
    l1=[]
    l2=[]
    for k in parent_id_data["course"]["exercises"]:
        if k["parent_exercise_id"]==None:
            print(s1,k["name"])
            print(" ",s2,k["slug"])
            s1+=1
            # new_num=1
            l1.append(k)
            l2.append(k)
        elif k["parent_exercise_id"]==k["id"]:
            print(s1,k["name"])
            s1+=1
            l1.append(k)
            l2.append(k)
            new_num=1
        elif  k["parent_exercise_id"]!=k["id"]:
            print(" ",new_num,k["name"])
            new_num+=1
            l2.append(k)
with open(" list1.json","w")as f:
    json.dump(l1,f,indent=4)  
with open("list2.json","w")as f:
    json.dump(l2,f,indent=4)
 
parent=int(input("enter the parent exercise do want:"))
for w in l1:
    if w["parent_exercise_id"]==w["id"]:
        print(l1[parent-1]["name"])
        num=(l1[parent-1]["id"])
        # s1+=1
        break
num=(l1[parent-1]["id"])
var=[]
var3=[]
new_num1=1
for a in l2:
    if a["parent_exercise_id"]==num:
        print(" ",new_num1,a["name"])
        var.append(a["name"])
        var3.append(a["content"])
        new_num1+=1
        # s1+=1

child=int(input("enter the child exercise do u want :"))
for s in range(len(var)):
    if (child-1)==s:
        print(var[s])
        print(var3[s])



