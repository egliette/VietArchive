import re

def text_normalization(text: str) -> str:
    '''
    Perform text normalization:
    - Convert to lowercase
    - Delete digits
    - Remove newline characters
    - Remove special characters
    :param:
        text: input string
    :return:
        normalized_text: input text after normalization
    '''

    text = text.lower()
    text = ''.join([i for i in text if not i.isdigit()])
    text = ' '.join([i for i in text.split('\n')])
    text = re.sub(r'[^\w\s]', '', text)

    return text