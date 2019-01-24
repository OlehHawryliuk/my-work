from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести кругову діаграму: у якого студента скільки тем
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

diagram = go.Pie(
    labels=(list(dataset.keys())),
    values=list(data.values())
)

fig = go.Figure(data=[diagram])

plotly.offline.plot(fig, filename="topics_pie.html")
