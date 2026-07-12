"""
🎮 FUN & GAMES (30 ระบบ)
"""
import discord
from discord.ext import commands
import random

class FunGames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name="fun", invoke_without_command=True)
    async def fun_group(self, ctx):
        """🎮 FUN & GAMES (30 ระบบ)"""
        embed = discord.Embed(
            title="🎮 FUN & GAMES (30 ระบบ)",
            description="เกมและความสนุก",
            color=discord.Color.purple()
        )
        
        embed.add_field(
            name="🎯 ระบบ",
            value="""
1. /fun coin - 💰 โยนเหรียญ
2. /fun dice - 🎲 ทอยลูกเต๋า
3. /fun rps @user - ✂️ Rock Paper Scissors
4. /fun joke - 😂 เล่าเรื่องตลก
5. /fun riddle - 🧩 ปริศนา
6. /fun rate <thing> - ⭐ ให้คะแนน
7. /fun hug @user - 🤗 กอด
8. /fun slap @user - 👋 ตบ
9. /fun kiss @user - 😘 จูบ
10. /fun dance - 💃 เต้น
11. /fun trivia - 🧠 ทดสอบความรู้
12. /fun magic8 - 🎱 ลูกสุ่มเสี่ยงทาย
13. /fun meme - 😂 เมม
14. /fun flip - 🎯 โยนเหรียญมหาศาล
15. /fun 8ball - 🎱 8 Ball
16. /fun fortune - 🔮 Fortuneteller
17. /fun compliment @user - 💕 ชมเชย
18. /fun roast @user - 🔥 ว่ากล่าว
19. /fun fact - 📚 ข้อเท็จจริง
20. /fun quote - 💭 Quote
21. /fun pokemon - 🎮 Pokemon
22. /fun war - ⚔️ Duel
23. /fun spin - 🎡 หมุนวงล้อ
24. /fun race - 🏁 แข่งเรียว
25. /fun bet <amount> - 💰 พนัน
26. /fun waifu - 👰 Waifu
27. /fun soulmate - 💑 Soul Mate
28. /fun ship @user - 💕 Ship
29. /fun uwu - 😚 UwU
30. /fun gay - 🌈 Gay Test
            """,
            inline=False
        )
        
        await ctx.send(embed=embed)
    
    @fun_group.command(name="coin")
    async def coin(self, ctx):
        result = random.choice(["🟤 หัว", "🔘 ก้อย"])
        embed = discord.Embed(title="💰 โยนเหรียญ", description=result, color=discord.Color.gold())
        await ctx.send(embed=embed)
    
    @fun_group.command(name="dice")
    async def dice(self, ctx, sides: int = 6):
        result = random.randint(1, sides)
        embed = discord.Embed(title=f"🎲 ทอยลูกเต๋า (1-{sides})", description=f"**{result}**", color=discord.Color.purple())
        await ctx.send(embed=embed)
    
    @fun_group.command(name="joke")
    async def joke(self, ctx):
        jokes = [
            "🔧 ทำไมปลาถึงไม่เล่นบาสเก็ตบอล? → เพราะมันกลัวลุงจะตักเด็ก!",
            "💻 ทำไมโปรแกรมเมอร์ถึงชอบอยู่บ้าน? → เพราะบ้านไม่มี bugs",
        ]
        embed = discord.Embed(title="😂 เรื่องตลก", description=random.choice(jokes), color=discord.Color.gold())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(FunGames(bot))
