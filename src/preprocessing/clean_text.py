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

def remove_emoji(text: str) -> str:
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )
    
    return emoji_pattern.sub(r'', text)


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
    
    # remove emoji
    text = remove_emoji(text)
    
    return text