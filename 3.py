'''3. Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
Sample Python dictionary data and list labels:
exam_data = {'name':['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
'attempts':[1,3,2,3,2,3,1,1,2,1],
'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes'],
'labels':['a','b','c','d','e','f','g','h','i','j']}'''

import pandas as pd
exam_data = pd.DataFrame({'name':['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
'score':[12.5,9,16.5,None,9,20,14.5,None,8,19],
'attempts':[1,3,2,3,2,3,1,1,2,1],
'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']},
index=['a','b','c','d','e','f','g','h','i','j'])
print(exam_data.info())