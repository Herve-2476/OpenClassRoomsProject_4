from tinydb import TinyDB


class Models(TinyDB):
    def __init__(self):
        super().__init__("db.json")

    def load_all(self, table):
        return table.all()

    def insert(self, table, data):
        return table.insert(data)

    def get_id(self, table, id):
        return table.get(doc_id=id)

    def update_id(self, table, id, table_object):
        return table.update(table_object, doc_ids=[id])

    def save(self):
        pass
