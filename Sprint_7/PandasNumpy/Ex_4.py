import pandas as pd

if __name__ == "__main__":

    df = pd.read_csv('actors.csv')
    res = df['#1 Movie'].value_counts().iloc[[0]]
    print(res)