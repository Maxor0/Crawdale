from datetime import datetime
import random
from Member import Member


members = []
def readMembers():
    file = open("SampleData2017.txt", "r")
    for line in file:
        newMember = line.strip()
        newMember = newMember.split(",")
        members.append(Member(newMember[0], newMember[1], int(newMember[2]), newMember[3], int(newMember[4]), int(newMember[5])))
    file.close()

def checkMembers(newID):
    Found = False
    for i in range(len(members)):
        if newID == Member.GetID(members[i]):
            Found = True
    return Found
def newMemeber():
    surname = input("Please enter your surname \n>")
    newID = surname[0:3] + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(datetime.now().year)[2:4]
    needNew = True
    while needNew:
        needNew = checkMembers(newID)
        newID = surname[0:3] + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(datetime.now().year)[2:4]
    members.append(Member(newID, surname, datetime.now().year, "Silver", 0, 0))
    print(f"Your new member ID is {newID}")

def newBooking():
    ID = input("Please enter your ID \n>")
    i = 0
    Found = False
    while not Found and i <= len(members):
        if ID == Member.GetID(members[i]):
            Found = True
        else:
            i += 1
    if Found:
        number_of_nights = 0
        if Member.GetPoints(members[i]) >= 25000:
            use_points = None
            while use_points != "y" and use_points != "n":
                use_points = input("Would you like to spend your points in this booking? (Y/N) \n>").lower()
            if use_points == "y":
                max_amount = Member.GetPoints(members[i])//25000
                print(f"You can book {max_amount} night(s) with your points")
                if max_amount >= 14:
                    while number_of_nights <= 0 or number_of_nights > 14:
                        number_of_nights = int(input(f"How many nights would you like to book? (1-14) \n>"))
                else:
                    while number_of_nights <= 0 or number_of_nights > max_amount:
                        number_of_nights = int(input(f"How many nights would you like to book? (1-{max_amount}) \n>"))
                subtract_points = -(number_of_nights*25000)
                Member.SetPoints(members[i], subtract_points)
            else:
                while number_of_nights <= 0 or number_of_nights > 14:
                    number_of_nights = int(input(f"How many nights would you like to book? (1-14) \n>"))
                    Member.SetPoints(members[i], number_of_nights)
        else:
            print("You don't have enough points to make a booking with points")
            while number_of_nights <= 0 or number_of_nights > 14:
                number_of_nights = int(input(f"How many nights would you like to book? (1-14) \n>"))
            Member.SetPoints(members[i], number_of_nights)
        Member.SetNightsBooked(members[i], number_of_nights)
    else:
        print("Member not found")

def MemberInfo():
    ID = input("Please enter your ID \n>")
    i = 0
    Found = False
    while not Found and i <= len(members):
        if ID == Member.GetID(members[i]):
            Found = True
        else:
            i += 1
    if Found:
        print(f" Member ID: {Member.GetID(members[i])}, Surname: {Member.GetSurname(members[i])}, Year joined: {Member.GetYearJoined(members[i])}, Membership type: {Member.GetMemberType(members[i])}, Number of nights booked: {Member.GetNightsBooked(members[i])}, Current Points: {Member.GetPoints(members[i])}")
    else:
        print("Member not found")

def Application():
    action = input("Would you like to add a member(1), book more nights(2) or display the information of a member(3)? \n>")
    if action == "1":
        newMemeber()
        repeat = None
        while repeat != "Y" and repeat != "N":
            repeat = input("Would you like to do something else? (Y/N) \n>")
            if repeat == "N":
                return False
            return True
    elif action == "2":
        newBooking()
        repeat = None
        while repeat != "Y" and repeat != "N":
            repeat = input("Would you like to do something else? (Y/N) \n>")
            if repeat == "N":
                return False
            return True
    elif action == "3":
        MemberInfo()
        repeat = None
        while repeat != "Y" and repeat != "N":
            repeat = input("Would you like to do something else? (Y/N) \n>")
            if repeat == "N":
                return False
            return True
    else:
        print("That is not a valid option")
        return True

more = True
readMembers()
while more:
    more = Application()