"""
📊 LEVELING SYSTEMS (15 ระบบ)
"""
import discord
from discord.ext import commands

class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_levels = {}
    
    @commands.group(name="level", invoke_without_command=True)
    async def level_group(self, ctx):
        """📊 LEVELING (15 ระบบ)"""
        embed = discord.Embed(title="📊 LEVELING", description="15 ระบบ", color=discord.Color.blue())
        embed.add_field(name="ระบบ", value="""
1. /level profile - 📊 Profile
2. /level leaderboard - 🏆 Leaderboard
3. /level rank - 🥇 Rank
4. /level progress - 📈 Progress
5. /level rewards - 🎁 Rewards
6. /level daily_quest - 📋 Quest
7. /level milestone - 🎯 Milestone
8. /level streak - 🔥 Streak
9. /level badge - 🏅 Badge
10. /level stats - 📊 Stats
11. /level multiplier - 2️⃣ Multiplier
12. /level reset - 🔄 Reset
13. /level top10 - 🥇 Top 10
14. /level compare @user - 🆚 Compare
15. /level upgrade - ⬆️ Upgrade
        """, inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Leveling(bot))
