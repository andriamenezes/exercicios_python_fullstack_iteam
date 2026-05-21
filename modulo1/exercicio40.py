# Exercício 40 – Sistema de Cadastro de Alunos
# Desafio Final – Módulo 1

import json
from datetime import datetime

ARQUIVO     = "alunos.json"
RELATORIO   = "relatorio_turma.json"


# ─────────────────────────────────────────
#  Helpers internos
# ─────────────────────────────────────────

def _ler() -> list[dict]:
    """Lê o arquivo de alunos. Retorna lista vazia se não existir."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _salvar(alunos: list[dict]) -> None:
    """Salva a lista de alunos no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=2, ensure_ascii=False)


def _media(notas: list[float]) -> float:
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas) if notas else 0.0


def _fmt(valor: float) -> str:
    """Formata um número no padrão brasileiro."""
    return f"{valor:_.2f}".replace(".", ",").replace("_", ".")


# ─────────────────────────────────────────
#  Funções principais
# ─────────────────────────────────────────

def cadastrar_aluno(nome: str, email: str, idade: int, notas: list[float]) -> dict:
    """Cadastra um novo aluno e persiste no arquivo JSON.

    Args:
        nome (str): Nome completo do aluno.
        email (str): Email do aluno.
        idade (int): Idade do aluno.
        notas (list[float]): Lista de notas do aluno.

    Returns:
        dict: Dicionário com os dados do aluno cadastrado.
    """
    alunos     = _ler()
    novo_id    = (max(a["id"] for a in alunos) + 1) if alunos else 1

    aluno = {
        "id":           novo_id,
        "nome":         nome.strip().title(),
        "email":        email.strip().lower(),
        "idade":        idade,
        "notas":        notas,
        "media":        round(_media(notas), 2),
        "ativo":        True,
        "cadastrado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    alunos.append(aluno)
    _salvar(alunos)
    return aluno


def listar_alunos() -> list[dict]:
    """Retorna todos os alunos cadastrados.

    Returns:
        list[dict]: Lista de alunos.
    """
    return _ler()


def buscar_por_nome(nome: str) -> dict | None:
    """Busca um aluno pelo nome (case-insensitive).

    Args:
        nome (str): Nome ou parte do nome a buscar.

    Returns:
        dict | None: Dados do aluno encontrado, ou None.
    """
    for aluno in _ler():
        if nome.lower() in aluno["nome"].lower():
            return aluno
    return None


def calcular_media_turma() -> float:
    """Calcula a média geral de todos os alunos ativos.

    Returns:
        float: Média geral da turma.
    """
    alunos = [a for a in _ler() if a["ativo"]]
    if not alunos:
        return 0.0
    return round(sum(a["media"] for a in alunos) / len(alunos), 2)


def exportar_relatorio() -> None:
    """Gera o arquivo relatorio_turma.json com resumo da turma.

    O relatório inclui: total de alunos, média geral,
    aluno com maior média e aluno com menor média.
    """
    alunos = [a for a in _ler() if a["ativo"]]

    if not alunos:
        print("Nenhum aluno cadastrado para gerar relatório.")
        return

    melhor = max(alunos, key=lambda a: a["media"])
    pior   = min(alunos, key=lambda a: a["media"])

    relatorio = {
        "gerado_em":       datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_alunos":    len(alunos),
        "media_geral":     calcular_media_turma(),
        "maior_media":     {"nome": melhor["nome"], "media": melhor["media"]},
        "menor_media":     {"nome": pior["nome"],   "media": pior["media"]},
    }

    with open(RELATORIO, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=2, ensure_ascii=False)

    print(f"Relatório exportado para '{RELATORIO}'.")


# ─────────────────────────────────────────
#  Demonstração
# ─────────────────────────────────────────

print("=" * 45)
print("   SISTEMA DE CADASTRO DE ALUNOS")
print("=" * 45)

# 1. Cadastrar 4 alunos
print("\n--- CADASTRANDO ALUNOS ---")
cadastrar_aluno("Ana Lima",       "ana@email.com",    22, [8.5, 9.0, 7.5])
cadastrar_aluno("carlos MELO",    "carlos@email.com", 25, [6.0, 7.0, 5.5])
cadastrar_aluno("Bia Souza",      "bia@email.com",    20, [9.5, 10.0, 9.0])
cadastrar_aluno("PEDRO Henrique", "pedro@email.com",  23, [7.0, 6.5, 8.0])
print("4 alunos cadastrados com sucesso.")

# 2. Listar
print("\n--- LISTA DE ALUNOS ---")
print(f"{'ID':<4} {'Nome':<18} {'Email':<22} {'Idade':>5} {'Media':>6}")
print("-" * 57)
for a in listar_alunos():
    print(f"{a['id']:<4} {a['nome']:<18} {a['email']:<22} {a['idade']:>5} {a['media']:>6.2f}")

# 3. Buscar
print("\n--- BUSCAR ALUNO ---")
resultado = buscar_por_nome("bia")
if resultado:
    print(f"Encontrado: {resultado['nome']} | Media: {resultado['media']:.2f} | Email: {resultado['email']}")
else:
    print("Aluno não encontrado.")

# 4. Média da turma
print("\n--- MEDIA DA TURMA ---")
print(f"Media geral: {calcular_media_turma():.2f}")

# 5. Exportar relatório
print("\n--- RELATORIO ---")
exportar_relatorio()

with open(RELATORIO, "r", encoding="utf-8") as f:
    rel = json.load(f)

print(f"Total de alunos : {rel['total_alunos']}")
print(f"Media geral     : {rel['media_geral']:.2f}")
print(f"Maior media     : {rel['maior_media']['nome']} ({rel['maior_media']['media']:.2f})")
print(f"Menor media     : {rel['menor_media']['nome']} ({rel['menor_media']['media']:.2f})")
print("=" * 45)