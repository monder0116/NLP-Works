import sys
import re

def hypo(x):
    isPython2 = False;
    if sys.version_info[0] < 3:
        isPython2 = True
    i = 0
    vw = "aeıioöuü"
    cn = "bcçdfgğhjklmnprsştvyz"


    if isPython2:
        vw = vw.decode("utf-8")
        cn = cn.decode("utf-8")

    while i < len(x):
        if x[i] in vw:
            if i + 1 < len(x) and x[i+1] in vw:
                return x[0:i+1] + " " + hypo(x[i+1:len(x)])
            elif i + 2 < len(x) and x[i+2] in vw:
                return x[0:i+1] + " " + hypo(x[i+1:len(x)])
            elif i + 3 == len(x) and x[i+1] in cn and x[i+2] in cn:
                return x[0:i+3] + " " + hypo(x[i+3:len(x)])
            elif i + 3 < len(x) and x[i+3] in vw:
                return x[0:i+2] + " " + hypo(x[i+2:len(x)])
            elif i+3 < len(x) and x[i+1] in cn and x[i+2] in cn and x[i+3] in cn:
                return x[0:i+3] + " " + hypo(x[i+3:len(x)])
            elif i + 3 < len(x) and x[i:i+3] == 'str' or 'ktr' or 'ntr':
                return x[0:i+2] + " " + hypo(x[i+2:len(x)])
            else:
                return x[0:i+3] + " " + hypo(x[i+3:len(x)])

        i += 1

    return x
def getKoks(context):
    isPython2 = False;
    if sys.version_info[0] < 3:
        isPython2 = True
    verbs=context
    if isPython2:
        verbs = verbs.decode("utf-8")

    verbs = verbs.replace("^", "")
    verbs = verbs.replace("%", "")
    verbs=verbs.split(' ')
    heceli=[]
    hece_arr=[]
    for i in verbs:
        heceli=str(hypo(i))
        for t in heceli.split(" "):
            if t!='':
                hece_arr.append(t)
    #print("kökler=",hece_arr)

    return hece_arr

def check_corpus(context):
    valid_harf=["a","b","c","ç", "d", "e" ,"f" ,"g", "ğ" ,"h" ,"ı" ,"i" ,"j" ,"k", "l"
    ,"m" ,"n" ,"o", "ö", "p" ,"r" ,"s" ,"ş" ,"t" ,"u" ,"ü", "v" ,"y" ,"z"," "]
    ncontext=""
    for i in range(len(context)):
        if context[i] in valid_harf:
            ncontext+=context[i]
        else:
            ncontext+=" "
    #print(ncontext)
    return ncontext
# Check python version
'''
corpus_file = open(sys.argv[1],'r')

verbs=corpus_file.read()
verbs=getKoks(verbs)
outfile = open(sys.argv[2],'w')
k=1
for i in verbs:
    outfile.write(heceli+ " ")
outfile.close()
'''
