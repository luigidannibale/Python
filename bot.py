# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:37:54 2021
@author: Luigi
"""
from ast import Call
from subprocess import call
import discord
from discord.ext import commands
import random
import datetime
from bs4 import BeautifulSoup
import requests
import re
from discord.ext.commands.cooldowns import Cooldown, BucketType, CooldownMapping

Nick_shuffle_service_documentation = "https://github.com/luigidannibale02/Discord-bot-services/blob/main/nick_shuffle_service.py"
Giappo_shuffle_service_documentation = "https://github.com/luigidannibale02/Discord-bot-services/blob/main/giappo_shuffle_service.py"


url_404 = "https://agenda-digitale.it/wp-content/uploads/2015/08/404.jpg"

Saluti = ["halo", "hello","belli","hi","bella","biella","helo","ciao","hey hot boy","what's up","hi there","what's going on","how be"]

TOKEN = ""

#Services are declared as boolean, True stands for active status, False stands for deactivated status
Nick_shuffle_service = True
Giappo_shuffle_service = True
Call_service = True
status = ['Disabled','Running']


#Those who got this role can have their name changed by the bot.
Name_change_role_id = "id=931218751951601685"

#Role to gather your friends in channel with style, easily writing "call" in channel they will be DMed by the bot to join you. 
#Be sure to join the channel firstly or you would like to be a Fallito.
Call_role_id = "id=940660118180212756"
Call_command_cooldown = 1800

id_film_channel = 941002057798787162

def sommatempi(t1,t2):
    if t1[0] == 24:
        t1[0] = 0
    if t2[0] == 24:
        t2[0] = 0
    ore = int(t1[0]) + int(t2[0])
    minuti = int(t1[1]) + int(t2[1])
    if minuti > 60:
        minuti -= 60
        ore += 1
    if ore > 24:
        ore -= 24
    if ore == 24:
        ore = "00"
    if ore < 10:
        ore = "0{}".format(ore)
    if minuti < 10:
        minuti = "0{}".format(minuti)
    return "{0}.{1}".format(ore,minuti)

def crea_dizionario(lista):
    diz = {}
    diz["titolo"] = lista[0].strip()
    diz["durata"] = lista[1].strip()
    diz["genere"] = " ".join(lista[2].split(","))
    diz["data"] = lista[3].strip()
    diz["orario"] = lista[4].strip()
    diz["immagine"] = ""
    if not lista[5].strip() == "-":
        diz["immagine"] = lista[5].strip()
    return diz

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
            # quando il comando usato è in cooldown
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
        Role to gather your friends in channel with style, easily writing "call" in channel they will be DMed by the bot to join you. 
        Be sure to join the channel firstly or you would like to be a Fallito.
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
                        if member_to_call.id == caller.id:
                            if member_to_call.dm_channel is None:
                                await member_to_call.create_dm()
                            ttl = 1800
                            await member_to_call.dm_channel.send("{0.name}, la sua onorevole presenza è richiesta dal gentile {1.name}".format(member_to_call, caller),delete_after=ttl)
                            await ctx.channel.send("{0.name} invitato! Sta sorta di fallito... \t\t\t Blacksbebond Blacksbebond 🎶🎵🎶🎵".format(member_to_call))
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
            options = ctx.message.content.replace(">services","").strip()
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
    
class cinema(commands.Cog):
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
            # quando il comando usato è in cooldown
            await ctx.send(f"{ctx.message.author.name}, non spammare, il comando è in cooldown! Cooldown - {datetime.timedelta(seconds=round(error.retry_after))}.")
        else:
            await ctx.send('An error occurred: {}'.format(str(error)))  
    @commands.command(name='embed-film',pass_context=True)
    async def _embed_film(self, ctx: commands.Context):

        message = ctx.message.content
        sender = ctx.message.author
        diz = crea_dizionario(message.split("\n")[1:])
        
        embed_sent = await ctx.channel.send(embed = discord.Embed(title=diz["titolo"],
                                                      colour = random.randint(0, 0xffffff),
                                                      #url = "https://www.google.com/search?q=pirati+dei+caraibi+2&oq=pirati+dei+caraibi&aqs=chrome.0.69i59j69i57j69i60l3.3080j0j1&sourceid=chrome&ie=UTF-8"
                                                      url="https://www.google.com/search?q={}".format(diz["titolo"].replace(" ","%20"))
                                                      )
                                                      
                                                    .set_author(name=" By {user}".format(user=sender.name), icon_url=sender.avatar_url)        
                                                    .set_image(url=diz["immagine"])  
                                                    .add_field(name= "Durata del film: ",value="{0} ore e {1}  minuti".format(diz["durata"].split(".")[0],diz["durata"].split(".")[1]))
                                                    .add_field(name="Data della visione: ",value= diz["data"])
                                                    .add_field(name="Genere/i: ",value= diz["genere"])
                                                    
                                                    .add_field(name="Orario dell'inizio (circa): ",value= diz["orario"])
                                                    .add_field(name="Orario della fine (stimato): ",value= sommatempi(diz["orario"].split("."),diz["durata"].split(".")))
                                                    
                                                    )
        await embed_sent.add_reaction('👍🏽')
        await embed_sent.add_reaction('👎🏽')
        await ctx.message.delete()
        with open("film.txt","a") as file:
            file.write("{0}-{1}".format(diz["titolo"],embed_sent.id))
        
    @commands.command(name="start-film",pass_context=True)
    async def _start_film(self, ctx: commands.Context, film_name = ""):
        if film_name == "":
            await ctx.channel.send("Errore, nessun film è stato specificato!")
            return
        caller = ctx.message.author
        server = ctx.guild
        id_messaggio = None
        with open("film.txt","r") as file:
            for riga in file.readlines():
                if film_name in riga:
                    id_messaggio = int(riga.split("-")[1].replace("\n",""))
        if id_messaggio == None:
            await ctx.channel.send("Errore, non esiste il film specificato!")
            return
        channel = [canale for canale in await ctx.guild.fetch_channels() if canale.id == id_film_channel][0]
        messaggio = await channel.fetch_message(id_messaggio)
        reazioni = messaggio.reactions
        users = []
        for reaction in reazioni:
            if reaction.emoji == "👍🏽":
                async for user in reaction.users():
                    users.append(user)
        if users == []:
            await ctx.channel.send("Sorry, bro, nessuno è interessato al film!")
            return
        for user in users:
            if not user.bot :
                member = await server.fetch_member(user.id)
                if member.dm_channel is None:
                    await member.create_dm()
                ttl = 30
                await member.dm_channel.send("Hey,{0.name} ti invita in canale, {1} sta per cominciare".format(caller,film_name),delete_after=ttl)            
                await ctx.channel.send("{0.name} arriva subito! Forse . .. .. . . .. . . .".format(member))
    @commands.command(name="film",pass_context=True)
    async def film(delf,ctx:commands.Context):
        options = ctx.message.content.replace(">film ","")
        sender = ctx.message.author
        url = "https://www.imdb.com/find?q=" + options.replace(" ","+")
        print("url: ",url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        semi_link = [a.attrs.get('href') for a in soup.select('td.result_text a')][0]
        film_link = "https://www.imdb.com/" + semi_link
        print("link: ",film_link)
        film_response = requests.get(film_link)
        film_soup = BeautifulSoup(film_response.text, 'lxml')
        #<ul class="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt" role="presentation" data-testid="hero-title-block__metadata"><li role="presentation" class="ipc-inline-list__item"><a href="/title/tt0371746/releaseinfo?ref_=tt_ov_rdat" class="ipc-link ipc-link--baseAlt ipc-link--inherit-color TitleBlockMetaData__StyledTextLink-sc-12ein40-1 rgaOW">2008</a><span class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex">2008</span></li><li role="presentation" class="ipc-inline-list__item"><a href="/title/tt0371746/parentalguide/certificates?ref_=tt_ov_pg" class="ipc-link ipc-link--baseAlt ipc-link--inherit-color TitleBlockMetaData__StyledTextLink-sc-12ein40-1 rgaOW">T</a><span class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex">T</span></li><li role="presentation" class="ipc-inline-list__item">2<!-- -->h<!-- --> <!-- -->6<!-- -->min</li></ul>
        l = film_soup.select("ul.TitleBlockMetaData__MetaDataList-sc-12ein40-0 li")
        titolo = options
        anno = l[0].get_text()[:4]
        durata = l[2].get_text().replace("h","").replace("m","").replace(" ",".")
        l_generi = [a.get_text() for a in film_soup.select("span.ipc-chip__text")[:3]]
        print(l_generi)
        generi = "{a[0]},{a[1]},{a[2]}".format(a=l_generi)
        orario_inizio = "20.45"
        embed_sent = await ctx.channel.send(embed = discord.Embed(title=titolo,
                                                      colour = random.randint(0, 0xffffff),
                                                      url=film_link
                                                      )                                
                                                    .set_author(name=" By {user}".format(user=sender.name), icon_url=sender.avatar_url)        
                                                    .set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHqLNcAAk0KaWRNIPXUR4Ss36cwil1_v6YKA&usqp=CAU")
                                                    .add_field(name= "Durata del film: ",value="{0} ore e {1}  minuti".format(durata.split(".")[0],durata.split(".")[1]))
                                                    .add_field(name="Anno: ",value=anno)
                                                    .add_field(name="Genere/i: ",value=generi)
                                                    .add_field(name="Orario dell'inizio (circa): ",value=orario_inizio)
                                                    .add_field(name="Orario della fine (stimato): ",value= sommatempi(orario_inizio.split("."),durata.split(".")))
                                                    )
        await embed_sent.add_reaction('👍🏽')
        await embed_sent.add_reaction('👎🏽')
        await ctx.message.delete()
    


bot = commands.Bot(command_prefix='>',
                   activity = discord.Activity(type=discord.ActivityType.listening, name="Laura Pausini"), 
                   status = discord.Status.do_not_disturb,
                   intents = discord.Intents().all())

bot._skip_check = lambda x, y: False
bot.add_cog(servizi(bot))
bot.add_cog(cinema(bot))

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
                with open("nomi.txt","r",encoding="utf-8") as file:
                    lista_di_nomi = [riga for riga in file]
                    import random
                    r_number = random.randint(0, len(lista_di_nomi)-1)
                    nickname = lista_di_nomi[r_number]
            except Exception as e:
                print(e)
        
        if Giappo_shuffle_service:
            try:
                with open("suffissi-giapponesi.txt","r",encoding="utf-8") as file:
                    lista_di_suffissi = [riga for riga in file]
                    dizionario_suffissi = {indice:str(suffisso).replace("-","") for indice,suffisso in enumerate(lista_di_suffissi)}
                    import random
                    r_number = random.randint(0, len(lista_di_suffissi)-1)
                    # controllo se ha già suffisso
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
        
        #Il nick viene cambiato solamente se si possiede il ruolo che permette la modifica sul nome
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