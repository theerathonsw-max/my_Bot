"""
👑 ADMIN & MODERATION (20 ระบบ)
"""
import discord
from discord.ext import commands

class AdminMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name="admin", invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def admin_group(self, ctx):
        """👑 ADMIN (20 ระบบ)"""
        embed = discord.Embed(title="👑 ADMIN SYSTEMS", description="20 ระบบ", color=discord.Color.gold())
        embed.add_field(name="คำสั่ง", value="""
1. /admin purge <n> - 🧹 ลบข้อความ
2. /admin kick @user - 👢 เตะ
3. /admin ban @user - 🚫 แบน
4. /admin warn @user - ⚠️ เตือน
5. /admin mute @user <time> - 🔇 ปิดเสียง
6. /admin unmute @user - 🔊 เปิดเสียง
7. /admin nickname @user <name> - 📝 ชื่อ
8. /admin announce <msg> - 📢 ประกาศ
9. /admin slowmode <sec> - ⏱️ Slow Mode
10. /admin lock - 🔒 ล็อก
11. /admin unlock - 🔓 ปลดล็อก
12. /admin unban <user> - 🔓 ปลด ban
13. /admin warns @user - 📋 ดูเตือน
14. /admin clear_warns @user - ❌ ลบเตือน
15. /admin audit - 📊 Audit Log
16. /admin pin <msg_id> - 📌 Pin
17. /admin unpin <msg_id> - 📍 Unpin
18. /admin rename <new_name> - 📝 เปลี่ยนชื่อห้อง
19. /admin topic <topic> - 📌 Topic
20. /admin nsfw - 🔞 NSFW Mode
        """, inline=False)
        await ctx.send(embed=embed)
    
    @admin_group.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        if amount <= 0:
            await ctx.send("❌ ต้องเป็นตัวเลขมากกว่า 0", delete_after=5)
            return
        deleted = await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(title="✅ ลบสำเร็จ", description=f"ลบแล้ว {len(deleted) - 1} ข้อความ", color=discord.Color.green())
        await ctx.send(embed=embed, delete_after=5)

async def setup(bot):
    await bot.add_cog(AdminMod(bot))
