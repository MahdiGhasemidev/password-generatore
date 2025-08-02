import random
import string
from abc import ABC, abstractmethod

import nltk

# nltk.download('words')

class PasswordGenerator(ABC):

    @abstractmethod
    def generate(self):
        pass



class PinGenerator(PasswordGenerator):
    def __init__(self, length: int =8):
        self.length = length

    def generate(self):
        return "".join(random.choice(string.digits)for _ in range(self.length))


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols
        self.characters = string.ascii_letters
        if include_numbers :
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        return "".join(random.choice(self.characters)for _ in range(self.length))

class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self,
                no_of_words: int = 3,
                separator: str = "-",
                capitalize: bool = False,
                full_words: bool = True,
                min_letters: int = 2,
                max_letters: int = 5,
                vocabulary: list = None,
                ):
            if vocabulary is None:
                vocabulary = nltk.corpus.words.words()

            self.no_of_words = no_of_words
            self.separator = separator
            self.full_words = full_words
            self.capitalize = capitalize
            self.vocabulary = vocabulary
            self.min_letters = min_letters
            self.max_letters = max_letters

    def generate(self):
        selected = random.choices(self.vocabulary, k = self.no_of_words)
        result = []

        for name in selected:
            name = name.strip()

            if self.full_words:
                part = name

            else:
                n_letters = random.randint(self.min_letters, min(self.max_letters, len(name)))
                indices = random.sample(range(len(name)), n_letters)
                part = "".join(name[i]for i in sorted(indices))

            if not self.capitalize:
                part = part.lower()

            result.append(part)

        final_result = self.separator.join(result)
        return final_result

if __name__  ==  "__main__":

    g1 = PinGenerator()
    print(g1.generate())

    g2 = RandomPasswordGenerator(length=12, include_numbers=True, include_symbols=True)
    print(g2.generate())

    g3 = MemorablePasswordGenerator(no_of_words=4, capitalize=True, full_words=False)
    print(g3.generate())

