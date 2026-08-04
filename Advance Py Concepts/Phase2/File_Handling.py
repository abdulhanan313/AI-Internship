#open() modes- r,w,a,rb,wb
#file=open("data.txt","w")

#"data.txt","w")
#Hello it's appeared again.\n")
#It's next line.")

#fruits = ["apple\n","banana\n","mango\n","amrood\n"]
#file=open("data.txt","a")
#file.writelines(fruits)
#file.write("Above are fruit names")
#file.close()


#file=open("data.txt","r")


#content = file.readlines()
#print(content)

#for line in file:
#   print(line.strip())
#file.close()

try :
    with open("data1.txt","r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("Filenot found")

print("File handling learning")

