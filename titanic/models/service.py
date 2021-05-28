from titanic.models.dataset import Dataset
import pandas as pd


class Service(object):

    dataset = Dataset()

    #dataset을 불러와 읽는 메소드
    def new_model(self, payload):  #외부에서 들어오는 값을 payload
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)





