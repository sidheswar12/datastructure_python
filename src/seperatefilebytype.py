baseFilename = "filename.txt"
content = []
with open(baseFilename) as f:
    content = f.readlines()
    content = [x.strip() for x in content] 

fileExtension = []
for i in content: 
    data = i.split(".")
    if(data[1] == 'c'):
        f= open("c_names_list_00.txt","a+")        
        f.write(i+'\n')
        f.close()
    elif(data[1] == 'cpp'):
        f1= open("cpp_names_list_01.txt","a+")
        f1.write(i+'\n')
        f1.close()
    else:
        f2= open("cs_names_list_02.txt","a+")
        f2.write(i+'\n')
        f2.close()
