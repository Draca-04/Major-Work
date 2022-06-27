# Must pip or pip3 install PySimpleGUI in order to work
# Must pip or pip3 install pandas to work

# imports
from operator import index
import pandas as pd
import PySimpleGUI as sg
import Test_Data as TD


# # Linear Search in Python
# def Linear_Search(List_Of_Athletes, Length_Of_Array, Search_Athlete):

#     # Going through array sequencially
#     for i in range(0, Length_Of_Array):
#         if (List_Of_Athletes[i] == Search_Athlete):
#             print("Athlete ID", i)
#     return -1


# List_Of_Athletes = ["Joe", "Paul", "Susan", "Aaron", "Charlie", "Bob"]
# AthleteID = "Bob"
# Length_Of_Array = len(List_Of_Athletes)
# result = Linear_Search(List_Of_Athletes, Length_Of_Array, AthleteID)
# if(result == -1):
#     print("Athlete not found")
# else:
#     print("AthleteID: ", result)

#Athlete_Name = str(input("Enter Athlete Name () "))

# Search = Linear_Search(TD.AthleteNameList, TD.LenOfAthleteList, Athlete_Name)


def Athlete(): 

    a = True
    b = True
    while b == True:
        b = False
        for i in range(TD.LenOfAthleteList):
            Athlete_Name = input("Enter Athlete Name ")
            if Athlete_Name == TD.AthleteNameList[i].lower():
                AthleteID = TD.AthleteProfileList[i]
                print("Athlete found!")

                while a == True:
                    NEW_time = input("Would you like to add a new time? ")
                    if NEW_time == "yes" or NEW_time == "y" or NEW_time == "Yes" or NEW_time == "Y":
                            Time = input("Print athlete's time eg(11.1) ")
                            AddToList = pd.DataFrame(
                                {"Athlete" : [str(Athlete_Name)],
                            "Times" : [Time]},
                            index = [1])

                            AthleteID = AthleteID.append(AddToList, ignore_index=True)
                            print(AthleteID)

                    else:
                        print(AthleteID)
                        a = False
                        NextAthlete = input("Search another athlete? ")
                        if NextAthlete == "yes" or NextAthlete == "y" or NextAthlete == "Yes" or NextAthlete == "Y":
                            b = True
                        else:
                            b = False
            
            elif Athlete_Name == TD.AthleteNameList[i].upper():
                AthleteID = TD.AthleteProfileList[i]
                print("Athlete found!")

                while a == True:
                    NEW_time = input("Would you like to add a new time? ")
                    if NEW_time == "yes" or NEW_time == "y" or NEW_time == "Yes" or NEW_time == "Y":
                            Time = input("Print athlete's time eg(11.1) ")
                            AddToList = pd.DataFrame(
                                {"Athlete" : [str(Athlete_Name)],
                            "Times" : [Time]},
                            index = [1])

                            AthleteID = AthleteID.append(AddToList, ignore_index=True)
                            print(AthleteID)

                    else:
                        print(AthleteID)
                        a = False
                        NextAthlete = input("Search another athlete? ")
                        if NextAthlete == "yes" or NextAthlete == "y" or NextAthlete == "Yes" or NextAthlete == "Y":
                            b = True
                        else:
                            b = False
            else:
                print("Error")

Athlete()         







    # def Times(TimeID, time, AthleteID, EventID):
    #     pass 
         

    # def Competition(CompID, Date_Event, Event):
    #      Athelete_name = pd.DataFrame(
    #     {"Athlete" : [str(CompID)],
    #     "Times" : [11.5, 11.8, 12.9]},
    #     index = [1, 2, 3])

    # def Event(EventID, Event_Type, CompID):


