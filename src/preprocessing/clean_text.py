import re


def remove_url(text: str) -> str:
    text = re.sub(r'http\S+|www\S+', '', text)
    return text


def remove_mentions(text: str) -> str:
    text = re.sub(r'@\w+', '', text)
    return text


def remove_hashtag_symbol(text: str) -> str:
    text = re.sub(r'#', '', text)
    return text


def normalize_repeated_char(text: str) -> str:
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)
    
    return text


def remove_extra_whitespace(text: str) -> str:
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def remove_rt_re(text: str) -> str:
    text = re.sub(r'\brt\b', '', text)
    text = re.sub(r'\bre\b', '', text)
    return text


def clean_text(text: str) -> str:
    # safety
    text = str(text)
    
    # lowercase
    text = text.lower()
    
    # remove url
    text = remove_url(text)
    
    # remove mentions
    text = remove_mentions(text)
    
    # remove rt & re
    text = remove_rt_re(text)
    
    # remove hashtag symbol only
    text = remove_hashtag_symbol(text)
    
    # normalize repeated chars
    text = normalize_repeated_char(text)
    
    # remove extra whitespace
    text = remove_extra_whitespace(text)
    
    return text