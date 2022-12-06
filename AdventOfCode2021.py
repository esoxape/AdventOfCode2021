import os
def Day1():    
    file = open("Day1.txt","r")
    depths = file.readlines()
    file.close()
    increases=0
    increases2=0
    for i in range(0, len(depths)-1, 1):
        if int(depths[i])<int(depths[i+1]):
            increases=increases+1
    for i in range(0, len(depths)-3, 1):                  
        if int(depths[i])+int(depths[i+1])+int(depths[i+2])<int(depths[i+1])+int(depths[i+2])+int(depths[i+3]):
            increases2=increases2+1
    print("Day 1 ")
    print("part1 "+str(increases)+" part2 "+str(increases2))
    print()
def Day2():
    file = open(os.getcwd()+"\Python\Day2.txt")
    depthFile = file.read()
    file.close()    
    depths=depthFile.split()
    horiz=0
    depth=0
    depth2=0
    aim=0  
    for i in range(0, len(depths)-1, 2):
        if depths[i]=="forward":
            horiz=horiz+int(depths[i+1]) 
            depth2=depth2+int(depths[i+1])*aim
        if depths[i]=="up":
            depth=depth-int(depths[i+1])
            aim=aim-int(depths[i+1])
        if depths[i]=="down":
            depth=depth+int(depths[i+1]) 
            aim=aim+int(depths[i+1])  
    print("stage1 "+str(depth*horiz)+" stage2 "+str(depth2*horiz))         
Day1()
Day2()