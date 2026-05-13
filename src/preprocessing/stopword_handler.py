from Sastrawi.StopWordRemover.StopWordRemoverFactory import (
    StopWordRemoverFactory
)


class IndonesianStopwordRemover:
    
    def __init__(self):
        factory = StopWordRemoverFactory()
        
        self.stopwords = set(
            factory.get_stop_words()
        )
    
    
    def remove(self, text: str) -> str:
        words = text.split()
        
        filtered_words = [
            word
            for word in words
            if word not in self.stopwords
        ]
        
        return ' '.join(filtered_words)