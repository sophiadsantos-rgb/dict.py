turma = [
    {"nome": "Lulu calvo", "idade": 16, "nota": 8.5},
    {"nome": "Fifia", "idade": 15, "nota": 7.0},
    {"nome": "Anilquinha", "idade": 16, "nota": 9.5}
]

print(turma[0]["nome"])
print(turma[2]["nota"])

print("---RELATÓRIO DA TURMA---")
for aluno in turma:
    print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']}")
