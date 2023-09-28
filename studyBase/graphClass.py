e = '\033[0m'
#normalised , standard 
sRed = '\033[38;2;170;0;0m'
sGreen = '\033[38;2;0;170;0m'
sYellow = '\033[38;2;170;85;0m'
sBlue = '\033[38;2;0;0;170m'
sMagenta = '\033[38;2;170;0;170m'
sCyan = '\033[38;2;0;170;170m'
sWhite = '\033[38;2;170;170;170m'
#bright
Gray = '\033[38;2;85;85;85m'
red = '\033[38;2;255;0;0m'
green = '\033[38;2;0;255;0m'
yellow = '\033[38;2;255;255;0m'
blue = '\033[38;2;0;0;255m'
magenta = '\033[38;2;255;0;255m'
cyan = '\033[38;2;0;255;255m'
white = '\033[38;2;255;255;255m'
#special
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

class Graph:
  def __init__(self,values_onX,values_onY,Length_graph=80,Breadth_graph=30,xSpace = 3,yLine = 3,scaleX=1,scaleY=1,Zacolor=e,autoRun = True): #give it 2 list
    '''
    warning values_onX devided by scaleX cannot be fractional and must be integral else error at line 36
    to_printX = round(x/self.scaleX) ...
    '''
    if len(values_onX) != len(values_onY):
      raise Exception("number of y and x values dont match")
    for a in values_onX:
      if a % scaleX != 0:
        raise Exception("values_onX devided by scaleX cannot be fractional")
    self.Length_graph = Length_graph #left to right
    self.Breadth_graph = Breadth_graph #top to bottom
    self.values_onX = values_onX
    self.values_onY = values_onY
    #signifies what one unit means , currently one unit is 3 spaces on x axis and is 3 line for y axis
    self.xSpace = xSpace
    self.scaleX = scaleX
    self.maximumX = round(max(self.values_onX)/self.scaleX) + 1 #in how many units will it reach max value in values_onX
    self.scaleY=scaleY #one unit is
    self.yLine = yLine #FIXME, this means how much each unit is in terms of lines
    self.maximumY = round(max(self.values_onY)/self.scaleY)
    
    self.Zacolor = Zacolor
    
    if self.maximumY > Breadth_graph/self.yLine:
      print("max value of values_onY wont fit with current settings of scaleY. if this looks wrong most likely cuz y values is one greator than required")
    if self.maximumX > Length_graph/self.xSpace:
      print("max value of values_onX wont fit with current settings of scaleX. if this looks wrong most likely cuz x values is one greator than required")
    if autoRun: self.graphPlotter()
      
  def graphPlotter(self):
    self.lisXnY = list(zip(self.values_onY,self.values_onX))
    self.lisXnY.sort(reverse = True)
    i = 1
    miniCounter = max(self.values_onY)
    compensator = 0
    shouldIRun_i = False
    gap = self.Breadth_graph - self.maximumY*self.yLine 
    
    oldminiCounter = miniCounter
    mesarun = False #way to stop plotting data before the highest number has been printed on y axis

    for ara in range(self.Breadth_graph): #y axis setup 
      if shouldIRun_i and (i % self.yLine ==0) :
        print("\n",f"    {miniCounter}"[-5:],sep="",end = "") #5 Characters including i
        mesarun = True
        miniCounter -= self.scaleY
      else:
        print("\n     ",sep ="",end = "") #5 spaces
      print("|",end="")
      if mesarun:
        to_printX = [round(x/self.scaleX) for y,x in self.lisXnY if y >= (oldminiCounter - 0.00005) ]
        spaces = " "*self.xSpace
        run = True
        to_printX.sort()
        
        for a in to_printX:
          if run:
            print((spaces*a)[:-1],self.Zacolor,".",e,sep="",end="")
            run = False
          else:
            print((spaces*(a-b))[:-1],self.Zacolor,".",e,sep="",end="")
          b = a #old a value
        oldminiCounter -= self.scaleY/self.yLine
      if not shouldIRun_i:
        compensator += 1
        if compensator >= gap:
          shouldIRun_i = True
          i += 1
        
      else:
        i +=1
      #breakpoint()
    
    print("\n     |",sep = "",end ="")
    
    for a in range(self.Length_graph): #x axis setup
      print("_" ,sep="",end="")
    
    print("\n     |",sep = "",end="") #5 spaces & 1 character
    miniCounter = self.scaleX
    for a in range(self.maximumX):
      print("     |"[-self.xSpace:],end="",sep="")
    
    print("\n      ",sep = "",end="") #6 tab spaces
    
    for a in range(self.maximumX):
      print(f"     {miniCounter}"[-self.xSpace:],sep="",end="")
      miniCounter += self.scaleX
      
    print("\ndone")