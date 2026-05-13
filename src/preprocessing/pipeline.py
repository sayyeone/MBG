from preprocessing.clean_text import clean_text
from preprocessing.slang_normalization import SlangNormalizer


class TextPreprocessor:
    
    def __init__(
        self,
        use_slang_normalization: bool = True,
        slang_path: str = "resources/slang_indo.csv"
    ):
        
        self.use_slang_normalization = use_slang_normalization
        
        
        # initialize slang normalizer
        if self.use_slang_normalization:
            
            self.slang_normalizer = SlangNormalizer(
                slang_path=slang_path
            )
    
    
    def preprocess(self, text: str) -> str:
        """
        Full preprocessing pipeline.
        """
        
        # basic cleaning
        text = clean_text(text)
        
        
        # slang normalization
        if self.use_slang_normalization:
            
            text = self.slang_normalizer.normalize(text)
        
        
        return text