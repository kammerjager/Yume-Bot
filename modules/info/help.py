#  Copyright (c) 2019.
#  MIT License
#
#  Copyright (c) 2019 YumeNetwork
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


#
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#
import discord
from discord.ext import commands

from modules.utils.format import Embeds


class Help(commands.Cog):
    conf = {}

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def bot(self, ctx):
        await ctx.send(f"**{ctx.author.name}**, this is my URL: \n<{discord.utils.oauth_url(self.bot.user.id)}>")

    @staticmethod
    async def command_help(ctx, bot: discord.User, command: str, description: str, usage: str, example: str = None,
                           permission: str = None):
        embed = await Embeds().command_help(ctx, bot, command, description, usage, example, permission)
        await ctx.send(embed=embed)

    @commands.group(aliases=["c", "commands", "h"])
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = await Embeds().format_commands_embed(ctx, self.bot.user.avatar_url)
            await ctx.send(embed=embed)

    @help.command()
    async def general(self, ctx):
        liste = "`jump`, `weather`, `gweather`, `afk`, `pokemon`, `anime`, `manga`, `character`, `anilist`"
        embed = await Embeds().format_cat_embed(ctx, self.bot.user.avatar_url, "General", liste)
        await ctx.send(embed=embed)

    @help.command()
    async def jump(self, ctx):
        await self.command_help(ctx, self.bot.user, "Jump", "Create a link to a message",
                                "--jump <message_id> [#channel]", "`--jump 645687761906434261 #general`")

    @help.command()
    async def meteo(self, ctx):
        await self.command_help(ctx, self.bot.user, "Weather", "Gives a city's weather forecast",
                                "--weather <city>",
                                "`--weather Paris`\n`--gweather Paris`")

    @help.command()
    async def afk(self, ctx):
        await self.command_help(ctx, self.bot.user, "Afk", "Set your profile to AFK", "--afk")

    @help.command()
    async def pokemon(self, ctx):
        await self.command_help(ctx, self.bot.user, "Pokemon", "Show pokemon info", "--pokemon <pokemon_name>",
                                "`--pokemon pikachu`")

    @help.command()
    async def anime(self, ctx):
        await self.command_help(ctx, self.bot.user, "Anime", "Shows information about an anime", "--anime <anime_name>",
                                "`--anime Naruto`")

    @help.command()
    async def manga(self, ctx):
        await self.command_help(ctx, self.bot.user, "Manga", "Shows information about a manga", "--manga <manga_name>",
                                "`--manga SAO`")

    @help.command()
    async def character(self, ctx):
        await self.command_help(ctx, self.bot.user, "Character", "Shows information about a manga/anime character",
                                "--character <character_name>",
                                "`--character Totoro`")

    @help.command()
    async def anilist(self, ctx):
        await self.command_help(ctx, self.bot.user, "Anilist", "Shows information about an anilist", "--anilist <user>",
                                "`--anilist yumenetwork`")

    @help.command()
    async def utils(self, ctx):
        liste = "`here`, `members`, `owner`, `age`, `whois`, `hackwhois`, " \
                "`avatar`, `icon`, `roleinfo`, `invite`, `channelinfo`, `tags`, `tag`"
        embed = await Embeds().format_cat_embed(ctx, self.bot.user.avatar_url, "Utils", liste)
        await ctx.send(embed=embed)

    @help.command()
    async def roleinfo(self, ctx):
        await self.command_help(ctx, self.bot.user, "RoleInfo", "Shows the information of a role", "--roleinfo <@role>",
                                "`--roleinfo @Member`")

    @help.command()
    async def channelinfo(self, ctx):
        await self.command_help(ctx, self.bot.user, "ChannelInfo", "Shows the information of a channel",
                                "--channelinfo <#channel>",
                                "`--channelinfo #general`")

    @help.command()
    async def invite(self, ctx):
        await self.command_help(ctx, self.bot.user, "Invite", "Gives a guild invitation", "--invite")

    @help.command()
    async def tags(self, ctx):
        await self.command_help(ctx, self.bot.user, "Tags", "Shows all tags", "--tags")

    @help.command()
    async def tag(self, ctx):
        await self.command_help(ctx, self.bot.user, "Tag", "Use a tag", "--tag <tag>", "`--tag vote`")

    @help.command()
    async def here(self, ctx):
        await self.command_help(ctx, self.bot.user, "Here", "Shows information about this guild", "--here")

    @help.command()
    async def members(self, ctx):
        await self.command_help(ctx, self.bot.user, "Members", "Shows members count", "--members")

    @help.command()
    async def owner(self, ctx):
        await self.command_help(ctx, self.bot.user, "Owner", "Shows the guild's owner", "--owner")

    @help.command()
    async def age(self, ctx):
        await self.command_help(ctx, self.bot.user, "Age", "Show the age of an account", "--age <@user>",
                                "`--age @YumeBot`")

    @help.command()
    async def whois(self, ctx):
        await self.command_help(ctx, self.bot.user, "Whois", "Show account information", "--whois <@user>",
                                "`--whois @YumeBot`")

    @help.command()
    async def hackwhois(self, ctx):
        await self.command_help(ctx, self.bot.user, "HackWhois", "Show account information using an id",
                                "--hackwhois <user_id>", "`--hackwhois 282233191916634113`")

    @help.command()
    async def avatar(self, ctx):
        await self.command_help(ctx, self.bot.user, "Avatar", "Steals a user's avatar", "--avatar <@user>",
                                "`--avatar @YumeBot`")

    @help.command()
    async def icon(self, ctx):
        await self.command_help(ctx, self.bot.user, "Icon", "Steals the guild's icon", "--icon")

    @help.command()
    async def info(self, ctx):
        liste = "`about`, `help`, `suggestion`, `feedback`"
        embed = await Embeds().format_cat_embed(ctx, self.bot.user.avatar_url, "Info", liste)
        await ctx.send(embed=embed)

    @help.command()
    async def about(self, ctx):
        await self.command_help(ctx, self.bot.user, "About", "Shows bot information", "--about")

    @help.command()
    async def suggestion(self, ctx):
        await self.command_help(ctx, self.bot.user, "Suggestion", "Create a suggestion post", "--suggestion")

    @help.command()
    async def feedback(self, ctx):
        await self.command_help(ctx, self.bot.user, "Feedback", "Create a feedback", "--feedback <text>",
                                "`--feedback Share this bot because it's an awesome one`")

    @help.command()
    async def mods(self, ctx):
        liste = "`mute`, `unmute`, `ban`, `hackban`, `unban`, `kick`, `purge`, `sanction`," \
                " `strike`, `slowmode`, `deaf`, `undeaf`, `vmute`, `vunmute`, `nick`, `topic`"
        embed = await Embeds().format_cat_embed(ctx, self.bot.user.avatar_url, "Mods", liste)
        await ctx.send(embed=embed)

    @help.command()
    async def mute(self, ctx):
        await self.command_help(ctx, self.bot.user, "Mute", "Mute an user", "--mute <user> <time> [reason]",
                                "`--mute @Yume 10m` - Mute Yume for 10 minutes")

    @help.command()
    async def unmute(self, ctx):
        await self.command_help(ctx, self.bot.user, "UnMute", "UnMute an user", "--mute <user> [reason]",
                                "`--unmute @Yume`")

    @help.command()
    async def ban(self, ctx):
        await self.command_help(ctx, self.bot.user, "Ban", "Ban an user", "--ban <user> [reason]",
                                "`--ban @Jack`")

    @help.command()
    async def hackban(self, ctx):
        await self.command_help(ctx, self.bot.user, "HackBan", "HackBan an user", "--ban <user_id> [reason]",
                                "`--hackban 282233191916634113`")

    @help.command()
    async def unban(self, ctx):
        await self.command_help(ctx, self.bot.user, "UnBan", "UnBan an user", "--unban <user_id>",
                                "`--unban 282233191916634113`")

    @help.command()
    async def kick(self, ctx):
        await self.command_help(ctx, self.bot.user, "Kick", "Kick an user", "--kick <user> [reason]",
                                "`--kick @Tux`")

    @help.command()
    async def purge(self, ctx):
        await self.command_help(ctx, self.bot.user, "Purge", "Purge the channel", "--purge <amount>",
                                "`--purge 100`")

    @help.command()
    async def sanction(self, ctx):
        await self.command_help(ctx, self.bot.user, "Sanction", "Provides information on a sanction report",
                                "--sanction <sanction_id>",
                                "`--sanction 20191225175936694142`")

    # TODO: Refaire une cmd de sanction séparé

    @help.command()
    async def sanctions(self, ctx):
        await self.command_help(ctx, self.bot.user, "Sanctions", "Retrieves the list of sanctions of an user", "--sanctions <user>",
                                "`--sanction @Totoro`")

    @help.command()
    async def strike(self, ctx):
        await self.command_help(ctx, self.bot.user, "Strike", "Strike someone", "--strike <user> [reason]",
                                "`--strike @Apple Stealing Information`")

    @help.command()
    async def mention(self, ctx):
        await self.command_help(ctx, self.bot.user, "mention", "Allows you to mention any role", "--mention <role name>",
        "--mention Moderator")

    @help.command()
    async def annonce(self, ctx):
        await self.command_help(ctx, self.bot.user, "annonce", "Create an announcement", "--annonce <role name> [message]",
        "--annonce @Member Merry Christmas")

    @help.command()
    async def massban(self, ctx):
        await self.command_help(ctx, self.bot.user, "massban", "HackBan multiple users", "--massban [reason] <user_ids>",
        "--massban 187900923014676490")

    @help.command()
    async def reset(self, ctx):
        await self.command_help(ctx, self.bot.user, "reset", "reset a users sanctions", "--reset <user/user_id>",
        "`--rank @Sp8ce`\n`--reset 411926525751853067`")

    @help.command()
    async def addrole(self, ctx):
        await self.command_help(ctx, self.bot.user, "addrole", "Add a role to everyone", "--addrole <role>",
        "--addrole @Member")

    @help.command()
    async def fresh(self, ctx):
        await self.command_help(ctx, self.bot.user, "fresh", "Refresh blacklist", "--fresh")

    @help.command()
    async def poll(self, ctx):
        await self.command_help(ctx, self.bot.user, "poll", "Create a poll", "--poll <question>",
        "--poll What is the game of the month?")

    @help.command()
    async def quickpoll(self, ctx):
        await self.command_help(ctx, self.bot.user, "quickpoll", "Create a poll with a single command", "--quickpoll <question> <answer> <answer> [answers]",
        "--quickpoll \"What do you think about Communism?\" \"Good Idea\" \"Bad idea?\"")

    @help.command()
    async def rank(self, ctx):
        await self.command_help(ctx, self.bot.user, "Rank", "Get someones Rank", "--rank <user/user_id>",
                                "`--rank @Erik`\n`--rank 226870774697426955`")

    @help.command()
    async def level_config(self, ctx):
        await self.command_help(ctx, self.bot.user, "level config", "Set up automatic roles for levels", "--level config <level> <role>",
                                "--level config 10 @No Life")

    @help.command()
    async def leaderboard(self, ctx):
        await self.command_help(ctx, self.bot.user, "leaderboard", "Show the XP leaderboard of your server", "--leaderboard")

    @help.command()
    async def setting_get(self, ctx):
        await self.command_help(ctx, self.bot.user, "setting get", "Show the current server settings", "--setting get")

    @help.command()
    async def setting_reset(self, ctx):
        await self.command_help(ctx, self.bot.user, "setting reset", "Reset the server settings", "--setting reset")

    @help.command()
    async def setting_setup(self, ctx):
        await self.command_help(ctx, self.bot.user, "setting setup", "Set up the server settings", "setting setup")

    @help.command()
    async def setting_role_mod(self, ctx):
        await self.command_help(ctx, self.bot.user, "setting role mod", "Make a role the Moderator role", "--setting role mod <role>",
                                "--setting role mod @Moderator")

    @help.command()
    async def setting_role_admin(self, ctx):
        await self.command_help(ctx, self.bot.user, "setting role admin", "Make a role the Admin role", "--setting role admin <role>",
                                "--setting role admin @Admin")

    @help.command()
    async def arr(self, ctx):
        await self.command_help(ctx, self.bot.user, "arr", "Add a reaction role", "--arr <channel> <message_id> <role> <emoji>",
                                "--arr #choose-role 659832029591896065 @ :regional_indicator_a: ")
    #unfinished
    @help.command()
    async def setting_color(self, ctx):
        await self.command_help(ctx, self.bot.user, "setting color", "Do something only VIP's can", "--setting color",
                                "--setting color")

    @help.command()
    async def color_list(self, ctx):
        await self.command_help(ctx, self.bot.user, "color list", "Show the html color names", "--color list")
    #unfinished
    @help.command()
    async def color_add(self, ctx):
        await self.command_help(ctx, self.bot.user, "color add", "Do something", "--color add <name>",
                                "--color add ")
    #unfinished
    @help.command()
    async def color_remove(self, ctx):
        await self.command_help(ctx, self.bot.user, "color remove", "Do something", "--color remove <name>",
                                "--color remove ")

    @help.command()
    async def color_remove(self, ctx):
        await self.command_help(ctx, self.bot.user, "color remove", "Do something", "--color remove <name>",
                                "--color remove ")

    @help.command()
    async def rd(self, ctx):
        await self.command_help(ctx, self.bot.user, "rd", "Do something", "--rd <name>",
                                "--rd ")

    @help.command()
    async def 8ball(self, ctx):
        await self.command_help(ctx, self.bot.user, "8ball", "Do something", "--8ball <name>",
                                "--8ball ")

    @help.command()
    async def cat(self, ctx):
        await self.command_help(ctx, self.bot.user, "cat", "Do something", "--cat <name>",
                                "--cat ")

    @help.command()
    async def dog(self, ctx):
        await self.command_help(ctx, self.bot.user, "dog", "Do something", "--dog <name>",
                                "--dog ")

    @help.command()
    async def lovepower(self, ctx):
        await self.command_help(ctx, self.bot.user, "lovepower", "Do something", "--lovepower <name>",
                                "--lovepower ")

    @help.command()
    async def choose(self, ctx):
        await self.command_help(ctx, self.bot.user, "choose", "Do something", "--choose <name>",
                                "--choose ")

    @help.command()
    async def linux(self, ctx):
        await self.command_help(ctx, self.bot.user, "linux", "Do something", "--linux <name>",
                                "--linux ")

    @help.command()
    async def number(self, ctx):
        await self.command_help(ctx, self.bot.user, "number", "Do something", "--number <name>",
                                "--number ")

    @help.command()
    async def trump(self, ctx):
        await self.command_help(ctx, self.bot.user, "trump", "Do something", "--trump <name>",
                                "--trump ")

    @help.command()
    async def chucknorris(self, ctx):
        await self.command_help(ctx, self.bot.user, "chucknorris", "Do something", "--chucknorris <name>",
                                "--chucknorris ")

    @help.command()
    async def geek_joke(self, ctx):
        await self.command_help(ctx, self.bot.user, "geek_joke", "Do something", "--geek_joke <name>",
                                "--geek_joke ")

    @help.command()
    async def cookie(self, ctx):
        await self.command_help(ctx, self.bot.user, "cookie", "Do something", "--cookie <name>",
                                "--cookie ")

    @help.command()
    async def today(self, ctx):
        await self.command_help(ctx, self.bot.user, "today", "Do something", "--today <name>",
                                "--today ")

    @help.command()
    async def ice(self, ctx):
        await self.command_help(ctx, self.bot.user, "ice", "Do something", "--ice <name>",
                                "--ice ")

    @help.command()
    async def lmgtfy(self, ctx):
        await self.command_help(ctx, self.bot.user, "lmgtfy", "Do something", "--lmgtfy <name>",
                                "--lmgtfy ")

    @help.command()
    async def love_calc(self, ctx):
        await self.command_help(ctx, self.bot.user, "love_calc", "Do something", "--love_calc <name>",
                                "--love_calc ")

    @help.command()
    async def urban(self, ctx):
        await self.command_help(ctx, self.bot.user, "urban", "Do something", "--urban <name>",
                                "--urban ")

    @help.command()
    async def hug(self, ctx):
        await self.command_help(ctx, self.bot.user, "hug", "Do something", "--hug <name>",
                                "--hug ")

    @help.command()
    async def pat(self, ctx):
        await self.command_help(ctx, self.bot.user, "pat", "Do something", "--pat <name>",
                                "--pat ")

    @help.command()
    async def kiss(self, ctx):
        await self.command_help(ctx, self.bot.user, "kiss", "Do something", "--kiss <name>",
                                "--kiss ")

    @help.command()
    async def lewd(self, ctx):
        await self.command_help(ctx, self.bot.user, "lewd", "Do something", "--lewd <name>",
                                "--lewd ")

    @help.command()
    async def lick(self, ctx):
        await self.command_help(ctx, self.bot.user, "lick", "Do something", "--lick <name>",
                                "--lick ")

    @help.command()
    async def slap(self, ctx):
        await self.command_help(ctx, self.bot.user, "slap", "Do something", "--slap <name>",
                                "--slap ")

    @help.command()
    async def cry(self, ctx):
        await self.command_help(ctx, self.bot.user, "cry", "Do something", "--cry <name>",
                                "--cry ")

    @help.command()
    async def hug(self, ctx):
        await self.command_help(ctx, self.bot.user, "hug", "Do something", "--hug <name>",
                                "--hug ")

    @help.command()
    async def pat(self, ctx):
        await self.command_help(ctx, self.bot.user, "pat", "Do something", "--pat <name>",
                                "--pat ")

    @help.command()
    async def kiss(self, ctx):
        await self.command_help(ctx, self.bot.user, "kiss", "Do something", "--kiss <name>",
                                "--kiss ")

    @help.command()
    async def lewd(self, ctx):
        await self.command_help(ctx, self.bot.user, "lewd", "Do something", "--lewd <name>",
                                "--lewd ")

    @help.command()
    async def lick(self, ctx):
        await self.command_help(ctx, self.bot.user, "lick", "Do something", "--lick <name>",
                                "--lick ")

    @help.command()
    async def slap(self, ctx):
        await self.command_help(ctx, self.bot.user, "slap", "Do something", "--slap <name>",
                                "--slap ")

    @help.command()
    async def cry(self, ctx):
        await self.command_help(ctx, self.bot.user, "cry", "Do something", "--cry <name>",
                                "--cry ")

    @help.command()
    async def truth(self, ctx):
        await self.command_help(ctx, self.bot.user, "truth", "Do something", "--truth <name>",
                                "--truth ")

    @help.command()
    async def dare(self, ctx):
        await self.command_help(ctx, self.bot.user, "dare", "Do something", "--dare <name>",
                                "--dare ")

    @help.command()
    async def wyr(self, ctx):
        await self.command_help(ctx, self.bot.user, "wyr", "Do something", "--wyr <name>",
                                "--wyr ")

    @help.command()
    async def nhie(self, ctx):
        await self.command_help(ctx, self.bot.user, "nhie", "Do something", "--nhie <name>",
                                "--nhie ")
    
    # TODO: finish a few commands

    @help.command()
    async def admin(self, ctx):
        liste = "`mention`, `annonce`, `massban`, `reset`, `addrole`, `fresh`, `poll`, `quickpoll`"
        embed = await Embeds().format_cat_embed(ctx, self.bot.user.avatar_url, "Admin", liste)
        await ctx.send(embed=embed)

    @help.command()
    async def level(self, ctx):
        liste = "`rank`, `level config`, `leaderboard`"
        embed = await Embeds().format_cat_embed(ctx, self.bot.user.avatar_url, "Level", liste)
        await ctx.send(embed=embed)

    @help.command()
    async def guild(self, ctx):
        liste = "`setting get`, `setting reset`, `setting setup`, `setting role mod`, `setting role admin`, `arr`, `setting color`, `color list`, " \
                "`color add`, `color remove`"
        embed = await Embeds().format_cat_embed(ctx, self.bot.user.avatar_url, "Guild", liste)
        await ctx.send(embed=embed)

    @help.command()
    async def fun(self, ctx):
        liste = "`rd`, `8ball`, `cat`, `dog`, `lovepower`, `choose`, `linux`, `number`, `trump`, `chucknorris`, `geek_joke`, `cookie`, `today`," \
                " `ice`, `lmgtfy`, `love_calc`, `urban`"
        embed = await Embeds().format_cat_embed(ctx, self.bot.user.avatar_url, "Fun", liste)
        await ctx.send(embed=embed)

    @help.command()
    async def social(self, ctx):
        liste = "`hug`, `pat`, `kiss`, `lewd`, `lick`, `slap`, `cry`"
        embed = await Embeds().format_cat_embed(ctx, self.bot.user.avatar_url, "Social", liste)
        await ctx.send(embed=embed)

    @help.command()
    async def game(self, ctx):
        liste = "`truth`, `dare`, `wyr`, `nhie`"
        embed = await Embeds().format_cat_embed(ctx, self.bot.user.avatar_url, "Game", liste)
        await ctx.send(embed=embed)

    # TODO: Add owner commands


def setup(bot):
    bot.add_cog(Help(bot))
