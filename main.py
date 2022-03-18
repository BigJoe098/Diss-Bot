
import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook
import random
import requests
from Assets.Emoji import create_sticker,delete_sticker,getSticker

TOKEN = "YOUR TOKEN GOES HERE"
COMMAND_TOKEN = '$'

client = commands.Bot(command_prefix=COMMAND_TOKEN)
client.remove_command("help")

# Golobal Variables
COMMAND_TOKEN = '$'
PICTURE_EXTENSIONS = ['png', 'jpeg', 'raw', 'jpg', 'gif']
RANDOM_STATMENTS = [
    "Woah That's Cool",
    "Damn That Looks Fine",
    "Aren't You Lucky",
    "Cool!"
]

EMOJI_LIST = [
    "\U0001F923",
    "\U0001F606",
    "\U0001F605",
    "\U0001F60D",
    "\U0001F44D",
    "\U0001F632",
    "\U0001F628",
    "\U0001F616",
    "\U0001F91E"
]


@client.event
async def on_ready():
    print("We have lift-off")


@client.command()
async def help(ctx, *arg):

    if arg == tuple():
        Help_Parameter = "nothing"
    else:
        Help_Parameter = arg[0]
        

    if Help_Parameter == "voice":
        embed = discord.Embed(title="Help Voice")
        embed.add_field(name=":mute: muteall <vc>",
                        value="Mutes all in a voice chat", inline=True)
        embed.add_field(name=":speaker: unmuteall <vc>",
                        value="Unmutes all in a voice chat", inline=True)
        embed.add_field(name=":satellite::x: unliveall <vc>",
                        value="Disables live for all in a voice chat", inline=True)
        embed.add_field(name=":satellite: liveall <vc>",
                        value="Enable live for all in a voice chat", inline=True)
        embed.add_field(
            name="Note", value="<vc> Stands for voice channel substitute the voice channel you want to perform the tasks on", inline=False)
    elif Help_Parameter == "member":
        embed = discord.Embed(title="Help Member")
        embed.add_field(name=":mute: mute <@m>",
                        value="Mutes the mentioned member", inline=True)
        embed.add_field(name=":speaker: unmute <@m>",
                        value="Unmutes the mentioned member", inline=True)
        embed.add_field(name=":satellite::x: unlive <@m>",
                        value="Disables live for mentioned member", inline=True)
        embed.add_field(name=":satellite: live <@m>",
                        value="Enable live for mentioned member", inline=True)
        embed.add_field(
            name="Note", value="<@m> Stands for @mention, you can use these commands on one particular user", inline=False)
    elif Help_Parameter == "sticker":
        embed = discord.Embed(title="Help Sticker")
        embed.add_field(name=":regional_indicator_s: sticker new <group> <name>",
                        value="This command is used to create new sticker and packs you need to attach a file for the bot to use as sticker", inline=False)
        embed.add_field(name=":regional_indicator_s: sticker delete <group> <name>",
                        value="This command will delete a sticker that exists", inline=False)
        embed.add_field(name="Using Stickers:",
                        value="In order for you to use a sticker you need to type group's name and the sticker's name with a - in between example try :genshin-keqing:", inline=False)
    else:
        embed = discord.Embed(title="Help")
        embed.add_field(name=":grey_question: $help voice",
                        value="To Get help on Voice Chat Commands", inline=True)
        embed.add_field(name=":grey_question: $help member",
                        value="To Get help on Member Commands", inline=True)
        embed.add_field(name=":grey_question: $help sticker",
                        value="To Get help on sticker Commands and how to use added stickers", inline=True)

    await ctx.send(embed=embed)


@client.command()
async def live(ctx, member: discord.Member, *reason):

    # Getting role and guild
    guild = ctx.guild
    Live = discord.utils.get(guild.roles, name="Live")

    # reason forming
    rea = ""
    flag = True

    for x in reason:
        rea += x+" "

    if rea == "":
        flag = False

    # Muteing the member
    try:
        await member.add_roles(Live)
        if flag:
            await ctx.send("Live Was Enabled for "+member.display_name+" for "+rea)
        else:
            await ctx.send("Live Was Enabled for "+member.display_name)
    except:
        await ctx.send("Failed To Enable Live for "+member.display_name)


