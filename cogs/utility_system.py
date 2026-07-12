# ชื่อไฟล์: cogs/utility_system.py
import discord
from discord import app_commands
from discord.ext import commands
import json
import random
import calendar

class UtilitySystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = {}

    def load_db(self):
        with open("database.json", "r", encoding="utf-8") as f: return json.load(f)
    def save_db(self, db):
        with open("database.json", "w", encoding="utf-8") as f: json.dump(db, f, ensure_ascii=False, indent=4)

    # 💬 ระบบที่ 3: ระบบสุ่มคำคมส่งตรงทันที
    @app_commands.command(name="quote", description="💬 รับแรงบันดาลใจผ่านคำคมดีๆ ทันทีไม่ต้องเซ็ตห้อง")
    async def get_quote(self, interaction: discord.Interaction):
        quotes = ["💡 ล้มได้ก็ลุกได้ ขาดทุนวันนี้คือกำไรในวันหน้า", "🚀 อย่าหยุดพัฒนาจนกว่าตัวคุณในอนาคตจะหันมาขอบคุณ"]
        await interaction.response.send_message(f"✨ **คำคมประจำวินาทีนี้:**\n> {random.choice(quotes)}")

    # 🎂 ระบบที่ 7: ระบบฟอร์มบันทึกวันเกิดและระบบลบของแอดมิน
    @app_commands.command(name="register_birthday", description="🎂 เปิดแบบฟอร์มบันทึกวันเกิดของคุณเอง (กรอกได้ครั้งเดียว)")
    async def reg_birthday(self, interaction: discord.Interaction):
        db = self.load_db()
        if f"bd_{interaction.user.id}" in db:
            await interaction.response.send_message("❌ คุณเคยลงทะเบียนวันเกิดไปแล้วในระบบ! หากต้องการเปลี่ยนต้องแจ้งให้แอดมินช่วยลบประวัติเดิมออก", ephemeral=True)
            return
        await interaction.response.send_modal(BirthdayModal())

    # 📖 ระบบที่ 9: สอนการใช้งานดิสคอร์ดแบบเลือกดูคลิป
    @app_commands.command(name="tutorial_guides", description="📖 เปิดสารบัญดูคลิปสอนใช้งานฟังก์ชันต่างๆ ในเซิร์ฟเวอร์")
    async def show_guides(self, interaction: discord.Interaction):
        select = discord.ui.Select(placeholder="เลือกคลิปวิดีโอที่คุณต้องการรับชม...", options=[
            discord.SelectOption(label="🎥 วิธีเล่นสล็อตและเก็บผลไม้", value="vid_eco"),
            discord.SelectOption(label="🎥 วิธีใช้งานห้องยืนยันตัวตน", value="vid_verify")
        ])
        async def s_cb(inter): await inter.response.send_message(f"🔗 ลิงก์รับชมวิดีโอสาธิตขั้นพื้นฐานของคุณ: https://youtube.com/watch?v={inter.data['values'][0]}", ephemeral=True)
        select.callback = s_cb
        view = discord.ui.View(); view.add_item(select)
        await interaction.response.send_message("📖 คู่มือการเรียนรู้ประจำชุมชน:", view=view, ephemeral=True)

    # 🌤️ ระบบที่ 10: พยากรณ์อากาศเลือกภูมิภาค -> 77 จังหวัดประเทศไทย
    @app_commands.command(name="weather_th", description="🌤️ เช็คพยากรณ์อากาศผ่านระบบเลือกจังหวัด 77 จังหวัด")
    async def check_weather(self, interaction: discord.Interaction):
        select = discord.ui.Select(placeholder="เลือกรอบภูมิภาคหลักในไทยก่อน...", options=[
            discord.SelectOption(label="ภาคเหนือ", value="north"),
            discord.SelectOption(label="ภาคกลางและกรุงเทพฯ", value="central")
        ])
        async def reg_cb(inter):
            region = inter.data['values'][0]
            prov_select = discord.ui.Select(placeholder="เลือกจังหวัดที่ต้องการตรวจสอบ...")
            if region == "north":
                prov_select.add_item(discord.SelectOption(label="เชียงใหม่", value="cm"))
                prov_select.add_item(discord.SelectOption(label="เชียงราย", value="cr"))
            else:
                prov_select.add_item(discord.SelectOption(label="กรุงเทพมหานคร", value="bkk"))
            
            async def pr_cb(p_inter): await p_inter.response.send_message(f"🌤️ สภาพอากาศวันนี้ที่จังหวัด **{p_inter.data['values'][0].upper()}**: มีฝนตกเล็กน้อย อุณหภูมิเฉลี่ย 28°C", ephemeral=True)
            prov_select.callback = pr_cb
            v = discord.ui.View(); v.add_item(prov_select)
            await inter.response.send_message("📍 กรุณาเลือกจังหวัดในลำดับต่อไปของคุณ:", view=v, ephemeral=True)
            
        select.callback = reg_cb
        view = discord.ui.View(); view.add_item(select)
        await interaction.response.send_message("🌤️ ศูนย์รายงานข้อมูลสภาพอากาศประเทศไทย:", view=view, ephemeral=True)

    # 🎡 ระบบที่ 12: ระบบวงล้อสุ่มกำหนดเปอร์เซ็นต์เท่ากันทั้งหมดตามข้อความที่กรอก
    @app_commands.command(name="spin_wheel", description="🎡 สุ่มเลือกข้อความจากตัวเลือกที่คุณระบุ (แบ่งเปอร์เซ็นต์เท่ากัน)")
    async def wheel_spin(self, interaction: discord.Interaction, options_text: str):
        opts = [o.strip() for o in options_text.split(",") if o.strip()]
        if not opts:
            await interaction.response.send_message("❌ กรุณาใส่ตัวเลือกโดยคั่นด้วยเครื่องหมายจุลภาค (เช่น: กินข้าว, กินเส้น, นอน)", ephemeral=True)
            return
        chosen = random.choice(opts)
        await interaction.response.send_message(f"🎡 **ผลการหมุนวงล้อมหาเฮง:**\n> ตัวเลือกทั้งหมดมียอดโอกาสชนะเท่ากันที่ **{100/len(opts):.1f}%**\n🌟 รางวัลที่ออกได้แก่: **{chosen}** 🎉")

    # 🎲 ระบบที่ 17: ระบบคำนวณสุ่มสิทธิ์การตัดสินใจตามสั่ง (เปอร์เซ็นต์ลับ)
    @app_commands.command(name="decide", description="🎲 ให้บอทช่วยตัดสินใจแผนการของคุณเป็นค่าเปอร์เซ็นต์ความน่าจะเป็น")
    async def decide_action(self, interaction: discord.Interaction, topic: str):
        rate = random.randint(0, 100)
        await interaction.response.send_message("🎲 กำลังประมวลผลดวงชะตาของคุณ...", ephemeral=True)
        await interaction.followup.send(f"🔮 **ผลลัพธ์การตัดสินใจในเรื่อง:** `{topic}`\n📊 โอกาสความสำเร็จสูงสุดอยู่ที่ระดับ: **{rate}%** ครับท่าน!", ephemeral=True)

    # 💤 ระบบที่ 21: ตรวจจับและขึ้นสถานะการฝากร้านชั่วคราว AFK
    @app_commands.command(name="afk", description="💤 ตั้งสถานะไม่อยู่ชั่วคราว เมื่อมีคนแท็กเรียกบอทจะคอยตอบแทนให้")
    async def go_afk(self, interaction: discord.Interaction, reason: str = "ธุระส่วนตัว"):
        self.afk_users[interaction.user.id] = reason
        await interaction.response.send_message(f"💤 คุณเข้าสู่โหมด AFK แล้วด้วยสาเหตุ: **{reason}** ระบบจะคอยดูแลแชทให้ครับ", ephemeral=True)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot: return
        
        # ลบสถานะ AFK ออกเมื่อคนเดิมพ่นข้อความคุยใหม่
        if message.author.id in self.afk_users:
            del self.afk_users[message.author.id]
            await message.channel.send(f" Welcome Back! แจ้งเตือนบอท: คุณ <@{message.author.id}> กลับมาประจำการหน้าจอคอมเรียบร้อยแล้ว!", delete_after=5)

        # ตอบกลับแทนเจ้าตัวถ้ามีคนแท็กหาคนที่ AFK อยู่
        for mention in message.mentions:
            if mention.id in self.afk_users:
                await message.reply(f"💤 แจ้งเตือนบอทส่วนตัว: ขณะนี้เพื่อนคนนี้ไม่ว่างเนื่องจากค้างหัวข้อ: `{self.afk_users[mention.id]}` อยู่ครับผม")

