import numpy as geek
#This file just contains the basic levenshtein function ie if I input 2 words it will return the minimum distance between the two words
#as seen by the example below of party and parties
def fix_word_format(word):
    newWord = ""
    newWord = newWord+"#"
    for s in range(len(word)):
     newWord = newWord+word[s]
    return newWord
def min_distance(firstWord, secondWord):
    firstWord =[i for i in firstWord]
    firstWord = fix_word_format(firstWord)
    secondWord = [i for i in secondWord]
    secondWord = fix_word_format(secondWord)
    answer = geek.zeros((len(secondWord), len(firstWord)))
    for j in range(len(firstWord)):
        answer[0,j]=j
    for j1 in range(len(secondWord)):
        answer[j1,0]=j1
    if(firstWord[1]!=secondWord[1]):
        answer[1,1]=2
        
    for c in range(1,len(firstWord)):
        for r in range(1, len(secondWord)):
            if(firstWord[c]!=secondWord[r]):
                if(answer[r-1,c]<answer[r, c-1]):
                    answer[r,c]= answer[r-1,c]+1
                else:
                    answer[r,c]= answer[r,c-1]+1 
            else:
                answer[r,c]= answer[r-1,c-1]
    a = len(secondWord)-1
    b= len(firstWord)-1
    return answer[a,b]
if __name__ == "__main__":
    print(min_distance("party","parties"))
