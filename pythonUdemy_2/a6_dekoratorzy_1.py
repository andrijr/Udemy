class Numbers:

    def __init__(self, numbers = []):
        self.numbers = numbers

    def sumNumbers(self):
        sumary = 0
        for x in self.numbers:
            sumary += x
        return sumary

    @staticmethod
    def substractMethod(a,b):
        print("Jestem statyczną metodą")
        return a -b

    @classmethod
    def printInformationAbautMe(cls):
        print("Jestem klasową metodą")
        print("Wywołana na rzecz klasy", cls)


Numbers.printInformationAbautMe()
