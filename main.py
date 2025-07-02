from dotenv import load_dotenv
import os
from ontology_monorepo.parser import Parser
from ontology_monorepo.search_engine import SearchEngine

load_dotenv()


def run():
    parser = Parser()  # переводит текст в триплеты
    ontology_path = os.getenv('ONTOL_PATH')
    es_host = os.getenv('ES_HOST')
    # тут должны быть записаны правила, в виде пригодном для сравнения
    ontology = parser.parse_marked_text(ontology_path)
    es_engine = SearchEngine(es_host=es_host, ontology=ontology)

    while True:
        # получаем вопрос
        question = input("введите вопрос: ")
        q_triplets = parser.parse_question(question)
        # формируем ответ
        answer = es_engine.get_answer(q_triplets)
        print(answer)


if __name__ == '__main__':
    run()
