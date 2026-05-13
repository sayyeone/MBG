from preprocessing.clean_text import clean_text
from preprocessing.slang_normalization import SlangNormalizer
from preprocessing.stemming import IndonesianStemmer
from preprocessing.stopword_handler import (
    IndonesianStopwordRemover
)


class TextPreprocessor:
    
    def __init__(
        self,
        
        # preprocessing options
        use_slang_normalization: bool = True,
        use_stemming: bool = False,
        use_stopword_removal: bool = False,
        remove_emoji: bool = True,
        
        # resources
        slang_path: str = "../data/resources/slang_indo.csv"
    ):
        
        self.use_slang_normalization = use_slang_normalization
        self.use_stemming = use_stemming
        self.use_stopword_removal = use_stopword_removal
        self.remove_emoji = remove_emoji
        
        # initialize slang normalizer
        if self.use_slang_normalization:
            
            self.slang_normalizer = SlangNormalizer(
                slang_path=slang_path
            )
        
        
        # initialize stemmer
        if self.use_stemming:
            
            self.stemmer = IndonesianStemmer()
        
        
        # initialize stopword remover
        if self.use_stopword_removal:
            
            self.stopword_remover = (
                IndonesianStopwordRemover()
            )
    
    
    def preprocess(self, text: str) -> str:
        # STEP 1 - BASIC CLEANING
        
        text = clean_text(text)
        
        # STEP 2 - SLANG NORMALIZATION
        
        if self.use_slang_normalization:
            
            text = self.slang_normalizer.normalize(text)
        
        # STEP 3 - STOPWORD REMOVAL
        
        if self.use_stopword_removal:
            
            text = self.stopword_remover.remove(text)
        
        # STEP 4 - STEMMING
        
        if self.use_stemming:
            
            text = self.stemmer.stem(text)
        
        return text