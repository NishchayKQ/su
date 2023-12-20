# %d == month in int
# %H %M hour mins
# name of topic, times revised, days ago

# FIXME use absolute paths so we can run from anywhere

from time import localtime, strftime
import graphClass as gh
import json


def analysis(L1):
    last7Days = L1[-1:-8:-1]
    last7x7Days = L1[-8:-15:-1]
    current7days = 0
    Counlast7Days = 0

    for x in last7Days:
        current7days += x
    for x in last7x7Days:
        Counlast7Days += x

    print("last seven days you studied \033[38;2;255;0;255m"
          f"{round(current7days, 2)}\033[0m hrs which is ", end=""
          )

    if current7days > Counlast7Days:
        print(f"\033[38;2;0;255;0m{round(current7days - Counlast7Days, 2)}"
              "\033[0m hrs more than last week !")
    else:
        print(f"\033[38;2;255;0;0m{round(Counlast7Days - current7days, 2)}"
              "\033[0m hrs less than last week \033[38;2;255;0;255m:(\033[0m")


def amPamConverter(Received, mode=1):
    if mode == 1:  # Received is string here
        H, m = Received.split()
        H = int(H)
        if H > 12:
            H = H - 12
            amPam = "pm"
        else:
            amPam = "am"
        return f"{H}:{m} {amPam}"
    if mode == 2:  # Received is like ["19 00 - 19 40\n" , "20 00 - 21 00\n" ]
        culturedList = []
        for amoeba in Received:
            am1 = "am"
            am2 = "am"
            nLessAmoeba = amoeba[:-1]
            init_timestamp, final_timeStamp = nLessAmoeba.split(" - ")
            # h1,m1,am1          h2 m2,am2
            h1, m1 = init_timestamp.split()
            h2, m2 = final_timeStamp.split()
            h1 = int(h1)
            h2 = int(h2)
            if h1 > 12:
                h1 = h1 - 12
                am1 = "pm"
            if h2 > 12:
                h2 = h2 - 12
                am2 = "pm"
            culturedList.append(f"{h1}:{m1} {am1} - {h2}:{m2} {am2}\n")
        return culturedList


def time_Subtraction(h1, h2, m1, m2):  # result in hours
    hours = h2 - h1  # hrs
    mins = m2 - m1
    if mins < 0:
        return str((hours*60 + mins)/60)
    else:
        return str(mins/60 + hours)


def check_st(studyHoursList):
    if studyHoursList:
        return (str(studyHoursList[0][:-1]))[:4]
    else:
        return "cry"


def check_br(breakHoursList):
    if breakHoursList:
        return (str(breakHoursList[0][:-1]))[:4]
    else:
        return "happy"


def PlsMulti(show=False, addMultiMode=False, returnerOfWorlds=False):
    with open("Gallias/multi.txt") as wryFile:
        allUlti = wryFile.readlines()
    if show:
        for ara in allUlti:
            a, b = ara[:-1].split(";")
            x = len(a)
            space = " "*(20 - x)
            print(f"{a}{space}{b}%")
    if addMultiMode:
        pass
    if returnerOfWorlds:
        tot = 0
        for ara in allUlti:
            a, b = ara[:-1].split(";")
            tot = tot + float(b)
        return tot


try:
    with open("suBase.json") as suFile:
        suDict = json.load(suFile)
except FileNotFoundError:
    with open("suBase.json", mode="w") as createrOfFiles:
        suDict = {"1yesterday": "Consistency is Key!",
                  "studyList": [],
                  "breakList": [],
                  "studyHours": 0,
                  "breakHours": 0,
                  "babaBreakSheep": ["under constuction"],
                  "7dayStudy": [],
                  "7dayBreak": []}
        json.dump(suDict, createrOfFiles, indent=4)

print("yesterday's message : \033[38;2;255;255;0m"
      f"{suDict["1yesterday"]}\033[0m")
studyList = suDict["studyList"]
breakList = suDict["breakList"]
SevendayBreakList = suDict["7dayBreak"]
SevendayStudyList = suDict["7dayStudy"]
breakHoursList = suDict["breakHours"]
studyHoursList = suDict["studyHours"]

