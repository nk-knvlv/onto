class SearchEngine:
    es_host: str

    def __init__(self, es_host, ontology, ontology_path):
        self.es_host = es_host
        self.ontology = ontology
        self.ontology_path = ontology_path

    def find_matches(self, ontology, question_triplets):
        pass

    def get_answer(self, question) -> str:
        answer = 'Нет информации по запросу'
        if self.can_answer(question):
            with open(self.ontology_path, 'r', encoding='utf-8') as f:
                text = f.read()
                entities = text.split(',')
                if question in entities:
                    answer = 'Утверждение верно'
        return answer

    def can_answer(self) -> bool:
        with open(self.ontology_path, 'r', encoding='utf-8') as f:
            text = f.read()
            if text:
                return True
        return False
