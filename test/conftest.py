from pytest import fixture
from MeuPacote.Programa import *

@fixture
def instancia_programa():
    return Programa("Programa Legal", 1.0)


@fixture
def instancia_programa_versao_dois(instancia_programa):
    instancia_programa.versao = 2.0
    return instancia_programa