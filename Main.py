from database import Database

def menu():
    print("\n1. Criar usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Sair")

def criar_usuario(db):
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    db.insert_usuario(nome, idade)
    print("Usuário criado com sucesso!")

def listar_usuarios(db):
    print("\nLista de Usuários:")
    usuarios = db.get_usuarios()
    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Idade: {usuario[2]}")

def atualizar_usuario(db):
    id = int(input("Digite o ID do usuário que deseja atualizar: "))
    nome = input("Digite o novo nome do usuário: ")
    idade = int(input("Digite a nova idade do usuário: "))
    db.update_usuario(id, nome, idade)
    print("Usuário atualizado com sucesso!")

def deletar_usuario(db):
    id = int(input("Digite o ID do usuário que deseja deletar: "))
    db.delete_usuario(id)
    print("Usuário deletado com sucesso!")

if __name__ == "__main__":
    db = Database(db_name="usuarios.db")

    while True:
        menu()
        opcao = input("\nDigite o número da operação desejada: ")

        if opcao == "1":
            criar_usuario(db)
        elif opcao == "2":
            listar_usuarios(db)
        elif opcao == "3":
            atualizar_usuario(db)
        elif opcao == "4":
            deletar_usuario(db)
        elif opcao == "5":
            db.close()
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
