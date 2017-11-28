class Guess:

    def __init__(self, word):
        self.word = word
        #추측에 사용된 글자들의 집합
        self.guessedChars = []
        #실패한 추측의 회수를 기록하기 위한 변수
        self.numTries = 0

        self.current = ["_"]*len(self.word)
        self.strcurrent = "_"*len(self.word)


    def display(self):
        print("Current :", self.strcurrent)
        print("")
        print("Tries: ", self.numTries)


    def guess(self, character):
        cnt = 0
        self.strcurrent = ""
        self.guessedChars.append(character)

        for i in range(len(self.word)):
            if self.word[i] == character:
                cnt += 1
                self.current[i] = character
            self.strcurrent += self.current[i]

        if cnt == 0:
            self.numTries += 1

        if self.word == self.strcurrent:
            return True
        else:
            return False