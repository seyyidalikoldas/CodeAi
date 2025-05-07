# 🤖 BardChat Discord Bot

Bu proje, Google Bard API'yi kullanarak kullanıcıdan gelen mesajlara cevap veren bir Discord botudur.  
Bot, uzun mesajları akıllıca kısaltır, fazladan boşlukları temizler ve "botu kim yaptı?" gibi sorulara özel cevaplar verir.

---

## 🚀 Özellikler

- 🔍 Google Bard API ile gerçek zamanlı yanıt üretme
- ✂️ Uzun yanıtları noktalama işaretlerine göre akıllıca kısaltma
- 🧹 Yanıtlardaki fazla boşlukları temizleyerek daha düzgün görünüm
- 📩 Bot etiketlendiğinde veya DM'den yazıldığında otomatik yanıt verme
- 👨‍🔧 "Yapımcı kim?" gibi sorulara özel cevap sistemi

---

## ⚙️ Kurulum ve Kullanım

1. **Projeyi klonlayın:**
   ```bash
   git clone https://github.com/seyyidalikoldas/bardchat-discord-bot.git
   cd bardchat-discord-bot
   ```

2. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```
   Gerekli kütüphaneler:
   - `discord.py`
   - `bardapi`

3. **Token bilgilerini girin:**

   `bot.py` dosyasının en üst kısmındaki alanları kendi bilgilerinizle doldurun:
   ```python
   DISCORD_TOKEN = "discord bot tokeninizi buraya girin"
   BARD_TOKEN = "tarayıcınızdaki __Secure-1PSID çerez değeri"
   ```

   > 🔐 **Not:** `BARD_TOKEN`, tarayıcınızdan alınan `__Secure-1PSID` çerezi değeridir.

4. **Botu çalıştırın:**
   ```bash
   python bot.py
   ```

---

## 📁 Dosya Yapısı

```
bardchat-discord-bot/
├── bot.py
├── README.md
├── requirements.txt
```

---

## 🧠 Kullanılan Teknolojiler

- Python  
- discord.py  
- bardapi  
- asyncio  
- re (Regex)

---

## 👨‍💻 Geliştirici

Bu bot **Seyyid Ali Koldaş** tarafından geliştirilmiştir.  
GitHub: [@seyyidalikoldas](https://github.com/seyyidalikoldas)

---

## 📜 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
