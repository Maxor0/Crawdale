from datetime import datetime
import random



SILVER = 2500
GOLD = 3000
PLATINUM = 4000

class Member:
    def __init__(self, id, surname, year_joined, member_type, nights_booked, points):
        self.__ID = id
        self.__Surname = surname
        self.__YearJoined = year_joined
        self.__MemberType = member_type
        self.__NightsBooked = nights_booked
        self.__Points = points


    def GetID(self):
        return self.__ID

    def GetSurname(self):
        return self.__Surname

    def GetMemberType(self):
        return self.__MemberType

    def GetYearJoined(self):
        return self.__YearJoined

    def SetMemberType(self):
        if self.__NightsBooked >= 30 and self.__NightsBooked<100:
            self.__MemberType = "Gold"
        elif self.__NightsBooked >= 100:
            self.__MemberType = "Platinum"

    def GetNightsBooked(self):
        return self.__NightsBooked

    def SetNightsBooked(self, newNights):
        self.__NightsBooked = self.__NightsBooked + newNights

    def SetPoints(self, newNights):
        if self.__MemberType == "Silver":
            self.__Points = self.__Points + SILVER*newNights
        elif self.__MemberType == "Gold":
            self.__Points = self.__Points + GOLD*newNights
        else:
            self.__Points = self.__Points + PLATINUM*newNights

    def GetPoints(self):
        return self.__Points


members = []
def readMembers():
    file = open("SampleData2017.txt", "r")
    for line in file:
        newMember = line.strip()
        newMember = newMember.split(",")
        members.append(Member(newMember[0], newMember[1], int(newMember[2]), newMember[3], int(newMember[4]), int(newMember[5])))
    file.close()

def checkMembers(newID):
    i = 0
    Found = False
    while newID != Member.GetID(members[i]) and i < len(members):
        i += 1
        if newID == Member.GetID(members[i]):
            Found = True
    if Found:
        return True
    else:
        return False
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
        numberOfNights = 0
        while numberOfNights <= 0 or numberOfNights > 14:
            numberOfNights = int(input("How many nights would you like to book? (1-14) \n>"))
        Member.SetNightsBooked(members[i], numberOfNights)
        Member.SetPoints(members[i], numberOfNights)
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
        while repeat!="Y" and repeat!="N":
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