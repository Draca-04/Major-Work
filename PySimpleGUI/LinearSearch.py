# Linear Search in Python
def Linear_Search(List_Of_Athletes, Length_Of_Array, Search_Athlete):

    # Going through array sequencially
    for i in range(0, Length_Of_Array):
        if (List_Of_Athletes[i] == Search_Athlete):
            return i
    return -1


List_Of_Athletes = ["Joe", "Paul", "Susan", "Aaron", "Charlie", "Bob"]
AthleteID = "Bob"
Length_Of_Array = len(List_Of_Athletes)
result = Linear_Search(List_Of_Athletes, Length_Of_Array, AthleteID)
if(result == -1):
    print("Athlete not found")
else:
    print("AthleteID: ", result)
