'''
 * Project Name: BiteSizeBayes
 * NAME: Answer
 * Made by Jaejun
 * Date: 2023-06-09
 * Desc: 
'''

from Answer import Answer as Original
import pandas as pd


class Answer(Original):

    def __init__(self, question_number: int):
        super().__init__(chapter=3, question_number=question_number)
        self.gss = self._load_data()

    def _load_data(self, ):
        gss = pd.read_csv('../gss_bayes.csv', index_col=0)
        return gss


# 3-1
class Question1(Answer):

    def __init__(self):
        super().__init__(question_number=1)

    def submit(self):
        from empiricaldist import Pmf
        hypos = [6, 8, 12]
        prior = Pmf(1 / 3, hypos)

        # Update Directly

        likelihood1 = 1 / 6, 1 / 8, 1 / 12
        likelihood2 = 1 / 6, 1 / 8, 1 / 12
        likelihood3 = 1 / 6, 1 / 8, 1 / 12
        likelihood4 = 0, 1 / 8, 1 / 12

        posterior = prior * likelihood1
        posterior.normalize()

        posterior *= likelihood2
        posterior.normalize()

        posterior *= likelihood3
        posterior.normalize()

        posterior *= likelihood4
        posterior.normalize()
        print(posterior[8])

        # Use update_dice
        self.update_dice(prior, 1)
        self.update_dice(prior, 3)
        self.update_dice(prior, 5)
        self.update_dice(prior, 7)
        print(prior[8])

        return


# 3-2
class Question2(Answer):

    def __init__(self):
        super().__init__(question_number=2)

    def submit(self):
        from empiricaldist import Pmf
        hypos = [4, 6, 8, 12, 20]
        hypos_prob = [1 / 25, 2 / 25, 3 / 25, 4 / 25, 5 / 25]

        prior = Pmf(hypos_prob, hypos)
        self.update_dice(prior, 7)
        print(prior[8])

        return


# 3-3
class Question3(Answer):

    def __init__(self):
        super().__init__(question_number=3)

    def submit(self):
        from empiricaldist import Pmf
        hypos = ['White', 'Black', 'Red', 'Green', 'Blue']

        prior = Pmf(1 / 5, hypos)

        likelihood1 = 1 / 2, 1 / 2, 1 / 2, 1 / 2, 1 / 2
        posterior = prior * likelihood1
        posterior.normalize()

        likelihood2 = 1 / 4, 1 / 4, 1 / 9, 1 / 9, 1 / 9
        posterior *= likelihood2
        posterior.normalize()

        print(posterior['White'])

        return


# 3-4
class Question4(Answer):

    def __init__(self):
        super().__init__(question_number=4)

    def submit(self):
        # 번역이 이상한 건지 데이터가 없는데..

        from empiricaldist import Pmf
        hypos = ['Identical', 'Fraternal']
        hypos_proba = [1 / 3, 2 / 3]
        prior = Pmf(hypos_proba, hypos)

        print(prior['Identical'])


if __name__ == "__main__":
    Question1().submit()
    Question2().submit()
    Question3().submit()
    Question4().submit()
