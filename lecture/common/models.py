from dataclasses import dataclass

import pandas as pd


@dataclass
class Dataset(object):
    context: str
    fname: str
    bugs: object
    melon: object


    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def bugs(self) -> object: return self._bugs

    @bugs.setter
    def bugs(self, bugs): self._bugs = bugs

    @property
    def melon(self) -> object: return self._melon

    @melon.setter
    def melon(self, melon): self._melon = melon


class Service(object):

    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)