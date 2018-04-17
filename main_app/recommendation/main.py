from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
import pandas as pd
import pickle
from scipy import sparse
from scipy.spatial.distance import cosine
import seaborn
from sklearn import preprocessing
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans

# ------------------------------------------------------------------------------


class Preprocess():

    def __init__(self):
        print('preprocessing')
        self.df = pd.DataFrame()
        self.dataRead()
        self.dropCloumns()

    def dataRead(self):
        # reading data from dataset
        print('reading data')
        self.df = pd.read_csv('../../combine.csv')
        print('Data read')

    def processing(self):
        df['age'] = df['age'].astype(float)

    def dropCloumns(self):
        print('droping columns')
        self.df = self.df.drop(
            ['phoneNo', 'id', 'availabilityPreference', 'aadharCard'],
            axis=1)
        self.df.dropna(inplace=True)


class Helper(Preprocess):

    def __init__(self):
        print('Initializing Helper functions')
        self.classesOfColumns = defaultdict(list)
        self.occupations = defaultdict(list)
        super().__init__()
        self.classMaker()
        self.all_occupations_in_a_location()
        self.occs_splitter()

    def classMaker(self):
        temp = self.df.columns.tolist()
        temp.remove('age')
        # print(type(temp))
        for i in temp:
            le = preprocessing.LabelEncoder()
            le.fit(self.df[i])
            self.classesOfColumns[i].append(le.classes_)
            self.df[i] = le.transform(self.df[i])
        print('Classes created')

    def all_occupations_in_a_location(self):
        print('Generating data')
        for index, row in self.df.iterrows():
            self.occupations[row['occupation']].append(index)

            for key, values in self.occupations.items():
                t_set = list(set(values))
                self.occupations[key] = t_set

    def occs_splitter(self):
        # key: occupation lst: list of worker having occupation
        # (index, location)
        print('Splitting data')
        for key in self.occupations.keys():
            temp_df = self.df.iloc[self.occupations[key]]
            temp_df.to_csv(str(key)+'.csv')


class KMeansClustering():

    def __init__(self):
        self.kmeans = []
        self.temp_files = []
        self.KmeansForEveryOccupation()
        self.KmeansPredictor()

    def KmeansForEveryOccupation(self):
        # read the csv file of the particular job example

        for i in range(24):
            self.temp_files.append(pd.read_csv(str(i)+'.csv'))
            self.kmeans.append(KMeans(max_iter=4, n_clusters=10,
                               n_init=10).fit(pd.read_csv(str(i)+'.csv')))

    def KmeansWorkerGetter(self):
        self.temp_files[0].loc[[0, 6]]

    def KmeansPredictor(self):
        # predict the worker 0 in with occupation 1
        print(
        self.kmeans[1].predict(self.temp_files[1].loc[0].values.reshape(1, -1))
        )


p = Preprocess()
h = Helper()
k = KMeansClustering()
