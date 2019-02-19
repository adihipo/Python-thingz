mylist = [x*x for x in range(3)]                   #list, because of []. Can be run infinite times
for i in mylist:
  print(i)

mygenerator = (x*x for x in range(3))              #generator, because of (). Can be run just ONCE
for i in mygenerator:
  print(i)
print("->")
for i in mygenerator:                              #Ez már nem printel semmit...
  print(i)
print("<-")

def createGenerator():                             #generator készítsése. 
  mylist = range(3)                                #először lista
  for i in mylist:
    yield i*i                                      #de a yield csak egyszer adja vissza nekünk amit kérünk.

mygenerator2 = createGenerator()                   #yield használata.
print(mygenerator2)
#<generator object createGenerator at 0x000001C1E82303B8>. Mert a mygenerator2 egy object.
for i in mygenerator2:
  print(i)
print("->")
for i in mygenerator2:                             #Ez sem printel már semmit...
  print(i)
print("<-")

