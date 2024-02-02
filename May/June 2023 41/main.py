#Animal is an array of string, length 20
#Colour is an array of string, length 10
#AnimalTopPointer is an integer
#ColourTopPointer is an integer
Animal = [None]*20
Colour = [None]*10
AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True
    #End if
#End function


def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        AnimalTopPointer -= 1
        return ReturnData
    #End if
#End function


def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True
    #End if
#End function


def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer-1]
        ColourTopPointer -= 1
        return ReturnData
    #End if
#End function


def ReadData():
    try:
        file = open("AnimalData.txt", "r")
        for line in file:
            PushAnimal(line.strip())
        #Next i
        file.close()
    except FileNotFoundError:
        print("The file you are trying to read from does not exist")
    try:
        file = open("ColourData.txt", "r")
        for line in file:
            PushColour(line.strip())
        #Next i
        file.close()
    except FileNotFoundError:
        print("The file you are trying to read from does not exist")
#End function


def OutputItem():
    AnimalName = PopAnimal()
    AnimalColour = PopColour()
    if AnimalName == "":
        print("No animal")
    elif AnimalColour == "":
        print("No colour")
    else:
        print(f"{AnimalName} {AnimalColour}")
    #End if
#End function

ReadData()
for i in range(3):
    OutputItem()
#Next i