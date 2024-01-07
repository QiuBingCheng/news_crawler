# -*- coding: utf-8 -*-
import os
import os.path

dir = './'


def listUiFile():
    list = []
    files = os.listdir(dir)
    for filename in files:
        if os.path.splitext(filename)[1] == '.ui':
            list.append(filename)

    return list


def transPyFile(filename):
    return os.path.splitext(filename)[0] + '.py'


def runMain():
    list = listUiFile()
    for uifile in list:
        pyfile = transPyFile(uifile)
        cmd = 'pyuic5 -o {pyfile} {uifile}'.format(
            pyfile=pyfile, uifile=uifile)
        # print(cmd)
        os.system(cmd)


# 程序的主入口
if __name__ == "__main__":
    runMain()
