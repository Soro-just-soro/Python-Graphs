import pandas as P 
import plotly.express as px
df=P.read_csv("data.csv")
fig=px.bar(df,x='Country', y='InternetUsers')
fig.show()