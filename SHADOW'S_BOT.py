import discord
import random
from random import choice
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.command(aliases=['ask_shadow'])
async def shadow_says(ctx, *, question):
    responses = ['that would make aqua cry again, so.. no way',
                 'i would rather watch gundam seed, absolutely not',
                 'like being asked if you would take sailor moon to be your wife, YES!',
                 'the answer is equivelent to the question is hatsune mikus singing good, oh yes',
                 'no baka!',
                 'if i told you that you could be transported into a harem anime as the protagonist what would you say? YES',
                 'thats like saying the berserk anime had godlike animation... NOOOO',
                 'hai',
                 'i rather give up on real girls and buy a waifu, nope',
                 'in the words of happy from fairytail: aiye!!!',
                 'if you really mean that, im going to take out a loan and disappear into the yakuza',
                 'you are as correct as the overlord ains ooal gown']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run('')
