# Importing Modules
import csv
import plotly.express as px
import numpy as np
import pandas as pd

# Plotting Data 1 On Scatter Chart
with open("data1.csv", newline="") as a:
  df = pd.read_csv(a)
  df.sort_values([df.columns[0], df.columns[1]],
                     axis=0,
                     ascending=[True, True], 
                     inplace=True)

  print("Plotting On Web..")
  fig = px.scatter(df, x="Temperature", y="Ice-Cream Sales", title="Correlation Between Temperature And Sales Of Ice-Cream")
  fig.show()

# Finding Correlation Of Data 1
def getDataSource(data_path):
    temprature = []
    sales_of_iceCream = []

    with open(data_path) as b:
        df1 = csv.DictReader(b)
        for row in df1:
            temprature.append(float(row["Temperature"]))
            sales_of_iceCream.append(float(row["Ice-Cream Sales"]))

    return {"x" : temprature, "y": sales_of_iceCream}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Temperature And Sales Of Ice Cream:-  \n--->", correlation[0,1])
    print()

data_path  = "data1.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)

# Plotting Data 2 Of Scatter Chart
with open("data2.csv", newline="") as c:
  ds = pd.read_csv(c)
  ds.sort_values([ds.columns[0], ds.columns[1]],
                     axis=0,
                     ascending=[True, True], 
                     inplace=True)

  print("Plotting On Web..")
  fig = px.scatter(ds, x="Size Of TV", y=" Average Time Spent Watching TV In A Week (in hours)", title="Correlation Between Size Of TV And Average Time Spent Watching TV")
  fig.show()

# Finding Correlation On Data 2
def getDataSource(data_path):
    size_of_tv = []
    Average_time_spent = []

    with open(data_path) as d:
        ds1 = csv.DictReader(d)
        for row in ds1:
            size_of_tv.append(float(row["Size Of TV"]))
            Average_time_spent.append(float(row[" Average Time Spent Watching TV In A Week (in hours)"]))

    return {"x" : size_of_tv, "y": Average_time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of TV and Average time spent watching TV in a week:-  \n--->", correlation[0,1])
    print()

data_path  = "data2.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)

# Plotting Data 3 On Scatter Chart
with open("data3.csv", newline="") as e:
  reader = pd.read_csv(e)
  reader.sort_values([reader.columns[1], reader.columns[2]],
                     axis=0,
                     ascending=[True, True], 
                     inplace=True)

  print("Plotting On Web..")
  fig = px.scatter(reader, x="Marks In Percentage", y="Days Present", title="Correlation Between Marks And Days Present")
  fig.show()

# Finding Correlation Of Data 3
def getDataSource(data_path):
    marks = []
    days_present = []

    with open(data_path) as f:
        reader1 = csv.DictReader(f)

        for row in reader1:
            marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : marks, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks and Days Present :-  \n--->", correlation[0,1])
    print()

data_path  = "data3.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)

# Plotting Data 4 On Scatter Chart
with open("data4.csv", newline="") as g:
  csv_reader = pd.read_csv(g)
  csv_reader.sort_values([csv_reader.columns[1], csv_reader.columns[2]],
                     axis=0,
                     ascending=[True, True], 
                     inplace=True)

  print("Plotting On Web..")
  fig = px.scatter(csv_reader, x="Coffee (in ml)", y="Sleep (in hours)", title="Correlation Between Coffee And Sleep")
  fig.show()

# Finding Correlation Of Data 4
def getDataSource(data_path):
    coffee = []
    sleep = []

    with open(data_path) as h:
        csv_reader1 = csv.DictReader(h)

        for row in csv_reader1:
            coffee.append(float(row["Coffee (in ml)"]))
            sleep.append(float(row["Sleep (in hours)"]))

    return {"x" : coffee, "y": sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee and Sleep :-  \n--->", correlation[0,1])

data_path  = "data4.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)
