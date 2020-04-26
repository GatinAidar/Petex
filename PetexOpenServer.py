# Python script to execute Petroleum Experts OpenServer commands.
# Written by Thorjan Knudsvik, January 2018
from typing import TextIO

import win32com.client

Server = win32com.client.Dispatch("PX32.OpenServer.1")


def DoSet(Sv, Val):
    Err = Server.SetValue(Sv, Val)
    AppName = GetAppName(Sv)
    Err = Server.GetLastError(AppName)
    if Err > 0:
        print(Server.GetErrorDescription(Err))


def DoCmd(Cmd):
    Err = Server.DoCommand(Cmd)
    if Err > 0:
        print(Server.GetErrorDescription(Err))


def DoGet(Gv):
    DoGet = Server.GetValue(Gv)
    AppName = GetAppName(Gv)
    Err = Server.GetLastError(AppName)
    if Err > 0:
        print(Server.GetLastErrorMessage(AppName))
    return str(DoGet)


def GetAppName(Strval):
    AppName = Strval.split('.')[0]
    if AppName not in ['PROSPER', 'MBAL', 'GAP', 'PVT', 'RESOLVE']:
        print('Unrecognised application name in tag string')
    return AppName


from PetexOpenServer import *

# DoCmd('GAP.START()')
# DoCmd('PROSPER.OPENFILE("C:\C-2.OUT")')
# DoSet('PROSPER.SIN.SUM.Comments', 'Testing OpenServer from Python')

# FOut: TextIO = open("C://prosper/test2.txt", 'w')
# i = 0
#
# while i <= 597:
#     a = str((DoGet('GAP.MOD[{PROD}].WELL['+str(i)+'].Label')))
#     FOut.write(a + '\n')
#     i = i+1
# # # FOut.write(123)
# FOut.close()

FIn: TextIO = open("C://prosper/test3.txt", 'r')

line = FIn.readline()

i = 0
while line:
    print(line)
    DoSet('GAP.MOD[{PROD}].WELL['+str(i)+'].Label', line)
    DoSet('GAP.MOD[{PROD}].WELL['+str(i)+'].File', 'C://prosper/Ak/' + line + '.Out')
    line = FIn.readline()
    i = i + 1
FIn.close()