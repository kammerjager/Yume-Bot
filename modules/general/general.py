#  Copyright (c) 2020.
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

import json

import aiohttp
import discord
from discord.ext import commands

from modules.utils import checks
from modules.utils.weather import data_fetch, data_return, url_meteo

with open('./config/config.json', 'r') as cjson:
    config = json.load(cjson)

OWNER = config["owner_id"]


class General(commands.Cog):
    conf = {}

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        """
        Pong !
        """
        await ctx.send("Pong !!")

    @commands.command()
    @commands.guild_only()
    async def pong(self, ctx):
        """
        Ping !
        """

        await ctx.send("Ping !!")

    @commands.command()
    @commands.guild_only()
    @checks.is_prince()
    async def jade(self, ctx):
        await ctx.message.delete()
        webhooks = await ctx.channel.webhooks()
        if not webhooks:
            webhook = await ctx.channel.create_webhook(name="Jade")
        else:
            webhook = webhooks[0]
        user_id = 292362017006944256
        user: discord.User = await self.bot.fetch_user(user_id)
        await webhook.send(content="On voit le résultat...", username=user.name, avatar_url=user.avatar_url, wait=True)

    @commands.command()
    @commands.guild_only()
    @checks.is_prince()
    async def jade2(self, ctx):
        await ctx.message.delete()
        await ctx.send("https://i.imgur.com/03SkULK.jpg?1")

    @commands.command()
    @commands.guild_only()
    @checks.is_prince()
    async def missette(self, ctx):
        await ctx.message.delete()
        webhooks = await ctx.channel.webhooks()
        if not webhooks:
            webhook = await ctx.channel.create_webhook(name="Missette")
        else:
            webhook = webhooks[0]
        user_id = 511135694207451146
        user: discord.User = await self.bot.fetch_user(user_id)
        await webhook.send(content="Petit faible...", username=user.name, avatar_url=user.avatar_url, wait=True)

    @commands.command()
    @commands.guild_only()
    @checks.is_prince()
    async def yume(self, ctx):
        await ctx.message.delete()
        webhooks = await ctx.channel.webhooks()
        if not webhooks:
            webhook = await ctx.channel.create_webhook(name="Yume")
        else:
            webhook = webhooks[0]
        user_id = 282233191916634113
        user: discord.User = await self.bot.fetch_user(user_id)
        await webhook.send(content="Je suis un petit faible", username=user.name, avatar_url=user.avatar_url, wait=True)

    @commands.command()
    @commands.guild_only()
    @checks.is_prince()
    async def yume2(self, ctx):
        await ctx.message.delete()
        await ctx.send("https://i.imgur.com/FOFjRCB.jpg")   
        webhooks = await ctx.channel.webhooks()
        if not webhooks:
            webhook = await ctx.channel.create_webhook(name="Le petit prince")
        else:
            webhook = webhooks[0]
        user_id = 282233191916634113
        user: discord.User = await self.bot.fetch_user(user_id)
        await webhook.send(content="Slurp Slurp Slurp...", username=user.name, avatar_url=user.avatar_url, wait=True)

    @commands.command(aliases=['gmto', 'gweather'])
    @commands.guild_only()
    async def gmeteo(self, ctx, city: str):
        """
        Full Weather report
        """

        result = url_meteo(city)
        fetch = data_fetch(result)
        data = data_return(fetch)

        condition = f"{data['main']}, {data['description']}"

        embed = discord.Embed(
            title="Meteo",
            color=discord.Colour.dark_red()
        )
        embed.set_footer(text="Powered by https://openweathermap.org")

        embed.add_field(name='🌍 **Location**', value=f"{data['city']}, {data['country']}")
        embed.add_field(name="\N{CLOUD} **Condition**", value=condition)

        embed.add_field(name="\N{THERMOMETER} **Temperature**", value=data['temp'])
        embed.add_field(name='Temperature min', value='{}°C'.format(
            data['temp_min']))
        embed.add_field(name='Temperature max', value='{}°C'.format(
            data['temp_max']))
        embed.add_field(name='\N{FACE WITH COLD SWEAT} **Humidity**', value="{}%".format(
            data['humidity']))
        embed.add_field(name='Pressure', value="{}hPa".format(
            data['pressure']))
        embed.add_field(name='\N{SUNRISE OVER MOUNTAINS} **Sunrise (UTC)**', value=data['sunrise'])
        embed.add_field(name='\N{SUNSET OVER BUILDINGS} **Sunset (UTC)**', value=data['sunset'])
        embed.add_field(
            name='\N{DASH SYMBOL} **Wind Speed**', value="{}m/s".format(data['wind']))
        embed.add_field(name='Cloudiness', value="{}%".format(
            data['cloudiness']))

        await ctx.send(embed=embed)

    @commands.command(aliases=["mto", "weather"])
    @commands.guild_only()
    async def meteo(self, ctx, city: str):
        """
        Simple Weather report
        """

        result = url_meteo(city)
        fetch = data_fetch(result)
        data = data_return(fetch)

        condition = f"{data['main']}, {data['description']}"

        embed = discord.Embed(
            title="Meteo",
            color=discord.Colour.dark_red()
        )

        embed.set_footer(text="Powered by https://openweathermap.org")

        embed.add_field(name='🌍 **Location**', value=f"{data['city']}, {data['country']}")
        embed.add_field(name="\N{CLOUD} **Condition**", value=condition)
        embed.add_field(name='\N{FACE WITH COLD SWEAT} **Humidity**', value="{}%".format(
            data['humidity']))
        embed.add_field(name="\N{THERMOMETER} **Temperature**", value=data['temp'])
        embed.add_field(
            name='\N{DASH SYMBOL} **Wind Speed**', value="{}m/s".format(data['wind']))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def jump(self, ctx, id: int, channel: discord.TextChannel = None):
        """
        Create a direct link to a message
        """
        if channel is None:
            channel = ctx.message.channel
        try:
            msg = await channel.fetch_message(id)
        except discord.NotFound:
            return await ctx.send(
                "We can't find the message")
        except discord.HTTPException:
            return await ctx.send("We can't find the message.")

        await ctx.send('Url :{}'.format(msg.jump_url))

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    async def pokemon(self, ctx, name_or_id):
        """Show pokemon info"""

        # Sources : https://github.com/Jintaku/Jintaku-Cogs-V3/blob/master/pokemon/pokemon.py

        try:
            headers = {"content-type": "application/json"}

            # Queries pokeapi for Name, ID and evolution_chain
            async with aiohttp.ClientSession() as session:
                async with session.get("https://pokeapi.co/api/v2/pokemon-species/" + name_or_id.lower(),
                                       headers=headers) as r1:
                    response1 = await r1.json()

        except:
            return await ctx.send("No pokemon found")

        # Handles response1
        if response1.get("detail") == "Not found.":
            await ctx.send("No pokemon found")
        else:
            evolution_url = response1["evolution_chain"]["url"]

            # Queries pokeapi for Height, Weight, Sprite
            async with aiohttp.ClientSession() as session:
                async with session.get("https://pokeapi.co/api/v2/pokemon/" + name_or_id.lower(),
                                       headers=headers) as r2:
                    response2 = await r2.json()

            # Queries pokeapi for Evolutions
            async with aiohttp.ClientSession() as session:
                async with session.get(str(evolution_url), headers=headers) as r3:
                    response3 = await r3.json()

            # Selects english description for embed
            description = ""
            for i in range(0, len(response1["flavor_text_entries"])):
                if response1["flavor_text_entries"][i]["language"]["name"] == "en":
                    description = response1["flavor_text_entries"][i]["flavor_text"]
                    break

            # Conversion for embed
            height = str(response2["height"] / 10.0) + "m"
            weight = str(response2["weight"] / 10.0) + "kg"

            # Deals with evolution_chain for presentation in embed
            evolution = response3["chain"]["evolves_to"]
            evolutions = [response3["chain"]["species"]["name"].capitalize()]
            while len(evolution) > 0:
                evolutions.append(evolution[0]["species"]["name"].capitalize())
                evolution = evolution[0]["evolves_to"]
            if len(evolutions) == 1:
                evolution_string = "No evolutions"
            else:
                evolution_string = " -> ".join(evolutions)

            # Build Embed
            embed = discord.Embed()
            embed.title = response1["name"].capitalize()
            embed.description = description
            embed.set_thumbnail(url=response2["sprites"]["front_default"])
            embed.add_field(name="Evolutions", value=evolution_string, inline=False)
            embed.add_field(name="Height", value=height)
            embed.add_field(name="Weight", value=weight)
            embed.set_footer(text="Powered by Pokeapi")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
