# import discord
# from discord.ext import commands
# import asyncio
# import os
# from datetime import timedelta

# # Create bot instance with command prefix '!'
# bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# # On_ready event handler (merged into a single handler)
# @bot.event
# async def on_ready():
#     """Execute when bot successfully connects"""
#     print(f'{bot.user} has connected to Discord!')
#     await bot.change_presence(activity=discord.Game(name="!help for commands"))
#     # Load the calculator cog (make sure 'cogs.calculator' is the correct path)
#     await bot.load_extension('cogs.calculator')

# # Respond to !hello command
# @bot.command(name='hello')
# async def hello(ctx):
#     """Responds to !hello command"""
#     await ctx.send(f'Hello {ctx.author.name}!')

# # About command to provide bot information
# @bot.command(name='about')
# async def about(ctx):
#     embed = discord.Embed(
#         title="About Hack Bot",
#         description="👋 Hey there! I am hack_bot😈, your friendly multipurpose Discord assistant!",
#         color=discord.Color.blue()
#     )
#     embed.add_field(
#         name="Features",
#         value="• Powerful moderation tools\n• Server organization\n• Games and entertainment\n• Channel management\n• Welcome messages\n• Polls and more!",
#         inline=False
#     )
#     embed.add_field(
#         name="How to Use",
#         value="Type !help to see all available commands",
#         inline=False
#     )
#     embed.set_footer(text="Made with ❤️ to serve your community")
#     await ctx.send(embed=embed)

# # Ping command to check latency
# @bot.command(name='ping')
# async def ping(ctx):
#     """Check bot's latency"""
#     latency = round(bot.latency * 1000)  # Convert to milliseconds
#     embed = discord.Embed(
#         title="🏓 Pong!",
#         description=f"Bot Latency: {latency}ms",
#         color=discord.Color.green()
#     )
#     await ctx.send(embed=embed)

# # Timeout command - mute a user temporarily
# @bot.command(name='timeout')
# async def timeout(ctx, member: discord.Member, seconds: int = 60):
#     """Mute a user for a given amount of seconds"""
#     # Check if the bot has permission to mute the member
#     if ctx.author.guild_permissions.administrator:
#         # Add timeout role (mute role, assuming you have one)
#         mute_role = discord.utils.get(ctx.guild.roles, name="Muted")  # Replace "Muted" with your actual mute role name
#         if mute_role is None:
#             await ctx.send("Error: No 'Muted' role found in this server!")
#             return

#         # Assign the mute role to the user
#         await member.add_roles(mute_role)
#         await ctx.send(f"{member.mention} has been muted for {seconds} seconds.")

#         # Wait for the timeout duration and then remove the mute
#         await asyncio.sleep(seconds)  # Use asyncio.sleep to wait
#         await member.remove_roles(mute_role)
#         await ctx.send(f"{member.mention} has been unmuted after {seconds} seconds.")
#     else:
#         await ctx.send("You don't have permission to use this command.")

# # Event handler for incoming messages (including help text)
# @bot.event
# async def on_message(message):
#     """Handle incoming messages"""
#     if message.author == bot.user:
#         return

#     # Process commands - this line is essential!
#     await bot.process_commands(message)
    
#     # Respond to specific words
#     if 'help' in message.content.lower() and not message.content.startswith('!'):
#         commands_list = """
# Available Commands:
# • !hello - Get a friendly greeting
# • !calcy - Access calculator
# • !about - Learn about the bot
# • !timeout - Timeout management
# • !ping - Check bot latency

# Type !help for more information
# """
#         embed = discord.Embed(
#             title="Help Menu",
#             description=commands_list,
#             color=discord.Color.blue()
#         )
#         await message.channel.send(embed=embed)

# # Ensure the bot token is stored securely (not hardcoded in the script)
# TOKEN = 'MTMwNjEwNTUzODYyNjU4ODgwNg.GI_fUj.USE5pkCagQ6VtuuVj1in7DsnzdYIdsckSNF4p0' # Make sure to set the environment variable 'DISCORD_TOKEN'

