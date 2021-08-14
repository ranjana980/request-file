import json
import requests
import os
if os.path.isfile("courses.json"):
    with open("courses.json","r") as saral_data:
        text=json.load(saral_data)
else:
    link_1 = "http://saral.navgurukul.org/api/courses"
    Data = requests.get(link_1)
    text=Data.json()
    with open("courses.json","w") as saral_data:
        file2  = json.dump(text,saral_data,indent=4)
i=0
while i<len(text["availableCourses"]):
    Courses_name = (text["availableCourses"][i]["name"])
    print(i+1,".",Courses_name,text["availableCourses"][i]["id"])
    i+=1

# userinput for printing any course

course_no = int(input("entre the any course no : "))
selected_Courses_name = text["availableCourses"][course_no-1]["name"]
parent_id = text["availableCourses"][course_no-1]["id"]
print(selected_Courses_name)
up_nagitation = input("do you want to contine yes or no : ")
if up_nagitation == "no":
    i=0
    while i<len(text["availableCourses"]):
        Courses_name = (text["availableCourses"][i]["name"])
        print(i+1,".",Courses_name,text["availableCourses"][i]["id"])
        i+=1
    course_no = int(input("entre the any course no : "))
    selected_Courses_name = text["availableCourses"][course_no-1]["name"]
    parent_id = text["availableCourses"][course_no-1]["id"]
    print(selected_Courses_name)
# calling parents Api
# new_file=text["availableCourses"][course_no-1]["id"]
if os.path.isfile("parent/parent"+str(parent_id)+".json"):
    with open("parent/parent"+str(parent_id)+".json") as saral_data2:
        Data_2=json.load(saral_data2)
        parents_data=Data_2
else:        
    link_2="https://saral.navgurukul.org/api/courses/" +  str(parent_id) +"/exercises" 
    Data_2 = requests.get(link_2)

    # converting parent data into Json

    parents_data = Data_2.json()

    # pushing data into json file

    with open("parent/parent"+str(parent_id)+".json","w")as saral_data2:
        file3 = json.dump(parents_data,saral_data2,indent=4)
    # for calling parent course

j = 0
while j< len(parents_data["data"]):
    parent_course = parents_data["data"][j]["name"]
    print(" ",j + 1,parent_course)

    # for calling childexercises or slug

    if parents_data["data"][j]["childExercises"] == []:
        slug =parents_data["data"][j]["slug"]
        print("     ","1.",slug)
    else:
        k = 0
        while k < len(parents_data["data"][j]["childExercises"]) :
            child_exercises = parents_data["data"][j]["childExercises"][k]["name"]
            print("     ",k+1,".",child_exercises)
            k = k + 1
    j+=1

# for print one parent course 
      
choose_parent_exercises_no = int(input("entre the parent exercises no: "))
up_nagitation1 = input("enter yes for continue or no for course yes/no: ")
if up_nagitation1 == "no":
    j = 0
    while j < len(parents_data["data"]):
        parent_course = parents_data["data"][j]["name"]
        print(" ",j + 1,parent_course)

        # for calling childexercises or slug

        if parents_data["data"][j]["childExercises"] == []:
            slug = parents_data["data"][j]["slug"]
            print("     ","1.",slug)
        else:
            k = 0
            while k < len(parents_data["data"][j]["childExercises"]) :
                child_exercises = parents_data["data"][j]["childExercises"][k]["name"]
                print("     ",k+1,".",child_exercises)
                k = k + 1
        j = j + 1
    choose_parent_exercises_no = int(input("entre the specific parent exercises : "))
parent_exercises = parents_data["data"][choose_parent_exercises_no-1]["name"]
print(choose_parent_exercises_no,parent_exercises,"id.",parents_data["data"][choose_parent_exercises_no-1]["id"])

#for calling  parent child

if parents_data["data"][choose_parent_exercises_no-1]["childExercises"]== []:
    print("     1.",parents_data["data"][choose_parent_exercises_no-1]["slug"])
else:
    l = 0
    my_list = []
    while l < len(parents_data["data"][choose_parent_exercises_no-1]["childExercises"]):
        print("     ", l+1 ,parents_data["data"][choose_parent_exercises_no-1]["childExercises"][l]["name"])
        child_id=parents_data["data"][choose_parent_exercises_no-1]["id"]
        # for calling childexercises 
        if os.path.isfile("child/child"+str(child_id)+".json"):
            with open("child/child"+str(child_id)+".json") as saral_data3:
                Data_4=json.load(saral_data3)
                parents_data1=Data_4
        else:
            # my_list = []
            slug = (parents_data["data"][choose_parent_exercises_no-1]["childExercises"][l]["slug"])
            link_3= ("http://saral.navgurukul.org/api/courses/" +  str(parent_id) +"/exercise/getBySlug?slug=" + slug )
            Data_4 = requests.get(link_3)
            #converting data into json
            child_exercise_data = Data_4.json()
            #   pusing data into json file
            with open("child/child"+str(child_id)+".json","w") as Saral_data3:
                    file4 = json.dump(child_exercise_data,Saral_data3,indent=4)
            content =child_exercise_data["content"]
            my_list.append(content)
        l=l+1
    choose_child_exercises_no = int(input("entre the question no : "))
    print(my_list[choose_child_exercises_no-1])
    count = choose_child_exercises_no - 1
    while choose_child_exercises_no > 0 :
        next_nagitation3 = input("Enter n for next or p for prevoius: ")
        if choose_child_exercises_no == len(my_list):
            print("next page")
        if next_nagitation3 == "p" :
            if choose_child_exercises_no == 1:
                print("no more questions")
                break
            elif choose_child_exercises_no > 0:
                choose_child_exercises_no = choose_child_exercises_no - 2
                print(my_list[choose_child_exercises_no])
        elif next_nagitation3 == "n":
            if choose_child_exercises_no < len(my_list):
                index = choose_child_exercises_no + 1
                print(my_list[index-1])
                count = count + 1
                choose_child_exercises_no = choose_child_exercises_no + 1 
                if count == (len(my_list)-1) :
                    print("next page")
                    break