change_inStudyList = False
change_inbreakList = False
change_inSevenBreakList = False
change_inSevenStudyList = False
change_inbreakHourList = False
change_instudyHourList = False


def balancer(mode):
    global studyList, breakList, breakHoursList, studyHoursList
    global change_inbreakHourList, change_instudyHourList
    global change_inStudyList, change_inbreakList, babaBreakSheepList
    print("negative value for studying/break detected , performing autopatch...")
    if mode == "b":
        print("overstep was in break time")
    else:
        print("overstep was in study time")
    whatToDo = input(
        "taking ending time as 23 59 by default, if you want to change this time just type the updated time \033[38;2;0;255;0mHH MM\033[0m\n: ")
    h2 = 23
    m2 = 59
    if whatToDo:
        h2, m2 = whatToDo.split()

    if mode == "b":
        h1, m1 = breakList[0][:-1].split()
        hours = float(time_Subtraction(int(h1), int(h2), int(m1), int(m2)))
        breakList.clear()
        change_inbreakList = True
        change_inbreakHourList = True
        temp = str(float(breakHoursList[0][:-1]) + hours)
        breakHoursList.clear()
        breakHoursList.append(temp + "\n")
        bobo = len(babaBreakSheepList)
        babaBreakSheepList[bobo - 1] += f" - {h2} {m2}\n"
        with open("suBase/babaBreakSheep.txt", mode="w") as xcFile:
            xcFile.writelines(babaBreakSheepList)

    elif mode == "s":
        h1, m1 = studyList[0][:-1].split()
        hours = float(time_Subtraction(int(h1), int(h2), int(m1), int(m2)))
        studyList.clear()
        change_inStudyList = True
        change_instudyHourList = True
        temp = str(float(studyHoursList[0][:-1]) + hours)
        studyHoursList.clear()
        studyHoursList.append(temp + "\n")


if studyList:
    current_time = localtime()
    temp = strftime("%H %M", current_time)
    h2, m2 = temp.split()
    h1, m1 = studyList[0][:-1].split()
    if float(toPrint := time_Subtraction(int(h1), int(h2), int(m1), int(m2))) < 0:
        balancer("s")
    if studyList:
        print(
            f"\n\033[38;2;0;255;0myou are studying for {(toPrint)[:4]} hours, since {amPamConverter(studyList[0][:-1])}\033[0m")
    yValues = []
    for x in SevendayStudyList:
        temp = x.split()
        yValues.append(float(temp[1]))
    if not studyHoursList:
        yValues.append(float(time_Subtraction(
            int(h1), int(h2), int(m1), int(m2))))
    else:
        yValues.append(float(time_Subtraction(int(h1), int(
            h2), int(m1), int(m2))) + float(studyHoursList[0][:-1]))
    analysis(yValues)
elif breakList:
    current_time = localtime()
    temp = strftime("%H %M", current_time)
    h2, m2 = temp.split()
    h1, m1 = breakList[0][:-1].split()
    if float(toPrint := time_Subtraction(int(h1), int(h2), int(m1), int(m2))) < 0:
        balancer("b")
    if breakList:
        print(
            f"\n\033[38;2;255;0;0myou are on break for {(toPrint)[:4]} hours, since {amPamConverter(breakList[0][:-1])}\033[0m")
    yValues = []
    for x in SevendayStudyList:
        temp = x.split()
        yValues.append(float(temp[1]))
    if studyHoursList:
        yValues.append(float(studyHoursList[0][:-1]))
    analysis(yValues)
else:
    yValues = []
    for x in SevendayStudyList:
        temp = x.split()
        yValues.append(float(temp[1]))
    if studyHoursList:
        yValues.append(float(studyHoursList[0][:-1]))
    analysis(yValues)

print(
    f"\033[38;2;0;170;0mhours studied : {check_st(studyHoursList)}"
    "\033[0m\n\033[38;2;255;0;0mhours taken break:"
    f" {check_br(breakHoursList)}\033[0m")


