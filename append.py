f=open("test.txt",'w')
for i in range(7,9):
    data=f"added line {i}\n"
    f.write(data)
f.close()