@client.command()
async def unlive(ctx, member: discord.Member, *reason):

    flag = False
    # Getting role and guild
    guild = ctx.guild
    Live = discord.utils.get(guild.roles, name="Live")
    for channel in guild.voice_channels:
        for mem in channel.members:
            if mem == member:
                second = ''
                for x in ctx.guild.voice_channels:
                    if x != channel:
                        second = x
                await member.move_to(second)
                await member.move_to(channel)
                flag = True

    # reason forming
    rea = ""
    Rflag = True

    for x in reason:
        rea += x+" "

    if rea == "":
        Rflag = False

    # Muteing the member
    if flag:
        if Rflag:
            await ctx.send("Live was disabled for "+member.display_name+" for "+rea)
        else:
            await ctx.send("Live was disabled for "+member.display_name)
    else:
        await ctx.send("Failed To Disable Live for "+member.display_name)


@client.command()
async def unmute(ctx, member: discord.Member, *reason):

    # Getting role and guild
    guild = ctx.guild
    Muted = discord.utils.get(guild.roles, name="Unmuted")

    # reason forming
    rea = ""
    flag = True

    for x in reason:
        rea += x+" "

    if rea == "":
        flag = False

    # Muteing the member
    try:
        await member.add_roles(Muted)
        if flag:
            await ctx.send(member.display_name+" Was Unmuted for "+rea)
        else:
            await ctx.send(member.display_name+" Was Unmuted")
    except:
        await ctx.send("Failed To Unmute "+member.display_name)


@client.command()
async def mute(ctx, member: discord.Member, *reason):

    # Getting role and guild
    guild = ctx.guild
    Muted = discord.utils.get(guild.roles, name="Unmuted")

    # reason forming
    rea = ""
    flag = True

    for x in reason:
        rea += x+" "

    if rea == "":
        flag = False

    # Muteing the member
    try:
        await member.remove_roles(Muted)
        if flag:
            await ctx.send(member.display_name+" Was Muted For "+rea)
        else:
            await ctx.send(member.display_name+" Was Muted")
    except:
        await ctx.send("Failed To Mute "+member.display_name)


@client.command()
async def muteall(ctx, VChannel):
    # Getting role and guild
    guild = ctx.guild
    Muted = discord.utils.get(guild.roles, name="Unmuted")

    # Getting the channel that is to be muted
    channel = discord.utils.get(guild.voice_channels, name=VChannel)

    # Checking if the channel is not none
    if channel != None:
        members = channel.members
        flag = False
        # Muting the members in the channel
        for member in channel.members:
            await member.remove_roles(Muted)
            flag = True
    else:
        await ctx.send("No such channel exists.")
        return

    # Giving the correct response
    if flag:
        await ctx.send("Unmuting The Channel... Success!")
    else:
        await ctx.send("Failed To Unmute Members.")


@client.command()
async def unmuteall(ctx, VChannel):

    # Getting role and guild
    guild = ctx.guild
    Muted = discord.utils.get(guild.roles, name="Unmuted")

    # Getting the channel that is to be muted
    channel = discord.utils.get(guild.voice_channels, name=VChannel)

    # Checking if the channel is not none
    if channel != None:
        members = channel.members
        flag = False
        # Unmuting the members in the channel
        for member in channel.members:
            await member.add_roles(Muted)
            flag = True
    else:
        await ctx.send("No such channel exists.")
        flag = True

    # Giving the correct response
    if flag:
        await ctx.send("Unmuting The Channel... Success!")
    else:
        await ctx.send("Failed To Unmute Members.")


@client.command()
async def unliveall(ctx, VChannel):
    # Getting role and guild
    guild = ctx.guild
    Live = discord.utils.get(guild.roles, name="Live")
    # Getting the channel that is to Live enable
    channel = discord.utils.get(guild.voice_channels, name=VChannel)

    second = ''
    for x in ctx.guild.voice_channels:
        if x != channel:
            second = x
            break

    flag = False
    # Checking if the channel is not none
    if channel != None:
        # Muting the members in the channel
        for member in channel.members:
            await member.remove_roles(Live)
            await member.move_to(second)
            await member.move_to(channel)
            flag = True
    else:
        await ctx.send("No Such Channel Exists.")
        return

    # Giving the correct response
    if flag:
        await ctx.send("Live Disabled To Users in The Channel.")
    else:
        await ctx.send("Failed To Disable Live.")


