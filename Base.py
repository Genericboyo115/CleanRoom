import os
import socket
def start1():
    print("Input your SCID here")
    print("Input data in this format: xx:xx:xx:xx:xx")
    a1 = input(">>>")
    print("Input your name in the following format: Last, Middle Initial, First")
    a2 = input(">>>")
    print("Input your Group name or number here")
    a3 = input(">>>")
    print("Input your CleanRoom Server IP address")
    a4 = input(">>>")
    print("Please enter you secure phrase")
    a6 = input(">>>")
    print("Please enter your assigned email")
    a7 = input(">>>")
    print("PLease enter your password")
    a8 = input(">>>")
    print("Please enter your group key")
    a9= input(">>>")
    print("Please input your assigned room")
    a10 = input(">>>")

    
    
    #JSON write script
    def jsonwrite():
        import json 
        # Data to be written
        dictionary = {
            "SCID": a1,
            "name": a2,
            "email": a7,
            "password": a8,
            "phrase": a6,
            "GroupName/Number": a3,
            "GroupKey" : a9,
            "room#" : a10,
            "serverIp": a4,
            "CurrentIP": "Not Currently Available"
        }
        with open(a2 + "UserData.json", "w") as outfile:
            json.dump(dictionary, outfile, indent=2)
    jsonwrite()
start1()