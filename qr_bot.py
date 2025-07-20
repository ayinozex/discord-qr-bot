import discord
from discord.ext import commands
import os
from dotenv import load_dotenv  # เพิ่มบรรทัดนี้

load_dotenv()  # โหลดค่าในไฟล์ .env

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ บอทพร้อมใช้งานแล้ว: {bot.user}")

@bot.command()
async def qr(ctx, *, text: str = "Hello from Discord!"):
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={text}"
    embed = discord.Embed(title="QR Code ของคุณ", color=0x00ff00)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1396209667457417346/1396540086149189752/34F4C865-36C2-4041-8152-3ABE30673664.jpg?ex=687e74ce&is=687d234e&hm=cf0ee8b53af9d506a1ca9481d4cc70c5c47ef835379790f9acf56482bc53445a&")
    await ctx.send(f"{ctx.author.mention} นี่คือ QR Code ของคุณ:", embed=embed)

# ดึง token จาก .env
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
