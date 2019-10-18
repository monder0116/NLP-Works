
import sys, time,os
def EOF(f):
    current_pos = f.tell()
    file_size = os.fstat(f.fileno()).st_size
    return current_pos >= file_size
def hypo(x):
    i = 0
    vw = "aeıioöuü"
    cn = "bcçdfgğhjklmnprsştvyz"
    while i < len(x):
        if x[i] in vw:
            if i + 1 < len(x) and x[i+1] in vw:
                return x[0:i+1] + "-" + hypo(x[i+1:len(x)])
            elif i + 2 < len(x) and x[i+2] in vw:
                return x[0:i+1] + "-" + hypo(x[i+1:len(x)])
            elif i + 3 == len(x) and x[i+1] in cn and x[i+2] in cn:
                return x[0:i+3] + "-" + hypo(x[i+3:len(x)])
            elif i + 3 < len(x) and x[i+3] in vw:
                return x[0:i+2] + "-" + hypo(x[i+2:len(x)])
            elif i+3 < len(x) and x[i+1] in cn and x[i+2] in cn and x[i+3] in cn:
                return x[0:i+3] + "-" + hypo(x[i+3:len(x)])
            elif i + 3 < len(x) and x[i:i+3] == 'str' or 'ktr' or 'ntr':
                return x[0:i+2] + "-" + hypo(x[i+2:len(x)])
            else:
                return x[0:i+3] + "-" + hypo(x[i+3:len(x)])

        i += 1

    return x
def check_corpus(input_file,outputfile):
    
    """Reads some lines of corpus from text file"""

    while(not EOF(input_file)):
        line=input_file.readline()
        heceli=hypo(line)
        outputfile.write(heceli)


def load_corpus(input_file):

    """Loads corpus from text file"""

    print('Loading corpus...')
    time1 = time.time()
    corpus = input_file.read()
    time2 = time.time()
    total_time = time2-time1
    print('It took %0.3f seconds to load corpus' %total_time)
    return corpus


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: python check_wiki_corpus.py <corpus_file> <outputfile>')
        sys.exit(1)

    corpus_file = open(sys.argv[1],'r')
    outfile = open(sys.argv[2],'w')
    check_corpus(corpus_file,outfile)
    outfile.close()
