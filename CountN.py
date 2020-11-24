'''
Created on 16/04/2018

@author: brunamendes
'''
import argparse

def CountN(file):
    fh=open(file)
    dic={}
    while True:
        fh.readline()
        seq=fh.readline()
        fh.readline()
        fh.readline()
        if len(seq) == 0:
            break
        num=seq.count('N')
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    fh.close()
    for i in dic:
        
        print("There are %s  reads with %s N" % (dic[i], i) )
    

parse = argparse.ArgumentParser(prog="CountN")
parse.add_argument('-f', '--CountN')
args = parse.parse_args()
# print argument of -s
print('argument: ',args.CountN)

CountN(args.CountN)