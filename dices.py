import random
import plotly.express as px
count = []
dics_result  = []
for i in range (0,100):
    dics1 = random.randint(1,6)
    dics2 = random.randint(1,6)
    dics_result.append(dics1 +  dics2)
    count.append(i)
print(count , dics_result)
fig = px.bar(x = dics_result , y = count)
fig.show()