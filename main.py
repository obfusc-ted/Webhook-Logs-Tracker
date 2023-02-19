import discord
from discord.ext import commands
import requests

token = ""

webhook_url = ""

client = commands.Bot(command_prefix="!", intents=discord.Intents.all()) # Enable all intents from Discord Developer Portal.

@client.event
async def on_guild_join(guild):
    inviter = None
    async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add, limit=5):
        if entry.target.id == client.user.id:
            inviter = entry.user

    req = requests.post(webhook_url, headers={'authorization':f'Bot {token}'}, json={'content':f'{inviter.name} invited the bot'})

client.run(token)
