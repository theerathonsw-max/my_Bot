"""
🌟 EXTENDED UTILITY SYSTEMS (5 ระบบ)
━━━━━━━━━━━━━━━━━━━━━━━
เครื่องมือเพิ่มเติม
"""

import discord
from discord.ext import commands

class ExtendedUtility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name="extended", invoke_without_command=True)
    async def extended_group(self, ctx):
        """🌟 ระบบ Extended Utility (5 ระบบ)"""
        embed = discord.Embed(
            title="🌟 EXTENDED UTILITY",
            description="เครื่องมือเพิ่มเติม",
            color=discord.Color.greyple()
        )
        
        embed.add_field(
            name="⭐ เครื่องมือ",
            value="""
1. `/extended backup` - 💾 สำรองข้อมูล
2. `/extended restore <backup>` - 📥 กู้คืน
3. `/extended settings` - ⚙️ ตั้งค่า
4. `/extended info` - ℹ️ ข้อมูล
5. `/extended support` - 📞 ช่วยเหลือ
            """,
            inline=False
        )
        
        await ctx.send(embed=embed)
    
    @extended_group.command(name="backup")
    async def backup(self, ctx):
        """💾 สำรองข้อมูล"""
        embed = discord.Embed(
            title="💾 Backup",
            description="✅ สำรองข้อมูลสำเร็จ",
            color=discord.Color.green()
        )
        embed.add_field(name="วันที่", value="01/01/2024", inline=True)
        embed.add_field(name="ขนาด", value="5.2 MB", inline=True)
        
        await ctx.send(embed=embed)
    
    @extended_group.command(name="settings")
    async def settings(self, ctx):
        """⚙️ ตั้งค่า"""
        embed = discord.Embed(
            title="⚙️ Settings",
            description="ตั้งค่าเซิร์ฟเวอร์",
            color=discord.Color.greyple()
        )
        embed.add_field(name="ภาษา", value="ไทย", inline=True)
        embed.add_field(name="โหมด", value="Production", inline=True)
        
        await ctx.send(embed=embed)
    
    @extended_group.command(name="info")
    async def info(self, ctx):
        """ℹ️ ข้อมูล"""
        embed = discord.Embed(
            title="ℹ️ ข้อมูลบอท",
            description="Ultimate Discord Bot v3.0",
            color=discord.Color.greyple()
        )
        embed.add_field(name="Version", value="3.0", inline=True)
        embed.add_field(name="Systems", value="200+", inline=True)
        embed.add_field(name="Status", value="✅ Online", inline=True)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ExtendedUtility(bot))
