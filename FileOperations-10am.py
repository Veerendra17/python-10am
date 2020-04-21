# File Operations -- Performing reading ,writing and appending on file..

# .txt,.py,.csv.xlsx,.json

# 2 ways to open a file..

# 1st Way:
    # variable = open("pathof file",modetoopen)

# 3 modes to open a file
    # read -- r
    # write -- w
    # append -- a

# file = open("C:\\Users\\sreddy\\Downloads\\sample-10am.txt",'r')

# file.close()
# print(file.closed)

# 2nd Way:

"""
with open(path of fiile, mode) as object:
    statements
"""

# with open("C:\\Users\\sreddy\\Downloads\\sample-10am.txt",'r') as file:
#     print(file)
# 
# print(file.closed)


# Reading -- 'r'
    # read - will read all the content in the file. But will read it by letter by letter...
    # readline - will read 1 line at atime..
    # readlines - Will read all the content line by line and return a list of elements where each element is one line inside the file...

# with open("C:\\Users\\sreddy\\Downloads\\sample-10am.txt",'r') as file:
    # print(file.read())
    # for j in file.read():
    #     print(j)
    # print(file.readline())
    # for j in file.readline():
    #     print(j)
    # print(file.readline())
    # print(file.readlines())
    # print(file.readlines()[2])
    # read_line = file.readlines()
    # for line in read_line:
    #     if "Python" in line:
    #         print(read_line.index(line))
    # print(file.readlines().index('Ipl is postponed due to carona.\n'))

# Writing ---- overwriting the previous content and adding only the new content...
# Writing can automatically create the file if the file not existed..
    # write -- its for adding only 1 string oncontent at atime...
    # writelines --- It can add n number of line of content..


# with open("C:\\Users\\sreddy\\Downloads\\sample-10am-1.txt","w") as file:
#     # file.write('Python is a programming language...')
#     # file.write("Django is a framework....")
#     file.writelines(["Python is a prgamming language\n","Django is a framework\n","Ipl is Postponed due carona.."])


# Appedning -- Adding the new content to the previous existing content..
# with open("C:\\Users\\sreddy\\Downloads\\sample-10am-1.txt","a") as file:
#     # file.write('\nPython is a programming language...')
# #     # file.write("Django is a framework....")
#     file.writelines(["\nPython is a prgamming language\n","Django is a framework\n","Ipl is Postponed due carona.."])


# CSV -- Comma Seperated Values

import csv



# with open("C:\\Users\\sreddy\\Downloads\\std_details.csv",'r') as file:
#     csv_reader = csv.reader(file)
#     # print(csv_reader)
#     next(csv_reader) #skip the line
#     for row in csv_reader:
#         if row[0]=="Rajesh":
#             print(row)
        # print(row)

# with open("C:\\Users\\sreddy\\Downloads\\std_details_1.csv","a",newline="") as file:
#     csv_writer = csv.writer(file)
#     i=0
#     no_time = int(input("Enter no of entries:-"))
#     while i<no_time:
#         name=input("Enter name:-")
#         email=input("Enter Email:-")
#         mobile =input("Enter Mobile:-")
#         csv_writer.writerow([name,email,mobile])
#         i+=1

    # csv_writer.writerow(['std_name','std_email','std_mobile'])
    # csv_writer.writerow(['Ramesh','ramesh@gmail.com','8898429892'])
    # csv_writer.writerows([['std_name','std_email','std_mobile'],['Ramesh','ramesh@gmail.com','8898429892']])
    


# first.txt --- a=5

# second.txt --- b=67

#thid.txt  ---- c=a-b,value of c=-62


# sample.csv --- 

# Specific the column to filter:- std_name
# Elements to perform search :- R..