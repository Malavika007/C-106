import plotly.express as px
import pandas as pd
import csv
import numpy as np


with open('cups of coffee vs hours of sleep.csv', newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

df = pd.read_csv('cups of coffee vs hours of sleep.csv')
fig = px.scatter(df, x = 'Coffee in ml', y = 'sleep in hours')
fig.show()
