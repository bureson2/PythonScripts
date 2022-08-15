#---------------SORT NUMBERS--------------------

def mergeSort(data, condition):
    if len(data) <= 1:
        return data
    middleIndex = len(data) // 2
    leftSide = data[:middleIndex] 
    rightSide = data[middleIndex:]
    #nutne kvuli neprepisovani
    leftSideForDivide = mergeSort(leftSide, condition)
    rightSideForDivide = mergeSort(rightSide, condition)

    if condition == "ASC": return mergeUp(leftSideForDivide,rightSideForDivide)
    if condition == "DESC": return mergeDown(leftSideForDivide,rightSideForDivide)

def mergeUp(leftSide, rightSide):
    bothSides = []
    while leftSide and rightSide:
        if leftSide[0] < rightSide[0]: bothSides.append(leftSide.pop(0))
        else: bothSides.append(rightSide.pop(0))
    #pridani zbytku vetsiho pole
    if leftSide: bothSides += leftSide
    elif rightSide: bothSides += rightSide

    return bothSides

def mergeDown(leftSide, rightSide):
    bothSides = []
    while leftSide and rightSide:
        if leftSide[0] > rightSide[0]: bothSides.append(leftSide.pop(0))
        else: bothSides.append(rightSide.pop(0))
    #pridani zbytku vetsiho pole
    if leftSide: bothSides += leftSide
    elif rightSide: bothSides += rightSide

    return bothSides

def sortNumbers(data, condition):
  return mergeSort(data, condition)

#---------------SORT DATA--------------------

def getDict(data, weights):
  dataDict = zip(data, weights)
  dataDict = {key:value for key, value in zip(data, weights)}
  return dataDict

def bubbleSortUp(weights, data):
  for i in range(0,len(weights)-1):
    for j in range(0,len(weights)-1):
      if weights[j] > weights[j+1]:
        weights[j], weights[j+1] = weights[j+1], weights[j]
        data[j], data[j+1] = data[j+1], data[j]

  return data
 
def bubbleSortDown(weights, data):
  for i in range(0,len(weights)-1):
    for j in range(0,len(weights)-1):
      if weights[j] < weights[j+1]:
        weights[j], weights[j+1] = weights[j+1], weights[j]
        data[j], data[j+1] = data[j+1], data[j]

  return data    

def sortData(weights, data, condition):
  if len(weights) != len(data):
    raise ValueError('Invalid input data')
  if condition == "ASC": return bubbleSortUp(weights, data)
  elif condition == "DESC": return bubbleSortDown(weights, data)

#---------------TESTS--------------------

#print(sortNumbers([5,4,8,9,7,4,1,2,3,4,45,4,0,1],"ASC"))
#print(sortData([7316, 1082, 5828, -941, 5054, 8017, 8665, 8927, 2464, 9172, 7292, 5100, 1934, 3343, 6381, 1152, 9195, 2955, 9615, 5748, 3819, 4943, -71], ['Praha', 'Brno', 'Pariz', 'Londyn', 'Bratislava', 'Pelhrimov', 'Jihlava', 'CB'], 'DESC'))
#print(sortData([2,6,5], ['Ford','BMW','Audi'], 'DESC'))
#print(sortData([2,5,6], ['Ford','BMW','Audi'], 'ASC'))
#print(sortData([3,2,4],['Ford','BMW','Audi'], 'DESC'))
print(sortData([2, 3, 4, 4, 5, 19, 2, 1],['Praha', 'Brno', 'Pariz', 'Londyn', 'Bratislava', 'Pelhrimov', 'Jihlava', 'CB'],"ASC"))