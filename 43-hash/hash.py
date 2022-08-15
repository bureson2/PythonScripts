import sys
import copy

class HashArray:
    def __init__(self, size, name):
        self.name = name
        self.actualSize = size
        self.defaultSize = size
        self.numberOfOriginalRecord = 0
        self.hashTable = [0] * self.actualSize
        
class HashRecord:
    def __init__(self, content):
        self.content = content
        self.multiplicity = 1

def setDirectionI(club, line):
    hashTableSizes = [int(s) for s in line.split() if s.isdigit()]
    for i in range(0, len(hashTableSizes)):
        club[i].actualSize = hashTableSizes[i]
        club[i].defaultSize = hashTableSizes[i]
        club[i].hashTable = [0] * hashTableSizes[i]
        
def writeMessageForAll(club, line):
    for member in club:
        writeRecord(member, line)
        if((member.numberOfOriginalRecord) / member.actualSize > 0.7): 
            enlargeHashTable(member) 
            
def deleteMessage(member, line):
    lineHash = hashContent(line, member.actualSize)
    
    while True:
        if(member.hashTable[lineHash] == 0):
            break
        elif(member.hashTable[lineHash] == -1): 
            lineHash = int((lineHash + 1) % member.actualSize)
        elif(member.hashTable[lineHash].content == line):
            if(member.hashTable[lineHash].multiplicity == 1):
                member.numberOfOriginalRecord -= 1
                member.hashTable[lineHash] = -1
                break
            else: 
                member.hashTable[lineHash].multiplicity -= 1
                break
        else:
            lineHash = int((lineHash + 1) % member.actualSize)
       
    if(member.actualSize > member.defaultSize and (member.numberOfOriginalRecord) / member.actualSize < 0.3):        
        reduceTable(member) 
 
def reduceTable(member):
    oldHashTable = copy.deepcopy(member.hashTable)         
    member.hashTable = int(member.actualSize / 2) * [0]
    member.actualSize = member.actualSize // 2
    member.numberOfOriginalRecord = 0
    for record in oldHashTable:
        if record != 0 and record != -1: 
            for _ in range(record.multiplicity):
               writeRecord(member, record.content)

                
def enlargeHashTable(member):
    oldHashTable = copy.deepcopy(member.hashTable)
    member.hashTable = (2 * member.actualSize) * [0]
    member.actualSize = member.actualSize * 2
    member.numberOfOriginalRecord = 0
    for record in oldHashTable:
        if record != 0 and record != -1: 
            for _ in range(record.multiplicity):
               writeRecord(member, record.content)     
    
def searchIndex(member, hashNumber, line):
    while True:
        if member.hashTable[hashNumber] == 0:
            return -1
        elif member.hashTable[hashNumber] == -1:
            hashNumber = (hashNumber + 1) % member.actualSize
        elif member.hashTable[hashNumber].content == line:
            return hashNumber
        else:
            hashNumber = (hashNumber + 1) % member.actualSize 
            
    
def writeRecord(member, line):
    hashNumber = hashContent(line, member.actualSize)
   
    index = searchIndex(member, hashNumber, line)
    if(index == -1):
        while member.hashTable[hashNumber] not in [-1,0]:
            hashNumber = (hashNumber + 1) % member.actualSize 
        member.hashTable[hashNumber] = HashRecord(line)
        member.numberOfOriginalRecord += 1
    else:
        member.hashTable[index].multiplicity += 1
        
def isCorrectNumber(line):
    if '#' not in line: return False
    if line[1].isdigit():
        if int(line[1]) > 5: 
            sys.stderr.write("Error: Chybny vstup!" + '\n')
            return False
        return True
    return False 
        
def hashContent(content, hashNumber):
    totalValue = 0    
    for i in range(len(content)-1):
        if(content[i] == ' '): 
            totalValue += (31 * (32 ** i))
        else:
            totalValue += ((ord(content[i]) - 96) * (32 ** i))   
    return int(totalValue % hashNumber)

if __name__ == "__main__":
    f = sys.stdin
    # f = open('c:/Users/bures/OneDrive/Plocha/DSA03/delete_09.in', 'r')
    lines = f.readlines()
        
    mirek = HashArray(11, 'Mirek')
    jarka = HashArray(11, 'Jarka')
    jindra = HashArray(11, 'Jindra')
    rychlonozka = HashArray(11, 'Rychlonozka')
    cervenacek = HashArray(11, 'Cervenacek')
    
    club = []
    club.append(mirek)
    club.append(jarka)
    club.append(jindra)
    club.append(rychlonozka)
    club.append(cervenacek)
    
    if("i" in lines[0]):
        setDirectionI(club, lines[0])    

    writeAll = False
    numberActive = False
    activeNumber = 0
    activeP = False
    activeD = False
    
    for line in lines:
        if "#a" in line:
            writeAll = True
            activeP = False
            activeD = False
            activeNumber = False
        elif "#" in line:
            writeAll = False

        if isCorrectNumber(line):
            activeNumber = int(line[1])
            activeP = False
            activeD = False
            
        
        
        if activeNumber and "#p" in line:
            print(club[activeNumber-1].name + "\n\t" + str(club[activeNumber-1].actualSize) + " " + str(club[activeNumber-1].numberOfOriginalRecord))
            activeP = True
            activeD = False
            
        if activeNumber and "#d" in line: 
            activeD = True
            activeP = False
        
        elif not activeNumber and ("#p" in line or "#d" in line):       
            sys.stderr.write("Error: Chybny vstup!" + '\n')
        
        if writeAll and '#' not in line:
            writeMessageForAll(club, line)
            
        if(activeP and "#p" not in line):
            messageHash = hashContent(line, club[activeNumber-1].actualSize)
            memberTable = club[activeNumber-1].hashTable     
            
            short = slice(len(line)-1)
            while(memberTable[messageHash] != 0):
                if(memberTable[messageHash] == -1): 
                    messageHash = int((messageHash + 1) % club[activeNumber - 1].actualSize)
                    continue
                if(memberTable[messageHash].content == line):
                    
                    print('\t' + line[short] + ' ' + str(messageHash) + ' ' + str(memberTable[messageHash].multiplicity))
                    break
                messageHash = int((messageHash + 1) % club[activeNumber - 1].actualSize)
                
            if(memberTable[messageHash] == 0): 
                print('\t' + line[short] + ' -1 0')

        if(activeD and "#d" not in line):
            deleteMessage(club[activeNumber-1], line)
    
    exit(0)