from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    # def modeling(self, train, test) -> object:
    #     service = self.service

    def preprocess(self, train) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        print(f'Train의 type은 {type(this.train)}')
        print(f'Train의 column은 {this.train.columns}')
        print(f'Train의 상위 5개 데이터는 {this.train.head()}')
        print(f'Train의 하위 5개 데이터는 {this.train.tail()}')