def options() -> None:
    # removed, 5 : time difference
    # removed, 5 : JEE last updated
    print(""" available commands :   \n
                                    1 : toggle study
                                    2 : toggle break
                                    3 : end of day
                                    4 : 30 day graph
                                    
                                    5 : revision helper
                                    6 : file rename
                                    7 : Gallias's Autoheal
                                    8 : Eat Eat bon repeat\n""")


def saveAndClose() -> None:
    pass


def toggleStudyOrBreak(intendedList: list, badList: list,
                       HoursList: list) -> list | int | tuple:
    if not badList:
        temp = strftime("%H %M", current_time)
        temp += "\n"
        intendedList.append(temp)

        if len(intendedList) == 2:
            h1, m1 = intendedList[0][:-1].split()
            h2, m2 = intendedList[1][:-1].split()
            hours = time_Subtraction(
                int(h1), int(h2), int(m1), int(m2))
            hours += "\n"
            HoursList.append(hours)
            intendedList.clear()

            if len(HoursList) == 2:
                temp = str(float(HoursList[0][:-1])
                           + float(HoursList[1][:-1]))
                temp += "\n"
                HoursList.clear()
                HoursList.append(temp)
            return (intendedList, HoursList)
        return intendedList
    else:
        return 1


def makeGraph(SevendayStudyList: list, SevendayBreakList: list):
    xValues = []
    yValues = []
    for x in SevendayStudyList:
        temp = x.split()
        xValues.append(int(temp[0]))
        yValues.append(float(temp[1]))

    # print("\t\t\t\033[1m\033[38;2;170;0;170mstudy graph\033[0m")
    temp = gh.Graph(xValues, yValues, yLine=4, scaleX=1, scaleY=2,
                    Zacolor=gh.green, Length_graph=100, Breadth_graph=30)
    print()
    analysis(yValues)
    xValues = []
    yValues = []
    for x in SevendayBreakList:
        temp = x.split()
        xValues.append(int(temp[0]))
        yValues.append(float(temp[1]))
    # print("\t\t\t\033[1m\033[38;2;170;0;0mbreak graph\033[0m")
    temp = gh.Graph(xValues, yValues, yLine=4, scaleX=1, scaleY=5,
                    Zacolor=gh.red, Length_graph=100, Breadth_graph=15)


