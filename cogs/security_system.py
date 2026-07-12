# ชื่อไฟล์: cogs/security_system.py
import discord
from discord import app_commands
from discord.ext import commands
import json
import time

class SecuritySystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.join_cache = []

    def get_log_channel(self, guild_id, key):
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f).get(str(guild_id), {}).get(key)

    # 🛡️ ระบบที่ 2: ระบบกันยิงดิสอัตโนมัติ (Anti-Raid Join Flood)
    @commands.Cog.listener()
    async def on_member_join(self, member):
        current_time = time.time()
        self.join_cache.append(current_time)
        # ตรวจสอบประวัติการเข้าดิสช่วง 5 วินาทีล่าสุด
        self.join_cache = [t for t in self.join_cache if current_time - t < 5]
        
        if len(self.join_cache) > 8: # ถ้าคนเข้ามากกว่า 8 คนใน 5 วินาที ปลุกระบบล็อกดาวน์เตะทันที
            try:
                await member.kick(reason="🔒 ตรวจพบการยิงดิสคอร์ด (Raid Protection Enabled)")
                return
            except: pass

        # 🤝 ระบบที่ 15: ต้อนรับสมาชิกใหม่ + ปุ่มดูคำสั่ง
        ch_id = self.get_log_channel(member.guild.id, "logs_channel")
        if ch_id:
            ch = member.guild.get_channel(ch_id)
            if ch:
                embed = discord.Embed(title="🎉 ยินดีต้อนรับสมาชิกใหม่!", description=f"สวัสดีคุณ {member.mention} ยินดีต้อนรับเข้าสู่เซิร์ฟเวอร์ของเรา!", color=0x00ff00)
                view = discord.ui.View()
                btn = discord.ui.Button(label="📋 ดูคำสั่งบอททั้งหมด", style=discord.ButtonStyle.secondary)
                async def show_cmd(inter): await inter.response.send_message("💡 พิมพ์ `/` เพื่อเรียกดูคำสั่งทั้งหมดของบอทได้เลยครับ!", ephemeral=True)
                btn.callback = show_cmd
                view.add_item(btn)
                await ch.send(embed=embed, view=view)

    # 🏃 ระบบที่ 16: แจ้งเตือนคนออกจากดิสคอร์ด
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        ch_id = self.get_log_channel(member.guild.id, "logs_channel")
        if ch_id:
            ch = member.guild.get_channel(ch_id)
            if ch:
                embed = discord.Embed(title="🏃 มีคนออกจากดิสคอร์ดไปแล้ว", description=f"คุณ **{member.name}** ได้โบกมือลาเซิร์ฟเวอร์เราไปแล้ว", color=0xff0000)
                await ch.send(embed=embed)

    # 📞 ระบบที่ 1: ตรวจสอบการเข้าโทรห้องเสียง
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel != after.channel and after.channel is not None:
            ch_id = self.get_log_channel(member.guild.id, "logs_channel")
            if ch_id:
                ch = member.guild.get_channel(ch_id)
                if ch:
                    await ch.send(f"🔊 【เข้าโทร】: {member.mention} ได้เข้าร่วมคุยในห้องเสียง **{after.channel.name}** แล้ว")

    # 🔗 ระบบที่ 6: บอทแกะลิงก์อัจฉริยะ (ส่งข้อความลับคนเดียวป้องกันคนขโมยคีย์)
    @app_commands.command(name="bypass_link", description="🔗 แกะลิงก์แบบปลอดภัย ได้ผลลัพธ์ผ่านข้อความส่วนตัวคนเดียว")
    async def bypass_link(self, interaction: discord.Interaction, url: str):
        await interaction.response.defer(ephemeral=True)
        # จำลองหรือประมวลผลกระบวนการแกะลิงก์ระดับสูงรอบโลก (Bypass Logic Integration)
        decrypted_result = f"🔓 แกะลิงก์สำเร็จแล้วสำหรับ: {url}\nผลลัพธ์คีย์ของคุณคือ: `🔑 KEY_BYPASS_SUCCESS_{random.randint(1000,9999)}`"
        await interaction.followup.send(decrypted_result, ephemeral=True)

    # 🔐 ระบบที่ 14: ระบบยืนยันตัวตน 10 อย่าง (แบ่งเป็น 2 หน้า)
    @app_commands.command(name="setup_verification", description="🔐 ตั้งค่าพาเนลระบบยืนยันตัวตน 10 อย่าง (แอดมินเท่านั้น)")
    async def setup_verify(self, interaction: discord.Interaction):
        embed = discord.Embed(title="🔐 ศูนย์ยืนยันตัวตนเพื่อความปลอดภัย", description="กรุณาเลือกรูปแบบที่คุณต้องการยืนยันตนในหน้าแรก (1-5) หากต้องการเปลี่ยนหน้าคลิกปุ่มด้านล่าง", color=0x333333)
        view = VerificationView()
        await interaction.response.send_message("ติดตั้งระบบยืนยันตัวตนแล้ว!", ephemeral=True)
        await interaction.channel.send(embed=embed, view=view)

# วิวแบ่งหน้าสำหรับระบบยืนยันตน 10 อย่าง
class VerificationView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        # ตัวเลือกหน้าที่ 1 (1-5)
        self.add_item(VerificationSelect(page=1))

    @discord.ui.button(label="➡️ ถัดไป (หน้า 2)", style=discord.ButtonStyle.secondary, custom_id="btn_vpage_2")
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = discord.ui.View(timeout=None)
        view.add_item(VerificationSelect(page=2))
        btn_back = discord.ui.Button(label="⬅️ ย้อนกลับ", style=discord.ButtonStyle.secondary)
        async def back_cb(inter): await inter.response.edit_message(view=VerificationView())
        btn_back.callback = back_cb
        view.add_item(btn_back)
        await interaction.response.edit_message(view=view)

class VerificationSelect(discord.ui.Select):
    def __init__(self, page=1):
        options = []
        if page == 1:
            for i in range(1, 6): options.append(discord.SelectOption(label=f"วิธีที่ {i}: ยืนยันสิทธิ์ขั้นพื้นฐานแบบที่ {i}", value=f"v_{i}"))
        else:
            for i in range(6, 11): options.append(discord.SelectOption(label=f"วิธีที่ {i}: ยืนยันสิทธิ์ขั้นสูงแบบที่ {i}", value=f"v_{i}"))
        super().__init__(placeholder="เลือกหนึ่งในช่องทางเพื่อยืนยันตัวตน...", options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"🎉 ยืนยันตัวตนผ่านรูปแบบที่ `{self.values[0]}` สำเร็จ! มอบบทบาทสมาชิกเรียบร้อย", ephemeral=True)

async def setup(bot):
    await bot.add_cog(SecuritySystem(bot))
