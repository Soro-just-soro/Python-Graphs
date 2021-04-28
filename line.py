import pandas as P 
import plotly.express as px
df=P.read_csv("line_chart.csv")
fig=px.line(df,x='Year', y='Per capita income', color='Country', title="Per-Capita Income")
fig.show()