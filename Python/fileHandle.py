##>>> 1. Open file (r for Read, r+ for read & Write, w for write, a for apend)
# f = open('hi.txt','r')
# print(f.name)

##>>> 2. Close File after all work done
# f.close()


##>>> 3. File Open with context Manager
# with open('hi.txt','r') as f:
#     print(f.name) 


##>>> 4. Read file lins
# with open('hi.txt','r') as f:
#     #print(f.read()) #Rad File Content
#     #print(f.readlines()) #Get list of lines
#     #print(f.readline()) #Get line one by one

#     #Read lils in a loop
#     for line in f:
#         print(line, end = '')


# ##>>> 4. Write file
# with open('hello.txt','w') as f:
#     f.write(" Ram Bone full pare ")


##>>> 5. Read and Writ files Together
with open('hi.txt','r') as fr:
    with open('hello.txt','w') as fw:
        for line in fr:
            fw.write(line)
