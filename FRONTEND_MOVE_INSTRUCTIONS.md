# 📁 Instruções para Mover o Frontend

## ✅ **Configurações já feitas:**

### 1. **API Service (`src/services/api.js`)**
- ✅ Configurado para detectar ambiente automaticamente
- ✅ URLs: `localhost:8000` (dev) e `api-cadastro-7.onrender.com` (prod)
- ✅ Interceptors para debug incluídos

### 2. **Vite Config (`vite.config.js`)**
- ✅ Base configurada para `/front-cadastro/` (GitHub Pages)
- ✅ Proxy configurado para desenvolvimento local
- ✅ Porta 5173 configurada

### 3. **Package.json**
- ✅ Scripts de deploy já configurados
- ✅ Dependências atualizadas

## 🚀 **Quando mover o frontend:**

### **Opção 1: Mover para repositório separado**

1. **Crie um novo repositório** no GitHub
2. **Copie a pasta frontend** para o novo repositório
3. **Configure o GitHub Pages** no novo repositório
4. **Atualize a URL** no `vite.config.js` se necessário

### **Opção 2: Mover para pasta específica**

1. **Crie uma pasta** onde quiser (ex: `C:\projetos\front-cadastro`)
2. **Copie a pasta frontend** para lá
3. **Mantenha as configurações** como estão

## 🔧 **Configurações importantes:**

### **Para desenvolvimento local:**
```bash
cd frontend
npm install
npm run dev
```

### **Para build de produção:**
```bash
cd frontend
npm run build
```

### **Para deploy no GitHub Pages:**
```bash
cd frontend
npm run deploy
```

## 📋 **Checklist ao mover:**

- [ ] Copiar toda a pasta `frontend`
- [ ] Manter o `vite.config.js` com as configurações
- [ ] Manter o `src/services/api.js` configurado
- [ ] Testar localmente com `npm run dev`
- [ ] Testar build com `npm run build`
- [ ] Configurar GitHub Pages se necessário

## 🌐 **URLs finais:**

- **Desenvolvimento**: `http://localhost:5173`
- **GitHub Pages**: `https://richardmoraessouza.github.io/front-cadastro`
- **API**: `https://api-cadastro-7.onrender.com`

## ⚠️ **Importante:**

1. **Não esqueça** de manter as configurações da API
2. **Teste sempre** antes de fazer deploy
3. **Verifique** se o CORS está funcionando
4. **Mantenha** o `base: '/front-cadastro/'` no vite.config.js

## 🎯 **Próximos passos:**

1. **Mova o frontend** para onde quiser
2. **Teste localmente** com `npm run dev`
3. **Configure o GitHub Pages** se necessário
4. **Teste a conexão** com a API

**Tudo está pronto para funcionar!** 🚀
