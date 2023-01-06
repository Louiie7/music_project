import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from genre import getGenre

def normalize():
    return "normalized"

def split_year(df):
    years = df["Year"].unique().tolist()
    df_split = {elem : pd.DataFrame() for elem in years}
    for y in df_split.keys():
        df_split[y] = df[:][df.Year == y]
    return df_split

def minute_sum(df):
    sum = df["Minutter"].sum()
    return sum

def mpa_analysis(df, y):
    mpa = minutes_per_artist(df[y])
    mpa.to_csv("mpa_{year}.csv".format(year = y))
    mpa = pd.read_csv("mpa_{year}.csv".format(year = y))
    mpa = pd.read_csv("mpa.csv")

    #Over threshold

    #mpa = mpa[:][mpa.Minutes >= 1000]
    mean = mpa[:]["Minutes"].mean()
    median = mpa[:]["Minutes"].median()

    #number of artists
    total_a = len(mpa)
    #total number of minutes
    total_min = mpa["Minutes"].sum()

    #number of artists whether fever than 10000 minutes
    number_of_a = len(mpa[:][mpa.Minutes <= 10000])

    #artists with under 10000 minutes percentage of total minutes played
    minutes_under = mpa[:][mpa.Minutes <= 10000]["Minutes"].sum()
    minute_percentage = minutes_under/total_min

    #Histogram showing this tendency
    easy_hist(mpa, "Minutes", "Minutes per artist","minutes_artist_{year}".format(year = y))
    easy_plot(mpa, "Main_Artist", "Minutes", "Main_Artist", "Minutes", "minutes_artist_{year}".format(year = y))
    return 1

def minutes_per_artist(df):
    time_start = time.time()
    artists = df["Main_Artist"].unique().tolist()
    rows_list = []
    dict_split = {elem : pd.DataFrame() for elem in artists}
    for a in dict_split.keys():
        row = {"Main_Artist" : a, "Minutes" : (df[:][df.Main_Artist == a])["Minutter"].sum()}
        rows_list.append(row)
    split_artist = pd.DataFrame(rows_list, columns = ["Main_Artist", "Minutes"])
    time_diff = time.time()-time_start
    print("Time lapsed: {time}".format(time = time_diff))

    return split_artist

def easy_plot(df, x, y, x_label, y_label, name):
    fig, ax = plt.subplots()
    ax.bar(df[x], df[y], width=1, edgecolor="white", linewidth=0.7)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    plt.savefig("plots/{name}.png".format(name = name))

def easy_hist(df, x, xlabel, name):
    plt.hist(df[x], density=True, bins=10) 
    plt.xlabel(xlabel)
    plt.ylabel("count")
    plt.show()
    plt.savefig("plots/{name}.png".format(name = name))


def labels(df):
    file = pd.DataFrame(df["Label"].unique().tolist())
    file.to_excel("labels.xlsx")

def analyze(df, split_year = True):
    #He wants the sum of minutes each year, some nice plots (musicians vs time played), how much time is used up by dr per year. Producent country
    if split_year:
        print("Splitting data...")
        year_split = split_year(df)
        print("Succesfully split data...")
        for y in year_split.keys():
            print("Analyzing data for year {year} ...".format(year = y))
    else:
        print("getting genres")
        df_main = getGenre(df)
        print("Succesfully got genres")
        return df_main