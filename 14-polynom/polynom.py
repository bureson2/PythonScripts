def polyEval(lst,x):
  value = lst[0]
  for i in range(1,len(lst)):
    value += lst[i] * (x ** i)
  return value


def polySum(lst1,lst2):
  #pomocne urceni vetsiho pole
  if len(lst1) >= len(lst2):
    big, small = lst1, lst2
  else: big , small = lst2, lst1
  #k prvkum vetsiho pole pricteme prvkz mensiho pole, zbytek se nemeni
  for i in range(0,len(small)):
    big[i] += small[i]
  big = polyControl(big)
  
  return big

def polyControl(lst):
  lst = lst[::-1] #potebujeme prochazet od zadu
  print(lst)
  for x in lst:
    if x != 0: break #kdyz skonci 0, ukonci se odmazavani
    else: lst.remove(x)
  lst = lst[::-1] #otoceni zpet
  return lst
  

def polyMultiply(lst1,lst2):
  exp = [] #pro velikosti exponentu x
  intermResults = [] #mezivysledky
  finalPoly = [] #vysledny polynom
  
  for i in range(0,len(lst1)):
    for j in range(0,len(lst2)):
      exp.append(i+j) 
      intermResults.append(lst1[i]*lst2[j])

  for i in range(0,max(exp)+1):
    res = 0
    for j in range(0,len(exp)):
      if exp[j] == i: #pokud je exponent mezivysledku na dane hodnote
        res += intermResults[j]
    finalPoly.append(res)
  
  return finalPoly