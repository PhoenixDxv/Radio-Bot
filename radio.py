import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="› Starte das VOID Radio!")
    async def play(self, ctx, stream: Option(str, "› Wähle einen Radio-Sender!", choices=["› VOID Radio", "› TANZ Radio", "› CHILL Radio", "› RAP Radio", "› MIX Radio", "› HIP-HOP Radio"])):
        if stream == "› VOID Radio":
            if ctx.author.voice is None:
                return await ctx.respond("Du musst erst einem Voice-Channel beitreten.", ephemeral=True)

            if not ctx.author.voice.channel.permissions_for(ctx.guild.me).connect:
                await ctx.respond("Ich habe keine Berechtigung deinen aktuellen Channel zu betreten.", ephemeral=True)

            if ctx.voice_client is None:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.voice_client.move_to(ctx.author.voice.channel)

            if ctx.voice_client.is_playing():
                ctx.voice_client.stop()

            ctx.voice_client.play(
                discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio109.mp3")
            )
            embed = discord.Embed(
                title="› THE VOID - RADIO",
                description="› Das Radio wurde erfolgreich ausgewählt & gestartet.\n"
                            "\n"
                            "\n"
                            "> *Ausgewähltes Radio:*\n  > **› VOID Radio**",
                color=discord.Color.green()
            )
            await ctx.respond(embed=embed)

        if stream == "› TANZ Radio":
            if ctx.author.voice is None:
                return await ctx.respond("Du musst erst einem Voice Channel beitreten!", ephemeral=True)

            if not ctx.author.voice.channel.permissions_for(ctx.guild.me).connect:
                await ctx.respond("Ich habe keine Berechtigung deinen aktuellen Channel zu betreten!", ephemeral=True)

            if ctx.voice_client is None:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.voice_client.move_to(ctx.author.voice.channel)

            if ctx.voice_client.is_playing():
                ctx.voice_client.stop()

            ctx.voice_client.play(
                discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio2.mp3")
            )
            embed = discord.Embed(
                title="› THE VOID - Radio",
                description="› Das Radio wurde erfolgreich ausgewählt & gestartet.\n"
                            "\n"
                            "\n"
                            "> *Ausgewähltes Radio:*\n  > **› TANZ Radio**",
                color=discord.Color.green()
            )
            await ctx.respond(embed=embed)

        if stream == "› CHILL Radio":
            if ctx.author.voice is None:
                return await ctx.respond("Du musst erst einem Voice Channel beitreten!", ephemeral=True)

            if not ctx.author.voice.channel.permissions_for(ctx.guild.me).connect:
                await ctx.respond("Ich habe keine Berechtigung deinen aktuellen Channel zu betreten!", ephemeral=True)

            if ctx.voice_client is None:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.voice_client.move_to(ctx.author.voice.channel)

            if ctx.voice_client.is_playing():
                ctx.voice_client.stop()

            ctx.voice_client.play(
                discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio17.mp3")
            )
            embed = discord.Embed(
                title="› THE VOID - RADIO",
                description="› Das Radio wurde erfolgreich ausgewählt & gestartet.\n"
                            "\n"
                            "\n"
                            "> *Ausgewähltes Radio:*\n  > **› CHILL Radio**",
                color=discord.Color.green()
            )
            await ctx.respond(embed=embed)

        if stream == "› RAP Radio":
            if ctx.author.voice is None:
                return await ctx.respond("Du musst erst einem Voice Channel beitreten!", ephemeral=True)

            if not ctx.author.voice.channel.permissions_for(ctx.guild.me).connect:
                await ctx.respond("Ich habe keine Berechtigung deinen aktuellen Channel zu betreten!", ephemeral=True)

            if ctx.voice_client is None:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.voice_client.move_to(ctx.author.voice.channel)

            if ctx.voice_client.is_playing():
                ctx.voice_client.stop()

            ctx.voice_client.play(
                discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio6.mp3")
            )
            embed = discord.Embed(
                title="› THE VOID - RADIO",
                description="› Das Radio wurde erfolgreich ausgewählt & gestartet.\n"
                            "\n"
                            "\n"
                            "> *Ausgewähltes Radio:*\n  > **› RAP Radio**",
                color=discord.Color.green()
            )
            await ctx.respond(embed=embed)

        if stream == "› MIX Radio":
            if ctx.author.voice is None:
                return await ctx.respond("Du musst erst einem Voice Channel beitreten!", ephemeral=True)

            if not ctx.author.voice.channel.permissions_for(ctx.guild.me).connect:
                await ctx.respond("Ich habe keine Berechtigung deinen aktuellen Channel zu betreten!", ephemeral=True)

            if ctx.voice_client is None:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.voice_client.move_to(ctx.author.voice.channel)

            if ctx.voice_client.is_playing():
                ctx.voice_client.stop()

            ctx.voice_client.play(
                discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio16.mp3")
            )
            embed = discord.Embed(
                title="› THE VOID - RADIO",
                description="› Das Radio wurde erfolgreich ausgewählt & gestartet.\n"
                            "\n"
                            "\n"
                            "> *Ausgewähltes Radio:*\n  > **› MIX Radio**",
                color=discord.Color.purple()
            )
            await ctx.respond(embed=embed)

        if stream == "› HIP-HOP Radio":
            if ctx.author.voice is None:
                return await ctx.respond("Du musst erst einem Voice Channel beitreten!", ephemeral=True)

            if not ctx.author.voice.channel.permissions_for(ctx.guild.me).connect:
                await ctx.respond("Ich habe keine Berechtigung deinen aktuellen Channel zu betreten!", ephemeral=True)

            if ctx.voice_client is None:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.voice_client.move_to(ctx.author.voice.channel)

            if ctx.voice_client.is_playing():
                ctx.voice_client.stop()

            ctx.voice_client.play(
                discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio10.mp3")
            )
            embed = discord.Embed(
                title="› THE VOID - RADIO",
                description="› Das Radio wurde erfolgreich ausgewählt & gestartet.\n"
                            "\n"
                            "\n"
                            "> *Ausgewähltes Radio:*\n  > **› HIP-HOP Radio**",
                color=discord.Color.green()
            )
            await ctx.respond(embed=embed)

    @slash_command(description="› Lasse den Bot den Kanal verlassen.")
    async def leave(self, ctx):
        if ctx.voice_client is None:
            return await ctx.respond("› Ich bin mit keinem Voice Channel verbunden.", ephemeral=True)

        await ctx.voice_client.disconnect()
        embed = discord.Embed(
            title="› THE VOID - RADIO",
            description="\n Der Bot hat den Kanal verlassen.",
            color=discord.Color.green()
        )
        await ctx.respond(embed=embed)

    @slash_command(description="› Pausiere das VOID Radio!")
    async def pause(self, ctx):
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        em = discord.Embed(
            title="THE VOID - Radio",
            description="\n Das VOID Radio wurde pausiert.",
            color=discord.Color.green()
        )
        await ctx.respond(embed=em)


def setup(bot):
    bot.add_cog(Radio(bot))
