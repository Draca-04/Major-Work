import pandas as pd 




AthleteName1 = "Paul"
AthleteName2 = "Joe"
AthleteName3 = "Bill"
AthleteName4 = "Usain"

AthleteNameList = ["Paul", "Joe", "Bill", "Usain"]
LenOfAthleteList = len(AthleteNameList)-1
 
Athlete1 = pd.DataFrame(
    {"Athlete" : [str(AthleteNameList[0])],
    "Times" : [11.94, 12.13, 12.19, 12.38],
    "Event" : ["Olympic Park", "Olympic Park", "Olympic Park", "Olympic Park"]},
    index = [1, 2, 3, 4])

Athlete2 = pd.DataFrame(
    {"Athlete" : [str(AthleteNameList[1])],
    "Times" : [16.94, 12.43, 13.19, 11.38],
    "Event" : ["Olympic Park", "Olympic Park", "Olympic Park", "Olympic Park"]},
    index = [1, 2, 3, 4])

Athlete3 = pd.DataFrame(
    {"Athlete" : [str(AthleteNameList[2])],
    "Times" : [15.94, 14.33, 12.09, 13.38],
    "Event" : ["Olympic Park", "Olympic Park", "Olympic Park", "Olympic Park"]},
    index = [1, 2, 3, 4])

Athlete4 = pd.DataFrame(
    {"Athlete" : [str(AthleteNameList[3])],
    "Times" : [9.95, 9.58, 9.69, 9.63],
    "Event" : ["Olympic Park", "Olympic Park", "Olympic Park", "Olympic Park"]},
    index = [1, 2, 3, 4])

df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'), index=['x', 'y'])


AthleteProfileList = [Athlete1, Athlete2, Athlete3, Athlete4]

