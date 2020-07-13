import discord
import traceback
import sys
from discord.ext import commands

class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      _error=""

      if hasattr(ctx.command, 'on_error'):
        return

      cog = ctx.cog
      if cog:
          if cog._get_overridden_method(cog.cog_command_error) is not None:
              return

      error = getattr(error, 'original', error)

      if isinstance(error, commands.DisabledCommand):
          _error=(f'{ctx.command} has been disabled.')

      elif isinstance(error, commands.NoPrivateMessage):
          try:
              await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
          except discord.HTTPException:
              pass

      # For this error example we check to see where it came from...
      elif isinstance(error, commands.BadArgument):
          _error=(f'Bad argument')

      elif isinstance(error, commands.MissingRequiredArgument):
          _error=("Missing argument")

      else:
          # All other Errors not returned come here. And we can just print the default TraceBack.
          print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
          traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
          _error=(error)

      embed=discord.Embed(color=0xf23a3a)
      embed.add_field(name="Error", value=str(_error), inline=False)
      await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(error(bot))