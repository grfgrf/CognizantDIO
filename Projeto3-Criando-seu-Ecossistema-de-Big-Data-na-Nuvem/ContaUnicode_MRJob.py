from mrjob.job import MRJob
from mrjob.step import MRStep
import re

exp_palavra = re.compile(r"[^\u0000-\u007F]+")

class ContaUnicodes(MRJob):

    def steps(self):
        return [
            MRStep (mapper = self.mapper, reducer = self.reducer)
        ]

    def mapper(self, _,linha):

        for elemento in exp_palavra.findall(linha):
            for i in range(len(elemento)):
                yield elemento[i], 1
                #yield "Total", 1

    def reducer(self,elemento,qnt):
       yield elemento,sum(qnt)


if __name__ == '__main__':
    ContaUnicodes.run()