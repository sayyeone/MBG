from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


class IndonesianStemmer:

    def __init__(self):
        factory      = StemmerFactory()
        self.stemmer = factory.create_stemmer()
        self._cache  = {}


    def stem(self, text: str) -> str:
        words  = text.split()
        result = [
            self._cache.setdefault(w, self.stemmer.stem(w))
            for w in words
        ]
        return ' '.join(result)