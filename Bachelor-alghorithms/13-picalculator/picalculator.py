import math

def leibnizPi(n):
  #vygenrovani pole lichych cisel
  odd = [x for x in range(1,2*n) if x%2 != 0]
  sum = 0
  sum = 0

  for i in range(0,n):
    #podle toho, zda se jedna o sudou nebo lichou pozici se vyhodnoti znamenko
    if i%2==0:
      sum += 4.0/odd[i]
    else:
      sum -= 4.0/odd[i]
  
  return sum


def nilakanthaPi(n):
  sum = 3
  coef = []
  #vyplneni pole deliteli jednotlivych clenu
  for i in range(1,n+1):  
    coef.append(i*2 * (i*2+1) * (i*2+2))
  if n > 1:
    #podle toho, zda se jedna o sudou nebo lichou pozici se vyhodnoti znamenko
    for i in range(0,n-1):
      if i%2 == 0:
        sum += 4.0/coef[i]
      else:
        sum -= 4.0/coef[i]
    return sum
  else: return sum

def newtonPi(n):
  nplus1 = n - (math.sin(n)/math.cos(n)) # hodnota clenu n+1
  while n != nplus1:
    n = nplus1
    nplus1 = n - (math.sin(n)/math.cos(n)) # hodnota noveho clenu n+1
  return n


print(nilakanthaPi(1))
