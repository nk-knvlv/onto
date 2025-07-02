from dotenv import load_dotenv
import os
from nlp import NLP
from ontology_monorepo.parser import Parser

load_dotenv()


def get_answer(question):
    answer = 'Нет информации по запросу'
    if can_answer(question):
        with open('/ontology_monorepo/faq.ontol', 'r', encoding='utf-8') as f:
            text = f.read()
            entities = text.split(',')
            if question in entities:
                answer = 'Утверждение верно'
    return answer


def can_answer(question) -> bool:
    """

    :param question:
    :return: Можем
    """
    with open('/ontology_monorepo/faq.ontol', 'r', encoding='utf-8') as f:
        text = f.read()
        if text:
            return True
    return False


def run():
    nlp = NLP()  # нормализует текст
    parser = Parser()  # переводит текст в триплеты
    ontology_path = os.getenv('ONTOL_PATH')
    # тут должны быть записаны правила, в виде пригодном для сравнения
    ontology = parser.parse_marked_text(ontology_path)

    while True:
        # получаем вопрос
        question = input("введите вопрос: ")
        tokens, lemmas = nlp.get_text_lemmas(question)
        # формируем ответ
        # print(get_answer(question))
        print(tokens, lemmas)


if __name__ == '__main__':
    run()
