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


    def GetMemberType(self):
        return self.__MemberType

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

readMembers()