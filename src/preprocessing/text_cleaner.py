import re


class TextCleaner:
    def __init__(self):
        self.email_pattern = re.compile(r'\S+@\S+')
        self.phone_pattern = re.compile(r"\+?\d[\d\s\-]{7,}")

    def clean(self, text: str) -> str:
       text=text.lower()
       text=self.email_pattern.sub(' ', text)
       text=self.phone_pattern.sub(' ', text)
       text=re.sub(r"[^a-z0-9\+\#\.\s]", " ", text)
       text=re.sub(r"\s+", " ", text).strip()
       return text


