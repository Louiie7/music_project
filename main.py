from os import pread
from load import load_xlsx, load_csv
from preprocess import preprocess
from analysis import analyze



def main():
    preprocessed = True
    if not preprocessed:
        df_list = []
        #Uncomment if you want to load xlsx files
        #df1 = load_xlsx("data/17_21.xlsx")
        #df2 = load_xlsx("data/11_16.xlsx")
        df2 = load_csv("data/2017_2021.csv")
        print("Size of data is " + str(df2.shape[0]))
        df1 = load_csv("data/2011_2016.csv")
        print("Size of datafile is " + str(df1.shape[0]))

        df_list.append(df1)
        df_list.append(df2)

        df = preprocess(df_list)
        df.to_excel
        #print("Writing to cleaned xlsx")
        #df.to_excel("data/data_cleaned_excel.xlsx")

        print("Writing to cleaned csv")
        df.to_csv("data/data_cleaned.csv")
        print("Succesfully written")

        #Uncomment if want to do analysis
        #analyze(df, False)
    else:
        df = load_csv("data/data_cleaned.csv")
        df_final = analyze(df, False)
        print("Writing to file")
        df_final.to_csv("data/data_with_genres.csv")
        print("Succesfully wrote to file")
    return 1

if __name__ == "__main__":
    main()


