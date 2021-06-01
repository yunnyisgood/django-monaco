from titanic.models.dataset import Dataset
from titanic.models.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


class Plot(object):
    # 시각화를 하기 위해 Template에 모델의 객체를 생성
    dataset: object = Dataset()
    service: object = Service()

    def __init__(self, fname):
        self.entity = self.service.new_model(fname)  # 원본

    def draw_survived_dead(self):
        this = self.entity  # 카피본. 여기서 this는 데이터프레임을 의미 -> 원본값을 변경시키지 않는다.
                            # this라는 인스턴스를 만들어서 카피본으로 사용
        # print(f'The data type of Train is {type(this.train)}.')
        # print(f'Columns of Train is {this.train.columns}.')
        # print(f'The top 5 superior data are {this.train.head}.')
        # print(f'The top 5 inferior data are {this.train.tail}.')
        f, ax = plt.subplots(1, 2, figsize = (18, 8)) # subplots => 한번에 여러 그래프를 보여주기 위해 사용
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])  # 여기서 data=this, 여기서 this는 데이터프레임
        plt.show()

    def draw_pclass(self):
        this = self.entity
        this['생존결과'] = this['Survived']\
            .replace(0, '사망자').replace(1, '생존자')
        this['Pclass'] = this['Pclass'].replace(1,'1등석').replace(2,'2등석').replace(3,'3등석')
        sns.countplot(data=this, x='좌석등급', hue='생존결과')
        plt.show()

    def draw_sex(self):
        this = self.entity
        f, ax = plt.subplots(1, 2, figsize = (18, 8))
        this['Survived'][this['Sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        this['Survived'][this['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
        ax[0].set_title('남성의 생존비율 [0.사망자 vs 1.생존자]')
        ax[1].set_title('여성의 생존비율 [0.사망자 vs 1.생존자]')
        plt.show()

    def draw_embarked(self):
        this = self.entity
        this['생존결과'] = this['Survived'] \
            .replace(0, '사망자').replace(1, '생존자')
        this['승선항구'] = this['Embarked'] \
            .replace("C", '쉘버그').replace("S", '사우스햄톤').replace("Q", '퀸즈타운')
        sns.countplot(data=this, x='승선항구', hue='생존결과')
        plt.show()

        '''
        The data type of Train is <class 'pandas.core.frame.DataFrame'>.
        Columns of Train is Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
               'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
              dtype='object').
        The top 5 superior data are <bound method NDFrame.head of      PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
        0              1         0       3  ...   7.2500   NaN         S
        1              2         1       1  ...  71.2833   C85         C
        2              3         1       3  ...   7.9250   NaN         S
        3              4         1       1  ...  53.1000  C123         S
        4              5         0       3  ...   8.0500   NaN         S
        ..           ...       ...     ...  ...      ...   ...       ...
        886          887         0       2  ...  13.0000   NaN         S
        887          888         1       1  ...  30.0000   B42         S
        888          889         0       3  ...  23.4500   NaN         S
        889          890         1       1  ...  30.0000  C148         C
        890          891         0       3  ...   7.7500   NaN         Q
        [891 rows x 12 columns]>.
        The top 5 inferior data are <bound method NDFrame.tail of      PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
        0              1         0       3  ...   7.2500   NaN         S
        1              2         1       1  ...  71.2833   C85         C
        2              3         1       3  ...   7.9250   NaN         S
        3              4         1       1  ...  53.1000  C123         S
        4              5         0       3  ...   8.0500   NaN         S
        ..           ...       ...     ...  ...      ...   ...       ...
        886          887         0       2  ...  13.0000   NaN         S
        887          888         1       1  ...  30.0000   B42         S
        888          889         0       3  ...  23.4500   NaN         S
        889          890         1       1  ...  30.0000  C148         C
        890          891         0       3  ...   7.7500   NaN         Q
        '''
