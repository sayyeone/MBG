import pandas as pd

class SlangNormalizer:
    
    def __init__(
        self,
        slang_path: str = "resources/slang_indo.csv"
    ):
        
        self.slang_dict = self.load_slang_dictionary(slang_path)
    
    
    def load_slang_dictionary(self, slang_path: str) -> dict:
        
        slang_df = pd.read_csv(
            slang_path,
            header=None,
            names=['slang', 'formal']
        )
        
        slang_dict = dict(
            zip(
                slang_df['slang'],
                slang_df['formal']
            )
        )
        
        return slang_dict
    
    
    def normalize(self, text: str) -> str:
        
        words = text.split()
        
        normalized_words = []
        
        for word in words:
            
            normalized_word = self.slang_dict.get(word, word)
            
            normalized_words.append(normalized_word)
        
        
        return ' '.join(normalized_words)