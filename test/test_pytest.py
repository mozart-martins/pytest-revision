from pytest import mark, fixture
from MeuPacote.Programa import *


def test_meu_primeiro_teste():
    message = "Hello world!" # Given

    response = Programa.view(message) # When

    assert message == response # Then



@mark.texto_para_numero
def test_mensagem_fixa():
    assert 999 == Programa.view("novenovenove")



@mark.parametrize(
    'mensagem, resultado',
    [("oi", "oi"), ("mozart", "mozart"), ("bom dia", "bom dia")]
)
def test_varias_mensagens(mensagem, resultado):
    assert Programa.view(mensagem) == resultado



@mark.xfail
def test_xfail():
    assert False


# Utilizando a fixture instancia_programa do arquivo conftest
def test_nome_do_programa(instancia_programa):
    assert instancia_programa.nome == "Programa Legal"

# Utilizando a fixture instancia_programa_versao_dois do arquivo conftest
def test_versao_dois_programa(instancia_programa_versao_dois):
    assert instancia_programa_versao_dois.versao == 2.0



