from heapq import merge
import sys
import random
 
def generate_sequence(count, max):
    numbers = []
    for i in range(count):
        numbers.append(random.randint(0, max))
        # if(i < 10): numbers.append(10 - i)
        # else: numbers.append(0)
    return numbers
     
# Kontrola kladneho max prvku  
def control_maximum(maximum):
    if(maximum < 1):
        sys.stderr.write("Error: Maximum neni kladne!" + '\n' + '\n')
        exit(1)

# Kontrola informaci o razeni
def control_arrangement(arrangement):
    if(arrangement not in [0,1,2]):
        sys.stderr.write("Error: Neznamy typ razeni posloupnosti!" + '\n' + '\n')
        exit(1) 
 
# Kontrola informace o viru        
def control_virus(virus):
    if(virus not in [0,1]):
        sys.stderr.write("Error: Nelze urcit, zda posloupnost napadl virus!" + '\n' + '\n')
        exit(1)  

def control_numbers_range(sequence, maximum):
    for number in sequence:
        if(number > maximum or number < 0):
            sys.stderr.write("Error: Prvek posloupnosti je mimo rozsah!" + '\n' + '\n')
            exit(1)  
            
def control_sequence_arrangement(sequence, arrangement):
    if(arrangement == 1):
        for i in range(0, len(sequence) - 1):
            if(sequence[i] > sequence[i+1]):
                sys.stderr.write("Error: Posloupnost neni usporadana!" + '\n' + '\n')
                exit(1)
    if(arrangement == 2):
        for i in range(0, len(sequence) - 1):
            if(sequence[i] < sequence[i+1]):
                sys.stderr.write("Error: Posloupnost neni usporadana!" + '\n' + '\n')
                exit(1)
                
def control_sequence_size(sequence):
    count = len(sequence)
    if(count < 1000):
        sys.stderr.write("Error: Posloupnost ma mene nez 1000 prvku!" + '\n' + '\n')
        exit(1)
    if(count > 1000000):
        sys.stderr.write("Error: Posloupnost ma mene nez 1000000 prvku!" + '\n' + '\n')
        exit(1)  
    return count               
 
def radixForbiddenWordThatMustNotEvenBeMeant(sequence, maximum, size):
    exponent = 1
    while maximum / exponent > 0:
        countingForbiddenWordThatMustNotEvenBeMeant(sequence, exponent, size)
        exponent *= 10

def countingForbiddenWordThatMustNotEvenBeMeant(sequence, exponent, size):
    forbiddenWordSequence = [0] * size
    count = [0] * 10 #nejvetsi cislo 2147483647 ma 10 cifer

    for i in range(0, size):
        index = sequence[i] // exponent
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = sequence[i] // exponent
        forbiddenWordSequence[count[index % 10] - 1] = sequence[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        sequence[i] = forbiddenWordSequence[i] 
 
def countForbiddenWordThatMustNotEvenBeMeant(sequence, maximum, size):
    help = [0] * (maximum + 1)
    for num in sequence:
        help[num] = help[num] + 1
    
    result = [0] * size
    resultIndex = 0
    
    for i in range(0,maximum+1):
        if(help[i] == 0):
            continue
        elif(help[i] == 1):
            result[resultIndex] = i
            resultIndex = resultIndex + 1
        else:
            for j in range(0, help[i]):
                result[resultIndex] = i
                resultIndex = resultIndex + 1
    
    return result

def mergeForbiddenWordThatMustNotEvenBeMeant(sequence, size):
    if size > 1:
        middleIndex = size // 2
        leftPart = sequence[0:middleIndex]
        rightPart = sequence[middleIndex:size] #mozno minus 1
        
        mergeForbiddenWordThatMustNotEvenBeMeant(leftPart, len(leftPart))
        mergeForbiddenWordThatMustNotEvenBeMeant(rightPart, len(rightPart))
        
        leftPartIndex = 0
        rightPartIndex = 0
        forbiddenWordIndex = 0
        leftPartLength = len(leftPart)
        rightPartLength = len(rightPart)
        
        while leftPartIndex < leftPartLength and rightPartIndex < rightPartLength:
            if(leftPart[leftPartIndex] < rightPart[rightPartIndex]):
                sequence[forbiddenWordIndex] = leftPart[leftPartIndex]
                leftPartIndex = leftPartIndex + 1
            else:
                sequence[forbiddenWordIndex] = rightPart[rightPartIndex]
                rightPartIndex = rightPartIndex + 1
            forbiddenWordIndex = forbiddenWordIndex + 1
        
        while leftPartIndex < leftPartLength:
            sequence[forbiddenWordIndex] = leftPart[leftPartIndex]
            leftPartIndex = leftPartIndex + 1
            forbiddenWordIndex = forbiddenWordIndex +1
            
        while rightPartIndex < rightPartLength:
            sequence[forbiddenWordIndex] = rightPart[rightPartIndex]
            rightPartIndex = rightPartIndex + 1
            forbiddenWordIndex = forbiddenWordIndex + 1 
        
    return sequence
 
if __name__ == "__main__":
    
    f = sys.stdin
     
    lines = f.readlines()
    task = lines.pop(0).split()
    maximum = int(task[0])
    arrangement = int(task[1])
    virus = int(task[2])
     
    # sequence = generate_sequence(10000, maximum)
    sequence = []
    for line in lines:
        sequence.append(int(line))
     
    control_maximum(maximum)
    control_arrangement(arrangement)
    control_virus(virus)
    control_numbers_range(sequence, maximum)
    if(virus != 1):
        control_sequence_arrangement(sequence, arrangement)
    size = control_sequence_size(sequence)      
     
    if(arrangement == 1 and virus != 1):
        for number in sequence:
            print(number)
        exit(0)
         
    if(arrangement == 2 and virus != 1):
        for i in range(len(sequence)-1, -1, -1):     
            print(sequence[i])
        exit(0)
         
    if(maximum < size):
        sequence = countForbiddenWordThatMustNotEvenBeMeant(sequence, maximum, size) 
    else:
        sequence = mergeForbiddenWordThatMustNotEvenBeMeant(sequence, size)
    
    for number in sequence:
            print(number)
    
    
    exit(0)
     