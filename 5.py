def outWords(words):
  #start
  upperCount = 0
  lowerCount = 0
  for x in words:
     if x.isupper():
        upperCount = upperCount + 1
     else:
        lowerCount = lowerCount + 1
  return upperCount,lowerCount
  #end
words=input()
upperCount=0
lowerCount=0
result=outWords(words)
print("upper is %d"%result[0])
print("lower is %d"%result[1])