import requests
import json
import os

file=os.path.exists("/home/rhutujapatil/Desktop/Request/course_name.json")
if file==True:
    with open("course_name.json","r") as m:
        info=json.load(m)
    print("course_name :")
    for i in range(len(info)):
        for k,v in info[i].items():
            if k=="name":
                print(i+1,v," :",info[i]["id"])
    choose_cource=int(input("which course you want :"))
    choose_cource1=choose_cource-1
    print(info[choose_cource1]["name"])                                                                                                                 
    print(info[choose_cource1]["id"])
else:
    print("this file is not exist 1 :")

# file=os.path.exists("cources_exercise.json")   
file=os.path.exists("/home/rhutujapatil/Desktop/Request/parentid_file.json")
if file==True:
    with open("parentid_file.json","r") as m:
        parent_id_data=json.load(m)
    
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
        elif k["parent_exercise_id"]==k["id"]:
            print(s1,k["name"])
            s1+=1
            l1.append(k)
            new_num=1
        elif k["parent_exercise_id"]!=k["id"]:
            print(" ",new_num,k["name"])
            new_num+=1
            l2.append(k)
    with open(" list1.json","w")as g:
        json.dump(l1,g,indent=4)
    with open(" list2.json","w")as g:
        json.dump(l2,g,indent=4)
else:
    print("this file is not exist 2 :")
    
file=os.path.exists("/home/rhutujapatil/Desktop/Request/ list1.json")
if file==True:
    with open ("/home/rhutujapatil/Desktop/Request/ list1.json")as g:
    # with open(" list1.json","r")as g:
        list1=json.load(g)
    # l1=[]
    parent=int(input("enter the parent exercise do want:"))
    for w in l1:
        if w["parent_exercise_id"]==w["id"]:
            print(l1[parent-1]["name"])
            num=(l1[parent-1]["id"])                                                                                                                                                                                                                                                                                                                                                                                                                                            
            break
    var=[]
    var3=[]
    num=(l1[parent-1]["id"])
    new_num1=1
    for a in l2:
        if a["parent_exercise_id"]==num:
            print(" ",new_num1,a["name"])
            var.append(a["name"])
            var3.append(a["content"])
            new_num1+=1
else:
    print("this file is not exist 3 :")
file=os.path.exists("/home/rhutujapatil/Desktop/Request/list2.json")
if file==True:
    with open("list2.json","r")as g:
        list2=json.load(g)
    child=int(input("enter the child exercise do u want :"))
    for s in range(len(var)):
        if (child-1)==s:
            print(var[s])
            print(var3[s])
        again_enter_childid=int(input("again enter the child exercise do u want :"))
        for s in range(len(var)):
            if (again_enter_childid-1)==s:
                print(var[s])
                print(var3[s])    
                
else:
    print("this file is not exist 4 :")