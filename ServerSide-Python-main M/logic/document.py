class Document(object):

    def __init__(self, id_document: int, numero_paginas: int, titulo: str = 'titulo', categoria: str = 'categoria',
                 autor: str = 'autor'):
        self._id_document = id_document
        self._numero_paginas = numero_paginas
        self._titulo = titulo
        self._categoria = categoria
        self._autor = autor

    @property
    def id_document(self) -> int:
        return self._id_document

    @id_document.setter
    def id_doc(self, id_document: int):
        self._id_document = id_document

    @property
    def numero_paginas(self) -> int:

        return self._numero_paginas

    @numero_paginas.setter
    def numero_paginas(self, numero_paginas: int):
        self._numero_paginas = numero_paginas

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self._titulo = titulo

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, categoria: str):
        self._categoria = categoria

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, autor: str):
        self._autor = autor

    def __str__(self):
        return '({0}, {1}, {2})'.format(self.id_document, self.numero_paginas, self.titulo, self.categoria, self.autor)


if __name__ == '__main__':
    doc = Document(id_document=252528, numero_paginas=300, titulo="LOVE ALARM", categoria="Love", autor="Paulina")
    doc.autor = "Antonio Ruble"
    print(doc)
