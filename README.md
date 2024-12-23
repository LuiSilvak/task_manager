# Gerenciador de Tarefas em Python
Este é um simples Gerenciador de Tarefas desenvolvido em Python, onde você pode adicionar, visualizar, marcar como concluída e excluir tarefas. É um ótimo projeto para aprender conceitos básicos de programação como listas, loops e interação com o usuário.

## Funcionalidades
* **Exibir Tarefas:** Visualize todas as tarefas registradas, com seu status (Pendente ou Concluída).
* **Adicionar Tarefa:** Adicione novas tarefas fornecendo um nome.
* **Marcar Tarefa como Concluída:** Marque as tarefas como concluídas pelo seu ID.
* **Excluir Tarefa:** Exclua uma tarefa existente pelo seu ID.
* **Sair:** Encerre o programa.

## Como Executar
Clone o repositório ou baixe o código-fonte:

> bash
```
git clone https://github.com/LuiSilvak/task_manager.git
cd task_manager
```

Certifique-se de ter o Python instalado: O projeto foi desenvolvido utilizando Python 3.x. Para verificar se o Python está instalado, execute:

> bash
```
python --version
```
ou

> bash
```
python3 --version
```

### Execute o programa: 
No terminal, execute o seguinte comando para rodar o gerenciador de tarefas:

> bash
```
python task_manager.py
```

### Estrutura do Projeto

> bash
```
task_manager/
├── task_manager.py    # Arquivo principal do gerenciador de tarefas
└── README.md          # Este arquivo com informações sobre o projeto
```

### Como Funciona
O programa oferece um menu simples no terminal para interagir com o usuário. A partir desse menu, o usuário pode escolher entre as opções para adicionar, exibir, concluir ou excluir tarefas.

#### Exemplo de Execução

> bash
```
--- Gerenciador de Tarefas ---
1. Exibir Tarefas
2. Adicionar Tarefa
3. Marcar Tarefa como Concluída
4. Excluir Tarefa
5. Sair
Escolha uma opção: 2
Digite o nome da tarefa: Estudar Python
Tarefa 'Estudar Python' adicionada com sucesso!
```

> bash
```
--- Gerenciador de Tarefas ---
1. Exibir Tarefas
2. Adicionar Tarefa
3. Marcar Tarefa como Concluída
4. Excluir Tarefa
5. Sair
Escolha uma opção: 1

Tarefas:
1. Estudar Python - Pendente
```

## Melhorias Futuras

1. **Persistência de Dados:** Utilizar arquivos JSON ou banco de dados para salvar as tarefas entre execuções.
2. **Interface Gráfica:** Criar uma interface gráfica utilizando Tkinter ou PyQt.
3. **Prioridade de Tarefas:** Adicionar a funcionalidade de definir prioridades para as tarefas.
4. **Data de Conclusão:** Registrar a data em que as tarefas foram concluídas.

## Contribuições
Contribuições são bem-vindas! Se você tem uma ideia de melhoria ou encontrou um bug, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a MIT License.
