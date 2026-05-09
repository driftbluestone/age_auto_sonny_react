import random, discord
from discord.ext import commands
sonny_list = ["frog", "sonny", "toad"]
reply_list = [":frog: Sonny the frog here to help!", ":frog: It seems I have been summoned!", ":frog: \*Ribbit*"]
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Sonny(bot=bot))

class Sonny(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        msg = message.content
        if message.author.bot: return
        if not any(sonny in msg.lower() for sonny in sonny_list): return
        await message.add_reaction("<:hyper_sonny:1471660647598002402>")
        if random.randint(1,100) == 100:
            await message.reply(random.choice(reply_list))