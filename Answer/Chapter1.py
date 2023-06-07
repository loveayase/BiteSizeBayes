'''
 * Project Name: BiteSizeBayes
 * NAME: Answer
 * Made by Jaejun
 * Date: 2023-06-07
 * Desc: 
'''

from Answer import Answer as Original
import pandas as pd


class Answer(Original):

    def __init__(self, question_number: int):
        super().__init__(chapter=1, question_number=question_number)
        self.gss = self._load_data()

    def _load_data(self, ):
        gss = pd.read_csv('../gss_bayes.csv', index_col=0)
        return gss


class Question1(Answer):

    def __init__(self):
        super().__init__(question_number=1)
        # 문제 1-1

    def submit(self):
        # 은행원일 확률
        banker = (self.gss['indus10'] == 6870)
        p = Answer.prob(banker)

        # 여성일 확률
        female = (self.gss['sex'] == 2)
        p = Answer.prob(female)

        # 진보 성향일 확률
        liberal = (self.gss['polviews'] <= 3)
        p = Answer.prob(liberal)

        # 민주 당원일 확률
        democrat = (self.gss['partyid'] <= 1)

        # 은행원일 경우 여성일 확률
        p_female_given_banker = Answer.conditional(female, given=banker)

        # 여성일 경우 은행원일 확률
        p_banker_given_female = Answer.conditional(banker, given=female)

        # 린다가 여성 은행원일 확률
        p = Answer.prob(female & banker)
        print(p)

        # 린다가 진보 성향의 여성 은행원일 가능성
        p = Answer.prob(female & banker & liberal)
        print(p)

        # 린다가 진보 성향의 여성 은행원일 가능성
        p = Answer.prob(female & banker & liberal & democrat)
        print(p)

        return


class Question2(Answer):

    def __init__(self):
        super().__init__(question_number=2)

    def submit(self):
        # 은행원일 확률
        banker = (self.gss['indus10'] == 6870)

        # 여성일 확률
        female = (self.gss['sex'] == 2)

        # 진보 성향일 확률
        liberal = (self.gss['polviews'] <= 3)

        # 민주 당원일 확률
        democrat = (self.gss['partyid'] <= 1)

        # 응답자가 민주당원일 경우 진보 성향일 확률
        p = Answer.conditional(liberal, given=democrat)
        print(p)

        # 응답자가 민주당원일 경우 진보 성향일 확률
        p = Answer.conditional(democrat, given=liberal)
        print(p)

        return


class Question3(Answer):

    def __init__(self):
        super().__init__(question_number=3)

    def submit(self):
        # 은행원일 확률
        banker = (self.gss['indus10'] == 6870)

        # 여성일 확률
        female = (self.gss['sex'] == 2)

        # 진보 성향일 확률
        liberal = (self.gss['polviews'] <= 3)

        # 민주 당원일 확률
        democrat = (self.gss['partyid'] <= 1)

        # 30세 미만인 경우
        young = (self.gss['age'] < 30)

        # 65세 이상인 경우
        old = (self.gss['age'] >= 65)

        # 보수적인 사람들
        conservative = (self.gss['polviews'] >= 5)

        # 임의로 고른 응답자가 젊은 진보 성향일 확률
        p = self.prob(young & liberal)
        print(p)

        # 젊은 사람이 진보적일 확률은 얼마인가?
        p = self.conditional(liberal, given=young)
        print(p)

        # 응답자가 늙고 보수 성향일 확률은 얼마인가?
        p = self.prob(old & conservative)
        print(p)

        # 보수 성향의 사람들이 늙었을 확률은 얼마인가?
        p = self.conditional(old, given=conservative)
        print(p)

        return


if __name__ == "__main__":
    Question1().submit()
    Question2().submit()
    Question3().submit()
