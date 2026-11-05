# Criando o catálogo com 2 produtos
catalogo = [
    {
        "produto": "Notebook",
        "preco": 3500.00,
        "em_estoque": True
    },
    {
        "produto": "Mouse",
        "preco": 89.90,
        "em_estoque": False
    }
]

# Percorrendo o catálogo e exibindo os produtos
for item in catalogo:
    print(f"Produto: {item['produto']} | Preço: R$ {item['preco']:.2f}")

Produto: Notebook | Preço: R$ 3500.00
Produto: Mouse | Preço: R$ 89.90
