import pandas as pd

if __name__ == "__main__":

    df = pd.read_csv('actors.csv')
    res = df.loc[df['Number of Movies'].idxmax()]
    print(res)