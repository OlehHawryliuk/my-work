from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: скільки тем в кожній дисципліні.

datas = dict()
data =dict()
for ident in list(dataset.keys()):
    datas[ident]={}
    for clas in dataset[ident]:
        if clas in datas[ident]:
            datas[ident][clas]+=1
            data[clas]+=1
        else:
            datas[ident][clas]=1
            data[clas] = 1
print(data)

diagram = go.Bar(
    x=list(data.keys()),
    y=list(data.values())
)

fig = go.Figure(data=[diagram])

plotly.offline.plot(fig, filename='user_topics.html')
