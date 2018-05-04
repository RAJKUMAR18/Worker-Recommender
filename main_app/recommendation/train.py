import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn import preprocessing
from scipy import sparse
from operator import itemgetter
from scipy.spatial.distance import cosine
import pickle
import seaborn
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans


def classes_maker(df):
    temp = df.columns.tolist()
    # temp.remove('age')

    for i in df.columns:
        le = preprocessing.LabelEncoder()
        le.fit(df[i])
        classesOfColumns[i].append(le.classes_)
        df[i] = le.transform(df[i])
    return df


def all_occupations_in_a_location(df):
    # location: index and occupation where index is the position of row in
    # Dataframe
    # key: occupation lst: list of worker having occupation (index, location)
    for index, row in df.iterrows():
        occupations[row['occupation']].append(index)

    for key, values in occupations.items():
        t_set = list(set(values))
        occupations[key] = t_set


def occs_splitter(df):

    for key in occupations.keys():
        temp_df = df.iloc[occupations[key]]
        temp_df.to_csv(str(key)+'.csv')


def pickler(model, i):
    print(f'pickling {i}')
    with open('models/model_'+str(i)+'.pk', 'wb') as file:
        pickle.dump(model, file)


def Kmeanmodelling():
    kmeans = []
# read the csv file of the particular job example
    temp_files = []
    for i in range(24):
        temp_files.append(pd.read_csv(str(i)+'.csv'))
        kmodel = KMeans(max_iter=4,
                        n_clusters=10, n_init=10).fit(temp_files[i])
        kmeans.append(kmodel)
        pickler(kmodel, i)


def build_and_train():
    df = pd.read_csv('../../combine.csv')
    df = df.drop(['phoneNo', 'id', 'availabilityPreference', 'aadharCard'],
                 axis=1)
    df.dropna(inplace=True)
    df = classes_maker(df)
    all_occupations_in_a_location(df)
    occs_splitter(df)
    Kmeanmodelling()
    print('Built and Trained')
    # print(occupations)
    # print(classesOfColumns)


if __name__ == '__main__':
    classesOfColumns = defaultdict(list)
    occupations = defaultdict(list)
    build_and_train()
