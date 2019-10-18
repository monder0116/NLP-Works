from ngram import Ngram
from languagemodel import LanguageModel
import sys,math
from hecele import getKoks,check_corpus
import pickle,os

def __main__():
    if len(sys.argv)!=2 :
        print("usage: python main.py <corpusfile>")
        exit()
    if  not os.path.exists(sys.argv[1]):
        print("file does not exists")
        exit() 
    file=open(sys.argv[1],"r")
    content=file.read().lower()

    modelanswer=str(input("Load last language model (y|n) ? ")).lower()

    modelname="last.bin"
    if modelanswer=="n":
        modelname=str(input("Enter new model name="))
        test1=LanguageModel(5,content)
        binary_file = open(modelname,mode='wb')
        obj = pickle.dump(test1, binary_file)
        binary_file.close()
    else:
        modelname=str(input("what's model filename?"))
    infile = open(modelname,'rb')
    test_language = pickle.load(infile)
    infile.close()
    log=False
    while(1):
        printmenu(log)
        inp=int(input("Select="))
        if inp==1:
            log=not log
            continue
        example=str(input("Enter a sentense="))
        if inp==2:
            print("letter Grams:")
            res,grams=test_language.Calculate_Perplexty_harf(example)
            if log:
                print(grams)

            for p in range(len(res)):
                print(p+1,"Gram Perplexty=",res[p])
            print("-----------")

            print("syllable Grams:")
            res,grams=test_language.Calculate_Perplexty_hece(example)
            if log:
                print(grams)
            for p in range(len(res)):
                print(p+1,"Gram Perplexty=",res[p])
            print("-----------")

        if inp==3:
            print("letter Grams:")
            res,grams=test_language.Calculate_Probs_harf(example)
            if log:
                print(grams)
            for p in range(len(res)):
                print(p+1,"Gram probability=",res[p])
            print("-----------")

            print("syllable Grams:")
            res,grams=test_language.Calculate_Probs_hece(example)
            if log:
                print(grams)

            for p in range(len(res)):
                print(p+1,"Gram probability=",res[p])
            print("-----------")
        if inp==4:
            break
    #print(test.getProb("ali ata bak ali"))
def printmenu(log):
    print("--------------------")
    print("1)Show log->",log)
    print("2)calculate Perplexty ")
    print("3)calculate probability")
    print("4)exit")

__main__()
