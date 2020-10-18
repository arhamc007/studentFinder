#Declaring the array and asking the user to enter their details 
array = []
totstu = int(input("Please enter the total number of students"))
for count in range (0, totstu):
    name = input("Please enter the name of the student")
    email = input("Please enter the email address of the student")
    n = name+"#"+email
    array.append(n)
print ("Name", " "*21, "Email Address")
for i in range (totstu):
    l=array[i].split("#")
    print(l[0], " "*(25-len(l[0])), l[1])
#in case a student decides to leave 
for x in array:
    if x != None or len(array) != 0:
        print(x)
#searching for a name in the array
search=input("Please enter your query")
for z in array:
    nam=z.split("#")
    if nam[0]==search:
        print(nam[1])
#searching for a name by the first few letters entered by the user
search=input("Please input your name")
for y in array:
    if y.startswith(search):
        l=y.split("#")
        print (l[0], " ", l[1]) 

studentarr=[]
for c in range (totstu):
    studentarr.append (4*["0"])
print (studentarr)

#converting it to a 2D array format 
for c in range (totstu):
    studentarr [c][0] = input("Please enter your name ")
    studentarr [c][1] = input("Please enter your email ")
    studentarr [c][2] = input("Please enter your DOB in the format DD/MM/YY ")
    studentarr [c][3] = input("Please enter your ID ")
print (studentarr) 
print ("Name" + " "*21 + "Email" + " "*21 + "DOB" + " "*21 + "Student ID")
for c in range (totstu):
    Name= studentarr [c][0]
    Email= studentarr [c][1]
    DOB= studentarr [c][2]
    StudentID= studentarr [c][3]
    print (Name + " "*(25-len(Name)) + Email + " "*(25-len(Email)) + DOB + " "*(25-len(DOB)) + StudentID)


    if Name != None and Email != None and DOB != None and StudentID != None :
        print (Name + " "*(25-len(Name)) + Email + " "*(25-len(Email)) + DOB + " "*(25-len(DOB)) + StudentID)

search= input("Please enter your Name ")
for y in range (totstu):
    Name = studentarr[y][0]
    if search==studentarr[y][0]:
        Email = studentarr[y][1]
        print (Email)

search= input("Please enter your Name ")
for y in range (totstu):
    if studentarr[y][0].startswith(search):
        Name = studentarr[y][0]
        Email = studentarr[y][1]
        DOB = studentarr[y][2]
        StudentID = studentarr[y][3]
        print ("Name" + " "*21 + "Email" + " "*21 + "DOB" + " "*21 + "Student ID")
        print (Name + " "*(25-len(Name)) + Email + " "*(25-len(Email)) + DOB + " "*(25-len(DOB)) + StudentID)
