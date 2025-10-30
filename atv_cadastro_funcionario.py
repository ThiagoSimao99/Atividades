'''lista de funcionários, adicionar funcionários a esta lista, listar funcionários, 
buscar funcionários por nome e calcular média salarial'''

def adicionar_funcionario(lista_funcionarios):
    nome = str(input('Digite o nome do funcionário: '))
    
    try:
        salario = float(input('Digite o salário: '))
    except ValueError:
        print('Erro: Salário inválido. Tente novamente.')
        return
    novo_funcionario = {
        'Nome': nome,
        'Salario': salario
    }
    
    lista_funcionarios.append(novo_funcionario)
    
    print(f"Funcionário {nome} adicionado com sucesso!")

def listar_funcionarios(lista_funcionarios):
    if not lista_funcionarios: 
        print("Nenhum funcionário cadastrado ainda.")
        return 
    
    for indice, funcionario in enumerate(lista_funcionarios, start = 1):
        nome = funcionario['Nome']
        salario = funcionario['Salario']
        
        print(f"  ID: {indice} | Nome: {nome} | Salário: R$ {salario:.2f}")
        
def buscar_funcionario(lista_funcionarios):
    nome_busca = input("Digite o nome do funcionário que deseja buscar: ").strip().lower()

    encontrou_funcionario = False 

    for funcionario in lista_funcionarios:
        if funcionario['Nome'].lower() == nome_busca:
            
            print("Funcionário encontrado:")
            salario_formatado = f"R$ {funcionario['Salario']:.2f}"
            print(f"   Nome: {funcionario['Nome']} | Salário: {salario_formatado}")
            
            encontrou_funcionario = True
            break 

    if not encontrou_funcionario:
        print(f"Nenhum funcionário com o nome '{nome_busca}' foi encontrado.")
        
def calcular_medial_salarial(lista_funcionarios):
    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado. Não é possível calcular a média.")
        return 

    
    soma_total = 0.0

    for funcionario in lista_funcionarios:
        soma_total += funcionario['Salario'] 

    quantidade_funcionarios = len(lista_funcionarios)
    media_salarial = soma_total / quantidade_funcionarios
    
    print(f"Total de funcionários: {quantidade_funcionarios}")
    print(f"Soma de todos os salários: R$ {soma_total:.2f}")
    print(f"Média Salarial: R$ {media_salarial:.2f}")
    
lista_funcionarios = []

#listar_funcionarios(lista_funcionarios)

#calcular_medial_salarial(lista_funcionarios)

#adicionar_funcionario(lista_funcionarios)
#adicionar_funcionario(lista_funcionarios)
#adicionar_funcionario(lista_funcionarios)

#listar_funcionarios(lista_funcionarios)
#calcular_medial_salarial(lista_funcionarios)

#buscar_funcionario(lista_funcionarios)

#adicionar_funcionario(lista_funcionarios)
#listar_funcionarios(lista_funcionarios)
#buscar_funcionario(lista_funcionarios)

#adicionar_funcionario(lista_funcionarios)
#adicionar_funcionario(lista_funcionarios)


#listar_funcionarios(lista_funcionarios)
