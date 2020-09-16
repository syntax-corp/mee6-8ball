from plugin import Plugin
from discord.ext import commands
import random


class _8ball(Plugin):

    is_global = True

    client = commands.Bot(command_prefix="!")

    @client.command(aliases=['8ball'])
    async def _8ball(ctx, *, question):
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        embed = discord.Embed(title="Magic 8 Ball", desc="", color=discord.Color.red())
        embed.add_field(name=":8ball:", value=random.choice(responses))
        await ctx.send(embed=embed)
