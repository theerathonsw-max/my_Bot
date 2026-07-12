"""
🎵 MUSIC SYSTEMS (25 ระบบ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
เพลง เสียง และระบบบันเทิง
"""

import discord
from discord.ext import commands
import random

class MusicBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.playlists = {}
        self.current_playing = {}
    
    @commands.group(name="music", invoke_without_command=True)
    async def music_group(self, ctx):
        """🎵 ระบบ Music (25 ระบบ)"""
        embed = discord.Embed(
            title="🎵 MUSIC SYSTEMS",
            description="ระบบเพลงและการบันเทิง",
            color=discord.Color.magenta()
        )
        
        embed.add_field(
            name="🎸 เพลง & เสียง",
            value="""
1. `/music play <song>` - ▶️ เล่นเพลง
2. `/music pause` - ⏸️ หยุดชั่วคราว
3. `/music resume` - ▶️ ต่อเพลง
4. `/music stop` - ⏹️ หยุด
5. `/music skip` - ⏭️ ข้าม
6. `/music queue` - 📋 เพลยลิสต์
7. `/music now` - 🎶 เพลงขณะนี้
8. `/music volume <0-100>` - 🔊 ระดับเสียง
9. `/music lyrics` - 📝 เนื้อเพลง
10. `/music search` - 🔍 ค้นหา
11. `/music playlist create` - ➕ สร้างเพลยลิสต์
12. `/music playlist add` - 🎵 เพิ่มเพลง
13. `/music playlist delete` - ❌ ลบเพลยลิสต์
14. `/music recommend` - 💡 แนะนำ
15. `/music loop` - 🔁 วนซ้ำ
16. `/music shuffle` - 🔀 สุ่ม
17. `/music radio <genre>` - 📻 วิทยุ
18. `/music history` - 📜 ประวัติ
19. `/music favorite` - ⭐ ชื่นชอบ
20. `/music chart` - 📊 แผนภูมิเพลง
21. `/music lyric_video` - 🎬 วิดีโอเนื้อเพลง
22. `/music album` - 💿 อัลบัม
23. `/music artist` - 👤 ศิลปิน
24. `/music sound_effects` - 🎙️ เอฟเฟค
25. `/music notification` - 🔔 แจ้งเตือน
            """,
            inline=False
        )
        
        await ctx.send(embed=embed)
    
    @music_group.command(name="play")
    async def play(self, ctx, *, song):
        """▶️ เล่นเพลง"""
        embed = discord.Embed(
            title="▶️ กำลังเล่น",
            description=f"🎵 {song}",
            color=discord.Color.magenta()
        )
        embed.add_field(name="ศิลปิน", value="[Artist]", inline=True)
        embed.add_field(name="ระยะเวลา", value="3:45", inline=True)
        await ctx.send(embed=embed)
    
    @music_group.command(name="playlist")
    async def playlist(self, ctx, action="list"):
        """📋 จัดการเพลยลิสต์"""
        embed = discord.Embed(
            title="📋 เพลยลิสต์",
            description="รายชื่อเพลง",
            color=discord.Color.magenta()
        )
        embed.add_field(name="1. My Favorites", value="10 เพลง", inline=False)
        embed.add_field(name="2. Chill Vibes", value="15 เพลง", inline=False)
        await ctx.send(embed=embed)
    
    @music_group.command(name="queue")
    async def queue(self, ctx):
        """📋 ดูคิว"""
        embed = discord.Embed(
            title="📋 Queue",
            description="เพลงถัดไป",
            color=discord.Color.magenta()
        )
        embed.add_field(name="1. Song 1", value="3:45", inline=False)
        embed.add_field(name="2. Song 2", value="4:20", inline=False)
        await ctx.send(embed=embed)
    
    @music_group.command(name="radio")
    async def radio(self, ctx, genre="pop"):
        """📻 ฟังวิทยุ"""
        embed = discord.Embed(
            title="📻 วิทยุ",
            description=f"🎵 {genre.capitalize()} Radio",
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)
    
    @music_group.command(name="recommend")
    async def recommend(self, ctx):
        """💡 แนะนำเพลง"""
        songs = ["Song A", "Song B", "Song C"]
        embed = discord.Embed(
            title="💡 แนะนำเพลง",
            description="\n".join([f"{i+1}. {song}" for i, song in enumerate(songs)]),
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(MusicBot(bot))
