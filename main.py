
def Add_Book():
    Name= input("Enter the name of the Book :  ")
    Author= input("Enter the name of the Author : ") 
    
    file= open('library.txt','a')
    file.write("\n")
    file.write(Name )
    file.write("\n")
    file.write(Author)

    print("Your Book has added successfully")
    
    
def Search_Book():
    
    file = open('library.txt', 'r')
    count = 0
    book = input("Type in the book you want to seacrh:  ").lower()
    i = 0
    while True:
    
        line = file.readline().strip('\n')
        line2 = file.readline().strip('\n')
        

        if book == line:
            print("book found at:  ", count ,"position")
            print(line)
            print(line2)
            break
        
        elif (book == line2):
            print("Author found at:  ", count ,"position")
            print(line)
            print(line2)
            break
        count += 1
        
        if(line):
            pass
    
        else:
            print("book not found")
            break


    

    
def Delete_Book():
    file=open('library.txt','r')
    line = file.read().split('\n')
    toDelete =input("Type in the book/author you want to delete:   ").lower()
    i = 0
    flag = False
    while(i<len(line)):
        if(line[i] == toDelete and i%2==0):
            
            flag = True
            line.remove(line[i+1])
            line.remove(line[i])
            
        elif(line[i] == toDelete):
            
            flag = True
            line.remove(line[i])
            line.remove(line[i-1])
            
        i+=1
    if(flag):
        
        file.close()
        
        file = open('library.txt','w')
        
        counter = 1
        length = len(line)
        
        for x in line:
            file.write(x)
            if(counter != length):
                file.write("\n")
            counter+=1
        print("Book deleted successfully")
    else:
        print("book/autor not present")
    
   
    
    
    
    
print("             Welcome to LIBRARY")
print(" To add a book in the LIBRARY:      PRESS 1>>>\n To seacrh the book in the LIBRARY: PRESS 2>>>\n To delete a book in the LIBRARY:   PRESS 3>>>")
x = int(input())
if(x==1):
    Add_Book()
elif(x==2):
    Search_Book()
elif(x==3):
    Delete_Book()
else:
    print("Wrong Input")
    