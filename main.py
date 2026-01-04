import discord
from discord import app_commands
import random
from datetime import datetime

class MyBot(discord.Client):
    def __init__(self):
        # 인텐트 설정 (기본값)
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # 슬래시 명령어 서버 동기화
        await self.tree.sync()

    async def on_ready(self):
        # activity=None으로 설정하여 상태 메시지를 삭제합니다
        await self.change_presence(status=discord.Status.online, activity=None)
        print(f'{self.user.name}이(가) 상태 메시지 없이 로그인되었습니다!')

bot = MyBot()

@bot.tree.command(name="추천", description="도도봇의 도박 종목 추천")
async def recommend(interaction: discord.Interaction):
    items = ["주사위", "배치", "발로", "룰렛", "수능", "마크", "소개팅"]
    selected_item = random.choice(items)
    selected_num = random.randint(1, 20)
    
    embed = discord.Embed(
        title="도도봇 도박 추천",
        description=f"추천하는 종목은 **{selected_item}**이며,\n**{selected_num}번째**에 올인하시는 것을 추천드립니다.",
        color=0x2ecc71,
        timestamp=datetime.now()
    )
    
    # 닉네임 대신 고유 사용자명이 나오도록 설정
    embed.set_author(
        name=interaction.user.name, 
        icon_url=interaction.user.display_avatar.url
    )
    
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.set_footer(text="좋은 결과가 있기를 바랍니다.")
    
    await interaction.response.send_message(embed=embed)

# 여기에 본인의 봇 토큰을 입력하세요
bot.run("MTQ1NzQ1NDk3MDMxMDg4NTU5Mg.GCeJQv.o7zDl7CXgob7Poj-proRWo4Hv-uox4S3wSec5Q")
