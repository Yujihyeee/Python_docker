import pandas as pd
from titanic2.models.dataset2 import Dataset2


class Service2(object):

    dataset2 = Dataset2()

    def new_madel2(self, payload):
        this = self.dataset2
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

