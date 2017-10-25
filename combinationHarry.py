# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:00:11 2017

@author: cmorris
"""
import pandas as pd
import json
import numpy as np

data = []

with open("C:\Users\cmorris\Downloads\Grenfell_DailyMail_comments.json") as f:
    data = json.loads(f.readline())
    
data=pd.DataFrame(data)

data['id'] = data['from'].apply(lambda x : x['id'])
data['name'] = data['from'].apply(lambda x : x['name'])

#df.loc('id') = data["id"]
#df.loc('name') = data["name"]

data = data.drop('from', 1)
data = data.drop('parent_id', 1)
data = data.drop('id', 1)
data = data.drop('likes', 1)


data_BBC = []

with open("C:\Users\cmorris\Downloads\Grenfell_BBC_comments.json") as g:
    data_BBC = json.loads(g.readline())
    
data_BBC=pd.DataFrame(data_BBC)

data_BBC['id'] = data_BBC['from'].apply(lambda x : x['id'])
data_BBC['name'] = data_BBC['from'].apply(lambda x : x['name'])

#df.loc('id') = data_BBC["id"]
#df.loc('name') = data_BBC["name"]

data_BBC = data_BBC.drop('from', 1)
data_BBC = data_BBC.drop('parent_id', 1)
data_BBC = data_BBC.drop('id', 1)
data_BBC = data_BBC.drop('likes', 1)
data_BBC = data_BBC.drop('i', 1)


data_guardian = []

with open("C:\Users\cmorris\Downloads\Grenfell_Guardian_comments.json") as h:
    data_guardian = json.loads(h.readline())
    
data_guardian=pd.DataFrame(data_guardian)

data_guardian['id'] = data_guardian['from'].apply(lambda x : x['id'])
data_guardian['name'] = data_guardian['from'].apply(lambda x : x['name'])

#df.loc('id') = data_guardian["id"]
#df.loc('name') = data_guardian["name"]

data_guardian = data_guardian.drop('from', 1)
data_guardian = data_guardian.drop('parent_id', 1)
data_guardian = data_guardian.drop('id', 1)
data_guardian = data_guardian.drop('likes', 1)


data_huff = []

with open("C:\Users\cmorris\Downloads\Grenfell_HuffingtonPost_comments.json") as h:
    data_huff = json.loads(h.readline())
    
data_huff=pd.DataFrame(data_huff)

data_huff['id'] = data_huff['from'].apply(lambda x : x['id'])
data_huff['name'] = data_huff['from'].apply(lambda x : x['name'])

#df.loc('id') = data_huff["id"]
#df.loc('name') = data_huff["name"]

data_huff = data_huff.drop('from', 1)
data_huff = data_huff.drop('parent_id', 1)
data_huff = data_huff.drop('id', 1)
data_huff = data_huff.drop('likes', 1)


data_indy = []

with open("C:\Users\cmorris\Downloads\Grenfell_Independent_comments.json") as f:
    data_indy = json.loads(f.readline())
    
data_indy=pd.DataFrame(data_indy)

data_indy['id'] = data_indy['from'].apply(lambda x : x['id'])
data_indy['name'] = data_indy['from'].apply(lambda x : x['name'])

#df.loc('id') = data_indy["id"]
#df.loc('name') = data_indy["name"]

data_indy = data_indy.drop('from', 1)
data_indy = data_indy.drop('parent_id', 1)
data_indy = data_indy.drop('id', 1)
data_indy = data_indy.drop('likes', 1)


data_standard = []

with open("C:\Users\cmorris\Downloads\Grenfell_Standard_comments.json") as h:
    data_standard = json.loads(h.readline())
    
data_standard=pd.DataFrame(data_standard)

data_standard['id'] = data_standard['from'].apply(lambda x : x['id'])
data_standard['name'] = data_standard['from'].apply(lambda x : x['name'])

#df.loc('id') = data_standard["id"]
#df.loc('name') = data_standard["name"]

data_standard = data_standard.drop('from', 1)
data_standard = data_standard.drop('parent_id', 1)
data_standard = data_standard.drop('id', 1)
data_standard = data_standard.drop('likes', 1)


data_sun = []

with open("C:\Users\cmorris\Downloads\Grenfell_TheSun_comments.json") as h:
    data_sun = json.loads(h.readline())
    
data_sun=pd.DataFrame(data_sun)

data_sun['id'] = data_sun['from'].apply(lambda x : x['id'])
data_sun['name'] = data_sun['from'].apply(lambda x : x['name'])
data_sun['ratio']=data_sun['like_count'].apply(data_sun['ratio'] / data_sun['comment_count'] : ['ratio'])

#df.loc('id') = data_sun["id"]
#df.loc('name') = data_sun["name"]

data_sun = data_sun.drop('from', 1)
data_sun = data_sun.drop('parent_id', 1)
data_sun = data_sun.drop('id', 1)
data_sun = data_sun.drop('likes', 1)


data_tely = []

with open("C:\Users\cmorris\Downloads\Grenfell_Telegraph_comments.json") as h:
    data_tely = json.loads(h.readline())
    
data_tely=pd.DataFrame(data_tely)

data_tely['id'] = data_tely['from'].apply(lambda x : x['id'])
data_tely['name'] = data_tely['from'].apply(lambda x : x['name'])

#df.loc('id') = data_tely["id"]
#df.loc('name') = data_tely["name"]

s = pd.Series(data =[ 0.2, 0.3, 0.5], index = ['a','b','c'])