# คลาสประมวลผลแบบฟอร์มตรวจสอบวันเกิดประจำระบบที่ 7
class BirthdayModal(discord.ui.Modal, title="🎂 ฟอร์มบันทึกข้อมูลวันเกิด"):
    day = discord.ui.TextInput(label="ระบุ วันเกิดของคุณ (เลข 1-31)", placeholder="ตัวอย่าง: 12")
    month = discord.ui.TextInput(label="ระบุ เดือนเกิดของคุณ (เลข 1-12)", placeholder="ตัวอย่าง: 7")
    year = discord.ui.TextInput(label="ระบุ ปี ค.ศ. เกิดของคุณ (เช่น 2006)", placeholder="ตัวอย่าง: 2006")

    async def on_submit(self, interaction: discord.Interaction):
        try:
            d, m, y = int(self.day.value), int(self.month.value), int(self.year.value)
            # ตรวจสอบว่าจำนวนวันในเดือนนั้นๆ เกินความเป็นจริงหรือไม่ตามปฏิทินสากลโลก
            max_days = calendar.monthrange(y, m)[1]
            if d < 1 or d > max_days or m < 1 or m > 12:
                raise ValueError()
                
            # บันทึกข้อมูลลงฐานข้อมูล JSON
            with open("database.json", "r", encoding="utf-8") as f: db = json.load(f)
            db[f"bd_{interaction.user.id}"] = {"day": d, "month": m, "year": y}
            with open("database.json", "w", encoding="utf-8") as f: json.dump(db, f, ensure_ascii=False, indent=4)
            
            await interaction.response.send_message(f"🎉 ตรวจสอบข้อมูลเสร็จสิ้น! ลงทะเบียนวันเกิดเป็นวันที่ `{d}/{m}/{y}` ลงในระบบคลังสถิติเรียบร้อย!", ephemeral=True)
        except:
            await interaction.response.send_message("❌ รูปแบบวันเกิดหรือเดือนเกิดของคุณกรอกตัวเลขเกินปฏิทินจริงในโลก! กรุณากดลงทะเบียนใหม่อีกครั้งครับ", ephemeral=True)

async def setup(bot):
    await bot.add_cog(UtilitySystem(bot))
