# Lista para armazenar as tarefas
tasks = []

# Função para exibição das tarefas
def show_tasks():
    if len(tasks) == 0:
        print("Nenhuma tarefa cadastrada!")
    else:
        print("\nTarefas:")
        for idx, task in enumerate(tasks, 1):
            status = "Concluída" if task['done'] else "Pendente"
            print(f"{idx}. {task['name']} - {status}")


# Função para adicionar uma nova tarefa
def add_task(name):
    task = {
        'name': name,
        'done': False
    }
    tasks.append(task)
    print(f"Tarefa '{name}' adicionada com sucesso!")


# Função para marcar uma tarefa como concluída
def mark_task_done(task_id):
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1]['done'] = True
        print(f"Tarefa {task_id} marcada como concluída!")
    else:
        print("ID de tarefa inválido!")


# Função para excluir uma tarefa
def delete_task(task_id):
    if 0 < task_id <= len(tasks):
        removed_task = tasks.pop(task_id - 1)
        print(f"Tarefa '{removed_task['name']}' excluída!")
    else:
        print("ID de tarefa inválido!")


# Função principal que interage com o usuário
def main():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Exibir Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Marcar Tarefa com Concluída")
        print("4. Excluir Tarefa")
        print("5. Sair")

        try:
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                show_tasks()
            elif choice == 2:
                task_name = input("Digite o nome da tarefa: ")
                add_task(task_name)
            elif choice == 3:
                task_id = int(input("Digite o ID da tarefa para marcar como concluída: "))
                mark_task_done(task_id)
            elif choice == 4:
                task_id = int(input("Digite o ID da tarefa para excluir: "))
                delete_task(task_id)
            elif choice == 5:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")


if __name__ == "__main__":
    main()
        
            