from datetime import datetime

import discord
from discord.ext import commands

from modules.sanction import Sanction
from modules.utils.db import Settings
from modules.utils.format import Mod


class Checks:

    @staticmethod
    async def member_check(member: discord.Member):
        guild = member.guild
        now = datetime.now()
        create = member.created_at

        strike = await Settings().get_strike_settings(str(guild.id), str(member.id))

        sanctions = len(strike)
        time = (now - create).days

        return sanctions, time


class Automod(commands.Cog):
    conf = {}

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if (
                not message.guild
                or message.author.bot
        ):
            return

        set = await Settings().get_server_settings(str(message.guild.id))

        if "automod" not in set:
            return

        if set["automod"] is True:
            if "discord.gg/" in message.content:
                await message.delete()
                await Sanction().create_strike(message.author, "Strike", message.guild, "Discord invite link")
            if len(message.mentions) > 5:
                await message.delete()
                await Sanction().create_strike(message.author, "Strike", message.guild, "Mentions Spam")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """

        :param member: The member who joined the guild
        """
        guild = member.guild
        set = await Settings().get_server_settings(str(guild.id))
        glob = await Settings().get_glob_settings()

        # Check if the user has already been muted to avoid any sanctions bypass
        if 'Mute' in set and member.id in set['Mute']:
            # Mute him again
            for chan in guild.text_channels:
                await chan.set_permissions(member, send_messages=False)
                await Sanction().create_strike(member.author, "Strike", member.guild, "Try to mute Bypass")

        # Check if the user is in the blacklist
        if 'Blacklist' in glob:
            if member.id in glob['Blacklist'] and set["bl"] is True:
                # Ban the member
                await guild.ban(member, reason="Blacklist")
            try:
                await member.send("you're in the blacklist ! If you think it's an error, ask here --> "
                              "yume.network@protonmail.com")
            except discord.Forbidden:
                return

        if set['logging'] is True:
            sanctions, time = await Checks().member_check(member)
            em = await Mod().check_embed(member, guild, sanctions, time)
            if 'LogChannel' in set:
                channel = self.bot.get_channel(int(set['LogChannel']))
                try:
                    await channel.send(embed=em)
                except discord.Forbidden:
                    return


def setup(bot):
    bot.add_cog(Automod(bot))
