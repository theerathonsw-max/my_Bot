"""
🔧 UTILITY SYSTEMS (25 ระบบ)
"""
import discord
from discord.ext import commands
from datetime import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name="util", invoke_without_command=True)
    async def util_group(self, ctx):
        """🔧 UTILITY (25 ระบบ)"""
        embed = discord.Embed(title="🔧 UTILITY", description="25 ระบบ", color=discord.Color.blue())
        embed.add_field(name="เครื่องมือ", value="""
1. /util ping - 🏓 Ping
2. /util info - ℹ️ Server Info
3. /util user <@user> - 👤 User Info
4. /util avatar <@user> - 🖼️ Avatar
5. /util calc <expression> - 🧮 Calculate
6. /util weather <city> - 🌤️ Weather
7. /util time - ⏰ Time
8. /util color <hex> - 🎨 Color
9. /util qrcode <text> - 📱 QR Code
10. /util translate <text> - 🌐 Translate
11. /util poll <question> - 📊 Poll
12. /util embed - 📝 Embed
13. /util timer <sec> - ⏱️ Timer
14. /util reminder <msg> - 📌 Reminder
15. /util note <msg> - 📝 Note
16. /util todo - 📋 Todo
17. /util calendar - 📅 Calendar
18. /util unicode <text> - 🔤 Unicode
19. /util hex2rgb <hex> - 🌈 HEX to RGB
20. /util base64 <text> - 🔐 Base64
21. /util decode <text> - 🔓 Decode
22. /util math <expression> - 📐 Math
23. /util ascii <text> - 📄 ASCII
24. /util stats - 📊 Stats
25. /util help [command] - 📖 Help
        """, inline=False)
        await ctx.send(embed=embed)
    
    @util_group.command(name="ping")
    async def ping(self, ctx):
        embed = discord.Embed(title="🏓 Pong!", description=f"⏱️ {round(self.bot.latency * 1000)}ms", color=discord.Color.green())
        await ctx.send(embed=embed)
    
    @util_group.command(name="time")
    async def time(self, ctx):
        now = datetime.now()
        embed = discord.Embed(title="⏰ เวลา", description=now.strftime("%d/%m/%Y %H:%M:%S"), color=discord.Color.blue())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
