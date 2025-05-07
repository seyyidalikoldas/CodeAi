import discord
from discord.ext import commands
from bardapi import Bard
import re
import os
import asyncio

# Ayarlar
DISCORD_TOKEN = ""
BARD_TOKEN = ""  # __Secure-1PSID değeri
MAX_LENGTH = 500  # 100 karakter sınırı 
CREATOR = "Kingsama"  # Yapımcı bilgisi


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

def smart_truncate(text, max_length=MAX_LENGTH):
    """Akıllı metin kısaltma fonksiyonu"""
    if len(text) <= max_length:
        return text
    
    # Noktalama işaretlerine göre kes
    last_punct = max(
        text.rfind(". ", 0, max_length),
        text.rfind("! ", 0, max_length),
        text.rfind("? ", 0, max_length),
        text.rfind("\n", 0, max_length),
        text.rfind(", ", 0, max_length)
    )
    
    truncated = text[:last_punct+1] if last_punct > 0 else text[:max_length]
    
    #if len(truncated) < len(text):
        #truncated += "\n\n[⚠️ Mesaj uzunluğu sınırı nedeniyle kısaltıldı]"
    
    return truncated

@bot.event
async def on_ready():
    print(f'✅ {bot.user.name} botu aktif!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Etiketlenme kontrolü (hem @mention hem de direkt mesaj)
    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        try:
            # Kullanıcı mesajını temizle
            clean_input = message.content.replace(f'<@{bot.user.id}>', '').strip()
            
            # Bard API'ye bağlan
            bard = Bard(token=BARD_TOKEN)
            response = bard.get_answer(clean_input)['content']
            
            # Formatlama ve kısaltma
            response = re.sub(r'\s+', ' ', response)  # Fazla boşlukları temizle
            final_response = smart_truncate(response)
            
            await message.reply(final_response)
            
        except Exception as e:
            error_msg = f"⚠️ Hata oluştu: {str(e)}"[:500]
            await message.reply(error_msg)
            print(f"BOT HATASI: {e}")

    await bot.process_commands(message)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Kingsama yapım kontrolü (sadece direkt sorulduğunda)
    if any(q in message.content.lower() for q in [
        "bu botu kim yaptı", 
        "bu botu yapan kim",
        "botu kim geliştirdi",
        "creator kim",
        "yapımcı kim"
    ]):
        await message.reply("🔧 Bu bot Kingsama tarafından geliştirildi.")
        return

    # Orijinal mesaj işleme kodu (değişmedi)
    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        try:
            clean_input = message.content.replace(f'<@{bot.user.id}>', '').strip()
            
            bard = Bard(token=BARD_TOKEN)
            response = bard.get_answer(clean_input)['content']
            
            response = re.sub(r'\s+', ' ', response)
            final_response = smart_truncate(response)
            
            await message.reply(final_response)
            
        except Exception as e:
            error_msg = f"⚠️ Hata oluştu: {str(e)}"[:500]
            await message.reply(error_msg)
            print(f"BOT HATASI: {e}")

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)