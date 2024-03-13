import sys

class Vertex:
    def __init__(self, height, posX, posY):
        self.height = height
        self.posX = posX
        self.posY = posY
        self.upElevation = 0
        self.upPrev = None
        self.downElevation = 0
        self.downPrev = None
        
        
    def __str__(self):
        return 'Vertex-x:' + str(self.posX) + '-y:' + str(self.posY) + '-h:' + str(self.height) + '-ue:' + str(self.upElevation) + '-de:' + str(self.downElevation)

    def __eq__(self, other):
        if isinstance(other, Vertex):
            if other.posX == self.posX and other.posY == self.posY: return True
            else: return False
    
    def __hash__(self):
        return hash((self.posX, self.posY))
    
    def __lt__(self, other):
        if self.height < other.height: return True
        else: return False
    
    def __gt__(self, other):
        if self.height > other.height: return True
        else: return False

if __name__ == "__main__":
    f = sys.stdin
    # f = open('c:/Users/bures/OneDrive/Plocha/DSA04/kopec_2_08.in', 'r')
    # lines = f.readlines()
    
    params = f.readline()
    params = [int(s) for s in params.split() if s.isdigit()]
    rows = int(params[0])
    columns = int(params[1])
    
    # print(rows)
    # print(columns)
    
    hill = [
        [ 0 for col in range(columns)]
        for row in range(rows)
    ]
    
    lines = f.readlines()
    # print(lines)
    rowCounter = 0
    for line in lines:
        # print(line)
        numbers = [int(s) for s in line.split() if s.isdigit()]
        # print(numbers)
        if(len(numbers) != columns):
            sys.stderr.write("Error: Chybny vstup!\n")
            exit(1)
        for i in range(0, columns):
            hill[rowCounter][i] = numbers[i]
        rowCounter += 1
        
    vertexUpMatrix = [
        [ Vertex(0, 0, 0) for col in range(columns)]
        for row in range(rows)
    ]
    
    reverseVertexUpMatrix = [
        [ Vertex(0, 0, 0) for col in range(columns)]
        for row in range(rows)
    ]
    
    for i in range(0, rows):
        for j in range(0, columns):
            vertexUpMatrix[i][j].posX = i
            vertexUpMatrix[i][j].posY = j
            vertexUpMatrix[i][j].height = hill[i][j]
            reverseVertexUpMatrix[i][j].posX = i
            reverseVertexUpMatrix[i][j].posY = j
            reverseVertexUpMatrix[i][j].height = hill[i][j]

    # go Up way ------------------------------------------------------------------------
    vectorQueue = []
    vectorQueue.append(vertexUpMatrix[0][0])
    peaks = set()
    
    while vectorQueue:
        v = vectorQueue.pop(0)
        isHigher = False 
        vX = v.posX
        vY = v.posY
        isXok = vX+1 < rows
        isYok = vY+1 < columns
                          
        if(isXok):
            next = vertexUpMatrix[vX+1][vY]
            dif = next.height - v.height
            if(dif > 0 and dif < v.upElevation):
                dif = v.upElevation
            if(dif > 0 and dif > next.upElevation):
                vectorQueue.append(next)
                next.upPrev = v
                next.upElevation = dif
                isHigher = True
                
        if(isYok):
            next = vertexUpMatrix[vX][vY+1]
            dif = next.height - v.height
            if(dif > 0 and dif < v.upElevation):
                dif = v.upElevation
            if(dif > 0 and dif > next.upElevation):
                vectorQueue.append(next)
                next.upPrev = v
                next.upElevation = dif
                isHigher = True
             
        
        if(not isHigher):
           peaks.add(v) 
    
    # go down way ------------------------------------------------------------------------
    
    reverseVectorQueue = []
    reverseVectorQueue.append(reverseVertexUpMatrix[rows-1][columns-1])
    reversePeaks = set()
    
    while reverseVectorQueue:
        v = reverseVectorQueue.pop(0)
        goHigher = False 
        vX = v.posX
        vY = v.posY
        isXok = vX > 0
        isYok = vY > 0
        
        if(isYok):
            next = reverseVertexUpMatrix[vX][vY-1]
            dif = next.height - v.height
            
            if(dif > 0 and dif < v.downElevation):
                dif = v.downElevation
            if(dif > 0 and dif > next.downElevation):
                reverseVectorQueue.append(next)
                next.downPrev = v
                next.downElevation = dif
                goHigher = True    
        
        if(isXok):
            next = reverseVertexUpMatrix[vX-1][vY]
            dif = next.height - v.height
            if(dif > 0 and dif < v.downElevation):
                dif = v.downElevation
            if(dif > 0 and dif > next.downElevation):
                reverseVectorQueue.append(next)
                next.downPrev = v
                next.downElevation = dif
                goHigher = True  
                  
        if(not goHigher):
           reversePeaks.add(v) 
    
    realPeaks = set()
    for p in peaks:
        for r in reversePeaks:
            if p == r:
                p.downPrev = r.downPrev
                realPeaks.add(p)
                # print(p)
                # print(p)
    
    highest = max(realPeaks)
    # print(highest.upPrev)
    # print(highest)
    
    mostRight = highest
    for p in realPeaks:
        if p.height == mostRight.height and p.posX > mostRight.posX:
            mostRight = p
    
    # print lift 
    
    resultPath = ''
    resultSecondPart = ''
    actualVertex = mostRight
    
    while actualVertex != None:
        resultPath = str(actualVertex.height) + ' ' + resultPath
        actualVertex = actualVertex.upPrev
    
    actualVertex = mostRight.downPrev
    # print(actualVertex)
    while actualVertex != None:
        resultSecondPart = resultSecondPart + str(actualVertex.height) + ' '
        actualVertex = actualVertex.downPrev

    print(rows + columns - 1)
    #TODO vypisova chyba
    if(len(resultSecondPart) == 0):
        result = resultPath[:len(resultPath)-1]
    else:
        result = resultPath + resultSecondPart[:len(resultSecondPart)-1]
    print(result)
    # print(result[-1])
    exit(0)
        
    
    
    
    
    
    
    
        
    