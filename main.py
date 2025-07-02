import re
from dotenv import load_dotenv
import os
from nlp import NLP

load_dotenv()



def get_answer(question):
    answer = 'Нет информации по запросу'
    if can_answer(question):
        answer = 'Утверждение верно'
    return answer


def can_answer(question):
    with open('user')
    pass


def parse_marked_text(marked_text):
    with open(marked_text, 'w') as mt:
        text = mt.read()
        pattern = r'<(.*?)>(.*?)(?=<|$)'
        fragments = re.findall(pattern, text)

        triples = []
        current_subject = None

        for tags, content in fragments:
            tags = [tag.strip() for tag in tags.split(',')]
            content = content.strip()

            if any('_s_' in tag for tag in tags):
                current_subject = content
            elif any('_r' in tag for tag in tags):
                predicate = content
            elif any('_f_' in tag for tag in tags):
                obj = content
                if current_subject and predicate:
                    triples.append({
                        "subject": current_subject,
                        "predicate": predicate,
                        "object": obj
                    })

        return {"triples": triples}


def run():
    # парсим триплеты
    nlp = NLP()
    # тут должны быть записаны правила, в виде пригодном для сравнения
    triples = parse_marked_text('user_query.ontol')

    while True:
        # получаем вопрос
        question = input("введите вопрос: ")
        tokens, lemmas = nlp.get_text_lemmas(question)
        # формируем ответ
        return get_answer(question)


if __name__ == '__main__':
    run()
