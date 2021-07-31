import unittest
import os
from titanic.models.service import Service


class TitanicServiceTest(unittest.TestCase):
    mock = Service()

    def test_new_model(self):
        print(os.getcwd())

    def create_train(self):
        return None

    def create_label(self):
        return None

    def drop_feature(self, *feature):
        return None

    def embarked_nominal(self):
        return None

    def fare_oridnal(self):
        return None

    def title_nominal(self):
        return None

    def gender_nominal(self):
        return None

    def age_ordinal(self):
        return None

    def create_k_fold(self):
        return None

    def accuracy_by_classfier(self):
        return None


if __name__ == '__main__':
    unittest.main()