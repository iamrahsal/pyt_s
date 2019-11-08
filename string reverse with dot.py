def sReverse(ss):
  stemp = ""
  slist = []
  slist1 = []

  for i in ss:
    if i == ".":
      slist.append(stemp)
      stemp = ""
    else:
      stemp = stemp + i
    
  slist.append(stemp)

  slist1 = slist[::-1]
  for j in slist1:
    if j == slist1[0]:
      resStr = slist1[0]
    else:
      resStr = resStr + "." + j
    
  return resStr

ss = input()
print( sReverse(ss) )