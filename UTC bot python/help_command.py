import discord
def main_help(ctx):
    em = discord.Embed(title = "Commands List", colour = ctx.author.color)

    em.add_field(name = "$ping", value = "Tell you the latency of the bot", inline=False)

    em.add_field(name = "$result <event name>", value = "Sends the live results", inline=False)

    em.add_field(name = "$account <@user>", value = "Shows the users past results (WIP)", inline=False)


    if "The UTC Team" in str(ctx.message.author.roles):
        em.add_field(name = "$announce <announcement type>", value = "Sends an announcement in #announcements (Mod only)", inline=False)

        em.add_field(name = "⠀", value = "for more info use $help <command name>", inline=False)
    return em

def help_result(ctx):  
    em = discord.Embed(title = "result", description = "Allows you to veiw the live results", colour = ctx.author.color)
    em.add_field(name = "syntax", value = "$result <event name>", inline=False)
    em.add_field(name = "event names", value = "3x3, 2x2, 3x3 oh, skewb etc...\naliases results", inline=False)
    return em

def help_account(ctx):
    em = discord.Embed(title = "account", description = "Allows you to veiw the users best single and average", colour = ctx.author.color)
    em.add_field(name = "syntax", value = "$account <@user>", inline=False)
    em.add_field(name = "errors", value = "The data might be wrong but only takes a minute to fix by DMing Ooms\naliases accounts", inline=False)
    return em