@client.command()
async def liveall(ctx, VChannel):

    # Getting role and guild
    guild = ctx.guild
    Live = discord.utils.get(guild.roles, name="Live")

    # Getting the channel that is to be muted
    channel = discord.utils.get(guild.voice_channels, name=VChannel)

    # Checking if the channel is not none
    if channel != None:
        members = channel.members
        flag = False
        # Unmuting the members in the channel
        for member in channel.members:
            await member.add_roles(Live)
            flag = True
    else:
        await ctx.send("No such channel exists.")
        flag = True

   # Giving the correct response
    if flag:
        await ctx.send("Live Enabled To Users in The Channel.")
    else:
        await ctx.send("Failed To Enable Live.")


@client.command()
async def sticker(ctx, Command, pack, name):
    if Command == "new":
        
        #initilisating all the variables
        download_path ="C:/Users/joela/Desktop/Work/Projects/Asher's Bot/Assets/Temp"
        download_url=str(ctx.message.attachments[0].proxy_url)
        filename = download_url.split("/")[-1]
        
        #downloading the pictiure to temp folder for procressing
        r = requests.get(download_url,allow_redirects=True)
        final = download_path+"/"+filename
        open(final, "wb").write(r.content)
        
        #returning appropriate message    
        out_message = create_sticker(pack,filename,name)
        await ctx.send(out_message)
    
    elif Command == "delete":
        
        #calling the delete function and returning appropriate message    
        out_message = delete_sticker(pack,name)
        await ctx.send(out_message)

async def GetSticker(message):
    
    #Getting messaeg content
    content = message.content.replace(':',' ').strip()
    group = content.split('-')[0]
    name = content.split('-')[1]
    #Deleteing the sent message
    await message.delete()
    
    #initilising variables
    author = str(message.author).split('#')[0]
    file_name, path = getSticker(group,name)
    avatar_url = str(message.author.avatar_url)
    
    #checking if the sticker was found or not
    if file_name == None:
        await message.channel.send("Did not find a sticker with that name and group.")
        return
    
    """Webhook url creation"""
    
    #Checking if a webhook exists in the current text Channel
    has_webhook = False
    while not has_webhook:
        for hook in await message.channel.webhooks():
            if hook.channel_id == message.channel.id:
                has_webhook = True
                webhook_url = hook.url
        if not has_webhook:
            await message.channel.create_webhook(name="Sticker-Hook")
    
    
    #sending the sticker requested as a message from the user
    webhook = DiscordWebhook(
        url=webhook_url, avatar_url=avatar_url, username=author)
    with open(path, "rb") as sticker:
        webhook.add_file(file=sticker.read(), filename="Sticker-"+file_name)
    response = webhook.execute()

async def Emojify(message):
    
    #deleting original message
    await message.delete()
    
    #generating the Message content
    Content = message.content.split("--emojify")[1]
    message_to_send = ""
    for char in Content:
        if char.isalpha():
            message_to_send += ":regional_indicator_"+char.lower()+":"
        elif char == " ":
            message_to_send += "  "
        else:
            message_to_send += char
            
    #initilising variables
    author = str(message.author).split('#')[0]
    avatar_url = str(message.author.avatar_url)

    #Checking if a webhook exists in the current text Channel
    has_webhook = False
    while not has_webhook:
        for hook in await message.channel.webhooks():
            if hook.channel_id == message.channel.id:
                has_webhook = True
                webhook_url = hook.url
        if not has_webhook:
            await message.channel.create_webhook(name="Sticker-Hook")
    
    #sending the generated as a message to the user
    webhook = DiscordWebhook(
        url=webhook_url, avatar_url=avatar_url, username=author, content=message_to_send
    )
    response = webhook.execute()
    
@client.event
async def on_message(message):
    
    #Ignore bot text
    if message.author == client.user:
        return
    
    #adding reaction to pictures sent by users
    if message.attachments:
        if message.attachments[0].filename.endswith(tuple(PICTURE_EXTENSIONS)) and not message.attachments[0].filename.startswith("Sticker-") and not message.content.startswith("$"):
            await message.channel.send(random.choice(RANDOM_STATMENTS))
            for emoji in EMOJI_LIST:
                await message.add_reaction(emoji)
    
    #adding reactions to links sent by users
    if message.content.startswith("https://") or message.content.startswith("http://"):
        await message.channel.send(random.choice(RANDOM_STATMENTS))
        for emoji in EMOJI_LIST:
            await message.add_reaction(emoji)
    
    #Sticker Message Procressing
    if message.content.startswith(':') and message.content.endswith(':'):
        if message.webhook_id:
            return
        await GetSticker(message)
        
    #Emojify the message sent
    if message.content.startswith('--emojify'):
        await Emojify(message)
    
    #executing the user commands
    await client.process_commands(message)


client.run(TOKEN)
