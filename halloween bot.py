import discord, random, asyncio, threading, time

démon = ["https://media1.tenor.com/images/b2ce897ba83f0f2453add0a2631e7532/tenor.gif?itemid=15952632",
        "https://media1.tenor.com/images/5f0785a904d3ea86edb6733b731974a1/tenor.gif?itemid=12666062",
        "https://media.melty.fr/article-4018245-ratio15_720-f5/media.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTlyiUhKbNAGAF8yvWsthZXlEJv_-HnLz_13w&usqp=CAU"]
vampire = ["https://teammanga.fr/wp-content/uploads/2020/08/noblesse-1.jpg",
            "https://149360821.v2.pressablecdn.com/wp-content/uploads/2017/11/Plumber-Vampire.jpg",
            "https://static.lpnt.fr/images/2020/10/21/20899750lpw-20900955-article-jpg_7430520_1250x625.jpg",
            "https://static.wikia.nocookie.net/bakemonogatari1645/images/1/17/Onomonogatari_bluray.jpg/revision/latest/top-crop/width/300/height/300?cb=20160711035646",
            "https://images-na.ssl-images-amazon.com/images/I/51O61yEQSfL._AC_.jpg",
            "https://pm1.narvii.com/7549/30487661d20c189be4c943ac09a1962903019d42r1-555-685v2_hq.jpg",
            "https://cdn.imgbin.com/7/17/9/imgbin-sonic-and-the-secret-rings-sonic-the-hedgehog-amy-rose-vampire-legendary-creature-others-x8LkqwpaC6LBgT3nWHp5bKbPX.jpg",
            "https://static.wikia.nocookie.net/fireemblem/images/d/d5/ShuraPortrait.png/revision/latest?cb=20150712180545&path-prefix=fr"]
fantôme  = ["https://static.vecteezy.com/ti/vecteur-libre/p1/1999137-halloween-blanc-fantome-dessin-anime-vecteur-conception-gratuit-vectoriel.jpg",
            "https://lh3.googleusercontent.com/WQny7hia6hGcJk7m8HK2CBD-qIFtkMRrU_7U7vv3FOdLc02ZxCcXeJE225reWGuAHTG1EuAdh4RE67Gt8Vy9=w1600-h789",
            "https://static.wikia.nocookie.net/mansionluigi/images/2/28/157283029117635715.png/revision/latest?cb=20191104012009",
            "https://static.wikia.nocookie.net/mario/images/9/9f/Boo_%21.png/revision/latest?cb=20130626141706&path-prefix=fr",
            "https://i.pinimg.com/originals/99/3e/c6/993ec6139c72b771eb5a9b727ba826da.jpg",
            "https://vignette.wikia.nocookie.net/villains-fr/images/6/6c/7e60648f75725bcb869e49f0f96581a6.png/revision/latest?cb=20200519122959&path-prefix=fr",
            "https://ih1.redbubble.net/image.1679365686.0212/st,small,507x507-pad,600x600,f8f8f8.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQsEM7Ly52A8GykgOLWwmo18-ltHuQw3jmknw&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT7XDfREtFHmMFMACU32Tvp4xUyKl-iPD2-EA&usqp=CAU",
            "https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Pok%C3%A9mon_Haunter_art.png/220px-Pok%C3%A9mon_Haunter_art.png",
            "https://cdn.bulbagarden.net/upload/a/a5/608Lampent.png"]

TOKEN = 'Njg3MzMwOTg2OTIwNjQwNTE0.XmkM3Q.4XO2g6C0hkOc6RB6Mh1IA0T_ztM'
client = discord.Client()

ghost_list = []

with open("stat", "r", encoding="utf-8") as fichier:
    stat = []
    for ligne in fichier:
        tset = []
        truc = ''
        for char in ligne:
            if char != '\n' and char != ';':
                truc += char
            if (char == ';' or char == '\n') and char != '':
                tset.append(truc)
                truc = ''
        stat.append(tset)
for liste in stat:
    del liste[len(liste)-1]

