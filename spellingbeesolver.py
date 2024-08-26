import pandas as pd

def readandclean():
    sblist=pd.read_csv("nytsolver\content\crosswd.txt")

    sblist.columns=['words']

    sbdict=sblist.dropna()

    sbdict=sbdict[~sbdict['words'].str.contains('s')] #spelling bee never has s

    sbdict['length']=sbdict.words.str.len()
    sbdict=sbdict[sbdict.length>=4]
    sbdict=sbdict[sbdict.length<=22] #feels like a reasonable one (longest historic word)
    return sbdict


def solver(sols):
    middle=input("Type the middle letter   ")

    sols=sols[sols['words'].str.contains(middle)]
    sols=sols.dropna()

    other=input("Type the other letters     ")
    letters=set(other+middle)

    answers=[]

    for i in sols.words:
        word=set(i)
        if word.issubset(letters):
            answers.append(i)
    return answers

if __name__=="__main__":
    cleaned = readandclean()
    answers=solver(cleaned)
    print(answers)