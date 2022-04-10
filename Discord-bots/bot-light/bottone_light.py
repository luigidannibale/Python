# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:37:54 2021
@author: Luigi D'annibale

Hi, its Luigi, please use this code only if you understand it, dont copy-paste without knowledge. Enjoy!
"""
import discord
from discord.ext import commands
import random
import datetime
from discord.ext.commands.cooldowns import BucketType

"""
Personalizable variables starts here
"""
Saluti = ["Hello!","Hi!"]
TOKEN = ""

Name_change_role_id = "id=931218751951601685" #Those who got this role can have their name changed by the bot.

#Role to gather your friends in channel with style, easily writing "call" in channel they will be DMed by the bot to join you. 
#Be sure to join the channel firstly or you would like to be a joker and the bot would know.
Call_role_id = "id=940660118180212756"
Call_command_cooldown = 1800

Bot_command_prefix = ">"
Bot_activity = discord.Activity(type=discord.ActivityType.listening, name="bot-name")
Bot_status = discord.Status.do_not_disturb

name_file = "File.txt"
suffix_file = "suffissi-giapponesi.txt"

"""
Personalizable variables finish here
"""
Nick_shuffle_service_documentation = "https://github.com/luigidannibale/Discord-bot-services/blob/main/nick_shuffle_service.py"
Giappo_shuffle_service_documentation = "https://github.com/luigidannibale/Discord-bot-services/blob/main/giappo_shuffle_service.py"
url_404 = "https://agenda-digitale.it/wp-content/uploads/2015/08/404.jpg"
#Services are declared as boolean, True stands for active status, False stands for deactivated status
Nick_shuffle_service = True
Giappo_shuffle_service = True
Call_service = True
status = ['Disabled','Running']

class servizi(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    def cog_unload(self):
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')
        return True

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandOnCooldown):
            # When used command is in cooldown
            await ctx.send(f"{ctx.message.author.name}, non spammare, il comando è in cooldown! Cooldown - {datetime.timedelta(seconds=round(error.retry_after))}.")
        else:
            await ctx.send('An error occurred: {}'.format(str(error)))  

    @commands.command(name='nick_shuffle',pass_context=True)
    async def _nick_shuffle(self, ctx: commands.Context, options = ""):
        """
        Nick_shuffle service :
            There's a secret file fulfilled with strange names on each line somewhere in this shitty world,
            while the service is active anytime a stupid dumbass joins a channel, his nickname will be renewed with a random one from the file.
            This service is provided by Shuffle, Nick Shuffle.
        
        Commands:
            >nick_shuffle -s : shows the current status of the service, it can be either running or disabled
            >nick_suhffle : toggles the service, admins only
        """
        try:
            caller = ctx.author.name
            global Nick_shuffle_service
            
            if options == "-s": #option "-s" stands for status, if so it only sends a message containings the actual status of the service that can be either Running or Disabled
                await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), url=Nick_shuffle_service_documentation, 
                                                      description="", 
                                                      color=discord.Color.blue())
                                        .add_field(name = "Nick shuffle service", value = "{}".format(status[int(Nick_shuffle_service)]),inline=False)))
            else: #without an option this is the actual command
            #the following if/else is a control over the permissions,for the moment only administrators can use the command
                if ctx.author.guild_permissions.administrator: 
                    Nick_shuffle_service = not Nick_shuffle_service
                    await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), url=Nick_shuffle_service_documentation, 
                                                          description="", 
                                                          color=discord.Color.green())
                                            .add_field(name = "Nick shuffle service", value = "{}".format(status[int(Nick_shuffle_service)]),inline=False)))
        
                else:
                    await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), url=Nick_shuffle_service_documentation, 
                                                          description="X", 
                                                          color=discord.Color.red())
                                            .add_field(name = "Nick shuffle service - {}".format(status[int(Nick_shuffle_service)]), value = "Non hai il permesso per cambiarlo")))
        except Exception as e:
            print(e)
    
    @commands.command(name='giappo_shuffle',pass_context=True)
    async def _giappo_shuffle(self, ctx: commands.Context, options = ""):
        """
        Giappo suffixo shuffle service:
            while the service is active anytime a stupid dumbass joins a channel, his nickname will be modified appendiang a japanese suffix 
            to its original nickname, if the nick originally contains another suffix it will be changed.
            This service is provided by Shuffle, Giappo Shuffle. Nick Shuffle's brothero. 
            (Can work alongside Nick_shuffle or not, he's got his own legs)            
        
        Commands:
            >giappo_shuffle -s : shows the current status of the service, it can be either running or disabled
            >giappo_shuffle : toggles the service, admins only
        """
        try:
            caller = ctx.author.name
            global Giappo_shuffle_service
            
            if options == "-s": #option "-s" stands for status, if so it only sends a message containings the actual status of the service that can be either Running or Disabled
                await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), url=Giappo_shuffle_service_documentation, 
                                                      description="", 
                                                      color=discord.Color.blue())
                                    .add_field(name = "Giappo suffixo shuffle service", value = "{}".format(status[int(Giappo_shuffle_service)]),inline=False)))
            else: #without an option this is the actual command
            #the following if/else is a control over the permissions,for the moment only administrators can use the command  
                if ctx.author.guild_permissions.administrator: 
                    Giappo_shuffle_service = not Giappo_shuffle_service
                    await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), url=Giappo_shuffle_service_documentation, 
                                                          description="", 
                                                          color=discord.Color.green())
                                            .add_field(name = "Giappo suffixo shuffle service", value = "{}".format(status[int(Giappo_shuffle_service)]),inline=False)))
        
                else:
                    await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), url=Giappo_shuffle_service_documentation, 
                                                          description="X", 
                                                          color=discord.Color.red())
                                            .add_field(name = "Giappo suffixo shuffle service - {}".format(status[int(Giappo_shuffle_service)]), value = "Non hai il permesso per cambiarlo")))
        except Exception as e:
            print(e)

    @commands.command(name="call",pass_context=True)
    @commands.cooldown(1, Call_command_cooldown, type=BucketType.default)
    async def call(self,ctx:commands.Context):
        """
        Service to gather your friends in channel with style, easily writing ">call" in channel they will be DMed by the bot to join you. 
        Be sure to join the channel firstly or you would like to be a joker and the bot would know.
        
        Commands:
        >call : sends a dm to all the users with role
        """
        try:
            #if service is active
            if Call_service:
                caller = ctx.message.author
                #the user who used the command has the permission to use it
                if Call_role_id in str(caller.roles):
                    members_to_call = [member for member in caller.guild.members if Call_role_id in str(member.roles)]
                    for member_to_call in members_to_call:
                        #calls every member out of channel who has the role
                        if not member_to_call.id == caller.id and member_to_call.voice == None:
                            if member_to_call.dm_channel is None:
                                await member_to_call.create_dm()
                            ttl = 1800
                            await member_to_call.dm_channel.send("{0.name}you are requested by {1.name}".format(member_to_call, caller),delete_after=ttl)
                            await ctx.channel.send("{0.name} invited!... \t\t\t Blacksbebond Blacksbebond 🎶🎵🎶🎵".format(member_to_call),delete_after=150)                            
                        #elif member_to_call.voice != None:
                        #    print(datetime.datetime.now().strftime("%b-%d-%Y,%H:%M:%S"), "\t {} è già in un canale vocale".format(member_to_call.name))
                    await ctx.message.delete()
                #the user who used the command miss the permission to use it
                else:
                    await ctx.send(embed = (discord.Embed(title="Fallito!", url="https://www.buzzfeed.com/stephenlaconte/are-you-dumb-quiz", 
                                                                description="X", 
                                                                color=discord.Color.red())
                                                    .add_field(name = "Call service - {}".format(status[int(Call_service)]), value = "Non hai il permesso per usarlo")))
                    await ctx.command.reset_cooldown(ctx)
            #service is not active
            else:
                await ctx.send(embed = (discord.Embed(title="Call service - {}".format(status[int(Call_service)]), url=url_404, 
                                                            description="X", 
                                                            color=discord.Color.blue())
                                                .add_field(name = "Fallito! ", value = "la mia testa dice wata wata wata")))
        except Exception as e:
            print(e)
    
    @commands.command(name="services",pass_context=True)
    async def services(self,ctx:commands.Context,options = ""):
        caller = ctx.author.name
        try:
            global Giappo_shuffle_service
            global Nick_shuffle_service
            global Call_service
            options = ctx.message.content.replace(Bot_command_prefix+"services","").strip()
            if options == "":
                await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller),
                                                    color=discord.Color.blue())
                                                    .add_field(name = "Giappo suffixo shuffle service", value = "{}".format(status[int(Giappo_shuffle_service)]),inline=False)
                                                    .add_field(name = "Nick shuffle service", value = "{}".format(status[int(Nick_shuffle_service)]),inline=False)
                                                    .add_field(name = "Call service", value = "{}".format(status[int(Call_service)]),inline=False)
                                                    ))
            
            elif options.startswith("-t"):
                
                servizio = options.replace("-t ","").strip().lower()
                if servizio == "":
                    pass
                elif servizio == "giappo shuffle":
                    if ctx.author.guild_permissions.administrator: 
                        Giappo_shuffle_service = not Giappo_shuffle_service
                        await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), 
                                                            description="", 
                                                            color=discord.Color.green())
                                                .add_field(name = "Giappo suffixo shuffle service", value = "{}".format(status[int(Giappo_shuffle_service)]),inline=False)))
            
                    else:
                        await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), 
                                                            description="X", 
                                                            color=discord.Color.red())
                                                .add_field(name = "Giappo suffixo shuffle service - {}".format(status[int(Giappo_shuffle_service)]), value = "Non hai il permesso per cambiarlo")))
                elif servizio == "nick shuffle":
                    if ctx.author.guild_permissions.administrator: 
                        Nick_shuffle_service = not Nick_shuffle_service
                        await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), url = Nick_shuffle_service_documentation,
                                                            description="", 
                                                            color=discord.Color.green())
                                                .add_field(name = "Nick shuffle service - {}".format(status[int(Nick_shuffle_service)]), value = " io te posso canta na canzone")))
            
                    else:
                        await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), url = Nick_shuffle_service_documentation,
                                                            description="X", 
                                                            color=discord.Color.red())
                                                .add_field(name = "Nick shuffle service", value = "{}".format(status[int(Nick_shuffle_service)]),inline=False)))
                elif servizio == "call":
                    if ctx.author.guild_permissions.administrator:
                        Call_service = not Call_service
                        await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller), url="https://www.buzzfeed.com/stephenlaconte/are-you-dumb-quiz", 
                                                                            description="", 
                                                                            color=discord.Color.blue())
                                                                .add_field(name = "Call service", value = "{}".format(status[int(Call_service)]),inline=False)))
                    else:
                        await ctx.send(embed = (discord.Embed(title="Hey {}!".format(caller),
                                                            description="X", 
                                                            color=discord.Color.red())
                                                .add_field(name = "Call service - {}".format(status[int(Call_service)]), value = "Non hai il permesso per cambiarlo")))
        except Exception as e:
            print(e)


bot = commands.Bot(command_prefix=Bot_command_prefix,
                   activity =Bot_activity, 
                   status = Bot_status,
                   intents = discord.Intents().all())

bot._skip_check = lambda x, y: False
bot.add_cog(servizi(bot))


@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

@bot.event
async def on_voice_state_update(member, before, after):
    #when a member joins a channel 
    if before.channel is None and after.channel is not None:
        nickname = member.nick
        if Nick_shuffle_service:
            try:
                with open(name_file,"r",encoding="utf-8") as file:
                    lista_di_nomi = [riga for riga in file]
                    import random
                    r_number = random.randint(0, len(lista_di_nomi)-1)
                    nickname = lista_di_nomi[r_number]
            except Exception as e:
                print(e)
        
        if Giappo_shuffle_service:
            try:
                with open(suffix_file,"r",encoding="utf-8") as file:
                    lista_di_suffissi = [riga for riga in file]
                    dizionario_suffissi = {indice:str(suffisso).replace("-","") for indice,suffisso in enumerate(lista_di_suffissi)}
                    import random
                    r_number = random.randint(0, len(lista_di_suffissi)-1)
                    # Controls if the user already has a suffix
                    controllo = nickname.split("-")
                    for indice,elemento in enumerate(controllo):
                        if not indice: 
                            continue
                        if elemento in dizionario_suffissi.values():
                            nickname.remove("-{}".format(elemento))
                    if len(nickname +  lista_di_suffissi[r_number]) <= 32:    
                        nickname = nickname +  lista_di_suffissi[r_number]
            except Exception as e:
                print(e)
        
        #Nick is changed only if the user has the role
        if Name_change_role_id in str(member.roles):    
            await member.edit(nick=nickname[0:32])      

    #when a member lefts a channel
    if before.channel is not None and after.channel is None:
        await member.edit(nick = member.name)

@bot.event
async def on_message(message):                              
    if message.author == bot.user:
        return

    msg = message.content
    if any(msg.lower().startswith(word) for word in Saluti):
        await message.channel.send("{random_greeting} {name_of_the_sender}".format(random_greeting = random.choice(Saluti),name_of_the_sender = message.author.name))

    await bot.process_commands(message)


bot.run(TOKEN)