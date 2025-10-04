import os
import asyncio
import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler

# === CONFIGURAÇÕES (Lidas de Variáveis de Ambiente) ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GROK_API_KEY = os.getenv("GROK_API_KEY")
GROK_MODEL = os.getenv("GROK_MODEL", "grok-4-latest")
GROK_API_URL = "https://api.x.ai/v1/chat/completions"

# Validação de variáveis
if not TELEGRAM_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN não configurado!")
if not GROK_API_KEY:
    raise ValueError("❌ GROK_API_KEY não configurado!")

print("✅ Bot iniciando com configurações carregadas...")

# === Função para conversar com Grok ===
async def chat_grok(message: str) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            payload = {
                "model": GROK_MODEL,
                "messages": [{"role": "user", "content": message}],
                "temperature": 0.7
            }
            headers = {
                "Authorization": f"Bearer {GROK_API_KEY}",
                "Content-Type": "application/json"
            }

            async with session.post(GROK_API_URL, json=payload, headers=headers) as resp:
                if resp.status != 200:
                    error_text = await resp.text()
                    print(f"⚠️ Erro Grok API ({resp.status}): {error_text}")
                    return f"⚠️ Erro na API Grok ({resp.status}). Tente novamente."

                data = await resp.json()
                return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"❌ Exceção em chat_grok: {e}")
        return f"❌ Erro ao processar sua mensagem: {str(e)}"

# === Comandos ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Olá! Eu sou seu bot com Grok IA!*\n\n"
        "Envie qualquer mensagem e responderei com inteligência artificial.\n\n"
        "Comandos disponíveis:\n"
        "/start - Mensagem de boas-vindas\n"
        "/help - Ajuda\n"
        "/status - Status do bot",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *Ajuda do Bot*\n\n"
        "• Envie qualquer texto e receba resposta da IA Grok\n"
        "• Use /status para verificar se estou online\n"
        "• Powered by Grok AI (X.ai)",
        parse_mode="Markdown"
    )

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ *Bot Online!*\n\n"
        f"🤖 Modelo: {GROK_MODEL}\n"
        "🔋 Status: Ativo e pronto para responder!",
        parse_mode="Markdown"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.message.from_user

    print(f"📩 Mensagem de {user.first_name} (@{user.username}): {text}")

    await update.message.chat.send_action("typing")
    response = await chat_grok(text)

    await update.message.reply_text(response)
    print(f"✅ Resposta enviada para {user.first_name}")

# === Inicialização ===
async def main():
    print("🚀 Iniciando bot...")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot rodando! Aguardando mensagens...")
    await app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
