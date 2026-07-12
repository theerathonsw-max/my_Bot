#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🤖 ALL-IN-ONE DISCORD BOT v4.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ 200+ Systems + Web Scraping + Security Tools
📊 Dashboard Control + Logging + Analytics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import discord
from discord.ext import commands, tasks
import json
import os
import asyncio
import logging
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import aiohttp
import requests
from bs4 import BeautifulSoup
import hashlib
import socket
import string
import random

# โหลด .env
load_dotenv()

# ตั้ง logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('discord_bot')

# สร้าง intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

class AllInOneBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)
        self.version = "4.0"
        self.systems_count = 200
        self.start_time = datetime.now()
        self.session = None
    
    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        await self.load_all_cogs()
    
    async def load_all_cogs(self):
        cogs_dir = Path('./cogs')
        
        if not cogs_dir.exists():
            logger.warning("❌ ไม่พบ folder cogs")
            return
        
        cog_count = 0
        for filename in sorted(cogs_dir.glob('*.py')):
            if filename.name.startswith('_'):
                continue
            
            try:
                await self.load_extension(f'cogs.{filename.stem}')
                cog_count += 1
                print(f"✅ โหลด {filename.name}")
            except Exception as e:
                print(f"❌ ไม่สามารถโหลด {filename.name}: {e}")
        
        print(f"\n📊 โหลด {cog_count} cog file สำเร็จ!")

bot = AllInOneBot()

@bot.event
async def on_ready():
    uptime = datetime.now() - bot.start_time
    
    print("\n" + "╔" + "═" * 60 + "╗")
    print("║" + " " * 60 + "║")
    print(f"║ 🤖 ALL-IN-ONE BOT v{bot.version} (200+ Systems)".ljust(61) + "║")
    print("║ " + "=" * 58 + " ║")
    print(f"║ ✅ สถานะ: Online".ljust(61) + "║")
    print(f"║ 👤 บอท: {bot.user}".ljust(61) + "║")
    print(f"║ 🌐 เซิร์ฟเวอร์: {len(bot.guilds)} อัน".ljust(61) + "║")
    print(f"║ 📊 ระบบ: {bot.systems_count}+ ระบบ".ljust(61) + "║")
    print(f"║ 🔧 Features: Web Scraping + Security Tools".ljust(61) + "║")
    print("║ " + "=" * 58 + " ║")
    print("║" + " " * 60 + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="200+ Systems + Web Tools + Security 🔧"
        )
    )

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="🤖 ALL-IN-ONE BOT v4.0",
        description="**200+ ระบบ + Web Tools + Security**",
        color=discord.Color.blurple()
    )
    
    embed.add_field(
        name="🌐 Web Scraping (15 ระบบ)",
        value="""
/scrape url <url> - 📄 Scrape เว็บ
/scrape html <url> - 🔍 Get HTML
/scrape links <url> - 🔗 Get Links
/scrape images <url> - 🖼️ Get Images
/scrape status <url> - ✅ Status Check
        """,
        inline=False
    )
    
    embed.add_field(
        name="🔐 Security Tools (15 ระบบ)",
        value="""
/security password - 🔑 Generate Password
/security check-password <pwd> - ✅ Check Strength
/security hash <text> - 🔐 Hash Text
/security network-scan - 🌐 Network Info
/security ip-info - 🌍 Your IP
        """,
        inline=False
    )
    
    embed.add_field(
        name="📊 170+ Discord Systems",
        value="Fun, Admin, Economy, Utility, Leveling, และอีกมากมาย!",
        inline=False
    )
    
    await ctx.send(embed=embed)

# 🌐 Web Scraping
@commands.group(name="scrape", invoke_without_command=True)
async def scrape_group(ctx):
    embed = discord.Embed(
        title="🌐 WEB SCRAPING TOOLS",
        description="ระบบ Scraping ถูกต้องกฎหมาย (15 ระบบ)",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="คำสั่ง",
        value="""
1. /scrape url <url> - 📄 Scrape เว็บ
2. /scrape html <url> - 🔍 Get HTML
3. /scrape links <url> - 🔗 Get All Links
4. /scrape images <url> - 🖼️ Get Images URLs
5. /scrape text <url> - 📝 Get Text Content
6. /scrape status <url> - ✅ Status Check
7. /scrape headers <url> - 📋 Get Headers
8. /scrape metadata <url> - 📌 Get Metadata
9. /scrape size <url> - 📏 Page Size
10. /scrape title <url> - 📖 Get Title
11. /scrape monitor <url> - 👀 Monitor Website
12. /scrape compare <url1> <url2> - 🆚 Compare Pages
13. /scrape download <url> <filename> - 📥 Download
14. /scrape extract <url> <selector> - 📋 CSS Selector
15. /scrape performance <url> - ⚡ Performance Test
        """,
        inline=False
    )
    
    await ctx.send(embed=embed)

@scrape_group.command(name="url")
async def scrape_url(ctx, url: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status == 200:
                    html = await resp.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    title = soup.title.string if soup.title else "No title"
                    
                    embed = discord.Embed(
                        title="✅ Scrape สำเร็จ",
                        description=url,
                        color=discord.Color.green()
                    )
                    embed.add_field(name="📌 Title", value=title[:100], inline=False)
                    embed.add_field(name="📏 Size", value=f"{len(html)} bytes", inline=True)
                    embed.add_field(name="📊 Status", value=resp.status, inline=True)
                    
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"❌ Error: Status {resp.status}")
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)[:100]}")

