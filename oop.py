import string
class Alphabet:
    def __init__(self,leng, letters):
        self.leng = leng
        self.letters = letters
    def print(self):
        print(self.letters)
    def letters_num(self):
        return len(self.letters)
class EngAlpabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_letters)
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False
    def letters_num(self):
        return EngAlpabet.__letters_num
    @staticmethod
    def example():
        print("Hi, my name is Lera")
eng_alf = EngAlpabet()
eng_alf.print()
print(eng_alf.letters_num())
print(eng_alf.is_en_letter('k'))



