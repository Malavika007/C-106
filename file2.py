import plotly.express as px
import pandas as pd
import csv
import numpy as np

with open('Size of TV,_Average time spent watching TV in a week (hours).csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

df = pd.read_csv('Size of TV,_Average time spent watching TV in a week (hours).csv')
fig = px.scatter(df, x = 'Size of TV', y = 'Average time spent watching TV in a week (hours)')
fig.show()