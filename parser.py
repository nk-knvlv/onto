import re


class Parser:

    @staticmethod
    def parse_marked_text(text_path: str) -> dict:
        with open(text_path, 'w') as mt:
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
