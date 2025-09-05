# 🚀 Configuração do GitHub Pages para front-cadastro

## 📋 Pré-requisitos

- ✅ Repositório [front-cadastro](https://github.com/richardmoraessouza/front-cadastro) no GitHub
- ✅ Backend Django rodando no Render
- ✅ Código React pronto para deploy

## 🔧 Passo a Passo

### 1. **Configurar o Frontend para Produção**

#### **A. Atualizar a URL da API**

No seu projeto React, crie um arquivo `.env.production`:

```bash
# .env.production
VITE_API_URL=https://api-cadastro-7.onrender.com
```

#### **B. Configurar o vite.config.js**

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/front-cadastro/', // Importante para GitHub Pages
  define: {
    'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV || 'development')
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false
      }
    }
  }
})
```

#### **C. Atualizar o serviço da API**

```javascript
// src/services/api.js
const API_URLS = {
  development: 'http://localhost:8000',
  production: 'https://api-cadastro-7.onrender.com'
};

const isProduction = import.meta.env.PROD || 
                    window.location.hostname.includes('github.io');

export const API_BASE_URL = isProduction ? API_URLS.production : API_URLS.development;
```

### 2. **Configurar GitHub Pages**

#### **A. Ativar GitHub Pages**

1. Vá para o repositório [front-cadastro](https://github.com/richardmoraessouza/front-cadastro)
2. Clique em **Settings**
3. Role até **Pages** no menu lateral
4. Em **Source**, selecione **GitHub Actions**

#### **B. Criar GitHub Action**

Crie o arquivo `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@v3
      
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
        
    - name: Install dependencies
      run: npm ci
      
    - name: Build
      run: npm run build
      env:
        VITE_API_URL: https://api-cadastro-7.onrender.com
        
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      if: github.ref == 'refs/heads/main'
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./dist
```

### 3. **Configurar o Build**

#### **A. Atualizar package.json**

```json
{
  "name": "front-cadastro",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.6.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@vitejs/plugin-react": "^4.2.1",
    "eslint": "^8.55.0",
    "eslint-plugin-react": "^7.33.2",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "vite": "^5.0.8"
  }
}
```

### 4. **Deploy**

#### **A. Fazer commit e push**

```bash
git add .
git commit -m "Configure for GitHub Pages deployment"
git push origin main
```

#### **B. Verificar o deploy**

1. Vá para a aba **Actions** do seu repositório
2. Aguarde o workflow completar
3. Acesse: `https://richardmoraessouza.github.io/front-cadastro`

### 5. **Testar a Conexão**

#### **A. Verificar se a API está funcionando**

```bash
curl https://api-cadastro-7.onrender.com/api/usuarios/
```

#### **B. Testar no navegador**

Abra o console do navegador e execute:

```javascript
fetch('https://api-cadastro-7.onrender.com/api/usuarios/')
  .then(response => response.json())
  .then(data => console.log('API funcionando:', data))
  .catch(error => console.error('Erro:', error));
```

## 🔍 Troubleshooting

### **Erro CORS**
- ✅ Já configurado no backend para `richardmoraessouza.github.io`
- Se der erro, verifique se a URL está correta

### **Erro 404 no GitHub Pages**
- Verifique se o `base: '/front-cadastro/'` está no vite.config.js
- Confirme se o build foi feito corretamente

### **API não conecta**
- Verifique se o backend está rodando no Render
- Teste a URL da API diretamente no navegador

## 📱 URLs Finais

- **Frontend**: `https://richardmoraessouza.github.io/front-cadastro`
- **Backend**: `https://api-cadastro-7.onrender.com`
- **API**: `https://api-cadastro-7.onrender.com/api/usuarios/`

## 🎯 Próximos Passos

1. **Configure o GitHub Pages** seguindo os passos acima
2. **Teste a conexão** entre frontend e backend
3. **Faça ajustes** se necessário
4. **Compartilhe** o link do seu projeto!

**Seu sistema estará 100% funcional no GitHub Pages!** 🚀
