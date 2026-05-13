import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

SLANG_PATH = BASE_DIR / "data" / "resources" / "slang_indo.csv"

class SlangNormalizer:
    
    def __init__(
        self,
        slang_path: str = str(SLANG_PATH)
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