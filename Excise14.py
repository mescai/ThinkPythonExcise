#coding=utf-8
import os

def walk(dirname):
    """
    print all paths of file in directionary dirname
    :param dirname:
    :return:
    """
    for name in os.listdir(dirname):
        path=os.path.join(dirname,name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)
def sed(pattern,replace,readfilename,writefilename):
    try:
        fin=open(readfilename,"r")
        fout=open(writefilename,"w")
        for line in fin:
            line=line.replace(pattern,replace)
            fout.write(line)

        fout.close()
        fin.close()
    except:
        print "Something went wrong"

def replace(name):
    pattern="ab"
    replace="cd"
    readfilename=name
    writefilename="output.txt"
    sed(pattern,replace,readfilename,writefilename)


def find_mp3(dirname):
    """
    print all paths of file in directionary dirname
    :param dirname:
    :return:
    """
    res=[]
    for name in os.listdir(dirname):
        path=os.path.join(dirname,name)
        if os.path.isfile(path):
            if os.path.splitext(path)[1]==".mp3":
                res.append(path)
        else:
            find_mp3(path)
    return res
import sys
import anydbm
import pickle
import wc

import urllib


