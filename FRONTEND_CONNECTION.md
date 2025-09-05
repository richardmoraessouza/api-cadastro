# Como Conectar Frontend (GitHub Pages) com Backend (Render)

## 🔗 Configuração da Conexão

### 1. **URLs da API**
- **Desenvolvimento local**: `http://localhost:8000`
- **Produção (Render)**: `https://api-cadastro-7.onrender.com`

### 2. **URLs do Frontend**
- **Desenvolvimento local**: `http://localhost:5173`
- **GitHub Pages**: `https://richardmoraessouza.github.io/front-cadastro`

### 3. **Configuração no Frontend**

#### **Para React/Vue/Angular:**
```javascript
// Configuração base
const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? 'https://api-cadastro-7.onrender.com' 
  : 'http://localhost:8000';

// Exemplo de uso
const response = await fetch(`${API_BASE_URL}/api/usuarios/`, {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
  },
});
```

#### **Para Vite (se estiver usando):**
```javascript
// vite.config.js
export default {
  define: {
    'process.env.API_URL': JSON.stringify(
      process.env.NODE_ENV === 'production' 
        ? 'https://api-cadastro-7.onrender.com'
        : 'http://localhost:8000'
    )
  }
}
```

### 3. **Endpoints Disponíveis**

#### **Listar usuários:**
```
GET https://api-cadastro-7.onrender.com/api/usuarios/
```

#### **Criar usuário:**
```
POST https://api-cadastro-7.onrender.com/api/usuarios/
Content-Type: application/json

{
  "nome": "João Silva",
  "email": "joao@email.com",
  "idade": 25
}
```

#### **Página principal (HTML):**
```
GET https://api-cadastro-7.onrender.com/
```

### 4. **CORS Configurado**

✅ **Permitido:**
- `https://*.github.io` (qualquer GitHub Pages)
- `http://localhost:5173` (desenvolvimento)
- `http://127.0.0.1:5173` (desenvolvimento)

### 5. **Testando a Conexão**

#### **Teste simples no navegador:**
```javascript
// Cole no console do navegador
fetch('https://api-cadastro-7.onrender.com/api/usuarios/')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Erro:', error));
```

#### **Teste com curl:**
```bash
curl -X GET https://api-cadastro-7.onrender.com/api/usuarios/
```

### 6. **Possíveis Problemas e Soluções**

#### **Erro CORS:**
- ✅ Já configurado para GitHub Pages
- Se der erro, verifique se a URL do frontend está correta

#### **Erro 404:**
- Verifique se o endpoint está correto
- Teste primeiro no navegador

#### **Erro 500:**
- Pode ser problema de banco de dados
- O fallback SQLite deve resolver automaticamente

### 7. **Deploy no GitHub Pages**

1. **Configure a variável de ambiente:**
   ```bash
   # No seu repositório do frontend
   echo "VITE_API_URL=https://api-cadastro-7.onrender.com" >> .env.production
   ```

2. **Use a variável no código:**
   ```javascript
   const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
   ```

3. **Faça o build e deploy:**
   ```bash
   npm run build
   # Deploy para GitHub Pages
   ```

## 🎯 **Resumo**

- ✅ **Backend**: Configurado e funcionando no Render
- ✅ **CORS**: Configurado para GitHub Pages
- ✅ **Banco**: MySQL com fallback SQLite
- ✅ **Endpoints**: Prontos para uso

**Sua API está pronta para receber conexões do GitHub Pages!** 🚀
