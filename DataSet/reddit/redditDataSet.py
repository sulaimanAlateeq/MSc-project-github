# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 04:47:19 2020

@author: DELL
"""
#https://github.com/AbhilashaRavichander/PrivacyQA_EMNLP
#Only Relevent answers will be used.
import pandas as pd
import numpy as np
import json
import re

#filename = 'policy_train_data1.csv'
#df = pd.read_csv(filename, sep='delimiter', header=None)
#df= df[df[0].str.contains("Relevant")]
#converts dataframe to json object (SQuAD Format)
#df1 = df[df[0].str.contains("	 ")]
#df3 = df[0].str.split("	", expand=True)
#specficWebsite = df[df[0].str.contains("../../Dataset/Train/com.reddit.frontpage")]
#specificWebsite1 = specficWebsite[0].str.split("	", expand=True)

specificWebsite1 = pd.read_csv('./DataSet/reddit/Modifiedreddit.csv')
specificWebsite1 = specificWebsite1.drop('11',1)

qas = []
r=1
for index, row in specificWebsite1.iterrows():    
    dicn = dict()
    answers = dict()
    dicn['question']=row[5]
    dicn['id']= int(str(220000) + str(r))
    r = r+1
    answers['text'] = row[6]
    aa , answers['answer_start']= find_index(row[6])
    dicn['answers'] = [answers]
    qas.append(dicn)
    dicn['is_impossible'] = False


# Saving SpecificWebsite1 after manual modification for 3 rows (To match the text)
#specificWebsite1.to_csv('./DataSet/reddit/Modifiedreddit.csv')
qasdict = dict()
qasdict['qas'] = qas
qasdict['context'] = aa
qasdict['document_id'] = 1


with open('./DataSet/reddit/data.json', 'w') as f:
    json.dump(qasdict, f)




def find_index(text1):
    with open('./DataSet/reddit/redditPrivacyPage.txt', 'r',encoding="utf8") as f:
        content = f.read()
        replaced_string = content.replace('“', "")
        replaced_string = replaced_string.replace('”', "")
        replaced_string = replaced_string.replace('\n', " ")
    return replaced_string,replaced_string.index(text1)

def select_rows(df,search_strings):
    for index, row in df.iterrows():
        print (type(row))
        
    
