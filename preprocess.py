import pandas as pd
import numpy as np
def combine(df1, df2):
    print("Combining...")
    res = pd.concat([df1, df2], axis=0, join = 'outer')
    print(df1.shape)
    print(df2.shape)
    print(res.shape)
    print("Succesfully combined!")
    return res

def remove_spaces(df):
    print("Removing spaces ...")
    df.columns = [c.replace(' ', '_') for c in df.columns]
    print("Succesfully removed spaces!")
    return df

def drop_year(df, year):
    print("Dropping year from data_frame")
    df = df.loc[df["Year"] != year]
    df.to_csv("df_dropped_{year}".format(year = year))
    return df

def remove(df, column, criteria, condition, type):
    df_new = df
    
    if condition == "remain":
        mask = np.zeros((df_new.shape[0], ))
        for i in criteria:
            print("Keeping data with condition: "+i)
            mask_c = ((df[column] == i).astype(int)) 
            print(np.sum(mask_c))
            mask = mask+mask_c.astype(int)

        rows_bf = df_new.shape[0]
        df_new = df_new.loc[mask == 1]
        rows_af = df_new.shape[0]
        output = "Totally kept {s} rows out of {r} rows".format(s = rows_af, r = rows_bf)
        print(output)
        
    elif condition == "remove":
        mask = np.zeros((df_new.shape[0], ))
        mask = np.full((df_new.shape[0], ), False)
        for i in criteria:
            if type == "contains":
                print("Removing. Condition: "+str(i))
                mask_c = df_new[column].str.contains(str(i), na = False)
                output = "Marked {s} rows for removal".format(s= np.sum(mask_c.astype(int)))
                print(output)
                mask = (mask | mask_c)
            elif type == "is":
                print("Removing. Condition: "+str(i))
                mask_c = (df[column] == i)
                output = "Marked {s} rows for removal".format(s= np.sum(mask_c.astype(int)))
                print(output)
                mask = (mask | mask_c)
                
        rows_bf = df_new.shape[0]
        df_new = df_new.loc[np.invert(mask)]
        rows_af = df_new.shape[0]
        rows_rm = rows_bf-rows_af
        output = "Succesfully removed {s} rows".format(s = rows_rm)
        print(output)
        

    return df_new

def splitExcel(df, split, column):
    if df.shape[0] >= 1040000:
        df_list = []
        for i in split:
            df_split = df.loc[(df[column] >= i[0]) & (df[column] <= i[1])]
            name = "data/{split_1}_{split_2}.csv".format(split_1 = i[0], split_2 = i[1])
            df_split.to_csv(name)
        print("Was too large: DID SPLIT")
    else:
        print("Didn't split")
        
        

        

def preprocess(df_list):
    df_main = pd.DataFrame([])
    for df in df_list:
        print("Shape before combining: " +str(df_main.shape))
        df_main = combine(df_main, df)
        print("Shape after combining: " +str(df_main.shape))
    
    
    df_main = drop_year(df_main, 2011)
    df_main = remove_spaces(df_main)

    print(df_main.shape)

    df_main = remove(df_main, "Label", ["DR", "DR Multimedie", "DR Salg", "Dr jingle", "Dr Drex", "Dr P2 Musik", "DR Ultra", "Dr P3", "DR P3 Live", "Danmarks Radio", "DR Børne 1'eren", "DR Red Dot Music", "DR UM", "Dr xclusive records", "DR-Arkiv", "DR2 Records", "Dr P2", "Upright", "Upright Music", "UPRIGHT", "upright", "Upright music forlag", "Upright Music ApS"], "remove", "is")
    print(df_main.shape)

    df_main = remove(df_main, "Station", ["P3", "P4", "P5D", "P6B", "P7M", "P8J", "DR1", "DR2", "DR3"], "remain", "is")

    print(df_main.shape)

    df_main = remove(df_main, "Phonogram_Title", ["upright", "Upright"], "remove", "contains")

    print(df_main.shape)

    df_main = remove(df_main, "Media_Code", [2, 5, 7, 9], "remove", "is")

    print(df_main.shape)


    print("Splitting in years if data is top large")
    splitExcel(df_main, [[2012, 2016], [2017,2021]], "Year")
    print("Finished preprocessing")

    return df_main