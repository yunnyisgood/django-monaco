import numpy as np

from dataset import Dataset
import pandas as pd

class Services(object):

    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context+this.fname+'.csv')

    @staticmethod
    def create_train(this):
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this):
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature):
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)

    @staticmethod
    def embarked_nominal(this):
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        this.train = this.train.map({'S':1, 'C':2, 'Q':3})
        this.test = this.test.map({'S':1, 'C':2, 'Q':3})
        return this

    @staticmethod
    def title_nominal(this):
        combine = [this.train, this.test]
        for i in combine:
            i['Title'] = i.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for i in combine:
            i['Title'] = i['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'],
                                                      'Rare')
            i['Title'] = i['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            i['Title'] = i['Title'].replace('Mlle', 'Mr')
            i['Title'] = i['Title'].replace('Ms', 'Miss')
            i['Title'] = i['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            i['Title'] = i['Title'].fillna(0)
            i['Title'] = i['Title'].map(title_mapping)


    @staticmethod
    def gender_nominal(this):
        combine = [this.test, this.train]
        gender_mapping = {'male':0, 'female':1}
        for i in combine:
            i['Gender'] = i['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ordinal(this):
        train = this.train
        test = this.test
        for i in train, test:
            i['Age'] = i['Age'].fillna(0)
        bins = [-1, 0, 5, 12, 18, 24, 35, 68, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                             'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for i in train, test:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_title_mapping)
        return this

    @staticmethod
    def fare_ordinal(this):
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)

        bins = [-1, 8, 15, 31, np.inf]
        this.train = this.train.drop(['FareBand'], axis=1)
        for i in this.train, this.test:
            i['FareBand'] = pd.cut(i['Fare'], bins=bins, labels=[1, 2, 3, 4])

