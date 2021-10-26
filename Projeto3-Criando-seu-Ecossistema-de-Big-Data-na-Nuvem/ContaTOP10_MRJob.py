from mrjob.job import MRJob
from mrjob.step import MRStep
import re

#valores diferentes do spark dataframe pois estava testando regras diferentes em reg_exp
exp_palavra = "[\w]+"
exp_unicode = re.compile(r"[^\u0000-\u007F]+")
#exp_aspas = re.compile(r"\u2019")

class ContaPalavra(MRJob):

    def steps(self):
        return [ MRStep(mapper=self.mapper,reducer=self.reducer),
                 MRStep(reducer=self.topdez)
        ]

    def mapper(self, _,linha):

        for elemento in linha.split():
            if re.match(exp_palavra, elemento):
                elemento =  re.sub(r'[^a-z|A-Z]+$|^[^a-z|A-Z]+',"",elemento).lower()
                #elemento = re.sub(exp_aspas,"'",elemento)
                yield elemento, 1


    def reducer(self,elemento,qnt):
       yield None, (sum(qnt),elemento)

    def topdez(self,_,pares):
        ordena = sorted(pares,reverse=True)
        for resultado_final in ordena[0:10]:
            yield resultado_final


if __name__ == '__main__':
    ContaPalavra.run()