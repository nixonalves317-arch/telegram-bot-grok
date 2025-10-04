# 🤖 Telegram Bot com Grok IA

Bot do Telegram integrado com a API Grok AI da X.ai para conversas inteligentes.

## 🚀 Deploy no Glitch.com

### Passo 1: Importar do GitHub
1. Acesse [glitch.com](https://glitch.com)
2. Clique em **New Project** > **Import from GitHub**
3. Cole a URL deste repositório
4. Aguarde a importação

### Passo 2: Configurar Variáveis de Ambiente
1. No Glitch, clique em **Tools** > **Secrets** (cadeado 🔒)
2. Adicione as seguintes variáveis:

```
TELEGRAM_BOT_TOKEN = seu_token_aqui
GROK_API_KEY = sua_chave_grok_aqui
GROK_MODEL = grok-4-latest
```

### Passo 3: Iniciar o Bot
1. O bot iniciará automaticamente
2. Veja os logs no console do Glitch
3. Teste enviando `/start` para seu bot no Telegram

## 📋 Como obter as credenciais

### Token do Telegram
1. Abra o Telegram e procure por `@BotFather`
2. Envie `/newbot` e siga as instruções
3. Copie o token fornecido

### Chave da API Grok
1. Acesse [console.x.ai](https://console.x.ai)
2. Faça login com sua conta X/Twitter
3. Crie uma nova API Key
4. Copie a chave

## 🔧 Comandos Disponíveis

- `/start` - Mensagem de boas-vindas
- `/help` - Ajuda sobre o bot
- `/status` - Verificar status do bot

## 🛠️ Estrutura do Projeto

```
telegram-bot-grok/
├── bot.py              # Código principal do bot
├── requirements.txt    # Dependências Python
├── .env.example       # Exemplo de variáveis de ambiente
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Este arquivo
```

## 🐛 Solução de Problemas

### Bot não responde
- Verifique se as variáveis de ambiente estão configuradas no Glitch
- Veja os logs no console do Glitch para erros
- Teste o token com `https://api.telegram.org/bot<TOKEN>/getMe`

### Erro na API Grok
- Verifique se a chave Grok está válida
- Confirme que tem créditos disponíveis na conta X.ai
- Veja os logs para mensagens de erro específicas

## 📝 Licença

MIT License - Livre para usar e modificar!

---

**Desenvolvido com ❤️ usando Telegram Bot API + Grok AI**