def endOfDay() -> None:
    datein = input("\ndate?: ")

    if not (1 < len(datein) <= 2):
        print("type date in this format \"01\" ")
        cmdGiven()

    else:

        if breakList:
            print("end your break first")
            cmdGiven()

        else:

            if studyList:
                print("end your study first")
                cmdGiven()

            else:

                SevendayBreakList.append(
                    f"{datein} {breakHoursList[0][:-1]}\n")
                breakHoursList.pop()
                breakHoursList.append("0.0\n")

                if len(SevendayBreakList) > 30:
                    SevendayBreakList.pop(0)
                SevendayStudyList.append(
                    f"{datein} {studyHoursList[0][:-1]}\n")

                with open("Gallias/streak.txt") as wryFile:
                    streakStr = wryFile.read()
                aCurrentStreak, bMaxStreak = streakStr.split(";")
                aCurrentStreak = int(aCurrentStreak)
                bMaxStreak = int(bMaxStreak)

                ch_coins = False

                if (todaysHours := (float(studyHoursList[0][:-1]))) >= 6:
                    aCurrentStreak = aCurrentStreak + 1
                    ch_coins = True
                    if aCurrentStreak > bMaxStreak:
                        bMaxStreak = aCurrentStreak
                    print(f"yay streak of {aCurrentStreak} days")

                    # coin update
                    with open("Gallias/coins.txt") as coinFile:
                        coins = float(coinFile.read())
                        mamamulti = 1 + PlsMulti(returnerOfWorlds=True) + aCurrentStreak*(
                            0.0166666667) + (todaysHours - 8)*0.0625
                        print(
                            f"multi is {mamamulti} or {round((mamamulti - 1)*100, 2)} % ,coin gain of {round(mamamulti*3, 2)} or {mamamulti*3}")
                    coins = coins + 3*(mamamulti)
                    print(
                        f"balance of {round(coins, 2)} or {coins} coins hehe")
                else:
                    print(
                        f"your streak of {aCurrentStreak} days broke :(")
                    aCurrentStreak = 0

                studyHoursList.pop()
                studyHoursList.append("0.0\n")

                if len(SevendayStudyList) > 30:
                    SevendayStudyList.pop(0)
                xValues = []
                yValues = []
                for x in SevendayStudyList:
                    temp = x.split()
                    xValues.append(int(temp[0]))
                    yValues.append(float(temp[1]))
                change_inSevenBreakList = True
                change_inSevenStudyList = True
                change_inbreakHourList = True
                change_instudyHourList = True

                # print("\t\t\t\033[1m\033[38;2;170;0;170mstudy graph\033[0m")
                temp = gh.Graph(
                    xValues, yValues, yLine=4, scaleX=1, scaleY=1, Zacolor=gh.green, Length_graph=100)
                analysis(yValues)
                xValues = []
                yValues = []
                for x in SevendayBreakList:
                    temp = x.split()
                    xValues.append(int(temp[0]))
                    yValues.append(float(temp[1]))
                # print("\t\t\t\033[1m\033[38;2;170;0;0mbreak graph\033[0m")
                temp = gh.Graph(
                    xValues, yValues, yLine=4, scaleX=1, scaleY=2, Zacolor=gh.red, Length_graph=100)

                GoodlookingListofTimeWasted = []
                timeWasteHourList = []

                for amoeba in babaBreakSheepList:
                    timeStampLow, timeStampHigh = amoeba[:-1].split(
                        " - ")
                    h1, m1 = timeStampLow.split()
                    h2, m2 = timeStampHigh.split()
                    hours = round(float(time_Subtraction(
                        int(h1), int(h2), int(m1), int(m2))), 2)
                    import math
                    hourOnly = math.floor(hours)
                    minsOnly = round((hours - hourOnly)*60, 2)
                    timeWasteHourList.append(hours)
                    GoodlookingListofTimeWasted.append(
                        f"{hourOnly} hrs {minsOnly} mins\n")

                temp = amPamConverter(babaBreakSheepList, mode=2)
                backupOfBreaks = []

                for amoeba, paramecium, fungi in zip(temp, timeWasteHourList, GoodlookingListofTimeWasted):
                    print()
                    backupOfBreaks.append(
                        f"{amoeba[:-1]} ------> {fungi}")
                    if 0 <= paramecium <= 0.5:
                        print(
                            f"{amoeba[:-1]} \033[38;2;85;85;85m{fungi[:-1]}\033[0m")
                    elif 0.5 <= paramecium <= 1:
                        print(
                            f"{amoeba[:-1]} \033[38;2;170;85;0m{fungi[:-1]}\033[0m")
                    else:
                        print(
                            f"{amoeba[:-1]} \033[38;2;255;0;255m{fungi[:-1]}\033[0m")

                with open("1Sheep.txt", mode="w") as mcFile:
                    mcFile.writelines(backupOfBreaks)

                with open("suBase/babaBreakSheep.txt", mode="w") as xcFile:
                    xcFile.writelines([])

                with open("Prevision.txt") as hFile:
                    temp = hFile.readlines()
                    P_topicNameList, P_timesRevisedList, P_daysAgoList = [], [], []
                    for x in temp:
                        t1, t2, t3 = x[:-1].split(",")
                        P_topicNameList.append(t1)
                        P_timesRevisedList.append(t2)
                        P_daysAgoList.append(t3)
                with open("Crevision.txt") as iFile:
                    temp = iFile.readlines()
                    C_topicNameList, C_timesRevisedList, C_daysAgoList = [], [], []
                    for x in temp:
                        t1, t2, t3 = x[:-1].split(",")
                        C_topicNameList.append(t1)
                        C_timesRevisedList.append(t2)
                        C_daysAgoList.append(t3)
                with open("Mrevision.txt") as jFile:
                    temp = jFile.readlines()
                    M_topicNameList, M_timesRevisedList, M_daysAgoList = [], [], []
                    for x in temp:
                        t1, t2, t3 = x[:-1].split(",")
                        M_topicNameList.append(t1)
                        M_timesRevisedList.append(t2)
                        M_daysAgoList.append(t3)
                i = 0
                for x in P_daysAgoList:
                    P_daysAgoList[i] = str(int(x) + 1)
                    i += 1
                temp = []
                for a, b, c in zip(P_topicNameList, P_timesRevisedList, P_daysAgoList):
                    temp.append(f"{a},{b},{c}\n")
                with open("Prevision.txt", mode="w") as savingfile:
                    savingfile.writelines(temp)

                i = 0
                for x in C_daysAgoList:
                    C_daysAgoList[i] = str(int(x) + 1)
                    i += 1
                temp = []
                for a, b, c in zip(C_topicNameList, C_timesRevisedList, C_daysAgoList):
                    temp.append(f"{a},{b},{c}\n")
                with open("Crevision.txt", mode="w") as savingfile:
                    savingfile.writelines(temp)

                i = 0
                for x in M_daysAgoList:
                    M_daysAgoList[i] = str(int(x) + 1)
                    i += 1
                temp = []
                for a, b, c in zip(M_topicNameList, M_timesRevisedList, M_daysAgoList):
                    temp.append(f"{a},{b},{c}\n")
                with open("Mrevision.txt", mode="w") as savingfile:
                    savingfile.writelines(temp)
                with open("Gallias/streak.txt", mode="w") as wryFile:
                    wryFile.write(f"{aCurrentStreak};{bMaxStreak}")

                with open("Gallias/hourBank.txt") as mooFile:
                    totHours = float(mooFile.read())
                with open("Gallias/hourBank.txt", mode="w") as mooFile:
                    mooFile.write(f"{totHours + todaysHours}")
                if ch_coins:
                    with open("Gallias/coins.txt", mode="w") as maaFile:
                        maaFile.write(f"{coins}")
                with open("Gallias/7dCal.txt", mode="r") as digestFile:
                    sevenDayCalList = digestFile.readlines()
                if len(sevenDayCalList) > 30:
                    sevenDayCalList.pop(0)

                with open("EatEatBonRepeat.txt", mode="r") as YumFile:
                    Tcals = YumFile.read()

                sevenDayCalList.append(f"{datein} {Tcals}\n")

                print(f"todays total KCals : {Tcals}")

                with open("EatEatBonRepeat.txt", mode="w") as YumFile:
                    YumFile.write("0")
                with open("Gallias/7dCal.txt", mode="w") as digestFile:
                    digestFile.writelines(sevenDayCalList)


printOptions = True
while True:
    if printOptions:
        printOptions = False
        options()

    WhatToDo = input(": ")

    match WhatToDo:
        case 'e' | '0':
            saveAndClose()
            break
        case '1':
            temp = toggleStudyOrBreak(studyList, breakList, studyHoursList)
            if type(temp) == list:
                studyList = temp
                change_inStudyList = True
                print("alright! Happy Studying!\n")
            elif type(temp) == tuple:
                studyList, studyHoursList = temp
                change_inStudyList = True
                change_instudyHourList = True
                print("ended current study session")
            else:
                print("end your break first")
        case '2':
            temp = toggleStudyOrBreak(breakList, studyList, breakHoursList)
            if type(temp) == list:
                breakList = temp
                change_inbreakList = True
                print("ok recorded starting time of break\n")
            elif type(temp) == tuple:
                breakList, breakHoursList = temp
                change_inbreakList = True
                change_inbreakHourList = True
                print("ended current break session")
            else:
                print("toggle study to off first")
        case '3':
            print("under maintenance")
        case '4':
            makeGraph(SevendayStudyList, SevendayBreakList)

        case _:
            print("not a valid command")
            printOptions = True
