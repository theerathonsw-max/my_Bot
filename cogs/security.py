"""
🛡️ SECURITY SYSTEMS (10 ระบบ)
"""
import discord
from discord.ext import commands

class Security(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name="security", invoke_without_command=True)
    async def security_group(self, ctx):
        """🛡️ SECURITY (10 ระบบ)"""
        embed = discord.Embed(title="🛡️ SECURITY", description="10 ระบบ", color=discord.Color.red())
        embed.add_field(name="ระบบ", value="""
1. /security antispam - 🤖 Anti Spam
2. /security filter - 🚫 Filter
3. /security verification - ✅ Verification
4. /security roles - 👑 Auto Roles
5. /security permissions - 🔐 Permissions
6. /security backup - 💾 Backup
7. /security restore - 📥 Restore
8. /security audit - 📊 Audit Log
9. /security logs - 📝 Logs
10. /security whitelist - ✅ Whitelist
        """, inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Security(bot))
