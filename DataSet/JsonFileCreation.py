# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 03:06:10 2020

@author: DELL
"""
import json

with open('./DataSet/cleanmaster/data.json') as json_file:
    cleanmaster = json.load(json_file)
    cleanmaster['document_id'] = 1
with open('./DataSet/epic/data.json') as json_file:
    epic = json.load(json_file)
    epic['document_id'] = 2
with open('./DataSet/evie/data.json') as json_file:
    evie = json.load(json_file)
    evie['document_id'] = 3
with open('./DataSet/goodreads/data.json') as json_file:
    goodreads = json.load(json_file)
    goodreads['document_id'] = 4
with open('./DataSet/habitbull/data.json') as json_file:
    habitbull = json.load(json_file)
    habitbull['document_id'] = 5
with open('./DataSet/herocraft/data.json') as json_file:
    herocraft = json.load(json_file)
    herocraft['document_id'] = 6
with open('./DataSet/imdb/data.json') as json_file:
    imdb = json.load(json_file)
    imdb['document_id'] = 7
with open('./DataSet/khanacademy/data.json') as json_file:
    khanacademy = json.load(json_file)
    khanacademy['document_id'] = 8
with open('./DataSet/pepperplate/data.json') as json_file:
    pepperplate = json.load(json_file)
    pepperplate['document_id'] = 9
with open('./DataSet/quickbooks/data.json') as json_file:
    quickbooks = json.load(json_file)
    quickbooks['document_id'] = 10
with open('./DataSet/reddit/data.json') as json_file:
    reddit = json.load(json_file)
    reddit['document_id'] = 11
with open('./DataSet/relaxio/data.json') as json_file:
    relaxio = json.load(json_file)
    relaxio['document_id'] = 12
with open('./DataSet/shutterfly/data.json') as json_file:
    shutterfly = json.load(json_file)
    shutterfly['document_id'] = 13
with open('./DataSet/smartinputv5/data.json') as json_file:
    smartinputv5 = json.load(json_file)
    smartinputv5['document_id'] = 14
with open('./DataSet/starbucks/data.json') as json_file:
    starbucks = json.load(json_file)
    starbucks['document_id'] = 15
with open('./DataSet/touchnote/data.json') as json_file:
    touchnote = json.load(json_file)
    touchnote['document_id'] = 16
with open('./DataSet/tripadvisor/data.json') as json_file:
    tripadvisor = json.load(json_file)
    tripadvisor['document_id'] = 17
with open('./DataSet/usps/data.json') as json_file:
    usps = json.load(json_file)
    usps['document_id'] = 18
with open('./DataSet/washingtonpost/data.json') as json_file:
    washingtonpost = json.load(json_file)
    washingtonpost['document_id'] = 19
with open('./DataSet/wordwebsoftware/data.json') as json_file:
    wordwebsoftware = json.load(json_file)
    wordwebsoftware['document_id'] = 20
with open('./DataSet/brilliant/data.json') as json_file:
    brilliant = json.load(json_file)
    brilliant['document_id'] = 21
with open('./DataSet/cakebrowser/data.json') as json_file:
    cakebrowser = json.load(json_file)
    cakebrowser['document_id'] = 22


para = dict()
Data = dict()

#brilliant
brilliantp = dict()
brilliantp['paragraphs'] = [brilliant]
#cakebrowser
cakebrowserp = dict()
cakebrowserp['paragraphs'] = [cakebrowser]
#cleanmaster
cleanmasterp = dict()
cleanmasterp['paragraphs'] = [cleanmaster]
#epic
epicp = dict()
epicp['paragraphs'] = [epic]
#evie
eviep = dict()
eviep['paragraphs'] = [evie]
#goodreads
goodreadsp = dict()
goodreadsp['paragraphs'] = [goodreads]
#habitbull
habitbullp = dict()
habitbullp['paragraphs'] = [habitbull]
#herocraft
herocraftp = dict()
herocraftp['paragraphs'] = [herocraft]
#imdb
imdbp = dict()
imdbp['paragraphs'] = [imdb]
#khanacademy
khanacademyp = dict()
khanacademyp['paragraphs'] = [khanacademy]
#pepperplate
pepperplatep = dict()
pepperplatep['paragraphs'] = [pepperplate]
#quickbooks
quickbooksp = dict()
quickbooksp['paragraphs'] = [quickbooks]
#reddit
redditp = dict()
redditp['paragraphs'] = [reddit]
#relaxio
relaxiop = dict()
relaxiop['paragraphs'] = [relaxio]
#shutterfly
shutterflyp = dict()
shutterflyp['paragraphs'] = [shutterfly]
#smartinputv5
smartinputv5p = dict()
smartinputv5p['paragraphs'] = [smartinputv5]
#starbucks
starbucksp = dict()
starbucksp['paragraphs'] = [starbucks]
#touchnote
touchnotep = dict()
touchnotep['paragraphs'] = [touchnote]
#tripadvisor
tripadvisorp = dict()
tripadvisorp['paragraphs'] = [tripadvisor]
#usps
uspsp = dict()
uspsp['paragraphs'] = [usps]
#washingtonpost
washingtonpostp = dict()
washingtonpostp['paragraphs'] = [washingtonpost]
#wordwebsoftware
wordwebsoftwarep = dict()
wordwebsoftwarep['paragraphs'] = [wordwebsoftware]








Data['data'] = [brilliantp,cakebrowserp,cleanmasterp,epicp,eviep,goodreadsp,habitbullp,herocraftp,imdbp,khanacademyp,pepperplatep,quickbooksp,redditp,relaxiop,shutterflyp,smartinputv5p,starbucksp,touchnotep,tripadvisorp,uspsp,washingtonpostp,wordwebsoftwarep]



with open('./DataSet/JsonAllFinal.json', 'w') as outfile:
    json.dump(Data, outfile)
