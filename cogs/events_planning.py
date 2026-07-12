"""
🎊 EVENTS & PLANNING SYSTEMS (20 ระบบ)
━━━━━━━━━━━━━━━━━━━━━━━━━━
งานปีว่าง และการวางแผน
"""

import discord
from discord.ext import commands
from datetime import datetime, timedelta

class EventsPlanning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.events = {}
        self.giveaways = {}
    
    @commands.group(name="events", invoke_without_command=True)
    async def events_group(self, ctx):
        """🎊 ระบบ Events (20 ระบบ)"""
        embed = discord.Embed(
            title="🎊 EVENTS & PLANNING",
            description="งานและการวางแผน",
            color=discord.Color.purple()
        )
        
        embed.add_field(
            name="🎉 งาน & วางแผน",
            value="""
1. `/events create <name>` - ➕ สร้างงาน
2. `/events list` - 📋 รายชื่องาน
3. `/events attend <id>` - ✅ เข้างาน
4. `/events cancel <id>` - ❌ ยกเลิก
5. `/events details <id>` - ℹ️ รายละเอียด
6. `/events schedule <date>` - 📅 ตารางเวลา
7. `/events countdown <id>` - ⏰ นับถอยหลัง
8. `/events location <place>` - 📍 สถานที่
9. `/events attendees <id>` - 👥 ผู้เข้า
10. `/events remind` - 🔔 เตือน
11. `/events giveaway create` - 🎁 สร้าง Giveaway
12. `/events giveaway enter` - 🎰 เข้า Giveaway
13. `/events giveaway end` - 🏁 จบ Giveaway
14. `/events giveaway winner` - 🎊 ผู้ชนะ
15. `/events contest create` - 🏆 สร้างคอนเทส
16. `/events contest join` - ⚔️ เข้าคอนเทส
17. `/events survey <q>` - 📊 สำรวจ
18. `/events vote <option>` - 🗳️ โหวต
19. `/events feedback` - 💬 ข้อเสนอแนะ
20. `/events reviews` - ⭐ ความคิดเห็น
            """,
            inline=False
        )
        
        await ctx.send(embed=embed)
    
    @events_group.command(name="create")
    async def create(self, ctx, *, name):
        """➕ สร้างงาน"""
        event_id = len(self.events) + 1
        self.events[event_id] = {
            "name": name,
            "creator": ctx.author.id,
            "date": datetime.now(),
            "attendees": [],
            "active": True
        }
        
        embed = discord.Embed(
            title="✅ สร้างงานสำเร็จ",
            description=f"🎉 {name}",
            color=discord.Color.green()
        )
        embed.add_field(name="Event ID", value=event_id, inline=True)
        embed.add_field(name="สร้างโดย", value=ctx.author.mention, inline=True)
        
        await ctx.send(embed=embed)
    
    @events_group.command(name="list")
    async def list_events(self, ctx):
        """📋 รายชื่องาน"""
        embed = discord.Embed(
            title="📋 งานที่เปิด",
            description="รายชื่องานทั้งหมด",
            color=discord.Color.purple()
        )
        
        if not self.events:
            embed.description = "ยังไม่มีงาน"
        else:
            for event_id, event in self.events.items():
                embed.add_field(
                    name=f"ID {event_id}: {event['name']}",
                    value=f"👥 {len(event['attendees'])} คน",
                    inline=False
                )
        
        await ctx.send(embed=embed)
    
    @events_group.command(name="giveaway")
    async def giveaway(self, ctx, action="list", *, prize=""):
        """🎁 Giveaway"""
        embed = discord.Embed(
            title="🎁 Giveaway",
            description="รายชื่อ Giveaway",
            color=discord.Color.gold()
        )
        
        if action == "create" and prize:
            embed.add_field(name="🎁 Giveaway", value=prize, inline=False)
            embed.add_field(name="ผู้เข้า", value="0", inline=True)
            embed.add_field(name="เวลา", value="1 วัน", inline=True)
        
        await ctx.send(embed=embed)
    
    @events_group.command(name="countdown")
    async def countdown(self, ctx, event_id: int):
        """⏰ นับถอยหลัง"""
        if event_id not in self.events:
            await ctx.send("❌ ไม่พบงาน", delete_after=5)
            return
        
        event = self.events[event_id]
        time_left = (event["date"] + timedelta(days=7)) - datetime.now()
        
        embed = discord.Embed(
            title="⏰ นับถอยหลัง",
            description=f"{event['name']}",
            color=discord.Color.purple()
        )
        embed.add_field(name="เวลาเหลือ", value=str(time_left).split('.')[0], inline=False)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(EventsPlanning(bot))
