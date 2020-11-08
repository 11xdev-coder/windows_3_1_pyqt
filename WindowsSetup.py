import os,time
from GraphicsSetup import start
from PyQt5 import QtWidgets

if os.path.exists("MS_DOS") and not os.path.exists("MS_DOS/SetupEnds"):
    print("Downloading MS-DOS...")
    time.sleep(10)
    os.mkdir("MS_DOS/SetupEnds")
    print("MS-DOS downloading finished successfully!")
    print("Please restart your computer")
    input()
elif os.path.exists("MS_DOS") and os.path.exists("MS_DOS/SetupEnds"):
    print("Starting MS-DOS...")
    time.sleep(2)
    if os.path.exists("drivers/cd_driver/success"):
        if input("C:\\>") == "win":
            start()
    if input("C:\\>") == "a:\\":
        if input("A:\\>") == "StartSetup.bat" and not os.path.exists("drivers/cd_driver/success"):
            print("""*******************************************************
CD DRIVER INSTALLER v.2.1
(c) Blake Burgess

Installing Drivers...
        1 file(s) copied
Updating Setting Files...

Setup Complete!
*******************************************************""")
            if not os.path.exists("drivers"):
                os.mkdir("drivers")
            if not os.path.exists("drivers/cd_driver/"):
                os.mkdir("drivers/cd_driver")
            if not os.path.exists("drivers/cd_driver/success"):
                os.mkdir("drivers/cd_driver/success")
    else:
        print("Invalid command. Try again")
else:
    print("Cannot find MS-DOS folder!")