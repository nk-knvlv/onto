import spacy


class NLP:
    core: spacy.Language

    def __init__(self):
        self.core = spacy.load("ru_core_news_sm")

    def get_text_lemmas(self, text) -> tuple:
        doc = self.core(text)

        tokens = [token.text for token in doc]
        lemmas = [token.lemma_ for token in doc]

        return tokens, lemmas

    # TODO нужно лучше разобраться может ли doc возвращать больше 1 леммы на слово
    def lemmatizate(self, text: str) -> str:
        return self.core(text)[0].lemma_