# if TOKEN is None:
#     print("Error: Bot token is missing! Make sure it's set in the environment variables.")
# else:
#     bot.run(TOKEN)
import discord
from discord.ext import commands
import asyncio
import os
from datetime import timedelta

# Create bot instance with command prefix '!'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# On_ready event handler (merged into a single handler)
@bot.event
async def on_ready():
    """Execute when bot successfully connects"""
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="!help for commands"))
    # Load the calculator cog (make sure 'cogs.calculator' is the correct path)
    await bot.load_extension('cogs.calculator')

# Respond to !hello command
@bot.command(name='hello')
async def hello(ctx):
    """Responds to !hello command"""
    await ctx.send(f'Hello {ctx.author.name}!')

# About command to provide bot information
@bot.command(name='about')
async def about(ctx):
    embed = discord.Embed(
        title="About Hack Bot",
        description="👋 Hey there! I am hack_bot😈, your friendly multipurpose Discord assistant!",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Features",
        value="• Powerful moderation tools\n• Server organization\n• Games and entertainment\n• Channel management\n• Welcome messages\n• Polls and more!",
        inline=False
    )
    embed.add_field(
        name="How to Use",
        value="Type !help to see all available commands",
        inline=False
    )
    embed.set_footer(text="Made with ❤️ to serve your community")
    await ctx.send(embed=embed)

# Ping command to check latency
@bot.command(name='ping')
async def ping(ctx):
    """Check bot's latency"""
    latency = round(bot.latency * 1000)  # Convert to milliseconds
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"Bot Latency: {latency}ms",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

# Timeout command - mute a user temporarily
@bot.command(name='timeout')
async def timeout(ctx, member: discord.Member, seconds: int = 60):
    """Mute a user for a given amount of seconds"""
    # Check if the bot has permission to mute the member
    if ctx.author.guild_permissions.administrator:
        # Add timeout role (mute role, assuming you have one)
        timeout_role = discord.utils.get(ctx.guild.roles, name="Cannot Type")  # Ensure the role name is correct
         
        if timeout_role is None:
            await ctx.send("Error: No 'Muted' role found in this server!")
            return

        # Assign the mute role to the user
        await member.add_roles(timeout_role)
        await ctx.send(f"{member.mention} has been muted for {seconds} seconds.")

        # Wait for the timeout duration and then remove the mute
        await asyncio.sleep(seconds)  # Use asyncio.sleep to wait
        await member.remove_roles(time)
        await ctx.send(f"{member.mention} has been unmuted after {seconds} seconds.")
    else:
        await ctx.send("You don't have permission to use this command.")

# Event handler for incoming messages (including help text)
@bot.event
async def on_message(message):
    """Handle incoming messages"""
    if message.author == bot.user:
        return

    # Process commands - this line is essential!
    await bot.process_commands(message)
    
    # Respond to specific words
    if 'help' in message.content.lower() and not message.content.startswith('!'):
        commands_list = """
Available Commands:
• !hello - Get a friendly greeting
• !calcy - Access calculator
• !about - Learn about the bot
• !timeout - Timeout management
• !ping - Check bot latency

Type !help for more information
"""
        embed = discord.Embed(
            title="Help Menu",
            description=commands_list,
            color=discord.Color.blue()
        )
        await message.channel.send(embed=embed)

# Ensure the bot token is stored securely (not hardcoded in the script)
TOKEN = 'MTMwNjEwNTUzODYyNjU4ODgwNg.GI_fUj.USE5pkCagQ6VtuuVj1in7DsnzdYIdsckSNF4p0'  # Make sure to set the environment variable 'DISCORD_TOKEN'

if TOKEN is None:
    print("Error: Bot token is missing! Make sure it's set in the environment variables.")
else:
    bot.run(TOKEN)
