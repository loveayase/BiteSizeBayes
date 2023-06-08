'''
 * Project Name: BiteSizeBayes
 * NAME: Answer
 * Made by Jaejun
 * Date: 2023-06-07
 * Desc: 
'''

from abc import abstractmethod
from pandas.core.frame import DataFrame


class Answer:
    def __init__(self, chapter: int, question_number: int):
        self.chapter = chapter
        self.question_number = question_number

        self.print_question_information()

    @abstractmethod
    def _load_data(self):
        pass

    @abstractmethod
    def submit(self):
        pass

    @staticmethod
    def prob(A: DataFrame):
        return A.mean()

    @staticmethod
    def conditional(proposition: DataFrame, given: DataFrame):
        return Answer.prob(proposition[given])

    @staticmethod
    def update(table: DataFrame):
        table['unnorm'] = table['prior'] * table['likelihood']
        prob_data = table['unnorm'].sum()
        table['posterior'] = table['unnorm'] / prob_data
        return prob_data

    def print_question_information(self):
        print(f'Question {self.chapter}-{self.question_number}')
