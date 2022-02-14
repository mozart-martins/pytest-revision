from pytest import mark
from Programa import Programa

def test_meu_primeiro_teste():
    message = "Hello world!" # Given

    response = Programa.hello_world(message) # When

    assert message == response # Then


@mark.texto_para_numero
def test_mensagem_fixa():
    assert 999 == Programa.hello_world("novenovenove")


@mark.parametrize(
    'mensagem, resultado',
    [("oi", "oi"), ("mozart", "mozart"), ("bom dia", "bom dia")]
)
def test_varias_mensagens(mensagem, resultado):
    assert Programa.hello_world(mensagem) == resultado