from pydantic import BaseModel
from typing import List, Optional, Set


class Entity(BaseModel):
    text: str
    tags: Set[str] = set()

    def __eq__(self, other: 'Entity') -> bool:
        return self.text == other.text and bool(self.tags & other.tags)


class Triplet(BaseModel):
    subject: Entity
    relation: Entity
    object: Entity

    def matches(self, other: 'Triplet') -> bool:
        return (self.subject == other.subject and
                self.relation == other.relation and
                self.object == other.object)
