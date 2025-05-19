# Sistema de Gerenciamento de Serviços

Sistema completo para gerenciamento de serviços internos, incluindo controle de tarefas, funcionários e departamentos.

## Funcionalidades

- **Autenticação de Usuários**
  - Login e controle de acesso
  - Níveis de permissão (admin/usuário)

- **Dashboard**
  - Visão geral das tarefas (pendentes, em andamento, concluídas, atrasadas)
  - Gráficos e métricas

- **Gerenciamento de Tarefas**
  - Criação e acompanhamento de tarefas
  - Atribuição a funcionários
  - Acompanhamento de status
  - Comentários e histórico

- **Cadastros**
  - Funcionários
  - Departamentos
  - Tipos de serviço

- **Relatórios**
  - Relatórios personalizados
  - Exportação para PDF/Excel

## Requisitos

- Python 3.8+
- PostgreSQL 12+
- pip (gerenciador de pacotes Python)

## Instalação

1. **Clonar o repositório**
   ```bash
   git clone <url-do-repositório>
   cd app_servicos
   ```

2. **Criar e ativar ambiente virtual**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar banco de dados**
   - Criar um banco de dados PostgreSQL chamado `app_servicos`
   - Executar o script SQL de inicialização:
     ```bash
     psql -U postgres -d app_servicos -f database_schema.sql
     ```

5. **Configurar variáveis de ambiente**
   Criar um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   DB_NAME=app_servicos
   DB_USER=postgres
   DB_PASSWORD=sua_senha
   DB_HOST=localhost
   DB_PORT=5432
   SECRET_KEY=sua_chave_secreta_aqui
   ```

## Executando o Sistema

1. **Modo Desenvolvimento**
   ```bash
   python sistema_servicos.py
   ```

2. **Criar Executável**
   ```bash
   pip install pyinstaller
   pyinstaller --onefile --windowed --name SistemaServicos sistema_servicos.py
   ```
   O executável estará disponível em `dist/SistemaServicos.exe`

## Acesso Inicial

- **Usuário**: admin
- **Senha**: admin123

## Estrutura do Projeto

```
app_servicos/
├── sistema_servicos.py    # Aplicação principal
├── database_schema.sql    # Script SQL do banco de dados
├── requirements.txt       # Dependências do Python
├── .env                  # Variáveis de ambiente
└── README.md             # Documentação
```

## Desenvolvimento

Para contribuir com o desenvolvimento:

1. Crie um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das alterações (`git commit -m 'Adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
