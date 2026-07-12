"""
🎮 GAMING & TOURNAMENT SYSTEMS (15 ระบบ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
เกมและการแข่งขัน
"""

import discord
from discord.ext import commands

class GamingTournament(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tournaments = {}
        self.leaderboards = {}
    
    @commands.group(name="gaming", invoke_without_command=True)
    async def gaming_group(self, ctx):
        """🎮 ระบบ Gaming (15 ระบบ)"""
        embed = discord.Embed(
            title="🎮 GAMING & TOURNAMENT",
            description="เกมและการแข่งขัน",
            color=discord.Color.red()
        )
        
        embed.add_field(
            name="🏆 เกม & การแข่งขัน",
            value="""
1. `/gaming tournament create` - 🏆 สร้างแข่งขัน
2. `/gaming tournament join` - ✅ เข้าแข่งขัน
3. `/gaming tournament leave` - ❌ ออกแข่งขัน
4. `/gaming tournament list` - 📋 รายชื่อ
5. `/gaming bracket` - 🗂️ วงเล็บ
6. `/gaming score <team>` - 📊 คะแนน
7. `/gaming match start` - ⚔️ เริ่มแมตช์
8. `/gaming match result` - 🏁 ผลลัพธ์
9. `/gaming leaderboard` - 🥇 อันดับ
10. `/gaming medals` - 🏅 เหรียญ
11. `/gaming achievement` - 🎖️ ความสำเร็จ
12. `/gaming ranking` - 📈 อันดับ
13. `/gaming prediction` - 🎯 ทำนาย
14. `/gaming betting` - 💰 พนัน
15. `/gaming schedule` - 📅 ตารางเวลา
            """,
            inline=False
        )
        
        await ctx.send(embed=embed)
    
    @gaming_group.command(name="tournament")
    async def tournament(self, ctx, action="list"):
        """🏆 จัดการแข่งขัน"""
        embed = discord.Embed(
            title="🏆 Tournament",
            description="การแข่งขันที่เปิด",
            color=discord.Color.red()
        )
        
        embed.add_field(name="1. E-Sports 2024", value="16 คน", inline=False)
        embed.add_field(name="2. Gaming Royale", value="32 คน", inline=False)
        embed.add_field(name="3. Championship", value="8 ทีม", inline=False)
        
        await ctx.send(embed=embed)
    
    @gaming_group.command(name="leaderboard")
    async def leaderboard(self, ctx):
        """🥇 อันดับ"""
        embed = discord.Embed(
            title="🥇 Leaderboard",
            description="ผู้นำ",
            color=discord.Color.gold()
        )
        
        ranks = [
            ("🥇 Player 1", "5000 pts"),
            ("🥈 Player 2", "4500 pts"),
            ("🥉 Player 3", "4000 pts"),
        ]
        
        for player, points in ranks:
            embed.add_field(name=player, value=points, inline=False)
        
        await ctx.send(embed=embed)
    
    @gaming_group.command(name="match")
    async def match(self, ctx, action="list"):
        """⚔️ แมตช์"""
        embed = discord.Embed(
            title="⚔️ Match",
            description="แมตช์ล่าสุด",
            color=discord.Color.red()
        )
        
        embed.add_field(name="Team A vs Team B", value="Team A won!", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GamingTournament(bot))
