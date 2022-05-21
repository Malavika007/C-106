import plotly.express as px
import pandas as pd
import csv
import numpy as np

with open('Student Marks vs Days Present.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

df = pd.read_csv('Student Marks vs Days Present.csv')
fig = px.scatter(df, x = 'Marks In Percentage', y = 'Days Present')
fig.show()