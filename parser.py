import re
from model.triplet import Triplet, Entity
from nlp import NLP


class Parser:
    nlp: NLP

    def __init__(self):
        self.nlp = NLP()  # нормализует текст

    @staticmethod
    def parse_marked_text(text_path: str) -> dict:
        with open(text_path, 'w') as mt:
            text = mt.read()
            pattern = r'<(.*?)>(.*?)(?=<|$)'
            fragments = re.findall(pattern, text)

            triplets = []
            current_subject = None

            for tags, content in fragments:
                tags = [tag.strip() for tag in tags.split(',')]
                content = content.strip()

                if any('_s_' in tag for tag in tags):
                    subject = Entity(text=content)
                elif any('_r' in tag for tag in tags):
                    relation = Entity(text=content)
                elif any('_f_' in tag for tag in tags):
                    obj = Entity(text=content)
                    if current_subject and relation:
                        triplet = Triplet(
                            subject=subject,
                            relation=relation,
                            object=obj
                        )

                        triplets.append(triplet)

            return {"triples": triplets}

    def parse_question(self, question) -> Triplet:
        tokens, lemmas = self.nlp.get_text_lemmas(question)
        return Triplet()
