class Programa:

    def __init__(self, nome, versao):
        self._nome = nome
        self._versao = versao

    def view(message):
        if message == 'novenovenove':
            return 999
        return message

    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, nome):
        self._nome = nome


    @property
    def versao(self):
        return self._versao

    @versao.setter
    def versao(self, versao):
        self._versao = versao

    