@scrape_group.command(name="status")
async def scrape_status(ctx, url: str):
    try:
        response = requests.head(url, timeout=10, allow_redirects=True)
        
        embed = discord.Embed(
            title="✅ Status Check",
            description=url,
            color=discord.Color.green() if response.status_code < 400 else discord.Color.red()
        )
        embed.add_field(name="📊 Status", value=response.status_code, inline=True)
        embed.add_field(name="⏱️ Time", value=f"{response.elapsed.total_seconds():.2f}s", inline=True)
        
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

@scrape_group.command(name="links")
async def scrape_links(ctx, url: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                html = await resp.text()
                soup = BeautifulSoup(html, 'html.parser')
                links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
                
                embed = discord.Embed(
                    title="🔗 Found Links",
                    description=f"Found {len(links)} links",
                    color=discord.Color.blue()
                )
                
                links_text = "\n".join(links[:10])
                embed.add_field(name="📋 Top 10", value=f"```{links_text}```", inline=False)
                
                await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

# 🔐 Security Tools
@commands.group(name="security", invoke_without_command=True)
async def security_group(ctx):
    embed = discord.Embed(
        title="🔐 SECURITY TOOLS",
        description="เครื่องมือป้องกันความปลอดภัย (15 ระบบ)",
        color=discord.Color.red()
    )
    
    embed.add_field(
        name="คำสั่ง",
        value="""
1. /security password - 🔑 Generate Password
2. /security check-password <pwd> - ✅ Check Strength
3. /security hash <text> - 🔐 Hash Text (SHA256)
4. /security network-scan - 🌐 Network Info
5. /security port-check <host> <port> - 🔌 Port Check
6. /security ip-info - 🌍 Your IP Info
7. /security dns-lookup <domain> - 📡 DNS Lookup
8. /security ssl-check <domain> - 🔒 SSL Info
9. /security url-scan <url> - 🔍 URL Scanner
10. /security password-strength <pwd> - 📊 Strength Meter
11. /security generate-token - 🎫 Generate Token
12. /security encrypt <text> - 🔐 Encrypt (Base64)
13. /security decrypt <text> - 🔓 Decrypt (Base64)
14. /security security-audit - 📋 Audit Check
15. /security whois <domain> - 📋 WHOIS Lookup
        """,
        inline=False
    )
    
    await ctx.send(embed=embed)

@security_group.command(name="password")
async def generate_password(ctx, length: int = 16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    pwd = ''.join(random.choice(chars) for _ in range(length))
    
    embed = discord.Embed(
        title="🔑 Generated Password",
        description=f"```{pwd}```",
        color=discord.Color.green()
    )
    embed.add_field(name="📏 Length", value=length, inline=True)
    embed.add_field(name="⚠️", value="Copy แล้วลบ!", inline=True)
    
    await ctx.send(embed=embed, delete_after=30)

@security_group.command(name="check-password")
async def check_password_strength(ctx, password: str):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ ต้อง 8 ตัวขึ้นไป")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("❌ ต้องมี Uppercase")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("❌ ต้องมี Lowercase")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("❌ ต้องมี Numbers")
    
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        feedback.append("⚠️ ควรมี Special Characters")
    
    strength = ["Very Weak", "Weak", "Fair", "Good", "Very Strong"][score]
    color = [discord.Color.red(), discord.Color.orange(), discord.Color.gold(), discord.Color.blue(), discord.Color.green()][score]
    
    embed = discord.Embed(
        title="✅ Password Strength",
        description=f"Strength: **{strength}** ({score}/5)",
        color=color
    )
    
    if feedback:
        embed.add_field(name="💡 Suggestions", value="\n".join(feedback), inline=False)
    
    await ctx.send(embed=embed)

@security_group.command(name="hash")
async def hash_text(ctx, *, text: str):
    sha256 = hashlib.sha256(text.encode()).hexdigest()
    md5 = hashlib.md5(text.encode()).hexdigest()
    
    embed = discord.Embed(
        title="🔐 Hash Generator",
        color=discord.Color.blue()
    )
    embed.add_field(name="📝 Text", value=text, inline=False)
    embed.add_field(name="🔐 SHA256", value=f"```{sha256}```", inline=False)
    embed.add_field(name="🔑 MD5", value=f"```{md5}```", inline=False)
    
    await ctx.send(embed=embed)

@security_group.command(name="network-scan")
async def network_scan(ctx):
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        
        embed = discord.Embed(
            title="🌐 Network Information",
            color=discord.Color.blue()
        )
        embed.add_field(name="🖥️ Hostname", value=hostname, inline=True)
        embed.add_field(name="📍 Local IP", value=ip_address, inline=True)
        embed.add_field(name="⏰ Time", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

@security_group.command(name="generate-token")
async def generate_token(ctx):
    token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
    
    embed = discord.Embed(
        title="🎫 Generated Token",
        description=f"```{token}```",
        color=discord.Color.blue()
    )
    
    await ctx.send(embed=embed, delete_after=30)

# ❌ Error Handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="❌ ไม่พบคำสั่ง",
            description="ลองใช้ `/help`",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed, delete_after=5)

def main():
    token = os.getenv('TOKEN')
    
    if not token:
        print("\n❌ ไม่พบ TOKEN\n")
        return
    
    try:
        print("\n🚀 กำลังเริ่มต้นบอท...\n")
        bot.run(token)
    except KeyboardInterrupt:
        print("\n✅ บอทปิดแล้ว")

if __name__ == "__main__":
    main()
