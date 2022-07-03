# importing modules
from discord.ext import commands
import discord, os, datetime, asyncio, ast

#importing each command
from get_results import get_results
from update_results import update_results
from infomation import announcments
from account_command import account_command
from help_command import main_help, help_result, help_account



client = commands.Bot(command_prefix = '$')

config_dict = {
  "mod_role":""
}


@client.event
async def on_ready():
  print("Online")
  await client.change_presence(activity=discord.Activity(type=5, name="UTC 16.0"))
@client.event
async def on_guild_join(guild):
    path = "server_settings/" + str(guild.id)
    try:
      os.makedirs(path)
      with open(path + "/server_settings.txt", "w") as f:
        f.write(str(config_dict))
      print("Making dir:" + path)
    # if the dir exist
    except FileExistsError:
        print("Dir exist " + path)

      

# all user commands
# help command
client.remove_command("help")
@client.group(invoke_wihout_commands=True)
async def help(ctx):
  await ctx.send(embed = main_help(ctx))

@help.command(aliases=["results", "result"])
async def _result(ctx):
  await ctx.send(embed = help_result(ctx))

@help.command(aliases=["account", "accounts"])
async def _account(ctx):
  await ctx.send(embed = help_account(ctx))



 # ping command
@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")



# results command
@client.command(aliases=["results", "result"])
async def _results(ctx, *, event_name=""):
  if event_name == "":
    await ctx.send("Choose an event!")
  else:
    try:
      await ctx.send(get_results(event_name, update_results(event_name)))
    except:
      await ctx.channel.send("Invalid event!")



@client.command(aliases=["accounts"])
async def account(ctx, *, user: discord.Member):
  await ctx.send(account_command(user))



# restricted commands
@client.command(pass_context=True)
async def check_settings(ctx):
  id = ctx.message.guild.id
  path = f"server_settings\{id}\server_settings.txt"
  with open(path, "r") as f:
    contents = f.read()
    global config_dict
    config_dict = ast.literal_eval(contents)




@client.command()
async def config(ctx, *, cmd_name):
  await ctx.send(config(ctx, cmd_name))

  if cmd_name == "":
    await ctx.send("Choose a command to configure")

  if cmd_name == "role":
    await ctx.send("Enter role name")
    msg = await client.wait_for("message")
    await ctx.send(f"Mod role set to {msg.content}")
     
    path = f"server_settings\{str(ctx.guild.id)}\server_settings.txt"
    with open(path, "r") as f:
      contents = f.read()
      config_dict = ast.literal_eval(contents)
    with open(path, "w") as f:
      config_dict["mod_role"] = msg.content
      f.write(str(config_dict))

  if cmd_name == "channel":
    await ctx.send("Enter channel name")
    msg = await client.wait_for("message")
    await ctx.send(f"channel set to {msg.content}")
     
    path = f"server_settings\{str(ctx.guild.id)}\server_settings.txt"
    with open(path, "r") as f:
      contents = f.read()
      config_dict = ast.literal_eval(contents)
    with open(path, "w") as f:
      config_dict["channel"] = msg.content
      f.write(str(config_dict))
    





#@client.command()
#@commands.is_owner()
#async def shutdown(ctx):
 # await ctx.send(f"Going offline for 10 minutes")
  #import shutdown
  #exit()


    
  #return config_dict



@client.command()
async def announce(ctx, *, type):
  await check_settings(ctx)
  channel = client.get_channel(int(config_dict["channel"]))
  if config_dict["mod_role"] in str(ctx.message.author.roles):
    await channel.send(announcments[type])

@client.command()
async def schedule_announcemnt(ctx, type):#
  await ctx.send("Message scheduled for 9:00am tomorrow")
  now = datetime.datetime.now()
  #then = now+datetime.timedelta(days=0)  # dont use when testing
  then = now.replace(hour=23, minute=30) # use when testing
  #then.replace(hour=23, minute=8)        # dont use when testing
  wait_time = (then-now).total_seconds()
  await asyncio.sleep(wait_time)

  await check_settings(ctx)
  channel = client.get_channel(int(config_dict["channel"]))
  if config_dict["mod_role"] in str(ctx.message.author.roles):
    await channel.send(announcments[type])
  


client.run("OTgyNjEzMTY1MTk4MTU1ODg2.Ghz7vV.cKMa8VVCfSoONkG87XHfav4GFVQyA9gprlpPQM") 