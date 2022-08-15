import sys

def convert(charInput):
    newString = ""
  
    for ch in charInput:
        newString += ch 

    return newString

def checkSize(maze, flags):
    
    mazeHeight = len(maze)
    mazeLength = len(maze[0])
    
    #kontrola obdelnikovosti
    for line in maze: 
        if len(line) != mazeLength:
            flags[0] = True
    
    if (mazeHeight < 5 or mazeHeight > 50):
        flags[4] = True
        
    if (mazeLength < 5 or mazeLength > 70):
        flags[3] = True
        
    return flags

def checkInOut(maze, flags):
    mazeHeight = len(maze)
    mazeLength = len(maze[0])
    
    #kontrola vstupu a vytsupu
    if (maze[0][1] != "."):
        flags[1] = True
    if (maze[mazeHeight - 1][mazeLength - 2] != "."):
        flags[2] = True
    return flags    

def checkSymbols(maze, flags):
    for r in range(0,len(maze)):
        for p in range(0,len(maze[0])):
            if ( (r == 0 and p == 1) or ( r == len(maze) - 1 and p == len(maze[0]) - 2) ):
                continue
            if ( r == 0 or r == len(maze) - 1 or p == 0 or p == len(maze[0]) -1 ) and ( maze[r][p] != "#"):
                flags[6] = True
            elif ( maze[r][p] not in [".", "#"]):
                flags[5] = True
                break

def checkErrors(maze, flags):
    flags = checkSize(maze, flags)
    flags = checkInOut(maze, flags)
    flags = checkSymbols(maze, flags)

if __name__ == "__main__":
    
    # vstup z brute - sys simuleje nas soubor
    f = sys.stdin  
    
    #pole priznaku
    flags = [False, False, False, False, False, False, False]
    errors = [
        "Error: Bludiste neni obdelnikove!",
        "Error: Vstup neni vlevo nahore!",
        "Error: Vystup neni vpravo dole!",
        "Error: Sirka bludiste je mimo rozsah!",
        "Error: Delka bludiste je mimo rozsah!", 
        "Error: Bludiste obsahuje nezname znaky!", 
        "Error: Bludiste neni oplocene!"
    ] 
    
    #uprava bludiste
    maze = f.read()
    maze = maze.splitlines()
    
    # kontrola pred zahajenim algoritmu
    checkErrors(maze, flags)
    for flag in range(0, len(flags)):
        if (flags[flag]):
            sys.stderr.write(errors[flag] + '\n' + '\n')
            exit(1)

    #rozmery
    mazeHeight = len(maze)
    mazeLength = len(maze[0])
    history = [(1,1)]  
            
    #smerove vektory       
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    curDir = 0
    curPos = (1,1)
    endPos = (len(maze) - 2, len(maze[0]) - 2) #posledni pozice nutna k navstiveni

    # Algoritmus na pruchod bludistem. Logika vzdy ve volne pravo
    while (curPos != endPos):
        
        newDir = (curDir - 1) % 4
        for i in range (0,4):
           newPos = (curPos[0] + directions[newDir][0], curPos[1] + directions[newDir][1]) 
           if(maze[newPos[0]][newPos[1]] == "."):
                curPos = (newPos[0], newPos[1])
                history.append(curPos)
                break
           else:
               newDir = (newDir + 1) % 4
        curDir = newDir 
    
    
    # Nalezeni inverzni cesty
    # curPos = potentialNodes[0]
    curPos = (1,1)
    directions = [(1,0), (0,-1), (-1,0), (0,1)]
    curDir = 0
    newHistory = [(1,1)]
    while (curPos != endPos):
        
        newDir = (curDir - 1) % 4
        for i in range (0,4):
           newPos = (curPos[0] + directions[newDir][0], curPos[1] + directions[newDir][1]) 
           if(maze[newPos[0]][newPos[1]] == "."):
                curPos = (newPos[0], newPos[1])
                newHistory.append(curPos)
                break
           else:
               newDir = (newDir + 1) % 4
        curDir = newDir

    # srovnani inverznich tras do trasy nove
    helpHistory = []   
    for point in history:
        if(point in newHistory):
            helpHistory.append(point)                           
    
    for i in range(0, len(maze)):
        maze[i] = list(maze[i])

    # doplneni ignorovanych pozic
    for point in helpHistory:
        maze[point[0]][point[1]] = '!'
    maze[0][1] = '!'
    maze[mazeHeight-1][mazeLength-2] = '!'
    
    
    for i in range(0, len(maze)):
        maze[i] = convert(maze[i])
            
    maze = "\n".join(maze)
    print(maze)
    exit(0)
    
        
    

    
