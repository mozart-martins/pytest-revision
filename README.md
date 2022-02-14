# Instalando pytest
pip install pytest
pip install pytest-sugar #plugin que melhora a exibição dos resultados

# Importando o sistema de marcações nos arquivos de teste
from pytest import mark
Uso com o decorator @mark.nome_da_tag
Para rodar o grupo com a tag, basta rodar pytest -m nome_da_tag
Para rodar todos menos os marcados com nome_da_tag, basta utilizar o comando pytest -m "not nome_da_tag"

# Rodando o pytest
pytest

# Status das respostas
. = Passou
F = Falhou
x = Falha esperada
X = Falha esperada que não falhou
s = Pulou (skiped)

# Rodando o pytest no modo verboso
pytest -v

# Rodando somente os testes com  a palavra "foo"
pytest -k "foo"

# Rodando o pytest com as saídas dos prints e do console
pytest -s

# Rodando o pytest no modo debug quando há erros
pytest --pdb

# Repetindo primeiro o que falhar (first to fail)
pytest --ff

# Rodar novamente apenas os que falharam
pytest --lf

# Relatório de teste no formato padrão (Junit)
pytest --junitxml report.xml

# Marcação do tipo skip
@mark.skip("Ainda não foi implementado...")
Para mostrar a mensagem quando rodar o pytest, basta utilizar o comando pytest -rs

# Utilizando várias entradas e saídas com o parametrize
@mark.parametrize(
    'parametro, resultado',
    [("oi", "oi"), ("ola","ola"), ("mozart", "mozart")]
)
def testando(parametro, resultado):
    assert resultado == qualquer_coisa(parametro)

# Quando um teste tem que falhar
@mark.xfail
def test_xfail():
    assert False
Isso vai retornar um x pequeno (falha esperada)


