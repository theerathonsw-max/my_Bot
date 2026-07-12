# ชื่อไฟล์: cogs/admin_system.py
import discord
from discord import app_commands
from discord.ext import commands
import json
import calendar

class AdminSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def load_db(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_db(self, filename, data):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # เช็คสิทธิ์แอดมิน
    def is_admin(interaction: discord.Interaction) -> bool:
        return interaction.user.guild_permissions.administrator

    # ⚙️ ระบบตั้งช่อง (ใช้ได้เฉพาะแอดมิน)
    @app_commands.command(name="set_channel", description="⚙️ ตั้งค่าห้องสำหรับระบบต่างๆ (แอดมินเท่านั้น)")
    @app_commands.check(is_admin)
    @app_commands.choices(system=[
        app_commands.Choice(name="ระบบตรวจคนเข้า/โทร", value="logs_channel"),
        app_commands.Choice(name="ระบบเปลี่ยนชื่อ", value="rename_channel"),
        app_commands.Choice(name="ระบบคืนยศ", value="restore_channel"),
        app_commands.Choice(name="ระบบวันเกิด", value="birthday_channel"),
        app_commands.Choice(name="ระบบร้านค้า", value="shop_channel"),
        app_commands.Choice(name="ระบบพยากรณ์อากาศ", value="weather_channel"),
        app_commands.Choice(name="ระบบยืนยันตัวตน", value="verify_channel")
    ])
    async def set_channel(self, interaction: discord.Interaction, system: str, channel: discord.TextChannel):
        config = self.load_db("config.json")
        guild_id = str(interaction.guild_id)
        if guild_id not in config: config[guild_id] = {}
        config[guild_id][system] = channel.id
        self.save_db("config.json", config)
        await interaction.response.send_message(f"✅ ตั้งค่าห้องระบบ `{system}` ไปที่ {channel.mention} เรียบร้อย!", ephemeral=True)

    # 📝 ระบบที่ 4: พาเนลเปลี่ยนชื่อแบบมีรูปภาพและแบบฟอร์ม Modal
    @app_commands.command(name="setup_rename", description="🎨 สร้างห้องเปลี่ยนชื่อพร้อมรูปภาพ (แอดมินเท่านั้น)")
    @app_commands.check(is_admin)
    async def setup_rename(self, interaction: discord.Interaction, embed_image: str = None):
        embed = discord.Embed(title="📝 เปลี่ยนชื่อของคุณในดิสคอร์ด", description="คลิกปุ่มด้านล่างเพื่อทำการยื่นเรื่องขอเปลี่ยนชื่อ", color=0x00ffcc)
        if embed_image: embed.set_image(url=embed_image)
        
        view = discord.ui.View(timeout=None)
        btn = discord.ui.Button(label="📝 คลิกเพื่อเปลี่ยนชื่อ", style=discord.ButtonStyle.primary, custom_id="btn_rename_start")
        
        async def rename_callback(inter: discord.Interaction):
            await inter.response.send_modal(RenameModal())
            
        btn.callback = rename_callback
        view.add_item(btn)
        await interaction.response.send_message("สร้างแผงควบคุมสำเร็จ!", ephemeral=True)
        await interaction.channel.send(embed=embed, view=view)

    # 👑 ระบบที่ 5: ระบบจำยศอัตโนมัติและคืนยศ
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # เก็บข้อมูลยศตลอดเวลา
        if before.roles != after.roles:
            db = self.load_db("database.json")
            user_id = str(after.id)
            role_ids = [role.id for role in after.roles if not role.is_default()]
            db[f"roles_{user_id}"] = role_ids
            self.save_db("database.json", db)

    @app_commands.command(name="setup_restore", description="👑 สร้างปุ่มคืนยศอัตโนมัติ (แอดมินเท่านั้น)")
    @app_commands.check(is_admin)
    async def setup_restore(self, interaction: discord.Interaction, image_url: str = None):
        embed = discord.Embed(title="👑 ระบบคืนยศอัตโนมัติ", description="หากยศหาย หรือเพิ่งกลับเข้าดิสคอร์ด กดปุ่มด้านล่างเพื่อดึงยศเดิมคืนมาได้ทันที", color=0xffd700)
        if image_url: embed.set_image(url=image_url)
        
        view = discord.ui.View(timeout=None)
        btn = discord.ui.Button(label="🔄 ดึงยศคืนของฉัน", style=discord.ButtonStyle.success, custom_id="btn_restore_roles")
        
        async def restore_callback(inter: discord.Interaction):
            db = self.load_db("database.json")
            saved_roles = db.get(f"roles_{inter.user.id}", [])
            
            # ส่งข้อความลับเห็นคนเดียวบอกว่ามียศอะไรบ้าง
            role_mentions = [f"<@&{rid}>" for rid in saved_roles]
            await inter.response.send_message(f"👁️ ยศเดิมที่คุณเคยมี: {', '.join(role_mentions) if role_mentions else 'ไม่พบประวัติยศของคุณ'}", ephemeral=True)
            
            # ส่งไปห้องแอดมินเพื่อกดยืนยัน
            config = self.load_db("config.json")
            admin_ch_id = config.get(str(inter.guild_id), {}).get("restore_channel")
            if admin_ch_id:
                admin_ch = inter.guild.get_channel(admin_ch_id)
                if admin_ch:
                    admin_embed = discord.Embed(title="🔔 คำขอคืนยศ", description=f"ผู้ใช้ {inter.user.mention} ต้องการคืนยศทั้งหมดดังนี้:\n{', '.join(role_mentions)}")
                    admin_view = discord.ui.View(timeout=None)
                    confirm_btn = discord.ui.Button(label="อนุมัติคืนยศ", style=discord.ButtonStyle.success)
                    
                    async def cf_callback(act_inter: discord.Interaction):
                        for rid in saved_roles:
                            role = act_inter.guild.get_role(rid)
                            if role: await inter.user.add_roles(role)
                        await act_inter.response.send_message(f"✅ คืนยศให้ {inter.user.name} สำเร็จ!", ephemeral=False)
                    
                    confirm_btn.callback = cf_callback
                    admin_view.add_item(confirm_btn)
                    await admin_ch.send(embed=admin_embed, view=admin_view)
                    
        btn.callback = restore_callback
        view.add_item(btn)
        await interaction.response.send_message("ติดตั้งระบบคืนยศสำเร็จ", ephemeral=True)
        await interaction.channel.send(embed=embed, view=view)

    # 🗑️ ระบบที่ 13: ลบข้อความด่วน
    @app_commands.command(name="clear", description="🗑️ ลบข้อความตามจำนวนที่กำหนด (แอดมินเท่านั้น)")
    @app_commands.check(is_admin)
    async def clear_messages(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer(ephemeral=True)
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.followup.send(f"🧹 ลบข้อความเรียบร้อยแล้วจำนวน {len(deleted)} ข้อความ!", ephemeral=True)

    # 📩 ระบบที่ 18: ระบบส่งเมลแจ้งเตือนคนทั้งดิสคอร์ด
    @app_commands.command(name="send_mail", description="📩 ส่งข้อความประกาศหาทุกคนในดิสคอร์ด")
    @app_commands.check(is_admin)
    async def send_mail(self, interaction: discord.Interaction, message: str, image_url: str = None):
        await interaction.response.send_message("🚀 กำลังส่งข้อความหาทุกคนในเซิร์ฟเวอร์...", ephemeral=True)
        embed = discord.Embed(title="📢 จดหมายข่าวสารจากแอดมิน", description=message, color=0xff0055)
        if image_url: embed.set_image(url=image_url)
        
        for member in interaction.guild.members:
            if not member.bot:
                try:
                    await member.send(embed=embed)
                except:
                    continue

# ฟอร์มเปลี่ยนชื่อสำหรับระบบที่ 4
class RenameModal(discord.ui.Modal, title="📝 ฟอร์มการเปลี่ยนชื่อ"):
    name_input = discord.ui.TextInput(label="ต้องการเปลี่ยนชื่อเป็นชื่ออะไร?", placeholder="ระบุชื่อใหม่ของคุณ...")
    confirm_input = discord.ui.TextInput(label="ยืนยันหรือไม่? (พิมพ์คำว่า 'ยืนยัน')", placeholder="พิมพ์คำว่า ยืนยัน หากแน่ใจ")

    async def on_submit(self, interaction: discord.Interaction):
        if self.confirm_input.value.strip() == "ยืนยัน":
            try:
                await interaction.user.edit(nick=self.name_input.value)
                await interaction.response.send_message(f"✨ เปลี่ยนชื่อเล่นของคุณเป็น **{self.name_input.value}** สำเร็จแล้ว!", ephemeral=True)
            except:
                await interaction.response.send_message("❌ เกิดข้อผิดพลาด บอทไม่มีอำนาจแก้ไขชื่อของคุณ", ephemeral=True)
        else:
            await interaction.response.send_message("❌ ยกเลิกแล้วเนื่องจากพิมพ์คำยืนยันไม่ถูกต้อง", ephemeral=True)

async def setup(bot):
    await bot.add_cog(AdminSystem(bot))
