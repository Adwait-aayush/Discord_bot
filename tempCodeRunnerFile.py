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
        await member.remove_roles(timeout_role)
        await ctx.send(f"{member.mention} has been unmuted after {seconds} seconds.")
    else:
        await ctx.send("You don't have permission to use this command.")