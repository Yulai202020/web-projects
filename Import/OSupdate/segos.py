import sys,settingsdata
sys.path.append(settingsdata.progfiles["pythapps"])
import datads,os
datads.is_connected()
datads.pwd()
datads.argv()
datads.init()
# datads argv() for args
# datads init() for start
# datads delin() for del app or install
# while
while True:
    # try
    try:
        inp = input("# ")
        insplit = inp.split()
        if insplit[0] == "os":
            if insplit[1] == "verinfo":
                print(datads.version_info)
            elif insplit[1] == "license":
                if os.path.isfile("LICENSE"):
                    print("LICENSE ")
                    with open("LICENSE") as f:
                        print(f.read())
            elif insplit[1] == "password":
                if insplit[1] == "del":
                    datads.pwddel()
                if insplit[1] == "set":
                    newpass = input("input new password: ")
                    datads.setpwd(newpass)
        elif insplit[0] == "echo":
            print(inp[5::])
        elif insplit[0] == "print":
            print(inp[6::])
        # open windows apps
        elif inp[0:4] == "open":
            if inp[5:12] == "windows":
                # paint
                if inp[13:18] == "paint":
                    os.system(settingsdata.OWA["PT"])
                # notepad
                elif inp[13:20] == "notepad":
                    os.system(settingsdata.OWA["NP"])
        elif insplit[0] == "run":
            # run
            if insplit[1] == settingsdata.OSA["KB"]:
                import kubgame
                kubgame.init()
            elif insplit[1] == settingsdata.OSA["GUG"]:
                import guessgame
                guessgame.init()
            elif insplit[1] == settingsdata.OSA["PG"]:
                import pinneygame
                pinneygame.init()
            elif insplit[1] == settingsdata.OSA["CA"]:
                import calculatorapp
                calculatorapp.init()
            elif insplit[1] == settingsdata.OSA["IA"]:
                import infoapp
                infoapp.init()
        elif insplit[0] == "game":
            # delete
            if insplit[1] == "delete":
                if insplit[2] == settingsdata.OSA["GUG"]:
                    datads.delin("del","game",settingsdata.OSA["GUG"])
                elif insplit[2] == settingsdata.OSA["PG"]:
                    datads.delin("del","game",settingsdata.OSA["PG"])
            # install
            elif insplit[1] == "install":
                if insplit[2] == settingsdata.OSA["GUG"]:
                    datads.delin("in","game",settingsdata.OSA["GUG"])
                elif insplit[2] == settingsdata.OSA["PG"]:
                    datads.delin("in","game",settingsdata.OSA["PG"])
        # app
        elif insplit[0] == "app":
            # delete
            if insplit[1] == "delete":
                if insplit[2] == settingsdata.OSA["CA"]:
                    datads.delin("del","app",settingsdata.OSA[""])
                elif insplit[2] == settingsdata.OSA["IA"]:
                    datads.delin("del","app",settingsdata.OSA[""])
            # install
            elif insplit == "install":
                if insplit[2] == settingsdata.OSA["CA"]:
                    datads.delin("in","app",settingsdata.OSA["CA"])
                elif insplit[2] == settingsdata.OSA["IA"]:
                    datads.delin("in","app",settingsdata.OSA["IA"])
    # excepts
    except FileNotFoundError as err:
        with open(settingsdata.Logs["perflogserropyth"]+"\\notfound.log","a") as file:
            file.write("Error 404\n\tError : File not found !!!\n")
        raise FileNotFoundError("Error : File not found !!!")
    except KeyboardInterrupt as err:
        with open(settingsdata.Logs["perflogsinfopyth"]+"\\exit.log","a") as file:
            file.write("Code 200\n\tExiting ...\n")
        print("^C")
        exit(0)
    except ModuleNotFoundError as err:
        with open(settingsdata.Logs["perflogserrorpyth"]+"\\notfound.log","a") as file:
            file.write("Error 500\n\tError : Module not found !!!\n")
        raise ModuleNotFoundError("Error : Module not found !!!")