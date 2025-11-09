"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():
    """
    Exibe uma mensagem de boas-vindas ao desafio.
    Retorno esperado: string com a mensagem "Bem-vindo ao Desafio de Git!"
    """
    pass

def listar_comandos_git_basicos():
    """
    Retorna uma lista com os principais comandos básicos do Git.
    Exemplo de saída:
    ["git init", "git add", "git commit", "git status", "git push"]
    """
    return ["git init", "git add", "git commit", "git status", "git push"]


def criar_mensagem_commit(funcao_nome):
    """
    Recebe o nome de uma função e retorna uma mensagem de commit padronizada.
    Exemplo:
    criar_mensagem_commit("listar_comandos_git_basicos") ->
    "Implementa função listar_comandos_git_basicos"
    """
    if not isinstance(funcao_nome, str):
        raise TypeError("funcao_nome deve ser uma string")
    nome = funcao_nome.strip()
    return f"Implementa função {nome}"


def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
    Retorna True se o formato for válido, caso contrário False.
    """
    import re
    if not isinstance(tag, str):
        raise TypeError("A tag deve ser uma string.")

    padrao = r"^v\d+\.\d+$"
    return bool(re.match(padrao, tag))


def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    if not isinstance(funcoes_concluidas, list):
        raise TypeError("O parâmetro deve ser uma lista.")
    if not all(isinstance(f, str) for f in funcoes_concluidas):
        raise ValueError("Todos os itens da lista devem ser strings.")

    relatorio = "Relatorio Final:\n"
    for funcao in funcoes_concluidas:
        relatorio += f"- {funcao}\n"
    return relatorio.strip()
