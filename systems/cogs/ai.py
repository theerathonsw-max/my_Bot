"""
🤖 AI SYSTEMS (15 ระบบ)
"""
import discord
from discord.ext import commands
import random

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name="ai", invoke_without_command=True)
    async def ai_group(self, ctx):
        """🤖 AI (15 ระบบ)"""
        embed = discord.Embed(title="🤖 AI SYSTEMS", description="15 ระบบ", color=discord.Color.purple())
        embed.add_field(name="ระบบ", value="""
1. /ai chat - 💬 Chat
2. /ai translate - 🌐 Translate
3. /ai sentiment - 😊 Sentiment
4. /ai summarize - 📝 Summarize
5. /ai question - ❓ Q&A
6. /ai joke - 😂 Joke
7. /ai story - 📖 Story
8. /ai quote - 💭 Quote
9. /ai fact - 📚 Fact
10. /ai image - 🖼️ Image
11. /ai code - 💻 Code
12. /ai poem - 📜 Poem
13. /ai lyrics - 🎵 Lyrics
14. /ai describe - 📝 Describe
15. /ai suggest - 💡 Suggest
        """, inline=False)
        await ctx.send(embed=embed)
    
    @ai_group.command(name="joke")
    async def joke(self, ctx):
        jokes = ["หลอดไฟขึ้นไปกี่ดวง?", "ทำไมไก่ถึงข้าม?"]
        embed = discord.Embed(title="😂 AI Joke", description=random.choice(jokes), color=discord.Color.gold())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(AI(bot))