class monster(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.t = time.time()
        self.s = s
    def run(self):
        while True:
            if self.t+self.s<time.time():
                self.t = time.time()
                for ghostin in ghost_list:
                    numbin = random.randint(0,8)
                    if 3<numbin:
                        listeréaction = ["👻",random.choice(["🧅","👹"])]
                        msg = asyncio.run_coroutine_threadsafe(random.choice(ghostin).send(embed = discord.Embed(title = '**__un fantôme  est apparue__**').set_footer(text = "cliquer sur 👻 pour le faire disparaitre").set_image(url = random.choice(fantôme ))),client.loop)
                    elif 0<numbin:
                        listeréaction = ["🧅",random.choice(["👻","👹"])]
                        msg = asyncio.run_coroutine_threadsafe(random.choice(ghostin).send(embed = discord.Embed(title = '**__un vampire est apparue__**').set_footer(text = "cliquer sur 🧅 pour le faire disparaitre").set_image(url = random.choice(vampire))),client.loop)
                    else:
                        listeréaction = ["👹",random.choice(["🧅","👻"])]
                        msg = asyncio.run_coroutine_threadsafe(random.choice(ghostin).send(embed = discord.Embed(title = '**__un démon est apparue__**').set_footer(text = "cliquer sur 👹 pour le faire disparaitre").set_image(url = random.choice(démon))),client.loop)
                    random.shuffle(listeréaction)
                    msg = msg.result()
                    asyncio.run_coroutine_threadsafe(msg.add_reaction(listeréaction[0]),client.loop)
                    asyncio.run_coroutine_threadsafe(msg.add_reaction(listeréaction[1]),client.loop)




@client.event
async def on_ready():
    print('ok')
    text2 = ""
    for guild in client.guilds:
        text2 += f'{client.user} is connected to the following guild:\n'+f'{guild.name}(id: {guild.id})\n'
        members = '\n - '.join([member.name for member in guild.members])
        text2 += f'Guild Members:\n - {members}'
        text2 += "\n"
    print(text2)

@client.event
async def on_reaction_add(reaction, author):
    if author.bot:
        return  
    if str(author) in str(stat):
        pass
    else:
        stat.append([str(author), "0", "0", "0", "0", "0"])
    if reaction.message.embeds[0].title.startswith('**__un fantôme  est apparue__**'):
        if str(reaction) == "👻":
            await reaction.message.delete()
            for ghost in stat:
                if ghost[0] == str(author):
                    stat[stat.index(ghost)][1] = str(int(stat[stat.index(ghost)][1])+1)
                    stat[stat.index(ghost)][2] = str(int(stat[stat.index(ghost)][2])+1)
            text2 = ""
            for ligne in stat:
                for mot in ligne:
                    text2 += mot + ";"
                text2 += "\n"
            mon_fichier = open("stat", "w", encoding="utf-8")
            mon_fichier.write(text2)
            mon_fichier.close
        else:
            for ghost in stat:
                if ghost[0] == str(author):
                    stat[stat.index(ghost)][1] = str(int(stat[stat.index(ghost)][1])-1)
            text2 = ""
            for ligne in stat:
                for mot in ligne:
                    text2 += mot + ";"
                text2 += "\n"
            mon_fichier = open("stat", "w", encoding="utf-8")
            mon_fichier.write(text2)
            mon_fichier.close
    elif reaction.message.embeds[0].title.startswith('**__un vampire est apparue__**'):
        if str(reaction) == "🧅":
            await reaction.message.delete()
            for ghost in stat:
                if ghost[0] == str(author):
                    stat[stat.index(ghost)][1] = str(int(stat[stat.index(ghost)][1])+3)
                    stat[stat.index(ghost)][3] = str(int(stat[stat.index(ghost)][3])+1)
            text2 = ""
            for ligne in stat:
                for mot in ligne:
                    text2 += mot + ";"
                text2 += "\n"
            mon_fichier = open("stat", "w", encoding="utf-8")
            mon_fichier.write(text2)
            mon_fichier.close
        else:
            for ghost in stat:
                if ghost[0] == str(author):
                    stat[stat.index(ghost)][1] = str(int(stat[stat.index(ghost)][1])-3)
            text2 = ""
            for ligne in stat:
                for mot in ligne:
                    text2 += mot + ";"
                text2 += "\n"
            mon_fichier = open("stat", "w", encoding="utf-8")
            mon_fichier.write(text2)
            mon_fichier.close
    elif reaction.message.embeds[0].title.startswith('**__un démon est apparue__**'):
        if str(reaction) == "👹":
            await reaction.message.delete()
            for ghost in stat:
                if ghost[0] == str(author):
                    stat[stat.index(ghost)][1] = str(int(stat[stat.index(ghost)][1])+5)
                    stat[stat.index(ghost)][5] = str(int(stat[stat.index(ghost)][3])+1)
            text2 = ""
            for ligne in stat:
                for mot in ligne:
                    text2 += mot + ";"
                text2 += "\n"
            mon_fichier = open("stat", "w", encoding="utf-8")
            mon_fichier.write(text2)
            mon_fichier.close
        else:
            for ghost in stat:
                if ghost[0] == str(author):
                    stat[stat.index(ghost)][1] = str(int(stat[stat.index(ghost)][1])-5)
            text2 = ""
            for ligne in stat:
                for mot in ligne:
                    text2 += mot + ";"
                text2 += "\n"
            mon_fichier = open("stat", "w", encoding="utf-8")
            mon_fichier.write(text2)
            mon_fichier.close

@client.event
async def on_message(message):
    if str(message.author) in str(stat):
        pass
    else:
        stat.append([str(message.author), "0", "0", "0", "0", "0"])
    if message.content.lower().startswith("!start in ") and message.author.guild_permissions.administrator:
        await message.channel.send(embed= discord.Embed(description="hou hou des monstres apparait dans les channel indiqué"))
        ghost_list.append(message.channel_mentions)
        a = monster(5)
        a.start()
    elif "!reset stat" in message.content.lower() and str(message.author) == "coco#8012":
        for pseudo in stat:
            pseudo[1] = "0"
            pseudo[2] = "0"
            pseudo[3] = "0"
            try:
                pseudo[5] = "0"
            except:
                pseudo.append("0")
        await message.channel.send(embed= discord.Embed(description="ça a bien été reset"))
        text2 = ""
        for ligne in stat:
            for mot in ligne:
                text2 += mot + ";"
            text2 += "\n"
        mon_fichier = open("stat", "w", encoding="utf-8")
        mon_fichier.write(text2)
        mon_fichier.close
    elif message.content.lower().startswith("!stat"):
        if str(message.author) in str(stat):
            pass
        else:
            stat.append([str(message.author), "0", "0", "0", "0", "0"])
        for pseudo in stat:
            if str(message.author) in pseudo[0]:
                await message.channel.send(embed= discord.Embed(description=f"""{pseudo[0]} votre score est {pseudo[1]} de monstre. vous avez capturer {pseudo[2]} de fantôme, {pseudo[3]} de vampire et {pseudo[3]} de démon."""))
    elif message.content.lower().startswith("!stat "):
        azerty = 0
        for pseudo in stat:
            if message.content.lower().endswith(pseudo[0].lower()) and pseudo[0] != '':
                azerty = 1
                await message.channel.send(embed= discord.Embed(description=f"""{pseudo[0]} son score est {pseudo[1]} de monstre. vous avez capturer {pseudo[2]} de fantôme, {pseudo[3]} de vampire et {pseudo[3]} de démon."""))
                
            if message.mentions:
                #print(str(message.mentions[0]),pseudo[0],str(message.mentions[0])==pseudo[0])
                if str(message.mentions[0])==pseudo[0]:
                    print(message.mentions[0])
                    azerty = 1
                    await message.channel.send(embed= discord.Embed(description=f"""{pseudo[0]} son score est {pseudo[1]} de monstre. vous avez capturer {pseudo[2]} de fantôme, {pseudo[3]} de vampire et {pseudo[3]} de démon."""))
                    
        if azerty != 1:
            await message.channel.send(embed= discord.Embed(description="soit je le connais pas ou soit il a pas encore dit de phrase"))
    elif message.content.lower().startswith("!lb fantôme "):
        statclass = sorted(stat, key=lambda student: int(student[2]), reverse= True)
        await message.channel.send(embed= discord.Embed(description=f"le classement est :\n1 er {statclass[0][0]} avec {statclass[0][2]}\n2 eme {statclass[1][0]} avec {statclass[1][2]}\n3 eme {statclass[2][0]} avec {statclass[2][2]}\n4 eme {statclass[3][0]} avec {statclass[3][2]}\n5 eme {statclass[4][0]} avec {statclass[4][2]}\n6 eme {statclass[5][0]} avec {statclass[5][2]}\n7 eme {statclass[6][0]} avec {statclass[6][2]}\n8 eme {statclass[7][0]} avec {statclass[7][2]}\n9 eme {statclass[8][0]} avec {statclass[8][2]}\n10 eme {statclass[9][0]} avec {statclass[9][2]}"))
    elif message.content.lower().startswith("!lb vampire"):
        statclass = sorted(stat, key=lambda student: int(student[3]), reverse= True)
        await message.channel.send(embed= discord.Embed(description=f"le classement est :\n1 er {statclass[0][0]} avec {statclass[0][3]}\n2 eme {statclass[1][0]} avec {statclass[1][3]}\n3 eme {statclass[2][0]} avec {statclass[2][3]}\n4 eme {statclass[3][0]} avec {statclass[3][3]}\n5 eme {statclass[4][0]} avec {statclass[4][3]}\n6 eme {statclass[5][0]} avec {statclass[5][3]}\n7 eme {statclass[6][0]} avec {statclass[6][3]}\n8 eme {statclass[7][0]} avec {statclass[7][3]}\n9 eme {statclass[8][0]} avec {statclass[8][3]}\n10 eme {statclass[9][0]} avec {statclass[9][3]}"))
    elif message.content.lower().startswith("!lb démon"):
        statclass = sorted(stat, key=lambda student: int(student[5]), reverse= True)
        await message.channel.send(embed= discord.Embed(description=f"le classement est :\n1 er {statclass[0][0]} avec {statclass[0][5]}\n2 eme {statclass[1][0]} avec {statclass[1][5]}\n3 eme {statclass[2][0]} avec {statclass[2][5]}\n4 eme {statclass[3][0]} avec {statclass[3][5]}\n5 eme {statclass[4][0]} avec {statclass[4][5]}\n6 eme {statclass[5][0]} avec {statclass[5][5]}\n7 eme {statclass[6][0]} avec {statclass[6][5]}\n8 eme {statclass[7][0]} avec {statclass[7][5]}\n9 eme {statclass[8][0]} avec {statclass[8][5]}\n10 eme {statclass[9][0]} avec {statclass[9][5]}"))
    elif message.content.lower().startswith("!lb"):
        statclass = sorted(stat, key=lambda student: int(student[1]), reverse= True)
        await message.channel.send(embed= discord.Embed(description=f"le classement est :\n1 er {statclass[0][0]} avec {statclass[0][1]}\n2 eme {statclass[1][0]} avec {statclass[1][1]}\n3 eme {statclass[2][0]} avec {statclass[2][1]}\n4 eme {statclass[3][0]} avec {statclass[3][1]}\n5 eme {statclass[4][0]} avec {statclass[4][1]}\n6 eme {statclass[5][0]} avec {statclass[5][1]}\n7 eme {statclass[6][0]} avec {statclass[6][1]}\n8 eme {statclass[7][0]} avec {statclass[7][1]}\n9 eme {statclass[8][0]} avec {statclass[8][1]}\n10 eme {statclass[9][0]} avec {statclass[9][1]}"))

client.run(TOKEN)