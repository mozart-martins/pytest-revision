# Instalando pytest

pip install pytest

pip install pytest-sugar #plugin que melhora a exibição dos resultados

  

# Importando o sistema de marcações nos arquivos de teste

from pytest import mark

Uso com o decorator @mark.nome_da_tag

Para rodar o grupo com a tag, basta rodar pytest -m nome_da_tag

Para rodar todos menos os marcados com nome_da_tag, basta utilizar o comando pytest -m "not nome_da_tag"

  

# Rodando o pytest

> pytest

*Lembrando que todos os arquivos e funções de teste devem começar com a palavra test_


# Status das respostas

. = Passou

F = Falhou

x = Falha esperada

X = Falha esperada que não falhou

s = Pulou (skiped)

  

# Rodando o pytest no modo verboso

> pytest -v

  

# Rodando somente os testes com a palavra "foo" no identificador

> pytest -k "foo"

  

# Rodando o pytest com as saídas dos prints e do console

> pytest -s

  

# Rodando o pytest no modo debug quando há erros

> pytest --pdb

  

# Repetindo primeiro o que falhar (first to fail)

> pytest --ff

  

# Rodar novamente apenas os que falharam

> pytest --lf

  

# Relatório de teste no formato padrão (Junit)

> pytest --junitxml report.xml

  

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

# Falha com condição

Espera-se que falhe no Windows:

    @mark.xfail(sys.platform == "win32")
    def test_xfail():
    	assert False

Ou, pode se pedir para dar skip quando for Windows ou outra condição:

    @mark.skipif(sys.platform == "win32")
    def test_skipif():
	    assert False

# Para descobrir as fixtures disponíveis

    pytest --fixtures

# Importando Fixtures

> from pytest import fixtures

# Fixture simples de exemplo

    @fixture(scope='function')
    def veiculo():
	    return Veiculo()

    def test_veiculo_eh_novo(veiculo):
	    assert veiculo.situacao == 'Novo'

# Scopos de uma fixture

 - Function;
 - Class;
 - Module;
 - Package; e
 - Session.

# Fixtures compostas

    @fixture
    def  instancia_programa():
    	return Programa("Programa Legal", 1.0)
    
    def  test_nome_do_programa(instancia_programa):
    	assert instancia_programa.nome ==  "Programa Legal"
    
    @fixture
    def  instancia_programa_versao_dois(instancia_programa):
    	instancia_programa.versao =  2.0
    	return instancia_programa
    
    def  test_versao_dois_programa(instancia_programa_versao_dois):
    	assert instancia_programa_versao_dois.versao ==  2.0

# Criando dados aleatórios

    from fake import Fake
    
    fake = Fake()
    
    @fixture
    def cartao():
	    return Cartao(nome=fake.pystr())

# Arquivo conftest.py

Serve para colocar itens de configuração como as fixtures.
