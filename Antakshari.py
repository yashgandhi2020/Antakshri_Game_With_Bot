import random

# back end && Data Base
class LyricsLoader:
    def __init__(self, path):
        li = open(path, "r")

        self.lyrics = []

        for i in li:
            i = i.strip()
            if len(i) > 0:
                self.lyrics.append(i)
        li.close()

    def getlyrics(self):
        return self.lyrics

#Logic

class Game_Maneger:
    def __init__(self, ref):
        self.lyrics = ref.getlyrics()

        random.shuffle(self.lyrics)

        self.l1 = self.lyrics[0::2]
        self.l2 = self.lyrics[1::2]

    def getsepreatelyrics(self):
        return(self.l1, self.l2)

class antakshari:
    def __init__(self, ref):
        self.ll1, self.ll2 = ref.getsepreatelyrics()

    def playwithgamebot(self, Name1):

        resultoffailures = []
        Players = [Name1, 'GameBot']# ll1 and ll2
        Scores = [0, 0]
        Current = 0
        Status = 0 # if Status is zero then no condition else if 1 then condition
        lastchar = ''

        print("Game Begins......")
        print(Players[0], "Score: ", Scores[0])
        print(Players[1], "score: ", Scores[1])
        print("Enter -1 for give up")

        while len(self.ll1) != 0 or len(self.ll2) != 0:
            if Current == 0:
                no = 1
                for i in self.ll1:
                    print(no, ")", i)
                    no += 1

                if Status == 0:# -1 or first time
                    ch = int(input("Yash Enter Choice: "))
                    if ch >= 1 and ch <= len(self.ll1):
                        print(Players[Current], "Play's: ", self.ll1[ch-1])
                        print(Players[0], "Score: ", Scores[0])
                        print(Players[1], "score: ", Scores[1])
                        lastchar = self.ll1[ch-1][-1]
                        del(self.ll1[ch-1])
                        Current = 1
                        Status = 1

                elif Status == 1:# Something else
                    ch = int(input("Yash Enter Choice: "))
                    if ch >= 1 and ch <= len(self.ll1) and self.ll1[ch-1][0] == lastchar:
                        print(Players[Current], "Play's: ", self.ll1[ch - 1])
                        print(Players[0], "Score: ", Scores[0])
                        print(Players[1], "score: ", Scores[1])
                        lastchar = self.ll1[ch - 1][-1]
                        del (self.ll1[ch - 1])
                        Current = 1

                    if ch == -1:
                        resultoffailures.append(lastchar)
                        Status = 0
                        Scores[1] += 1
                        print(Players[1], "Score Increased by 1")

            elif Current == 1:

                if Status == 0:  # -1 or first time
                    no = 0
                    ok = True
                    if len(resultoffailures) > 0:
                        for i in resultoffailures:
                            no = 0
                            for j in self.ll2:
                                if ok:
                                    if i == j[-1]:
                                        print("GameBot Catched played: ", j)
                                        Current = 0
                                        Status = 1
                                        lastchar = j[-1]
                                        del(self.ll2[no])
                                        ok = False
                                no += 1
                    if ok:
                        number = random.randrange(len(self.ll2))
                        print("GameBot played:", self.ll2[number])
                        Current = 0
                        Status = 1
                        lastchar = self.ll2[number][-1]
                        del (self.ll2[number])

                elif Status == 1:  # Something else
                    no = 0
                    flag = 0
                    ok = True

                    for i in resultoffailures:
                        no = 0
                        for j in self.ll2:
                            if ok:
                                if lastchar == j[0] and j[-1] == i:
                                    print("GameBot played:", self.ll2[no])
                                    Current = 0
                                    lastchar = j[-1]
                                    del (self.ll2[no])
                                    flag = 1
                                    ok = False
                            no += 1

                    if flag == 0:
                        no = 0
                        ok = True
                        for j in self.ll2:
                            if ok:
                                if lastchar == j[0]:
                                    print("GameBot played:", self.ll2[no])
                                    Current = 0
                                    lastchar = j[-1]
                                    del (self.ll2[no])
                                    flag = 1
                                    ok = False
                            no += 1

                    if flag == 0:
                        print("GameBot gives up")
                        print(Players[0], "Score Increased By 1")
                        Scores[0] += 1
                        Status = 0
                        Current = 1

        if Scores[0] > Scores[1]:
            print("Yash Wins :)")
        elif Scores[0] < Scores[1]:
            print("GameBot Wins :)")
        elif Scores[0] == Scores[1]:
            print("Match Draw Both well played ....")

    def playwithyourfrined(self, Name1, Name2):
        resultoffailures = []
        Players = [Name1, Name2]# ll1 and ll2
        Scores = [0, 0]
        Current = 0
        Status = 0 # if Status is zero then no condition else if 1 then condition
        lastchar = ''
        print("Game Begins......")
        print(Players[0], "Score: ", Scores[0])
        print(Players[1], "score: ", Scores[1])
        print("Enter -1 for give up")
        while len(self.ll1) != 0 or len(self.ll2) != 0:
            if Current == 0:
                no = 1
                for i in self.ll1:
                    print(no, ")", i)
                    no += 1

                if Status == 0:# -1 or first time
                    ch = int(input("Yash Enter Choice: "))
                    if ch >= 1 and ch <= len(self.ll1):
                        print(Players[Current], "Play's: ", self.ll1[ch-1])
                        print(Players[0], "Score: ", Scores[0])
                        print(Players[1], "score: ", Scores[1])
                        lastchar = self.ll1[ch-1][-1]
                        del(self.ll1[ch-1])
                        Current = 1
                        Status = 1

                elif Status == 1:# Something else
                    ch = int(input("Yash Enter Choice: "))
                    if ch >= 1 and ch <= len(self.ll1) and self.ll1[ch-1][0] == lastchar:
                        print(Players[Current], "Play's: ", self.ll1[ch - 1])
                        print(Players[0], "Score: ", Scores[0])
                        print(Players[1], "score: ", Scores[1])
                        lastchar = self.ll1[ch - 1][-1]
                        del (self.ll1[ch - 1])
                        Current = 1

                    if ch == -1:
                        Status = 0
                        Scores[1] += 1
                        print(Players[1], "Score Increased by 1")

            elif Current == 1:
                no = 1
                for i in self.ll2:
                    print(no, ")", i)
                    no += 1

                if Status == 0:  # -1 or first time
                    ch = int(input("Sanket Enter Choice: "))
                    if ch >= 1 and ch <= len(self.ll2):
                        print(Players[Current], "Play's: ", self.ll2[ch - 1])
                        print(Players[0], "Score: ", Scores[0])
                        print(Players[1], "score: ", Scores[1])
                        lastchar = self.ll2[ch - 1][-1]
                        del (self.ll2[ch - 1])
                        Current = 0
                        Status = 1

                elif Status == 1:  # Something else
                    ch = int(input(" Sanket Enter Choice: "))
                    if ch >= 1 and ch <= len(self.ll2) and self.ll2[ch - 1][0] == lastchar:
                        print(Players[Current], "Play's: ", self.ll2[ch - 1])
                        print(Players[0], "Score: ", Scores[0])
                        print(Players[1], "score: ", Scores[1])
                        lastchar = self.ll2[ch - 1][-1]
                        del (self.ll2[ch - 1])
                        Current = 0

                    if ch == -1:
                        Status = 0
                        Scores[0] += 1
                        print(Players[0], "Score Increased by 1")

        if Scores[0] > Scores[1]:
            print("Yash Wins :)")
        elif Scores[0] < Scores[1]:
            print("Sanket Wins :)")
        elif Scores[0] == Scores[1]:
            print("Match Draw well played Both....")


def main():
    ls = LyricsLoader("lyrics.txt")
    gm = Game_Maneger(ls)
    an = antakshari(gm)
    print("Enter: ")
    print("1. For Two Players: ")
    print("2. Play with Intelligent GameBot: ")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        an.playwithyourfrined("Yash", "Sanket")

    elif ch ==2:
        an.playwithgamebot("Yash")
        
main()