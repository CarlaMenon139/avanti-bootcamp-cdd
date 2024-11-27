# Dicionário de dados para o conjunto de dados de diamantes
dicionario_dados = {
    'price': {
        'descricao': 'Preço do diamante em dólares.',
        'tipo': 'quantitativa',
        'subtipo': 'contínua'
    },
    'carat': {
        'descricao': 'Peso do diamante em quilates.',
        'tipo': 'quantitativa',
        'subtipo': 'contínua'
    },
    'cut': {
        'descricao': 'Qualidade do corte do diamante (Ideal, Premium, Good, Fair, Poor).',
        'tipo': 'qualitativa',
        'subtipo': 'nominal'
    },
    'color': {
        'descricao': 'Cor do diamante, variando de D (melhor) a J (pior).',
        'tipo': 'qualitativa',
        'subtipo': 'ordinal'
    },
    'clarity': {
        'descricao': 'Clareza do diamante (variando de IF a I3).',
        'tipo': 'qualitativa',
        'subtipo': 'ordinal'
    },
    'x': {
        'descricao': 'Comprimento do diamante em milímetros.',
        'tipo': 'quantitativa',
        'subtipo': 'contínua'
    },
    'y': {
        'descricao': 'Largura do diamante em milímetros.',
        'tipo': 'quantitativa',
        'subtipo': 'contínua'
    },
    'z': {
        'descricao': 'Profundidade do diamante em milímetros.',
        'tipo': 'quantitativa',
        'subtipo': 'contínua'
    },
    'depth': {
        'descricao': 'Profundidade total do diamante como uma porcentagem do diâmetro.',
        'tipo': 'quantitativa',
        'subtipo': 'contínua'
    },
    'table': {
        'descricao': 'Largura da mesa do diamante como uma porcentagem do diâmetro.',
        'tipo': 'quantitativa',
        'subtipo': 'contínua'
    }
}

# Exibindo o dicionário
for variavel, info in dicionario_dados.items():
    print(f"Variável: {variavel}\nDescrição: {info['descricao']}\nTipo: {info['tipo']}\nSubtipo: {info['subtipo']}\n")
