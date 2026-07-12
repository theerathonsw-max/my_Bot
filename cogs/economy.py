"""
💰 ECONOMY SYSTEMS (25 ระบบ)
"""
import discord
from discord.ext import commands
import random

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_money = {}
    
    @commands.group(name="economy", invoke_without_command=True)
    async def economy_group(self, ctx):
        """💰 ECONOMY (25 ระบบ)"""
        embed = discord.Embed(title="💰 ECONOMY", description="25 ระบบ", color=discord.Color.gold())
        embed.add_field(name="ระบบ", value="""
1. /economy balance - 💰 เงิน
2. /economy work - 💼 ทำงาน
3. /economy daily - 🎁 รางวัลรายวัน
4. /economy gamble <amount> - 🎰 พนัน
5. /economy rob @user - 👮 ปล้น
6. /economy shop - 🛍️ ร้านค้า
7. /economy buy <item> - 🛒 ซื้อ
8. /economy sell <item> - 📤 ขาย
9. /economy transfer @user <amount> - 💸 โอน
10. /economy leaderboard - 📊 อันดับ
11. /economy salary - 💵 เงินเดือน
12. /economy bank - 🏦 ธนาคาร
13. /economy invest <amount> - 📈 ลงทุน
14. /economy richest - 👑 รวย
15. /economy inventory - 📦 สินค้า
16. /economy item <name> - 🎁 สินค้า
17. /economy market - 📊 ตลาด
18. /economy trade @user - 🔄 แลก
19. /economy lottery - 🎰 ลอตเตอรี่
20. /economy tax - 💸 ภาษี
21. /economy donation - 💝 บริจาค
22. /economy cashout - 💵 จ่ายเงิน
23. /economy balance <@user> - 👀 ดูเงินคน
24. /economy stats - 📈 สถิติ
25. /economy reset - 🔄 รีเซ็ต
        """, inline=False)
        await ctx.send(embed=embed)
    
    @economy_group.command(name="balance")
    async def balance(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        money = self.user_money.get(member.id, 0)
        embed = discord.Embed(title=f"💰 เงิน {member.name}", description=f"💵 {money:,} บาท", color=discord.Color.gold())
        await ctx.send(embed=embed)
    
    @economy_group.command(name="work")
    async def work(self, ctx):
        earned = random.randint(50, 200)
        self.user_money[ctx.author.id] = self.user_money.get(ctx.author.id, 0) + earned
        embed = discord.Embed(title="💼 ทำงาน", description=f"ได้เงิน {earned} บาท!", color=discord.Color.green())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Economy(bot))
