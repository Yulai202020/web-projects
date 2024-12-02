import os
def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size
def init():
    print("-----------------------")
    print("InfoApp ...")
    print("-----------------------")
    if getFolderSize("\\..\\..\\D#")/1024 >= 1:
        print(str(getFolderSize("\\..\\..\\D#")//1024)+" KB ("+str(getFolderSize("\\..\\..\\D#"))+" bates)\n")
    elif getFolderSize("\\..\\..\\D#")/1024/1024 >= 1:
        print(str(getFolderSize("\\..\\..\\D#")//1024//1024)+" MB ("+str(getFolderSize("\\..\\..\\D#")//1024)+" KB)\n")
    print("Weighs OS\n")
    print(".\\bin  \n.\\Drives")
    print(".\\Perflogs\\*  \n.\\Perflogs\\errorlogs  \n.\\Perflogs\\infologs")
    print(".\\Programs Files")
    print(".\\SEGOS\\*  \n.\\SEGOS\\sys32  \n.\\SEGOS\\data")
    print("-----------------------")