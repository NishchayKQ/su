#%d == month in int
# %H %M hour mins
#name of topic, times revised, days ago

#FIXME use absolute paths so we can run from anywhere

from time import localtime,strftime
import graphClass as gh

def analysis(L1):
  last7Days = L1[-1:-8:-1]
  last7x7Days =L1[-8:-15:-1]
  current7days = 0
  Counlast7Days = 0
  
  for x in last7Days:
    current7days += x
  for x in last7x7Days:
    Counlast7Days += x
  print(f"last seven days you studied \033[38;2;255;0;255m{round(current7days,2)}\033[0m hrs which is ", end = "")
  if current7days > Counlast7Days: print(f"\033[38;2;0;255;0m{round(current7days - Counlast7Days,2)}\033[0m hrs more than last week !")
  else: print(f"\033[38;2;255;0;0m{round(Counlast7Days - current7days,2)}\033[0m hrs less than last week \033[38;2;255;0;255m:(\033[0m")

def amPamConverter(Received,mode = 1):
  if mode == 1: # Received is string here
    H,m = Received.split()
    H = int(H)
    if H > 12:
      H = H - 12
      amPam = "pm"
    else: amPam = "am"
    return f"{H}:{m} {amPam}"
  if mode == 2: # Received is like ["19 00 - 19 40\n" , "20 00 - 21 00\n" ]
    culturedList = []
    for amoeba in Received:
      am1 = "am"
      am2 = "am"
      nLessAmoeba = amoeba[:-1]
      init_timestamp,final_timeStamp = nLessAmoeba.split(" - ")
      # h1,m1,am1          h2 m2,am2
      h1,m1 = init_timestamp.split()
      h2,m2 = final_timeStamp.split()
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

def time_Subtraction(h1,h2,m1,m2): #result in hours
  hours = h2 - h1 #hrs 
  mins = m2 - m1
  if mins < 0:return str((hours*60 + mins)/60)
  else: return str(mins/60 + hours)

def check_st(studyHoursList):
  if studyHoursList:
    return (str(studyHoursList[0][:-1]))[:4]
  else: return "cry"

def check_br(breakHoursList):
  if breakHoursList :
    return (str(breakHoursList[0][:-1]))[:4]
  else: return "happy"

def PlsMulti(show = False,addMultiMode = False,returnerOfWorlds = False):
  with open("Gallias/multi.txt") as wryFile:
    allUlti = wryFile.readlines()
  if show:
    for ara in allUlti:
      a,b = ara[:-1].split(";")
      x = len(a)
      space = " "*(20 - x) 
      print(f"{a}{space}{b}%")
  if addMultiMode:
    pass
  if returnerOfWorlds:
    tot = 0
    for ara in allUlti:
      a,b = ara[:-1].split(";")
      tot = tot + float(b)
    return tot

with open("suBase/studyList.txt") as aFile:
  studyList = aFile.readlines()
with open("suBase/breakList.txt") as bFile:
  breakList = bFile.readlines()
with open("suBase/7dayBreak.txt") as curuFile:
  SevendayBreakList = curuFile.readlines()
with open("suBase/7dayStudy.txt") as dFile:
  SevendayStudyList = dFile.readlines()
with open("suBase/breakHours.txt") as eFile:
  breakHoursList = eFile.readlines()
with open("suBase/studyHours.txt") as fFile:
  studyHoursList = fFile.readlines()
with open("suBase/1yesterday.txt") as gFile:

  print(f"yesterday's message : \033[38;2;255;255;0m{gFile.read()}\033[0m")
with open("suBase/babaBreakSheep.txt") as xcFile:
  babaBreakSheepList = xcFile.readlines()
print(""" available commands :   \n
                                   1 : toggle study
                                   2 : toggle break
                                   3 : end of day
                                   4 : 30 day graph
                                   5 : JEE last updated
                                   6 : revision helper
                                   7 : file rename
                                   8 : Gallias's Autoheal
                                   9 : Eat Eat bon repeat\n""") # removed, 5 : time difference

change_inStudyList ,change_inbreakList,change_inSevenBreakList,change_inSevenStudyList,change_inbreakHourList,change_instudyHourList = False,False,False,False,False,False


