'''
 * Project Name: BiteSizeBayes
 * NAME: Answer
 * Made by Jaejun
 * Date: 2023-06-08
 * Desc: 
'''

from Answer import Answer as Original
import pandas as pd


class Answer(Original):

    def __init__(self, question_number: int):
        super().__init__(chapter=2, question_number=question_number)
        self.gss = self._load_data()

    def _load_data(self, ):
        gss = pd.read_csv('../gss_bayes.csv', index_col=0)
        return gss


# 2-1
class Question1(Answer):

    def __init__(self):
        super().__init__(question_number=1)

    def submit(self):
        table = pd.DataFrame(index=['Coin 1', 'Coin 2'])
        table['prior'] = 1 / 2, 1 / 2
        table['likelihood'] = 1 / 2, 1
        table['unnorm'] = table['prior'] * table['likelihood']
        prob_data = self.update(table)
        print(table['posterior']['Coin 2'])

        return


# 2-2
class Question2(Answer):

    def __init__(self):
        super().__init__(question_number=2)

    def submit(self):
        # P(DD|D) = P(DD) * P(D|DD) / P(D)
        # P(D) = 딸일 확률 = 0.5
        # P(D|DD) = 딸 두명이 주어졌을 경우 딸일 확률 = 1
        # P(DD) = 자식이 딸이 두 명일 확률 = 0.25
        # P(DD|D) = 1 / 4 * 1 / (1/2)

        table = pd.DataFrame(index=['DD', 'DS(SD)', 'SS'])
        # 전체 자식의 조합
        table['prior'] = 1 / 4, 2 / 4, 1 / 4
        # 자식 중에서 딸을 뽑았을 확률
        table['likelihood'] = 1, 1 / 2, 0
        table['unnorm'] = table['prior'] * table['likelihood']
        prob_data = self.update(table)
        print(table['posterior']['DD'])
        return


# 2-3
class Question3(Answer):

    def __init__(self):
        super().__init__(question_number=3)

    def submit(self):
        table = pd.DataFrame(index=['D1', 'D2', 'D3'])
        # 최초 선택시 문에 상품이 있을 확률
        table['prior'] = 1 / 3, 1 / 3, 1 / 3
        table['likelihood'] = 1 / 2, 0, 1
        table['unnorm'] = table['prior'] * table['likelihood']
        prob_data = self.update(table)
        print(table['posterior']['D3'])

        table = pd.DataFrame(index=['D1', 'D2', 'D3'])
        # 최초 선택시 문에 상품이 있을 확률
        table['prior'] = 1 / 3, 1 / 3, 1 / 3
        table['likelihood'] = 0, 1, 0
        table['unnorm'] = table['prior'] * table['likelihood']
        prob_data = self.update(table)
        print(table['posterior']['D2'])

        return


# 2-4
class Question4(Answer):

    def __init__(self):
        super().__init__(question_number=4)

    def submit(self):
        table = pd.DataFrame(index=['1994', '1996'])
        # 최초 선택시 문에 상품이 있을 확률
        table['prior'] = 1 / 2, 1 / 2
        table['likelihood'] = 0.2 * 0.2, 0.1 * 0.14
        table['unnorm'] = table['prior'] * table['likelihood']
        prob_data = self.update(table)
        print(table['posterior']['1994'])
        return


if __name__ == "__main__":
    Question1().submit()
    Question2().submit()
    Question3().submit()
    Question4().submit()
