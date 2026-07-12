# ชื่อไฟล์: cogs/economy_system.py
import discord
from discord import app_commands
from discord.ext import commands
import json
import random

class EconomySystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_user_money(self, user_id):
        with open("database.json", "r", encoding="utf-8") as f:
            db = json.load(f)
        return db.get(f"money_{user_id}", 0)

    def add_user_money(self, user_id, amount):
        with open("database.json", "r", encoding="utf-8") as f:
            db = json.load(f)
        db[f"money_{user_id}"] = db.get(f"money_{user_id}", 0) + amount
        with open("database.json", "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=4)

    # 🍊 ระบบหาเงินจากการเก็บผลไม้
    @app_commands.command(name="harvest", description="🍊 ออกไปหาผลไม้ป่าเพื่อนำไปขายสร้างรายได้")
    async def harvest(self, interaction: discord.Interaction):
        fruits = ["🍉 แตงโมยักษ์", "🍊 ส้มหวาน", "🍎 แอปเปิ้ลวิเศษ", "🍇 องุ่นม่วง"]
        selected = random.choice(fruits)
        reward = random.randint(50, 200)
        self.add_user_money(interaction.user.id, reward)
        await interaction.response.send_message(f"🧺 คุณออกเดินทางไปเก็บได้ **{selected}** นำไปขายให้พ่อค้าแอดมิน ได้รับเงินมา จำนวน **${reward}** 💸")

    # 💰 ตรวจเช็คเงินคงเหลือ
    @app_commands.command(name="balance", description="💰 ตรวจสอบจำนวนเงินคงเหลือในกระเป๋าของคุณ")
    async def balance(self, interaction: discord.Interaction):
        money = self.get_user_money(interaction.user.id)
        await interaction.response.send_message(f"💳 บัญชีของคุณ: **{interaction.user.name}** มีเงินสะสมอยู่ทั้งหมด: **${money}** คอร์น")

    # 🛒 แผงควบคุมระบบร้านค้าแบบสไลด์หน้าสินค้าซ้าย-ขวาอัตโนมัติ
    @app_commands.command(name="shop", description="🛒 เปิดระบบร้านค้าดิสคอร์ดเลือกซื้อไอเทมตกแต่งและยศ")
    async def open_shop(self, interaction: discord.Interaction):
        # สร้างสินค้าจำลองขึ้นมา 15 ชิ้น เพื่อทดสอบขีดจำกัดหน้าตาการสไลด์เลื่อนแถบ
        shop_items = [f"🎁 สินค้าไอเทมชิ้นที่ {i}" for i in range(1, 16)]
        view = ShopPaginationView(shop_items)
        embed = view.make_embed()
        await interaction.response.send_message(embed=embed, view=view)

# คลาสประมวลผลการสไลด์หน้าสินค้าซ้ายขวาในกรณีไอเทมเกิน 10 รายการ
class ShopPaginationView(discord.ui.View):
    def __init__(self, items):
        super().__init__(timeout=60)
        self.items = items
        self.current_page = 0
        self.items_per_page = 8 # หน้าละ 8 ชิ้นเพื่อความสวยงามสแกนง่าย

    def make_embed(self):
        start = self.current_page * self.items_per_page
        end = start + self.items_per_page
        page_items = self.items[start:end]
        
        embed = discord.Embed(title="🛒 ร้านค้าสวัสดิการชุมชน", color=0xffaa00)
        for i, item in enumerate(page_items, start=start+1):
            embed.add_field(name=f"{i}. {item}", value=f"ราคา: `${100 * i}`", inline=True)
        embed.set_footer(text=f"หน้า {self.current_page + 1} / {(len(self.items)-1)//self.items_per_page + 1}")
        return embed

    @discord.ui.button(label="◀️ เลื่อนซ้าย", style=discord.ButtonStyle.blurple)
    async def prev_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            await interaction.response.edit_message(embed=self.make_embed(), view=self)
        else:
            await interaction.response.send_message("⏮️ นี่คือหน้าแรกสุดแล้วครับ!", ephemeral=True)

    @discord.ui.button(label="เลื่อนขวา ▶️", style=discord.ButtonStyle.blurple)
    async def next_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        if (self.current_page + 1) * self.items_per_page < len(self.items):
            self.current_page += 1
            await interaction.response.edit_message(embed=self.make_embed(), view=self)
        else:
            await interaction.response.send_message("⏭️ นี่คือหน้าสุดท้ายแล้วครับ!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(EconomySystem(bot))