def balancer(mode):
  global studyList,breakList,breakHoursList,studyHoursList,change_inbreakHourList,change_instudyHourList,change_inStudyList ,change_inbreakList,babaBreakSheepList
  print("negative value for studying/break detected , performing autopatch...")
  if mode == "b": print("overstep was in break time")
  else: print("overstep was in study time")
  whatToDo = input("taking ending time as 23 59 by default, if you want to change this time just type the updated time \033[38;2;0;255;0mHH MM\033[0m\n: ")
  h2 = 23
  m2 = 59
  if whatToDo:
    h2,m2 = whatToDo.split()
  
  
  if mode == "b":
    h1,m1 = breakList[0][:-1].split()
    hours = float(time_Subtraction(int(h1),int(h2),int(m1),int(m2)))
    breakList.clear()
    change_inbreakList = True
    change_inbreakHourList = True
    temp = str(float(breakHoursList[0][:-1]) + hours)
    breakHoursList.clear()
    breakHoursList.append(temp + "\n")
    bobo = len(babaBreakSheepList)
    babaBreakSheepList[bobo - 1] += f" - {h2} {m2}\n"
    with open("suBase/babaBreakSheep.txt" , mode = "w") as xcFile:
      xcFile.writelines(babaBreakSheepList)
  
  elif mode == "s":
    h1,m1 = studyList[0][:-1].split()
    hours = float(time_Subtraction(int(h1),int(h2),int(m1),int(m2)))
    studyList.clear()
    change_inStudyList = True
    change_instudyHourList = True
    temp = str(float(studyHoursList[0][:-1]) + hours)
    studyHoursList.clear()
    studyHoursList.append(temp + "\n")

if studyList:
  current_time = localtime()
  temp = strftime("%H %M",current_time)
  h2,m2 = temp.split()
  h1,m1 = studyList[0][:-1].split()
  if float(toPrint := time_Subtraction(int(h1),int(h2),int(m1),int(m2))) < 0:
    balancer("s")
  if studyList:
    print(f"\n\033[38;2;0;255;0myou are studying for {(toPrint)[:4]} hours, since {amPamConverter(studyList[0][:-1])}\033[0m")
  yValues = []
  for x in SevendayStudyList:
    temp = x.split()
    yValues.append(float(temp[1]))
  if not studyHoursList:
    yValues.append(float(time_Subtraction(int(h1),int(h2),int(m1),int(m2))))
  else:
    yValues.append(float(time_Subtraction(int(h1),int(h2),int(m1),int(m2))) + float(studyHoursList[0][:-1]))
  analysis(yValues)
elif breakList:
  current_time = localtime()
  temp = strftime("%H %M",current_time)
  h2,m2 = temp.split()
  h1,m1 = breakList[0][:-1].split()
  if float(toPrint := time_Subtraction(int(h1),int(h2),int(m1),int(m2))) < 0:
    balancer("b")
  if breakList:
    print(f"\n\033[38;2;255;0;0myou are on break for {(toPrint)[:4]} hours, since {amPamConverter(breakList[0][:-1])}\033[0m")
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

print(f"\033[38;2;0;170;0mhours studied : {check_st(studyHoursList)}\033[0m\n\033[38;2;255;0;0mhours taken break: {check_br(breakHoursList)}\033[0m")


