import random as r

class Solver:
    def bestMove(self, curr: str):
        with open("sowpods.txt","r") as f:
            dict=f.readlines()
            for i in range(len(dict)):
                dict[i]=dict[i].replace("\n","")
            #check if current string is a valid word
            if curr in dict:
                return "That's a word, computer wins"
            #For each word in the dictionary, check if the current string is a substring of it.
            #If it isn't a substring of any, the opponent is bluffing.
            bluff=True
            for i in dict:
                if curr in i:
                    bluff=False
                    break
            if bluff:
                return "Computer calls the bluff and wins"
            #Calculate best move since initial checks passed
            alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            hypo=()
            poss=[]
            for i in alpha:
                #minus and plus moves
                hypo=(curr+i,i+curr)
                for x in hypo:
                    subdict=self.C_subdict(x,dict)
                    if not(self.validWord(x,dict)) and len(subdict)>0 and not(self.allOdd(subdict)):
                        if self.allEven(subdict):
                            print("yeye")
                            return x
                        hypo2=()
                        #check if opponent can force an odd word
                        works=True
                        for j in alpha:
                            #minus moves
                            hypo2=x+j
                            subsubdict=self.C_subdict(hypo2,subdict)
                            if not(self.validWord(hypo2,dict)) and len(subsubdict)>0:
                                if self.allOdd(subsubdict):
                                    #hypo won't work
                                    works=False
                                    break
                            #plus moves
                            hypo2=j+x
                            subsubdict=self.C_subdict(hypo2,subdict)
                            if not(self.validWord(hypo2,dict)) and len(subsubdict)>0:
                                if self.allOdd(subsubdict):
                                    #hypo won't work
                                    works=False
                                    break
                        if works:
                            poss.append(x)
            if len(poss)>0:
                print("eh")
                return r.choice(poss)
            currSubdict=self.C_subdict(curr,dict)
            #find longest word
            longest=""
            for i in currSubdict:
                if len(i)>len(longest):
                    longest=i
            return "Computer surrenders"
    def respond(self,curr):
        with open("sowpods.txt","r") as f:
            dict=f.readlines()
            for i in range(len(dict)): dict[i]=dict[i].replace("\n","")
            sub=self.C_subdict(curr,dict)
            if len(sub)==0:
                return "I got nothing"
            return r.choice(sub)
    def validWord(self, word: str, dict: list[str]):
        if word in dict:
            return True
        return False
    def C_subdict(self,word:str,dict:list[str]):
        sub=[]
        for i in dict:
            if word in i:
                sub.append(i)
        return sub
    def allOdd(self,li:list[str]):
        for i in li:
            if len(i)%2==0:
                return False
        return True
    def allEven(self,li:list[str]):
        for i in li:
            if not len(i)%2==0:
                return False
        return True
