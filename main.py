from dataclasses import dataclass

@dataclass
class Member:
    ID: str
    Surname: str
    YearJoined: int
    MemberType: str
    NightsBooked: int
    Points: int


members = []

def readMembers():
    file = open("SampleData2017.txt", "r")
    for line in file:
        newMember = line.strip()
        newMember = newMember.split(",")
        members.append(Member(newMember[0], newMember[1], int(newMember[2]), newMember[3], int(newMember[4]), int(newMember[5])))

def showMembers():
    for i in range(len(members)):
        print(f"{members[i].ID} {members[i].Surname:<9} {members[i].YearJoined} {members[i].MemberType:<8} {members[i].NightsBooked:<4} {members[i].Points}")

readMembers()
showMembers()