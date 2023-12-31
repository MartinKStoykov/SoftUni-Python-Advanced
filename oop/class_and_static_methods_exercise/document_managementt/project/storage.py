from class_and_static_methods_exercise.document_managementt.project.topic import Topic
from class_and_static_methods_exercise.document_managementt.project.category import Category
from class_and_static_methods_exercise.document_managementt.project.document import Document

class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = next(c for c in self.categories if c.id == category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = next(t for t in self.topics if t.id == topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = next(d for d in self.documents if d.id == document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id: int):
        category = next(c for c in self.categories if c.id == category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = next(t for t in self.topics if t.id == topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = next(d for d in self.documents if d.id == document_id)
        self.documents.remove(document)

    def get_document(self, document_id: int):
        return next(d for d in self.documents if d.id == document_id)

    def __repr__(self):
        return '\n'.join([d.__repr__() for d in self.documents])