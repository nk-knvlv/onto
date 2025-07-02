class SearchEngine:
    es_host: str

    def __init__(self, es_host, ontology):
        self.es_host = es_host
        self.ontology = ontology

    def find_matches(self, ontology, question_triplets):
        pass

    def get_answer(self, question) -> str:
        answer = 'Нет информации по запросу'
        if self.can_answer(question):
            with open('/ontology_monorepo/faq.ontol', 'r', encoding='utf-8') as f:
                text = f.read()
                entities = text.split(',')
                if question in entities:
                    answer = 'Утверждение верно'
        return answer

    def can_answer(self, question) -> bool:
        with open('/ontology_monorepo/faq.ontol', 'r', encoding='utf-8') as f:
            text = f.read()
            if text:
                return True
        return False
