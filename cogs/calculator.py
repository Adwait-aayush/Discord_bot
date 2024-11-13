import discord
from discord.ext import commands
import re

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='calcy', aliases=['calculate'])
    async def calculator(self, ctx, *, expression=None):
        """Calculate mathematical expressions"""
        if not expression:
            await ctx.send("Please provide a mathematical expression! Example: `!calcy 2 + 2`")
            return

        # Clean the expression
        expression = expression.replace('x', '*')  # Replace 'x' with '*'
        expression = expression.replace('÷', '/')  # Replace '÷' with '/'
        
        # Remove any characters that aren't numbers, operators, decimals, or spaces
        expression = re.sub(r'[^0-9+\-*/().\ ]', '', expression)
        
        try:
            # Evaluate the expression
            result = eval(expression)
            
            # Create an embed for better presentation
            embed = discord.Embed(title="Calculator", color=discord.Color.blue())
            embed.add_field(name="Expression", value=f"```{expression}```", inline=False)
            embed.add_field(name="Result", value=f"```{result}```", inline=False)
            
            await ctx.send(embed=embed)
            
        except ZeroDivisionError:
            await ctx.send("❌ Error: Division by zero!")
        except Exception as e:
            await ctx.send(f"❌ Error: Invalid expression! Please use basic arithmetic operations only. Error: {str(e)}")

# Setup the cog
async def setup(bot):
    await bot.add_cog(Calculator(bot))
