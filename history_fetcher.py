# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:17:08 2021

@author: Raza_Jutt
"""
import concurrent.futures
import numpy as np
import time
import csv
#import pandas as pd
#import os
from blockchain import blockexplorer


def funtion(i):
    a=1
    print(i)
    while a:
        try :
            block = blockexplorer.get_block(str(i-1))
            pre_block = str(block.hash)
            block = blockexplorer.get_block(str(i))
            return block,i,pre_block
        except:
            print("Stuck >>>>>>>  waiting")
            time.sleep(2)
        



with concurrent.futures.ThreadPoolExecutor() as executor:
    num = list(range(219514,400001))
    results = executor.map(funtion,num)
    
    with open('3.csv', 'a') as g:
        writer = csv.writer(g)
        for block,i,pre_block in results:
            writer.writerow([i, block.hash, "link" , pre_block ,block.nonce])
            f = open("C:/Users/Raza Jutt/Desktop/transcations/"+str(i)+".txt","w")
            f.write(str(block.transactions))
            f.close()
            
#data = pd.read_csv('BitCoin_Chain.csv')
#data.dropna()
#data.to_csv("Bitcoin_Blockchain.csv",header=["Height", "Hash", "Transcations","Previous_Hash","Nonce"], index=False)
#os.remove('BitCoin_Chain.csv')
# 679487 
