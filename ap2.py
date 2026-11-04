import random

def classificar_produto(quantidade):
    if quantidade == 0:
        return "Sem estoque"
    elif quantidade <= 5 and quantidade > 0:
        return "Estoque baixo"
    elif quantidade <= 20 and quantidade > 0:
        return "Estoque normal"
    elif quantidade > 20 and quantidade:
        return "Estoque alto"
    elif quantidade < 0: 
        return "Quantidade inválida"

def inverter_texto(texto):
    return (' '.join(texto.split()[::-1])).strip()

def gerar_codigo():
    return f"USR-{random.randint(1000, 9999)}"

def criar_identificacao(nome):
    codigo = gerar_codigo()
    return f"Usuário {nome} cadastrado com código {codigo}."

def verificar_permissao(usuario):
    usuarios_permitidos = ["admin", "carlos", "alan"]
    return usuario in usuarios_permitidos

def acessar_sistema(usuario):
    if verificar_permissao(usuario):
        return "Acesso autorizado"
    else:
        return "Acesso negado"

def obter_proximo_cliente(fila):
    if len(fila) > 0:
        return fila.pop(0)
    return None

def registrar_atendimento(cliente):
    return True

def atender_proximo_cliente():
    cliente = obter_proximo_cliente()
    if not cliente:
        return "Fila vazia"
    if registrar_atendimento(cliente):
        return "Atendimento realizado"
    else:
        return "Falha no atendimento"