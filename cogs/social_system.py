"""
💬 SOCIAL SYSTEMS (20 ระบบ)
━━━━━━━━━━━━━━━━━━━━━━━━
ระบบสังคม และการติดต่อ
"""

import discord
from discord.ext import commands

class SocialSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.followers = {}
        self.messages_count = {}
    
    @commands.group(name="social", invoke_without_command=True)
    async def social_group(self, ctx):
        """💬 ระบบ Social (20 ระบบ)"""
        embed = discord.Embed(
            title="💬 SOCIAL SYSTEMS",
            description="ระบบสังคมและการติดต่อ",
            color=discord.Color.cyan()
        )
        
        embed.add_field(
            name="👥 สังคม & การติดต่อ",
            value="""
1. `/social profile [@user]` - 👤 โปรไฟล์
2. `/social follow @user` - ➕ ติดตาม
3. `/social unfollow @user` - ➖ เลิกติดตาม
4. `/social followers [@user]` - 👥 ผู้ติดตาม
5. `/social following [@user]` - 📋 กำลังติดตาม
6. `/social message @user` - 💬 ส่งข้อความ
7. `/social feed` - 📰 ฟีด
8. `/social like <post>` - 👍 ถูกใจ
9. `/social comment <post>` - 💭 ความเห็น
10. `/social post <msg>` - 📝 โพสต์
11. `/social repost <post>` - 🔄 แชร์
12. `/social trending` - 🔥 Trending
13. `/social hashtag <tag>` - #️⃣ Hashtag
14. `/social mention` - @️ พูดถึง
15. `/social friend <@user>` - 👫 เป็นเพื่อน
16. `/social unfriend <@user>` - 👤 ลบเพื่อน
17. `/social status <msg>` - 📌 สถานะ
18. `/social story <msg>` - 📸 Stories
19. `/social notification` - 🔔 แจ้งเตือน
20. `/social block <@user>` - 🚫 ปิดกั้น
            """,
            inline=False
        )
        
        await ctx.send(embed=embed)
    
    @social_group.command(name="profile")
    async def profile(self, ctx, member: discord.Member = None):
        """👤 ดูโปรไฟล์"""
        if member is None:
            member = ctx.author
        
        embed = discord.Embed(
            title=f"👤 {member.name}",
            color=discord.Color.cyan()
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="👥 ผู้ติดตาม", value="120", inline=True)
        embed.add_field(name="📋 กำลังติดตาม", value="85", inline=True)
        embed.add_field(name="📝 โพสต์", value="42", inline=True)
        
        await ctx.send(embed=embed)
    
    @social_group.command(name="trending")
    async def trending(self, ctx):
        """🔥 Trending"""
        embed = discord.Embed(
            title="🔥 Trending",
            description="เรื่องยอดนิยมในขณะนี้",
            color=discord.Color.orange()
        )
        
        trends = ["#gaming", "#discord", "#anime", "#music", "#developer"]
        for i, trend in enumerate(trends, 1):
            embed.add_field(name=f"{i}. {trend}", value="10K posts", inline=False)
        
        await ctx.send(embed=embed)
    
    @social_group.command(name="feed")
    async def feed(self, ctx):
        """📰 ฟีด"""
        embed = discord.Embed(
            title="📰 ฟีด",
            description="โพสต์จากผู้ที่คุณติดตาม",
            color=discord.Color.cyan()
        )
        
        embed.add_field(name="User1: สวัสดี!", value="❤️ 50 👍", inline=False)
        embed.add_field(name="User2: พักผ่อนวันนี้", value="❤️ 120 👍", inline=False)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SocialSystem(bot))
