#Arithmatic
a = 20
b = 3
print("Add: a+b = ", a+b)
print("Sub: a-b = ", a-b)
print("Mul: a*b = ", a*b)
print("Div: a/b = ", a/b)
print("Div no decimal: a//b = ", a//b)
print("Rem: a%b = ", a%b)
print("Exp: b**b = ", b**b)

#Strings
print("________________________________________")
print("Its 5AM")
print('The backslash in \'don\'t\' is an escape character')
print('Text in double quotes "like this" is printable \n'
      'when you use single quotes')
print(r'Adding 'r' in front of a link which already contains backslashes prints the raw text.')

firstName = 'Gordon'
lastName = 'Ramsay'
print("__________________________")
print("Concatenation of names:")
print(firstName+lastName)
print(firstName + ' ' + lastName)
print("Prints name multiple times:")
print(firstName*3)
print(lastName*3)

print("_____________________")
print("This is a list:")
players = [66, 45, 22, 44]
print("List: ", players)
print ("players[0]: ", players[0])
#Printing using for loop
print("Printing using for loop:")
for item in players:
    print(item)

print("Adding items to the list using '+': ")
players + [56, 25, 63]
print(players)
print("Appending using list.append:")
players.append('yay')
print(players)
print("Slicing list items using ':'. Stops at n:")
print(players)
print(players[0:1])
print(players[0:2])
print(players[0:3])
players[:2] = [0, 0]  #Added 0,0 to the first of the list
#print(players[:2])
#players[:2] = []
print(players)
players[:] = [] #Empties the whole list
print("Empty the whole list when assigned as '[]':")
print(players)

#Program - if elif else
print("_______________________")
print("Program - if elif else:")
name = 'Priyanka'
if name == 'Priyanka': #Do not forget the colon :(((((
    print("No more falafel for you!")
else:
    print("FALAFEL!!")

print("_______________________________")
print("Printing a new list and their char lengths:")
cityList = ['Peoria', 'Chicago', 'New York','California']
for c in cityList:
    print(c)
    print(len(c))

print("_______________________________")
print("Let's print something using a range")
for c in range(5):
    print("Priyanka is the best")
print("\nNow when I print the same variable, it takes the values in the range i.e, 0-5")
for c in range(5):
    print(c)

print("_________________________________")
print("Mentioning a range (5,12) prints c as 5 to 12:")
for c in range(5, 12):
    print(c)

print("_________________________________")
print("Passing arguments like (starting num, last num, increment prints:")
for c in range(10, 40, 5):
    print(c)

print("________________________")
print("Here goes a 'while' loop:")
falafels = 5
while falafels < 10:
    print(falafels)
    falafels +=1 #adds 1 each time

print("________________________")
print("...statement... results in a multilinequote")

print("Magic Number")
magicNumber = 11

for c in range(100):
    if c is magicNumber:
        print(c, "is the Magic Number!")
        break
    else:
        print(c)

print("_________________________")
print("The 'continue' statement prints numbers except the ones mentioned:")
numTaken = [2,4,6,]
print("These are odd")
for n in range(1,10):
    if n in numTaken:
        continue
    print(n)  #indentation is important

print("____________________________")
def printFunc():
    print("A function printed me!")
printFunc()

def drivingAge(age):
    age <= 18
    return age

driveAge = drivingAge(18)
print("Can drive if", driveAge, "or older")

print("_________________")
def momSays(ans= 'No'):
    if ans is 'School':
        ans = 'Yes'
    elif ans is 'Homework':
        ans = 'Yes'
    print(ans)   #Indentation confused you again

momSays('School')
momSays('Homework')
momSays()
print("_________________")
print("Keyword arguments:")
def madlib(noun="You",verb = "are", adj="beautiful"):
    print(noun,verb,adj)

madlib()
madlib(adj="sweet")
madlib(adj="kind")
madlib(adj="important")

print("_______________________")
def addNum(*args):
    total = 0
    for a in args:
        total += a
    print(total)

addNum(3)
addNum(30,3,4,8)

print("_______________________")
print("Unpacking arguments using(*):")
def bmiCal(weight, height): #data in kgs & meters
    bmi = (weight/(height*height))
    print(bmi)


bmiPri = (50,1.6256)
bmiCal(bmiPri[0], bmiPri[1])
bmiCal(*bmiPri)

print("_______________________")
print("This is an Arabic Dictionary:") #{}for a dictionary

words = {'Salam':" Peace", 'Alhumdulillah':" Praises to Allah"}
print(words['Salam']) #prints only the value
for k, v in words.items():
    print(k+v)

print("_______________________")
print("Modules test - include another file")
import modFile
modFile.fish()

print("_______________________")
print("printing a random number...")
import random
x = random.randrange(1,50)
print(x)

print("_______________________")
import urllib.request #requestttt

def downloadImg(url):
    name = random.randrange(1,1000)
    fullname = str(name) + '.jpeg' #python doesn't like mixing strings and numbers so convert str to int
    urllib.request.urlretrieve(url, fullname)

#downloadImg("https://i2.wp.com/designbroth.com/wp-content/uploads/2017/09/koffee-lub.-1-2.png?w=500")

print("____________________________")
fw = open('sample.txt', 'w')
fw.write('This is some random text in a file I created using python!!')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
print("____________________________")
