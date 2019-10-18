from ngram import Ngram
class LanguageModel:
    def __init__(self,maxNgramcount,content):
        self.maxNgramcount=maxNgramcount
        self.corpus=content
        print("Hece gramları oluşturuluyor")
        self.ngrams_hece=[(Ngram(i+1,self.corpus,"hece",self)) for i in range(self.maxNgramcount)]
        print("---------------------------")
        print("Harf gramları oluşturuluyor")
        self.ngrams_harf=[(Ngram(i+1,self.corpus,"harf",self)) for i in range(self.maxNgramcount)]
    def Calculate_Probs_harf(self,example):
        prob_result=[]
        grams=[]
        for grammodel in self.ngrams_harf:
            gram_prob,gram,_=grammodel.CalculateProb(example)
            prob_result.append(gram_prob)
            grams.append(gram)
        return prob_result,grams
    def Calculate_Probs_hece(self,example):
        prob_result=[]
        grams=[]
        for grammodel in self.ngrams_hece:
            example_total_gram_prob,example_intersec_grams,gram_props=grammodel.CalculateProb(example)
            prob_result.append(example_total_gram_prob)
            grams.append(example_intersec_grams)
        return prob_result,grams

    def Calculate_Perplexty_harf(self,example):
        perp_arr=[]
        i=1
        grams=[]
        for grammodel in self.ngrams_harf:
            perp_result,gram =grammodel.Calculate_Perplexty(example)
            perp_arr.append(perp_result)
            grams.append(gram)
            i+=1
        return perp_arr,grams
    def Calculate_Perplexty_hece(self,example):
        perp_arr=[]
        i=1
        grams=[]
        for grammodel in self.ngrams_hece:
            perp_result,gram =grammodel.Calculate_Perplexty(example)
            perp_arr.append(perp_result)
            grams.append(gram)
            i+=1
        return perp_arr,grams
    def searchinAllGram(self,p,n,create_metod):
        if p==[]:
            summ=sum(self.ngrams_harf[0].ngram_intersec.values())
            return summ
        if create_metod=="hece":
            res=0
            gram=[]
            for i in range(n):
                c=self.ngrams_hece[i].getCount(p)
                if c!=0:
                    res=c
            if res!=0:
                #print("p=",p," n=",n," res=",res)

                return res
            #print("arama",n ," gramda bulunamadı!->",p,"->",p[:-1])
        else:
            res=0
            for i in range(n):
                c=self.ngrams_harf[i].getCount(p)
                if c!=0:
                    res=c
            if res!=0:
                #print("p=",p," n=",n," res=",res)
                return res
        return self.searchinAllGram(p[:-1],n-1,create_metod)
