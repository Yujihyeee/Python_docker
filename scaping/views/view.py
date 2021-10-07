from common.dataset import Dataset
from scaping.models.service import Service


class View(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, bugs, melon):
        this = self.preprocessing(bugs, melon)
        print(f'The Type of This is {type(this.bugs)}')
        print(f'The Type of This is{this.bugs.head(2)}')
        print(f'The Type of This is{this.melon.head(2)}')


    def preprocessing(self, bugs, melon) -> object:
        service = self.service
        this = self.dataset
        this.bugs = service.new_model(bugs)
        this.melon = service.new_model(melon)
        return this


if __name__ == '__main__':
    view = View()
    view.modeling('bugs.csv', 'melon.csv')