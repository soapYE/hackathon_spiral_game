import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import json

df_blink = pd.read_csv(r'.\eeg_boiler_blink_blink.csv')
df_close_open = pd.read_csv(r'.\eeg_boiler_close_open.csv')
df_blink.columns = ['c1','c2','c3','c4']
df_close_open.columns = ['c1','c2','c3','c4']

#function to get the data from bci
#bst = blink start threshold
#ws = window size
#lws = threshold left window size
#is_up = bigger than threshold or not
def getBlinkList(df,bst,ws,lws,is_up):

    blink_list = []

    c1_list = []
    t_list=[]

    #blink start threshold


    #window size
    ws = 0.8

    #threshold left window size
    lws = 0.2

    #prepare data in list
    for i in range(len(df)-1):
        c1_list.append(df.loc[i,'c1'])
        t_list.append(i*(1/256))

    #prepare blink data from list
    i = 0
    while i<len(c1_list):
        #if out of window size
        if int(i+(0.4*256))>len(c1_list): break
        
        if is_up:
            if c1_list[i]>=bst:
                start = i - lws*256
                end = i + ws*256 - lws*256
                sample = []
                for j in range(int(start),int(end)):
                    sample.append(c1_list[j])
                blink_list.append(sample)
                i = int(end+1)
            else:
                i+=1
        else:
            if c1_list[i]<=bst:
                start = i - lws*256
                end = i + ws*256 - lws*256
                sample = []
                for j in range(int(start),int(end)):
                    sample.append(c1_list[j])
                blink_list.append(sample)
                i = int(end+1)
            else:
                i+=1

    return blink_list

blink_result = getBlinkList(df_blink,-200,0.8,0.2,False)
open_result = getBlinkList(df_close_open,150,0.8,0.2,True)
close_result = getBlinkList(df_close_open,-200,0.8,0.2,False)
print(len(blink_result))
print(len(open_result))
print(len(close_result))

json_r = {"blink":blink_result,"open":open_result,"close":close_result}

# the json file where the output must be stored
out_file = open("blink.json", "w")

json.dump(json_r,out_file)


