# To-Do API

API para gerenciamento de tarefas com autenticação e logs estruturados.

## 📋 Estrutura do Projeto

```
├── domain/               # Regras de negócio e entidades
│   └── task.py          # Entidade Task
├── interface/           # Camada de apresentação
│   └── user_controller.py # Controller para manipulação de tarefas
├── usecase/            # Casos de uso da aplicação
│   └── addtask.py     # Caso de uso para adicionar tarefas
├── infra/             # Infraestrutura
│   ├── db/           # Camada de banco de dados
│   │   ├── authenticator.py  # Autenticação do banco
│   │   ├── db.py            # Implementação do banco
│   │   └── repository.py    # Repositório de tarefas
│   └── logging/      # Sistema de logs
│       └── logger.py # Logger estruturado com correlation ID
├── tests/            # Testes da aplicação
│   └── test_lambda_handler.py
└── lambda_handler.py # Ponto de entrada da aplicação
```

## 🚀 Funcionalidades

### Gerenciamento de Tarefas
- Criação de tarefas com nome e descrição
- Identificador único para cada tarefa
- Validações de dados de entrada

### Autenticação
- Sistema de autenticação para acesso ao banco de dados
- Credenciais padrão:
  - Usuário: `admin`
  - Senha: `senha123`
- Validação de credenciais antes de operações no banco

### Logs Estruturados
- Correlation ID único para cada requisição
- Rastreamento completo do fluxo de execução
- Níveis de log (INFO, WARNING, ERROR)
- Timestamp em todas as mensagens
- Contexto detalhado em cada operação

## 🔧 Arquitetura

O projeto segue uma arquitetura limpa (Clean Architecture) com as seguintes camadas:

1. **Domain**: Regras de negócio e entidades
   - Definição da entidade Task
   - Validações de domínio

2. **Use Cases**: Lógica de aplicação
   - Implementação dos casos de uso
   - Orquestração das operações

3. **Interface**: Camada de apresentação
   - Controllers para manipulação de requisições
   - Tratamento de erros
   - Formatação de respostas

4. **Infraestrutura**: Implementações técnicas
   - Sistema de banco de dados
   - Autenticação
   - Logging

## 🔒 Tratamento de Erros

### Tipos de Erro
- 400: Erros de validação (dados inválidos)
- 401: Erros de autenticação
- 500: Erros internos do servidor

### Exemplo de Resposta com Erro
```json
{
    "statusCode": 401,
    "body": {
        "error": "Não foi possível conectar ao banco de dados. Verifique suas credenciais.",
        "correlation_id": "3d065e8b-3f38-4cc9-a222-9c7c6a9b1fd9"
    }
}
```

## 📝 Exemplo de Uso

### Criar uma Nova Tarefa

Request:
```json
{
    "body": {
        "name": "Estudar Python",
        "description": "Aprender mais sobre Python e seus frameworks",
        "db_username": "admin",
        "db_password": "senha123"
    }
}
```

Response:
```json
{
    "statusCode": 200,
    "body": {
        "name": "Estudar Python",
        "description": "Aprender mais sobre Python e seus frameworks",
        "id": 1,
        "correlation_id": "6e2e7c17-fa0a-46b0-87ab-60fa23219c48"
    }
}
```

## 🔍 Logs e Monitoramento

### Exemplo de Log
```
2025-09-06 20:48:33 [6e2e7c17-fa0a-46b0-87ab-60fa23219c48] INFO: Lambda recebeu a requisição
2025-09-06 20:48:33 [6e2e7c17-fa0a-46b0-87ab-60fa23219c48] INFO: Iniciando processamento no Controller
...
```

### Rastreamento de Requisições
Cada requisição recebe um ID único (correlation_id) que permite rastrear todo o fluxo de execução através das diferentes camadas da aplicação.

## 🛠️ Próximos Passos

1. Implementar novas operações:
   - Listar tarefas
   - Atualizar tarefas
   - Excluir tarefas
   - Marcar tarefas como concluídas

2. Melhorias de segurança:
   - Implementar autenticação JWT
   - Adicionar rate limiting
   - Implementar armazenamento seguro de credenciais

3. Melhorias de infraestrutura:
   - Adicionar banco de dados persistente
   - Implementar cache
   - Adicionar métricas de performance

## 👥 Contribuição

Para contribuir com o projeto:
1. Fork o repositório
2. Crie uma branch para sua feature
3. Faça commit das suas alterações
4. Push para a branch
5. Crie um Pull Request
