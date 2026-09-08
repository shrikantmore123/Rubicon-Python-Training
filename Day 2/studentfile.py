import os

filename="student.txt"
try:
    with open(filename,"w") as file:
        file.write("Name: Anteshwar\n")
        file.write("course : python \n")
        file.write("Age : 89\n")
    print("File created Successfully")
    
    # write operation
    with open(filename,"w") as file:
        file.write("Name : yogesh \n")
        file.write("course : python , Django \n")
        file.write("Age : 89\n")
        file.close()
    print("Data submit Successfully")

    # Read operation
    with open(filename,"r") as file:
        data=file.read()
    print("File read Successfully")
    print(data)
    # read line
    with open(filename,"r") as file:
        line=file.readline()
    print("Read line Successfully")
    print(line)

    # read lines 
    with open(filename,"r") as file:
        lines=file.readlines()
    print(" All line  read Successfully")
    print(lines)

    # append file
    with open(filename,"w") as file:
        file.write("Technology :  Web developement\n")
        file.write("Experiment : 3.5 \n")
    print("Data is append successfully \n")
    # updated file data
    with open(filename,"r") as file:
        print(" Updated File read Successfully\n")
        data=file.read()
        print(data)
    

   #  check file exist or not 
    if (os.path.exist(filename)):
        print("exist file")
        
        # file info
    size=os.path.getsize(filename)
    print("File size is :",size)

except FileExistsError:
    print("file already exist")
except FileNotFoundError:
    print("File not present")
except Exception as e:
    print("error",e)

#  default file
if (os.path.exists(filename)):
    os.remove(filename)
    print("file removed")