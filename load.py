import pandas as pd


def load_xlsx(filename):
    print("Loading data...")
    df = pd.read_excel(filename)
    out = "Succesfully loaded data of size: {s}".format(s=str(df.shape))
    print(out)


    print("Writing to csv instead of xlsx for future purposes")
    f_info = filename.split(".")
    name = f_info[0]
    fmt = f_info[1]
    df.to_csv("{name}.csv".format(name = name))
    print("Succesfully written to file")

    return df

def load_csv(filename):
    print("Loading data...")
    df = pd.read_csv(filename)
    out = "Succesfully loaded data of size: {s}".format(s=str(df.shape))
    print(out)
    return df