
import sys,math
from hecele import getKoks,check_corpus
import pickle
class Ngram:
    def __init__(self,n,corpus,create_metod,languageModel,loadmodel=False):
        self.ngrams = dict()
        self.n=n
        self.loadmodel=False
        self.create_metod=create_metod
        self.corpus=corpus
        self.languageModel=languageModel
        #self.ngram_data=self.generate_ngrams_fromfile(filename)
        if create_metod=="hece":
            self.ngram_intersec=self.count_ngrams(self.generate_ngrams(corpus))
            #print("train data=",self.ngram_intersec)
        else:
            self.ngram_intersec=self.count_ngrams(self.generate_ngrams(corpus))
            #print("train data=",self.ngram_intersec)
        print(n,"Gram Data Created.")
        self.add_one_to_Grams()
        print(n,"Gram Data Smoothed.")
    def generate_ngrams(self,corpus):
        corpus=check_corpus(corpus)
        if self.create_metod=="hece":
            grams_intersec=self.create_ngrams(getKoks(corpus))
        else:
            corpus=self.converttoSpell(corpus)
            grams_intersec=self.create_ngrams(corpus)
        return grams_intersec
    def create_ngrams(self , input):
        #if self.create_metod=="hece":
        #    input.replace("
        gram_arr=[]

        for i in range(len(input)-self.n+ 1):
            key_intersec=input[i:i+self.n]
            gram_arr.append(key_intersec)

        return gram_arr
    def count_ngrams(self , ngrams):
        #if self.create_metod=="hece":
        #    input.replace("
        grams_intersec=dict()
        for i in ngrams:
            gramstr=self.gramArrayToStr(i)
            if gramstr in grams_intersec.keys():
                grams_intersec[gramstr]+=1
            else:
                grams_intersec[gramstr]=1
        return grams_intersec
    def gramArrayToStr(self,gram):
        return ' '.join(gram)
    def converttoSpell(self,corpus):
        spell_corpus_arr=[]
        for i  in range(len(corpus)):
            spell_corpus_arr.append(corpus[i])
        return spell_corpus_arr
    def add_one_to_Grams(self):
        #print("addoneönce=",self.ngram_union)
        for key in self.ngram_intersec :
            #print(key
            self.ngram_intersec[key]=self.ngram_intersec[key]+1
        #print("addonesonra=",self.ngram_union)
    def CalculateProb(self,example):
        example_intersec_grams=self.generate_ngrams(example)
        example_total_gram_prob=1
        gram_props=[]
        #print("gelen=",example_intersec_grams)
        unknown=0
        for gram in example_intersec_grams:
            gram_union=gram[:-1]
            gram_intersec=gram
            gram_intersec_count=1
            if self.n==1:
                gram_union_count=sum(self.ngram_intersec.values())
            else:
                gram_union_count=self.languageModel.searchinAllGram(gram_union,self.n-1,self.create_metod)
                #print("aranan=",gram_union," bulunan count=",gram_union_count)

            if self.getCount(gram)!=0:
                gram_intersec_count=self.getCount(gram)
            gram_prob=gram_intersec_count/gram_union_count
            gram_props.append(gram_prob)
            example_total_gram_prob+=math.log(gram_prob,10)
        example_total_gram_prob=math.exp(example_total_gram_prob)
        return example_total_gram_prob,example_intersec_grams,gram_props
    def getCount(self,p):
        count=0
        for key in self.ngram_intersec.keys():
            if self.gramArrayToStr(p) == key:
                count=self.ngram_intersec[key]
        return count
    def Calculate_Perplexty(self,example):
        prob,intersec,gram_probs=self.CalculateProb(example)
        sum=1
        for p in gram_probs:
            sum*=1/p
        result=sum**(1/len(intersec))
        return result,intersec
