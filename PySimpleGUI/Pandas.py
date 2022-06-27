# Must pip or pip3 install PySimpleGUI in order to work
# Must pip or pip3 install pandas to work

# imports
from operator import index
import pandas as pd
import PySimpleGUI as sg
import Test_Data as TD



def Athlete(): 

    a = True
    b = True
    while b == True:
        b = False
        for i in range(TD.LenOfAthleteList):                    # Use the range of the list to search through it
            Athlete_Name = input("Enter Athlete Name ")         # Must be strictly uppercase or lowercase
            if Athlete_Name == TD.AthleteNameList[i].lower():   # Checks if the name corresponds with the list
                AthleteID = TD.AthleteProfileList[i]            # Assigns a variable to the corresponding name
                print("Athlete found!")                         # Confirmation

                while a == True:
                    NEW_time = input("Would you like to add a new time? ")                              
                    if NEW_time == "yes" or NEW_time == "y" or NEW_time == "Yes" or NEW_time == "Y" or NEW_time == "YES":    # Given a few different ways of responding, responses such as ye or Ye will not be accepted
                            Time = input("Print athlete's time eg(11.1) ")                                                   # Variable assigned to add time
                            
                            # Dataframe used to append to the existing athlete
                            AddToList = pd.DataFrame(
                                {"Athlete" : [str(Athlete_Name)],
                            "Times" : [Time]},
                            index = [1])

                            AthleteID = AthleteID.append(AddToList, ignore_index=True)  # Adds (AddToList) to the athletes profile, makes a true index rather than having to constantly add 5, 6, 7...
                            print(AthleteID)

                    else:
                        print(AthleteID) # If user does not want to add a new time they can simply view stats here
                        a = False
                        NextAthlete = input("Search another athlete? ")
                        if NextAthlete == "yes" or NextAthlete == "y" or NextAthlete == "Yes" or NextAthlete == "Y" or NextAthlete == "YES": # Given a few different ways of responding, responses such as ye or Ye will not be accepted
                            b = True
                        else:
                            b = False
            
            # Exactly the same as first if statement just checking if response was in uppercase
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
                print("Error")  # Error message if athlete is not found... Error occurs temporarily if you search for athletes that are not at index 0

Athlete()   # Runs function