def cmdGiven():
  #print("you are on lowest level input")
  cmd = input("\n: ")
  def decider():
    global studyList,breakList,SevendayStudyList,SevendayBreakList,breakHoursList,studyHoursList,babaBreakSheepList,change_inStudyList ,change_inbreakList,change_inSevenBreakList,change_inSevenStudyList,change_inbreakHourList,change_instudyHourList
    current_time = localtime()
    
    if cmd == "0":
      return
    
    elif cmd == "1":
      if not breakList:
        if len(studyList) == 0: print("ara ara hopefully you last longer this time fufu~\n")
        temp = strftime("%H %M",current_time)
        temp += "\n"
        studyList.append(temp)
        print("registered current time...")
        change_inStudyList = True
        
        if len(studyList) ==2:
          h1,m1 = studyList[0][:-1].split()
          h2,m2 = studyList[1][:-1].split()
          hours =time_Subtraction(int(h1),int(h2),int(m1),int(m2))
          hours += "\n"
          studyHoursList.append(hours)
          studyList.clear()
          print("ended current study session")
          change_instudyHourList = True
          
          if len(studyHoursList) == 2:
            temp = str(float(studyHoursList[0][:-1]) + float(studyHoursList[1][:-1]))
            temp += "\n"
            studyHoursList.clear()
            studyHoursList.append(temp)
            cmdGiven()
          else:
            cmdGiven()
      else:
        print("end your break first")
        cmdGiven()
    
    elif cmd == "2":
      
      if not studyList: # true if studyList is empty
        if not breakList:
          #print("ok recorded starting time of break\n") #true if breakList is empty
          input("""if you truly regret 16th march then use today like theres no tomorrow""")
        
        temp = strftime("%H %M",current_time)
        #new babaBreakSheepList system
        bobo = len(babaBreakSheepList)
        if breakList:
          temp += "\n"
          babaBreakSheepList[bobo - 1] += " - " + temp
        else:
          babaBreakSheepList.append(temp)
          temp += "\n"
        
        with open("suBase/babaBreakSheep.txt" , mode = "w") as xcFile:
          xcFile.writelines(babaBreakSheepList)
        # end of babaBreakSheepList system
        
        breakList.append(temp)
        print("registered current time...")
        change_inbreakList = True
        if len(breakList) ==2:
          h1,m1 = breakList[0][:-1].split()
          h2,m2 = breakList[1][:-1].split()
          hours =time_Subtraction(int(h1),int(h2),int(m1),int(m2))
          hours += "\n"
          breakHoursList.append(hours)
          breakList.clear()
          print("ended current break session")
          change_inbreakHourList = True
        
          if len(breakHoursList) == 2:
            temp = str(float(breakHoursList[0][:-1]) + float(breakHoursList[1][:-1]))
            temp += "\n"
            breakHoursList.clear()
            breakHoursList.append(temp)
            cmdGiven()
          else:
            cmdGiven()

      else:
        print("toggle study to off first")
        cmdGiven()
    
    elif cmd == "3":
      
      temp = input("\nwant to end day, confirm? (blank enter cancel) :")
      
      if temp:
        datein = input("\ndate?: ")
        
        if not (1<len(datein)<=2): 
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
              
              
              SevendayBreakList.append(f"{datein} {breakHoursList[0][:-1]}\n")
              breakHoursList.pop()
              breakHoursList.append("0.0\n")
              
              if len(SevendayBreakList) > 30:SevendayBreakList.pop(0)
              SevendayStudyList.append(f"{datein} {studyHoursList[0][:-1]}\n")
              
              with open("Gallias/streak.txt") as wryFile:
                streakStr = wryFile.read()
              aCurrentStreak,bMaxStreak = streakStr.split(";")
              aCurrentStreak = int(aCurrentStreak)
              bMaxStreak = int(bMaxStreak)
              
              ch_coins = False
              
              if (todaysHours:=(float(studyHoursList[0][:-1]))) >= 6 :
                aCurrentStreak = aCurrentStreak + 1
                ch_coins = True
                if aCurrentStreak > bMaxStreak: bMaxStreak = aCurrentStreak
                print(f"yay streak of {aCurrentStreak} days")
                
                #coin update
                with open("Gallias/coins.txt") as coinFile:
                  coins = float(coinFile.read())
                  mamamulti = 1 + PlsMulti(returnerOfWorlds = True) + aCurrentStreak*(0.0166666667) + (todaysHours - 8)*0.0625
                  print(f"multi is {mamamulti} or {round((mamamulti - 1)*100,2)} % ,coin gain of {round(mamamulti*3,2)} or {mamamulti*3}")
                coins = coins + 3*(mamamulti)
                print(f"balance of {round(coins,2)} or {coins} coins hehe")
              else:
                print(f"your streak of {aCurrentStreak} days broke :(")
                aCurrentStreak = 0
                
              
              studyHoursList.pop()
              studyHoursList.append("0.0\n")
              
              if len(SevendayStudyList) > 30: SevendayStudyList.pop(0)
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
              
              #print("\t\t\t\033[1m\033[38;2;170;0;170mstudy graph\033[0m")
              temp = gh.Graph(xValues,yValues,yLine=4,scaleX=1,scaleY=1,Zacolor=gh.green,Length_graph=100)
              analysis(yValues)
              xValues = []
              yValues = []
              for x in SevendayBreakList:
                temp = x.split()
                xValues.append(int(temp[0]))
                yValues.append(float(temp[1]))
              #print("\t\t\t\033[1m\033[38;2;170;0;0mbreak graph\033[0m")
              temp = gh.Graph(xValues,yValues,yLine=4,scaleX=1,scaleY=2,Zacolor=gh.red,Length_graph=100)
              
              
              
              GoodlookingListofTimeWasted = []
              timeWasteHourList = []
              
              for amoeba in babaBreakSheepList:
                timeStampLow,timeStampHigh = amoeba[:-1].split(" - ")
                h1,m1 = timeStampLow.split()
                h2,m2 = timeStampHigh.split()
                hours = round(float(time_Subtraction(int(h1),int(h2),int(m1),int(m2))),2)
                import math
                hourOnly = math.floor(hours)
                minsOnly = round((hours - hourOnly)*60,2)
                timeWasteHourList.append(hours)
                GoodlookingListofTimeWasted.append(f"{hourOnly} hrs {minsOnly} mins\n")
              
              temp = amPamConverter(babaBreakSheepList,mode =2)
              backupOfBreaks = []
              
              for amoeba,paramecium,fungi in zip(temp,timeWasteHourList,GoodlookingListofTimeWasted):
                print()
                backupOfBreaks.append(f"{amoeba[:-1]} ------> {fungi}")
                if 0 <= paramecium <= 0.5:
                  print(f"{amoeba[:-1]} \033[38;2;85;85;85m{fungi[:-1]}\033[0m")
                elif 0.5 <= paramecium <= 1:
                  print(f"{amoeba[:-1]} \033[38;2;170;85;0m{fungi[:-1]}\033[0m")
                else:
                  print(f"{amoeba[:-1]} \033[38;2;255;0;255m{fungi[:-1]}\033[0m")
              
              with open("1Sheep.txt" , mode = "w") as mcFile:
                mcFile.writelines(backupOfBreaks)
              
              with open("suBase/babaBreakSheep.txt" , mode = "w") as xcFile:
                xcFile.writelines([])
              
              with open("Prevision.txt") as hFile:
                temp = hFile.readlines()
                P_topicNameList,P_timesRevisedList,P_daysAgoList = [],[],[]
                for x in temp:
                   t1,t2,t3 = x[:-1].split(",")
                   P_topicNameList.append(t1)
                   P_timesRevisedList.append(t2)
                   P_daysAgoList.append(t3)
              with open("Crevision.txt") as iFile:
                temp = iFile.readlines()
                C_topicNameList,C_timesRevisedList,C_daysAgoList = [],[],[]
                for x in temp:
                   t1,t2,t3 = x[:-1].split(",")
                   C_topicNameList.append(t1)
                   C_timesRevisedList.append(t2)
                   C_daysAgoList.append(t3)
              with open("Mrevision.txt") as jFile:
                temp = jFile.readlines()
                M_topicNameList,M_timesRevisedList,M_daysAgoList = [],[],[]
                for x in temp:
                   t1,t2,t3 = x[:-1].split(",")
                   M_topicNameList.append(t1)
                   M_timesRevisedList.append(t2)
                   M_daysAgoList.append(t3)
              i = 0
              for x in P_daysAgoList:
                P_daysAgoList[i] = str(int(x) + 1)
                i += 1
              temp = []
              for a,b,c in zip(P_topicNameList,P_timesRevisedList,P_daysAgoList):
                temp.append(f"{a},{b},{c}\n")
              with open("Prevision.txt",mode = "w") as savingfile:
                savingfile.writelines(temp)
             
              i = 0
              for x in C_daysAgoList:
                C_daysAgoList[i] = str(int(x) + 1)
                i += 1
              temp = []
              for a,b,c in zip(C_topicNameList,C_timesRevisedList,C_daysAgoList):
                temp.append(f"{a},{b},{c}\n")
              with open("Crevision.txt",mode = "w") as savingfile:
                savingfile.writelines(temp)
              
              i = 0
              for x in M_daysAgoList:
                M_daysAgoList[i] = str(int(x) + 1)
                i += 1
              temp = []
              for a,b,c in zip(M_topicNameList,M_timesRevisedList,M_daysAgoList):
                temp.append(f"{a},{b},{c}\n")
              with open("Mrevision.txt",mode = "w") as savingfile:
                savingfile.writelines(temp)
              with open("Gallias/streak.txt", mode = "w") as wryFile:
                wryFile.write(f"{aCurrentStreak};{bMaxStreak}")
              
              with open("Gallias/hourBank.txt") as mooFile:
                totHours = float(mooFile.read())
              with open("Gallias/hourBank.txt", mode = "w") as mooFile:
                mooFile.write(f"{totHours + todaysHours}")
              if ch_coins:
                with open("Gallias/coins.txt", mode = "w") as maaFile:
                  maaFile.write(f"{coins}")
              with open("Gallias/7dCal.txt", mode = "r") as digestFile:
                sevenDayCalList = digestFile.readlines()
              if len(sevenDayCalList) > 30: sevenDayCalList.pop(0)
              
              with open("EatEatBonRepeat.txt", mode = "r") as YumFile:
                Tcals = YumFile.read()
              
              sevenDayCalList.append(f"{datein} {Tcals}\n")
              
              print(f"todays total KCals : {Tcals}")
              
              with open("EatEatBonRepeat.txt",mode = "w") as YumFile:
                YumFile.write("0")
              with open("Gallias/7dCal.txt",mode = "w" ) as digestFile:
                digestFile.writelines(sevenDayCalList)
      else:
        cmdGiven()
    
    elif cmd == "4":
      xValues = []
      yValues = []
      for x in SevendayStudyList:
        temp = x.split()
        xValues.append(int(temp[0]))
        yValues.append(float(temp[1]))
      
      #print("\t\t\t\033[1m\033[38;2;170;0;170mstudy graph\033[0m")
      temp = gh.Graph(xValues,yValues,yLine=4,scaleX=1,scaleY=2,Zacolor=gh.green,Length_graph=100,Breadth_graph=30)
      print()
      analysis(yValues)
      xValues = []
      yValues = []
      for x in SevendayBreakList:
        temp = x.split()
        xValues.append(int(temp[0]))
        yValues.append(float(temp[1]))
      #print("\t\t\t\033[1m\033[38;2;170;0;0mbreak graph\033[0m")
      temp = gh.Graph(xValues,yValues,yLine=4,scaleX=1,scaleY=5,Zacolor=gh.red,Length_graph=100,Breadth_graph=15)
      cmdGiven()
    
    elif cmd == "5":
      import urllib.request as ara
      import re
      
      #ara.urlretrieve("http://jeeadv.ac.in/","Gallias/nta.html")
      ara.urlretrieve("https://jeemain.nta.nic.in/","Gallias/nta.html")
      ara.urlcleanup()
      with open("Gallias/nta.html") as ntFile:
        look = ntFile.read()
      
      """
      with open("Gallias/last updated old.txt") as tfFile:
        oldDate = tfFile.read()
      if oldDate != look:
        print("\033[38;2;255;255;0mAlert JEE's website was updated !!!\033[0m")
        with open("Gallias/last updated old.txt",mode = "w") as tfFile:
          tfFile.write(look)
      """
      whereisUpdated = (re.search("Last Updated: <strong>",look)).end()
      
      if not whereisUpdated:
        print("error couldnt find last updated...exiting command")
        cmdGiven()
      gamma = 0
      while look[whereisUpdated + gamma] != "<":
        gamma = gamma + 1
      date = look[whereisUpdated:whereisUpdated + gamma]
      
      print(f"\033[38;2;85;85;85mlast updated on {date}\033[0m")
      
      with open("Gallias/last updated old.txt") as tfFile:
        oldDate = tfFile.read()
      
      if oldDate != date:
        print("\033[38;2;255;255;0mAlert JEE's website was updated !!!\033[0m")
      
      with open("Gallias/last updated old.txt",mode = "w") as tfFile:
        tfFile.write(date)
      
      yesMaster = input("show titles?")
      if yesMaster:
        BadallLinks = re.finditer('<a download href="' , look)
        downloadLinks = []
        for a in BadallLinks:
          i = 0
          start = a.end()
          while look[i + start] != '"':
            i = i + 1
          downloadLinks.append(look[start:start + i])

        Badtitles = re.finditer('title="download" >',look)

        titles = []
        
        for a in Badtitles:
          i = 0
          start = a.end()
          while look[i + start] != '<':
            i = i + 1
          titles.append(look[start:start + i])
        i = 0
        print("-------------titles--------------------------\n\n")
        for a in titles:
          if i % 2 == 0:
            print(i,a,sep = "       ")
          else:
            print(i,a,sep = " - - - ")
          i += 1
        yesMaster = input("wanna download any? :")
        if yesMaster:
          while True:
            try:
              yesMaster = int(yesMaster)
              bye = True
            except ValueError:
              print("input a number...", end = "")
              bye = False
            if bye:
              if (len(titles) - 1) >= yesMaster:
                break
              print("number given out of maximum available",end=", ")
            yesMaster = input("specify the number on the left of title to download :")
          
          print(f"downloading doc associated with {titles[yesMaster]}")
          url = downloadLinks[yesMaster]
          where = (re.search("pdf",url)).start()
          i = 0
          while url[where - 1 + i] != "/":
            i = i - 1
          nameForFile = url[where + i:where]
          
          ara.urlretrieve(url,f"/storage/emulated/0/Download/{nameForFile}pdf")
          ara.urlcleanup()
          print("done")
        
      cmdGiven()
      """print("time difference between\033[38;2;0;255;255m given time and current time\033[0m")
      print(temp:=strftime("%H %M",current_time))
      h2,m2 = temp.split()
      enteredTime = input("\nenter time,24H \"HH MM\"\n")
      h1,m1 = enteredTime.split()
      temp = float(time_Subtraction(int(h1),int(h2),int(m1),int(m2)))
      print(f"from {h1}:{m1} to {h2}:{m2} \033[38;2;255;255;0m{round(temp,2)} hrs\033[0m or\033[38;2;255;255;0m {round(temp*60)} mins\033[0m have passed")
      cmdGiven()"""
    
    elif cmd == "6":
      with open("Prevision.txt") as hFile:
        temp = hFile.readlines()
        P_topicNameList,P_timesRevisedList,P_daysAgoList = [],[],[]
        for x in temp:
           t1,t2,t3 = x[:-1].split(",")
           P_topicNameList.append(t1)
           P_timesRevisedList.append(t2)
           P_daysAgoList.append(t3)
      with open("Crevision.txt") as iFile:
        temp = iFile.readlines()
        C_topicNameList,C_timesRevisedList,C_daysAgoList = [],[],[]
        for x in temp:
           t1,t2,t3 = x[:-1].split(",")
           C_topicNameList.append(t1)
           C_timesRevisedList.append(t2)
           C_daysAgoList.append(t3)
      with open("Mrevision.txt") as jFile:
        temp = jFile.readlines()
        M_topicNameList,M_timesRevisedList,M_daysAgoList = [],[],[]
        for x in temp:
           t1,t2,t3 = x[:-1].split(",")
           M_topicNameList.append(t1)
           M_timesRevisedList.append(t2)
           M_daysAgoList.append(t3)
      with open("algo.txt") as kFile:
        algo = kFile.read(1)
      yesMaster = input("\n enter = chose for today,\"a\" for all: ")
      if not yesMaster:
        algo = input("\n m/p/c revision?").upper()
        #if algo == "M":
        if algo == "P":
          #algo = "P"
          i = 0
          print("-------------Physics--------------------------\n\n")
          for a,b,c in zip(P_topicNameList,P_timesRevisedList,P_daysAgoList):
            if i % 2 == 0:
              print(f"{i}   \033[38;2;0;170;170m{c} days ago\033[0m   {a}")
            else:
              print(f"{i} - \033[38;2;0;170;170m{c} days ago\033[0m - {a}")
            i += 1
          try:
            whichOne = int(input("\nnumber or for exit enter: "))
            P_daysAgoList[whichOne] = "0"
            P_timesRevisedList[whichOne] = str(int(P_timesRevisedList[whichOne]) + 1)
            print(f"ok so you are going to revise \033[38;2;0;170;170m{P_topicNameList[whichOne]}\033[0m")
            temp = []
            for a,b,c in zip(P_topicNameList,P_timesRevisedList,P_daysAgoList):
              temp.append(f"{a},{b},{c}\n")
            with open("Prevision.txt",mode = "w") as savingfile:
              savingfile.writelines(temp)
            cmdGiven()
            #with open("algo.txt",mode = "w") as savingfile:
            #  savingfile.write(algo)
          except ValueError:
            print("exited")
            cmdGiven()
          except IndexError:
            print("out of index list is")
            cmdGiven()

        #elif algo == "P":
        elif algo == "C":
          #algo = "C"
          i = 0
          print("-------------Chemistry--------------------------\n\n")
          for a,b,c in zip(C_topicNameList,C_timesRevisedList,C_daysAgoList):
            if i % 2 == 0:
              print(f"{i}   \033[38;2;0;170;170m{c} days ago\033[0m   {a}")
            else:print(f"{i} - \033[38;2;0;170;170m{c} days ago\033[0m - {a}")
            i += 1
          try:
            whichOne = int(input("\nnumber or for exit enter: "))
            C_daysAgoList[whichOne] = "0"
            C_timesRevisedList[whichOne] = str(int(C_timesRevisedList[whichOne]) + 1)
            print(f"ok so you are going to revise \033[38;2;0;170;170m{C_topicNameList[whichOne]}\033[0m")
            temp = []
            for a,b,c in zip(C_topicNameList,C_timesRevisedList,C_daysAgoList):
              temp.append(f"{a},{b},{c}\n")
            with open("Crevision.txt",mode = "w") as savingfile:
              savingfile.writelines(temp)
            cmdGiven()
            #with open("algo.txt",mode = "w") as savingfile:
              #savingfile.write(algo)
          except ValueError:
            print("exited")
            cmdGiven()
          except IndexError:
            print("out of index list is")
            cmdGiven()
          
        #elif algo == "C":
        elif algo == "M":
          #algo = "M"
          i = 0
          print("-------------Maths--------------------------\n\n")
          for a,b,c in zip(M_topicNameList,M_timesRevisedList,M_daysAgoList):
            if i % 2 == 0:print(f"{i}   \033[38;2;0;170;170m{c} days ago\033[0m   {a}")
            else:print(f"{i} - \033[38;2;0;170;170m{c} days ago\033[0m - {a}")
            i += 1
          try:
            whichOne = int(input("\nnumber or for exit enter: "))
            M_daysAgoList[whichOne] = "0"
            M_timesRevisedList[whichOne] = str(int(M_timesRevisedList[whichOne]) + 1)
            print(f"ok so you are going to revise \033[38;2;0;170;170m{M_topicNameList[whichOne]}\033[0m")
            temp = []
            for a,b,c in zip(M_topicNameList,M_timesRevisedList,M_daysAgoList):
              temp.append(f"{a},{b},{c}\n")
            with open("Mrevision.txt",mode = "w") as savingfile:
              savingfile.writelines(temp)
            cmdGiven()
            #with open("algo.txt",mode = "w") as savingfile:
              #savingfile.write(algo)
          except ValueError:
            print("exited")
            cmdGiven()
          except IndexError:
            print("out of index list is")
            cmdGiven()
        
        else:
          print("not in option")
          cmdGiven()
      
      elif yesMaster == "a":
        i = 0
        print("-------------Maths--------------------------\n\n")
        for a,b,c in zip(M_topicNameList,M_timesRevisedList,M_daysAgoList):
          if i % 2 == 0:
            print(f"\033[38;2;0;170;170m{c}\033[0m   ×{b}   {a}")
          else:
            print(f"\033[38;2;0;170;170m{c}\033[0m - ×{b} - {a}")
          i += 1
        print("")
        i = 0
        print("-------------Physics--------------------------\n\n")
        for a,b,c in zip(P_topicNameList,P_timesRevisedList,P_daysAgoList):
          if i % 2 == 0:
            print(f"\033[38;2;0;170;170m{c}\033[0m   ×{b}   {a}")
          else:
            print(f"\033[38;2;0;170;170m{c}\033[0m - ×{b} - {a}")
          i += 1
        print("")
        i = 0
        print("-------------Chemistry--------------------------\n\n")
        for a,b,c in zip(C_topicNameList,C_timesRevisedList,C_daysAgoList):
          if i % 2 == 0:
            print(f"\033[38;2;0;170;170m{c}\033[0m   ×{b}   {a}")
          else:
            print(f"\033[38;2;0;170;170m{c}\033[0m - ×{b} - {a}")
          i += 1
        cmdGiven()
      
      else:
        cmdGiven()
    
    elif cmd == "7":
      topicToRename = input("m/p/c ?: ")
      if topicToRename == "m": 
        temp = "/storage/emulated/0/Notes/0 maths/"
        with open("m.txt") as zFile:
          counter = int(zFile.read()) + 1
        with open("m.txt",mode = "w") as zFile:
          zFile.write(f"{counter}")
      elif topicToRename == "p":
        temp = "/storage/emulated/0/Notes/1 Phy/"
        with open("p.txt") as zFile:
          counter = int(zFile.read()) + 1
        with open("p.txt",mode = "w") as zFile:
          zFile.write(f"{counter}")
      elif topicToRename == "c": 
        temp = "/storage/emulated/0/Notes/2 chem/"
        with open("c.txt") as zFile:
          counter = int(zFile.read()) + 1
        with open("c.txt",mode = "w") as zFile:
          zFile.write(f"{counter}")
      else:
        print("error 7")
        cmdGiven()
      from os import listdir,rename,mkdir
      import re
      chapName = input("whats the topic name: ")
      pathToSaveAt = f"{temp}{counter} {chapName}"
      mkdir(pathToSaveAt)
      saveFrom = "/storage/emulated/0/PhysicsWallah/PDF/"
      pdfList = listdir(saveFrom)
      hugo60 = []
      for a in pdfList:
        ryuu = a.replace(":","")
        hugo60.append(ryuu)
      print(hugo60)
      common = input("what do the files have in common? :")
      comRemove = input("common thingy to remove? :")
      i = 0
      for a in pdfList:
        b = re.search(common,hugo60[i])
        c = re.search(comRemove,hugo60[i])
        refinedName = hugo60[i][b.start():c.start()] + ".pdf"
        refinedName.replace("  "," ")
        rename(f"{saveFrom}{pdfList[i]}",f"{pathToSaveAt}/{refinedName}")
        i += 1
      print("done")
      cmdGiven()
    
    elif cmd == "8":
      while True:
        hrsclaims = input("\nhow many hrs do u think u can study today? : ")
        try:
          hrsclaims = float(hrsclaims)
          print()
          break
        except:
          print("input should be a float/int")
      
      with open("Gallias/streak.txt") as wryFile:
        streakStr = wryFile.read()
        aCurrentStreak,bMaxStreak = streakStr.split(";")
      aCurrentStreak = int(aCurrentStreak)
      if hrsclaims >= 6:
        aCurrentStreak = aCurrentStreak + 1
      else:
        aCurrentStreak = 0
        print("note: actually u wont receive any coins, as min hrs is 6hrs")
      mamamulti = 1 + PlsMulti(returnerOfWorlds = True) + aCurrentStreak*(0.0166666667) + (hrsclaims - 8)*0.0625
      print(f"total coin gain multi = {round((mamamulti - 1)*100,2)} % bonus coins or \033[38;2;170;85;0m{mamamulti}\033[0m × 3 = \033[38;2;255;0;255m{mamamulti*3}\033[0m coins")
      cmdGiven()
    
    elif cmd == "9":
      i = 0
      while True:
        try:
          wryy = input("did u eat? ehehhehe (yes: x Kcals, no blank enter :")
          if wryy:
            i = i + int(wryy)
          else:
            break
        except ValueError:
          print("input a integer")
      with open("EatEatBonRepeat.txt", mode="r") as YumFile:
        z = int(YumFile.read())
        i = z + i
      print(f"todays total KCals : {i}")
      with open("EatEatBonRepeat.txt",mode = "w") as digestFile:
        digestFile.write(str(i))
      cmdGiven()
    else:
      print("wrong cmd entered, re enter. called from decider else block")
      cmdGiven()
  decider()

cmdGiven()
whatChanged = (change_inSevenBreakList,change_inSevenStudyList,change_inbreakHourList,change_inbreakList,change_instudyHourList,change_inStudyList)
#print(f"""changes detected in \n
#                                 7D break : {change_inSevenBreakList}
##                                7D study : {change_inSevenStudyList}
  #                             breakHours : {change_inbreakHourList}
   #                             breakList : {change_inbreakList}
    #                           studyHours : {change_instudyHourList}
      #                          studyList : {change_inStudyList}\n""")

noChangeI = 0
while noChangeI < 6:
  OneoutOfsix = ("7dayBreak","7dayStudy","breakHours","breakList","studyHours","studyList")
  HaveTosaveList = (SevendayBreakList,SevendayStudyList,breakHoursList,breakList,studyHoursList,studyList)
  if whatChanged[noChangeI]:
    with open(f"suBase/{OneoutOfsix[noChangeI]}.txt",mode = "w") as savingfile:
      savingfile.writelines(HaveTosaveList[noChangeI])
      print(f"saved {HaveTosaveList[noChangeI]}")
  noChangeI += 1
print("\n\nSaved all changes if at all")


