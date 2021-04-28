import pandas as P 
import plotly.express as px
df=P.read_csv("data.csv")
fig=px.scatter(df,x='Population', y='Per capita', size="Percentage", color="Country", size_max=60)
fig.show()