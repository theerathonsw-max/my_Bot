# ชื่อไฟล์: main.py
import discord
from discord.ext import commands
from flask import Flask, render_template_string, request
import threading
import os
import json
import asyncio
import time
import random

# 📊 1. คลังเก็บสถิติรวมของระบบบอท (จากโค้ดเดิมของคุณ)
stats = {
    "total_runs": 0, "success_runs": 0, "failed_runs": 0,
    "platorelay_runs": 0, "global_runs": 0,
    "last_reset": time.strftime("%Y-%m-%d %H:%M:%S"),
    "recent_logs": []
}

app = Flask(__name__)
COOKIES_DIR = "bot_sessions"
if not os.path.exists(COOKIES_DIR): os.makedirs(COOKIES_DIR)

@app.route('/')
def home():
    return "<h1>📊 Bot Dashboard & Discord Bot Are Running Successfully!</h1>"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# 🤖 2. แกนหลักบอทสแลชคอมมานด์ (Slash Commands Setup)
class EpicMegaBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="/", intents=intents)

async def setup_hook(self):
        # โซนโหลด Cogs อัตโนมัติ (สามารถแตกไฟล์เพิ่มได้ถึง 200 ระบบ)
        if not os.path.exists('./cogs'):
            os.makedirs('./cogs')
        
        # ⚠️ เติมส่วนลูปสแกนและโหลดไฟล์ Cogs ตรงนี้เข้าไปด้วยครับ:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f"📦 Loaded Cog: {filename}")

    async def on_ready(self):
        print(f"🟢 {self.user.name} ออนไลน์และพร้อมใช้งานแล้ว!")
        # 🔄 พอบอทออนจะรีคำสั่งสแลชทั้งหมดทันทีทั่วโลก
        try:
            synced = await self.tree.sync()
            print(f"🔄 รีเฟรชและ Sync คำสั่งสำเร็จ! (รวมทั้งหมด {len(synced)} คำสั่ง)")
        except Exception as e:
            print(f"❌ รีคำสั่งล้มเหลว: {e}")

bot = EpicMegaBot()

def init_dbs():
    # สร้างไฟล์เก็บข้อมูลหากยังไม่มี
    for db in ["config.json", "database.json"]:
        if not os.path.exists(db):
            with open(db, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    init_dbs()
    # รันเว็บเซิร์ฟเวอร์เคียงคู่บอทดิสคอร์ด
    threading.Thread(target=run_flask, daemon=True).start()
    
    # รันบอทดิสคอร์ดของคุณ
    TOKEN = os.environ.get("DISCORD_TOKEN", "ใส่โทเค็นบอทของคุณตรงนี้")
    bot.run(TOKEN)
