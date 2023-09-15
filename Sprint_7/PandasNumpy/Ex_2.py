import pandas as pd

if __name__ == "__main__":

    df = pd.read_csv('actors.csv')
    print(df.head())
    res = df['Number of Movies'].mean()
    print(res)