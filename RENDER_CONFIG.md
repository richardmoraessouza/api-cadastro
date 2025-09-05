# Configuração para Deploy no Render

## 🚀 SISTEMA INTELIGENTE DE BANCO DE DADOS

A aplicação agora tem **fallback automático**:

1. **Tenta MySQL primeiro** - Se configurado e funcionando
2. **Fallback para SQLite** - Se MySQL der erro (automático!)
3. **Desenvolvimento local** - Usa MySQL local normalmente

### Como funciona:
- ✅ **MySQL funcionando** → Usa MySQL
- ❌ **MySQL com erro** → Troca automaticamente para SQLite
- 🔄 **Transparente** → Você não precisa fazer nada!

## Variáveis de Ambiente (Opcionais)

### Para usar MySQL no Render (Recomendado):
```
DB_NAME=nome_do_banco_mysql
DB_USER=usuario_mysql
DB_PASSWORD=senha_mysql
DB_HOST=host_mysql
DB_PORT=3306
```

### Variáveis Obrigatórias:
```
DEBUG=False
SECRET_KEY=sua_chave_secreta_super_segura
```

## Como Configurar no Render

1. **Criar um banco MySQL no Render:**
   - Vá para "Databases" no painel do Render
   - Clique em "New Database"
   - Escolha "MySQL"
   - Configure nome, usuário e senha

2. **Configurar as variáveis de ambiente:**
   - Acesse o painel do Render
   - Vá para o seu serviço
   - Clique em "Environment"
   - Adicione as variáveis de ambiente listadas acima

## Banco de Dados

- **Produção (Render)**: MySQL
- **Desenvolvimento local**: MySQL

## Migrações

Após configurar o banco, execute as migrações:
```bash
python manage.py migrate
```

## Exemplo de Configuração no Render

Se você criou um banco MySQL chamado "api_cadastro" no Render, configure:

```
DB_NAME=api_cadastro
DB_USER=usuario_do_banco
DB_PASSWORD=senha_do_banco
DB_HOST=host_do_render_mysql
DB_PORT=3306
DEBUG=False
SECRET_KEY=sua_chave_secreta_aqui
```
