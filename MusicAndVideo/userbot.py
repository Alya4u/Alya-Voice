import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("🥵")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🏓 PONG</b> `{delta_ping * 1000:.3f} ms` \n<b>⏳ AKTIF</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ Userbot Di Mulai Ulang**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 Hallo {m.from_user.mention}!

🛠 MENU BANTUAN MUSIC PLAYER

⚡ PERINTAH UNTUK SEMUA ORANG
• {HNDLR}play [judul lagu | link youtube | balas file audio] - untuk memutar lagu
• {HNDLR}vplay [judul video | link youtube | balas file video] - untuk memutar video
• {HNDLR}playlist untuk melihat daftar putar
• {HNDLR}ping - untuk cek status
• {HNDLR}id - untuk melihat id pengguna
• {HNDLR}video - judul video | link yt untuk mencari video
• {HNDLR}song - judul lagu | link yt untuk mencari lagu
• {HNDLR}help - untuk melihat daftar perintah

⚡ PERINTAH PLUGINS FUN
• {HNDLR}q - untuk membuat qoute
• {HNDLR}tts - balas ke pesan | untuk membuat suara
• {HNDLR}github - untuk melihat data github
• {HNDLR}truth - untuk seru seruan
• {HNDLR}dare - untuk tantangan


⚡ PERINTAH UNTUK SEMUA ADMIN
• {HNDLR}resume - untuk melanjutkan pemutaran lagu atau video
• {HNDLR}pause - untuk untuk menjeda pemutaran lagu atau video
• {HNDLR}skip - untuk melewati lagu atau video
• {HNDLR}end - untuk mengakhiri pemutaran</b>
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋 Hallo {m.from_user.mention}!

🗃️ Music Dan Video Player UserBot

🔰 Telegram UserBot Untuk Memutar Lagu Dan Video Di Obrolan Suara Telegram.

👩‍💻 Dipersembahkan Oleh 
• [Flicks Support](http://t.me/flicksrobotsupport)


📝 Persyaratan
• Python 3.8+
• FFMPEG
• Nodejs v16+

🛠 MENU BANTUAN MUSIC BOT

⚡ PERINTAH UNTUK SEMUA ORANG
• `{HNDLR}play` [judul lagu | link youtube | balas file audio] - untuk memutar lagu
• `{HNDLR}vplay` [judul video | link youtube | balas file video] - untuk memutar video
• `{HNDLR}playlist` untuk melihat daftar putar
• `{HNDLR}ping` - untuk cek status
• `{HNDLR}id` - untuk melihat id pengguna
• `{HNDLR}video` - judul video | link yt untuk mencari video
• `{HNDLR}song` - judul lagu | link yt untuk mencari lagu
• `{HNDLR}help` - untuk melihat daftar perintah

⚡ PERINTAH PLUGINS FUN
• `{HNDLR}q` - untuk membuat qoute
• `{HNDLR}tts` - balas ke pesan | untuk membuat suara
• `{HNDLR}truth` - untuk seru seruan
• `{HNDLR}github` - untuk melihat data github
• `{HNDLR}dare` - untuk tantangan

⚡ PERINTAH UNTUK SEMUA ADMIN
• `{HNDLR}id` - untuk cek status
• `{HNDLR}resume` - untuk melanjutkan pemutaran lagu atau video
• `{HNDLR}pause` - untuk untuk menjeda pemutaran lagu atau video
• `{HNDLR}skip` - untuk melewati lagu atau video
• `{HNDLR}end` - untuk mengakhiri pemutaran

🦹🏻 Deployment Userbot
💜 Heroku

 [𝗗𝗘𝗣𝗟𝗢𝗬 𝗞𝗘 𝗛𝗘𝗥𝗢𝗞𝗨](https://heroku.com/deploy?template=https://github.com/Alya4u/Alya-Voice)

📝 Variabel Yang Dibutuhkan
• `API_ID` - Dapatkan Dari [my.telegram.org](https://my.telegram.org)
• `API_HASH` - Dapatkan Dari [my.telegram.org](https://my.telegram.org)
• `SESSION` - Sesi String Pyrogram. Dapatkan String Dari [Sini](https://replit.com/@fjgaming212/StringSession#main.py)
• `SUDO_USER` - ID Akun Telegram Yang Digunakan Sebagai Admin
• `HNDLR` - Handler untuk menjalankan userbot mu


❤️‍🔥 KREDIT DEVOLOPER
• [Skyzo](https://github.com/ridho17-ind)
• [Tomi](https://github.com/XtomiSN)</b>
"""
    await m.reply(REPO, disable_web_page_preview=True)
