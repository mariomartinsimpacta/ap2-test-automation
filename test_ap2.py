from ap2 import classificar_produto, inverter_texto, criar_identificacao, acessar_sistema, atender_proximo_cliente
from unittest.mock import patch


def test_classificar_produto_zero():
    quantidade = 0 
    resultado = classificar_produto(quantidade)
    assert resultado == "Sem estoque"

def test_classificar_produto_1_5():
    quantidade = 3
    resultado = classificar_produto(quantidade)
    assert resultado == "Estoque baixo"

def test_classificar_produto_6_20():
    quantidade = 11
    resultado = classificar_produto(quantidade)
    assert resultado == "Estoque normal"

def test_classificar_produto_acima_20():
    quantidade = 25
    resultado = classificar_produto(quantidade)
    assert resultado == "Estoque alto"

def test_classificar_produto_negativo():
    quantidade = -300
    resultado = classificar_produto(quantidade)
    assert resultado == "Quantidade inválida"

def test_inverter_palavras_varias_palavras():
    texto = "Cachorro anda e come frango"
    resultado = inverter_texto(texto)
    assert resultado == "frango come e anda Cachorro"

def test_inverter_palavras_uma_palavra():
    texto = "Alan"
    resultado = inverter_texto(texto)
    assert resultado == "Alan"

def test_inverter_palavras_vazio():
    texto = ""
    resultado = inverter_texto(texto)
    assert resultado == ""

def test_inverter_palavras_espacos_extras():
    texto = "Eu              jogo bola"
    resultado = inverter_texto(texto)
    assert resultado == "bola jogo Eu"    

def test_inverter_palavras_varias_palavras_numeros():
    texto = "minha senha é 123123"
    resultado = inverter_texto(texto)
    assert resultado == "123123 é senha minha"

# ---------- Exercício 4 ----------
@patch("ap2.gerar_codigo")
def test_criar_identificacao_mensagem(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-1234"
    resultado = criar_identificacao("Carlos")
    assert resultado == "Usuário Carlos cadastrado com código USR-1234."

@patch("ap2.gerar_codigo")
def test_criar_identificacao_chamou_gerar_codigo(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-1234"
    criar_identificacao("Carlos")
    mock_gerar_codigo.assert_called()

@patch("ap2.gerar_codigo")
def test_criar_identificacao_chamada_uma_vez(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-1234"
    criar_identificacao("Carlos")
    mock_gerar_codigo.assert_called_once()

@patch("ap2.gerar_codigo")
def test_criar_identificacao_codigos_diferentes(mock_gerar_codigo):
    mock_gerar_codigo.side_effect = ["USR-1111", "USR-2222"]
    resultado1 = criar_identificacao("Carlos")
    resultado2 = criar_identificacao("Carlos")
    assert resultado1 == "Usuário Carlos cadastrado com código USR-1111."
    assert resultado2 == "Usuário Carlos cadastrado com código USR-2222."

@patch("ap2.gerar_codigo")
def test_criar_identificacao_nomes_diferentes(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-9999"
    resultado1 = criar_identificacao("Alan")
    resultado2 = criar_identificacao("Maria")
    assert resultado1 == "Usuário Alan cadastrado com código USR-9999."
    assert resultado2 == "Usuário Maria cadastrado com código USR-9999."


# ---------- Exercício 5 ----------
@patch("ap2.verificar_permissao")
def test_acessar_sistema_com_permissao(mock_verificar_permissao):
    mock_verificar_permissao.return_value = True
    resultado = acessar_sistema("Alan")
    assert resultado == "Acesso autorizado"

@patch("ap2.verificar_permissao")
def test_acessar_sistema_sem_permissao(mock_verificar_permissao):
    mock_verificar_permissao.return_value = False
    resultado = acessar_sistema("Visitante")
    assert resultado == "Acesso negado"

@patch("ap2.verificar_permissao")
def test_acessar_sistema_chamou_verificar_permissao(mock_verificar_permissao):
    mock_verificar_permissao.return_value = True
    acessar_sistema("Alan")
    mock_verificar_permissao.assert_called()

@patch("ap2.verificar_permissao")
def test_acessar_sistema_usuario_correto(mock_verificar_permissao):
    mock_verificar_permissao.return_value = True
    acessar_sistema("Alan")
    mock_verificar_permissao.assert_called_with("Alan")

@patch("ap2.verificar_permissao")
def test_acessar_sistema_dois_cenarios(mock_verificar_permissao):
    mock_verificar_permissao.side_effect = [True, False]
    resultado1 = acessar_sistema("Alan")
    resultado2 = acessar_sistema("Visitante")
    assert resultado1 == "Acesso autorizado"
    assert resultado2 == "Acesso negado"


# ---------- Exercício 6 ----------
@patch("ap2.registrar_atendimento")
@patch("ap2.obter_proximo_cliente")
def test_atender_proximo_cliente_sucesso(mock_obter, mock_registrar):
    mock_obter.return_value = "Ana"
    mock_registrar.return_value = True
    resultado = atender_proximo_cliente()
    assert resultado == "Atendimento realizado"

@patch("ap2.registrar_atendimento")
@patch("ap2.obter_proximo_cliente")
def test_atender_proximo_cliente_fila_vazia(mock_obter, mock_registrar):
    mock_obter.return_value = None
    resultado = atender_proximo_cliente()
    assert resultado == "Fila vazia"

@patch("ap2.registrar_atendimento")
@patch("ap2.obter_proximo_cliente")
def test_atender_proximo_cliente_falha(mock_obter, mock_registrar):
    mock_obter.return_value = "Ana"
    mock_registrar.return_value = False
    resultado = atender_proximo_cliente()
    assert resultado == "Falha no atendimento"

@patch("ap2.registrar_atendimento")
@patch("ap2.obter_proximo_cliente")
def test_atender_proximo_cliente_chamou_obter(mock_obter, mock_registrar):
    mock_obter.return_value = "Ana"
    mock_registrar.return_value = True
    atender_proximo_cliente()
    mock_obter.assert_called_once()

@patch("ap2.registrar_atendimento")
@patch("ap2.obter_proximo_cliente")
def test_atender_proximo_cliente_registrar_cliente_correto(mock_obter, mock_registrar):
    mock_obter.return_value = "Bruno"
    mock_registrar.return_value = True
    atender_proximo_cliente()
    mock_registrar.assert_called_once_with("Bruno")

@patch("ap2.registrar_atendimento")
@patch("ap2.obter_proximo_cliente")
def test_atender_proximo_cliente_nao_registra_fila_vazia(mock_obter, mock_registrar):
    mock_obter.return_value = None
    atender_proximo_cliente()
    mock_registrar.assert_not_called()