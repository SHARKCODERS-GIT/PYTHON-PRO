import requests

def gestor_de_tarefas():
    url_base = "https://jsonplaceholder.typicode.com/todos"

    while True:
        print("\nGestor de Tarefas:")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                response = requests.get(url_base)
                response.raise_for_status()
                tarefas = response.json()

                # Exemplo de dados retornados pela API:
                # [
                #     {"userId": 1, "id": 1, "title": "Tarefa exemplo", "completed": false},
                #     {"userId": 1, "id": 2, "title": "Outra tarefa", "completed": true}
                # ]

                print("\nTarefas:")
                for tarefa in tarefas[:10]:  # Limitando a 10 tarefas para não sobrecarregar o terminal
                    status = "Concluída" if tarefa["completed"] else "Pendente"
                    print(f"ID: {tarefa['id']} | Título: {tarefa['title']} | Status: {status}")

            except requests.RequestException as e:
                print(f"Erro ao obter tarefas: {e}")

        elif opcao == "2":
            titulo = input("Digite o título da nova tarefa: ")
            nova_tarefa = {"userId": 1, "title": titulo, "completed": False}
            try:
                response = requests.post(url_base, json=nova_tarefa)
                response.raise_for_status()
                print(f"Tarefa adicionada com sucesso: {response.json()}")
            except requests.RequestException as e:
                print(f"Erro ao adicionar tarefa: {e}")

        elif opcao == "3":
            id_tarefa = input("Digite o ID da tarefa a remover: ")
            try:
                response = requests.delete(f"{url_base}/{id_tarefa}")
                if response.status_code == 200:
                    print("Tarefa removida com sucesso!")
                else:
                    print("Erro ao remover tarefa.")
            except requests.RequestException as e:
                print(f"Erro ao remover tarefa: {e}")

        elif opcao == "4":
            break

        else:
            print("Opção inválida.")

gestor_de_tarefas()
