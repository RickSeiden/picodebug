from machine import RTC


def logPrint(myParam, outputToConsole = False, outputToFile = True, makeTimeStamp = True):
    
    if outputToConsole:
        print(f"{RTC().datetime()} - {myParam}")
    if outputToFile:
        with open("log1.txt", "a") as f:
            if makeTimeStamp:
                f.write(f"{RTC().datetime()} - {myParam}\n")
            else:
                f.write(f"{myParam}\n")

def logClean():
    import os
    maxFiles = 8
   
    for i in range(maxFiles): 
        try:
            os.remove(f"log{i+1}.txt")
        except:
            pass

def logRotate():
    import os

    fileSize = 0
    maxSize = 100000
    maxFiles = 8

    try:
        fileSize = os.stat('log1.txt')[6]

        #We should do rotation
        if fileSize >= maxSize:
    
            #Remove last file and free space 
            try:
     
                os.remove(f"log{maxFiles}.txt")
               
            except:
              
                pass

            #Shift files 
            for i in range(maxFiles - 1, 0, -1):
           
                try:
         
                    os.rename(f"log{i}.txt", f"log{i+1}.txt")
             
                except:
                 
                    pass
    except:
        pass
