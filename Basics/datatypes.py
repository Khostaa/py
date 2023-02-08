# for comment

myint = 5
print(myint)

myfloat = 2.00
print(myfloat)

mystr = "I am string"
print(mystr)

mybool = True
print(mybool)

mylist = [0, 1, "two", 3.0, False] # [big brackets for list]
print(mylist)

mytuple = (0,1,2) #(small brackets for tuple)
print(mytuple) #once declared can't be changed

mydict = { "key" : 3, "one": 1} #(curly braces for dictionary)
print(mydict) # in the form { "key" : value}

# to access member of sequence type, use [index]
print(mylist[2]) #index starts with 0
print(mytuple[0])

#use slices to get part of sequence
print(mylist[1:3]) # prints from index 1 to 3
print(mylist[:3]) #no index means before/after all are included

print(mylist[0:4:2]) #prints form index 0 to 4 and skips every 2 elements

#variables of different types cannot be combined
print("String"+ "123")

def func():
    mystr = "I am new string" # this is local variable
    print (mystr)

func()
print(mystr)    #this is global variable

def func():
    global mystr #global variable called inside function
    print (mystr)
func()

del mystr # deletes varaible
