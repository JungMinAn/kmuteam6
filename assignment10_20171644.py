class Guess:

    def __init__(self, word):

        self.hiddenword = word
        self.guessedChars = []
        self.numTries = 0
        self.letterposition = []
        self.tf = False

    def display(self):
        print('Current:' + self.hiddenword +" ", end="")
        for i in range (0, len(self.hiddenword)):
            if self.hiddenword[i] in self.letterposition:
                print(self.hiddenword[i], end="")
            else:
                print("_ ", end="")
        print('\nTries:'+ str(len(self.guessedChars)))



    def guess(self, character):
        tf = self.tf
        self.cword = character
        self.guessedChars.append(character)
        if character in self.hiddenword:
            self.letterposition.append(character)
            for i in range(0,len(self.hiddenword)):
                if self.hiddenword[i] in self.letterposition:
                    tf = True
                else:
                    tf = False
                    break
            return tf
        else:
            self.numTries+=1
            return False

    def currentStatus(self):
        for i in range (0, len(self.hiddenword)):
            if self.hiddenword[i] in self.letterposition:
                print(self.hiddenword[i] + " " , end="")
            else:
                print("_ ", end="")
