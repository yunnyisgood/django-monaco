from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test)-> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test)-> object:
        service = self.service
        this = self.dataset

        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']

        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.age_ordinal(this)
        this = service.fare_ordinal(this)

        this = service.drop_feature(this, "Cabin", "Ticket", "Name", "Sex", "Age", "Fare")

        self.print_this(this)

        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(this)
        print(f'Train 의 type \n {type(this.train)} 이다.')
        print(f'Train 의 column \n {this.train.columns} 이다.')
        print(f'Train 의 상위 5개 행\n {type(this.train.head(1))} 이다.')
        print(f'Train 의 null\n {this.train.isnull().sum()}개')
        print(f'Test 의 type \n {type(this.test)} 이다.')
        print(f'Test 의 column \n {this.test.columns} 이다.')
        print(f'Test 의 상위 5개 행\n {type(this.test.head(1))} 이다.')
        print(f'Test 의 null \n {this.test.isnull().sum()}개')
        print('*' * 100)
