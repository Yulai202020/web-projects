import os,requests,sys,socket
version_info = "v2.0.3"
apin = "App is downloaded !!!"
gain = "Game is downloaded !!!"
pwdcorrect="123"
def pwddel():
    pwdcorrect = ""
    with open("password.key","w") as f:
        f.write(pwdcorrect)
def pwd():
    with open("password.key","r") as f:
        pwdcorrect=f.read()
    if pwdcorrect == "":
        return
    else:
        password = input("Input password # ")
        if password == pwdcorrect:
            pass
        else:
            exit(0)
def setpwd(pwd):
    with open("password.key","w") as f:
        f.write(pwd)
def is_connected():
    try:
        socket.create_connection(("localhost", 8080))
    except OSError:
        exit()
def argv():
    try:
        if sys.argv[1] == "--info":
            print("<game|app> <delete|install> <pinneygame|calculatorapp|guessgame|infoapp> \n<print|echo> # for print\n<run> <pinneygame|calculatorapp|guessgame|infoapp>")
            exit(0)
    except:
        pass
def delin(oper="del",typer="app",name="calculatorapp"):
    if oper == "del" and typer == "app":
        deleter('..\\..\\Programs Files\\'+name+'.py')
        print("App is deleted !!!")
    elif oper == "del" and typer == "game":
        deleter('..\\..\\Programs Files\\'+name+'.py')
        print("Game is deleted !!!")
    elif oper == "in" and typer == "app":
        downloadFile("http://localhost:8080/files/"+name,"..\\..\\Programs Files\\",name)
        print("App is installed !!!")
    elif oper == "in" and typer == "game":
        downloadFile("http://localhost:8080/files/"+name,"..\\..\\Programs Files\\",name)
        print("Game is installed !!!")
def init():
    with open("..\\data\\setup.sys","r") as files:
        print(files.read())
def downloadFile(URL=None,pyth="..\\Programs Files\\apps",ver="0"):
    req = requests.get(URL)
    with open (pyth+ver+".py","w") as file:
        file.write(req.text)
    with open(pyth+ver+".py", 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()
def deleter(pyth):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), pyth)
    os.remove(path)