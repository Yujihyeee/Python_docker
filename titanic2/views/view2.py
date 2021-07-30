from titanic2.models.dataset2 import Dataset2
from titanic2.models.service2 import Service2


class View(object):

    dataset2 = Dataset2()
    service2 = Service2()

    def modeling(self, train, test):

        this = self.preprocessing(train, test)
        print(f'The Type of This is {type(this.train)}')
        print(f'The Type of This is \n{this.train.head(2)}')


    def preprocessing(self, train, test) -> object:
        service2 = self.service2
        this = self.dataset2
        this.train = service2.new_madel2(train)
        this.test = service2.new_madel2(test)
        return this

if __name__ == '__main__':
    view = View()
    view.modeling('train.csv', 'test.csv')

