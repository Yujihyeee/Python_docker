from titanic.models.dataset import Dataset
import pandas as pd


class TitanicService(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        return pd.read_csv(f"/data/{payload}.csv")


    @staticmethod
    def create_train(this) -> object:
        return this.train.drop("Survived", axis=1)
    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this


    def embarked_nominal(this) -> str:
        return this


    def fare_oridnal(this) -> object:
        return this


    def title_nominal(this) -> str:
        return this


    def gender_nominal(this) -> str:
        return this


    def age_ordinal(this) -> object:
        return this


    def create_k_fold(self) -> None:
        return None


    def accuracy_by_classfier(this) -> str:
        return None


