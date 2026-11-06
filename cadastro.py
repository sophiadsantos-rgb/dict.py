
cadastros = [
    {"nome": "João", "idade": 15, "curso": "Informática"},
    {"nome": "Maria", "idade": 16, "curso": "Administração"}
]

print("Cadastro de aluno")

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
curso = input("Digite o curso: ")

aluno = {
    "nome": nome,
    "idade": idade,
    "curso": curso
}

cadastros.append(aluno)

print("\nLista de alunos:")

for aluno in cadastros:
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Curso:", aluno["curso"])
    print("----------------")
