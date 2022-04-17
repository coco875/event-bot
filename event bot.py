import discord, random, asyncio, threading, time, json

type_event = "Pâques"

type1 = []
type2 = []
type3  = []

data = {}

with open("type.json", "r", encoding='utf-8') as f:
    data = json.load(f)[type_event]
    
    print(data)
    type1 = data["type1"]
    type2 = data["type2"]
    type3 = data["type3"]

TOKEN = 'Njg3MzMwOTg2OTIwNjQwNTE0.XmkM3Q.4XO2g6C0hkOc6RB6Mh1IA0T_ztM'
client = discord.Client()

ghost_list = []

with open("stat", "r", encoding="utf-8") as fichier:
    stat = json.load(fichier)

class monster(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.t = time.time()
        self.s = s
        self.stop = True
    def run(self):
        while self.stop:
            if self.t+self.s<time.time():
                self.t = time.time()
                for ghostin in ghost_list:
                    numbin = random.randint(0,8)
                    if 3<numbin:
                        listeréaction = [type3["emoji"],random.choice([type1,type2])["emoji"]]
                        embed = discord.Embed(title = f'**__un {type3["name"]}  est apparue__**')
                        embed.set_footer(text = f"cliquer sur {type3['emoji']} pour le faire disparaitre")
                        embed.set_image(url = random.choice(type3["url"]))

                        msg = asyncio.run_coroutine_threadsafe(random.choice(ghostin).send(embed = embed),client.loop)
                    elif 0<numbin:
                        listeréaction = [type2["emoji"],random.choice([type1,type3])["emoji"]]
                        embed = discord.Embed(title = f'**__un {type2["name"]}  est apparue__**')
                        embed.set_footer(text = f"cliquer sur {type2['emoji']} pour le faire disparaitre")
                        embed.set_image(url = random.choice(type2["url"]))

                        msg = asyncio.run_coroutine_threadsafe(random.choice(ghostin).send(embed = embed),client.loop)
                    else:
                        listeréaction = [type1["emoji"],random.choice([type2,type3])["emoji"]]
                        embed = discord.Embed(title = f'**__un {type1["name"]}  est apparue__**')
                        embed.set_footer(text = f"cliquer sur {type1['emoji']} pour le faire disparaitre")
                        embed.set_image(url = random.choice(type1["url"]))

                        msg = asyncio.run_coroutine_threadsafe(random.choice(ghostin).send(embed = embed),client.loop)
                    random.shuffle(listeréaction)
                    msg = msg.result()
                    asyncio.run_coroutine_threadsafe(msg.add_reaction(listeréaction[0]),client.loop)
                    asyncio.run_coroutine_threadsafe(msg.add_reaction(listeréaction[1]),client.loop)




@client.event
async def on_ready():
    print('connected')

@client.event
async def on_reaction_add(reaction, author):
    if author.bot:
        return  
    if str(author.id) in str(stat):
        pass
    else:
        stat.append({
            "name_id":author.id, 
            "type1":0, 
            "type2":0, 
            "type3":0, 
            "total":0
            })

    for num, name in enumerate(data):
        if reaction.message.embeds[0].title.startswith(f'**__un {data[name]["name"]}  est apparue__**'):
            if reaction.emoji == data[name]["emoji"]:
                for j in stat:
                    if author.id == j["name_id"]:
                        j[name] += 1
                        j["total"] += data[name]["points"]
                        with open("stat", "w", encoding="utf-8") as fichier:
                            json.dump(stat, fichier, indent=4)
                        await reaction.message.delete()
                        await reaction.message.channel.send(f'{author.mention} a capturé un {data[name]["name"]}')
                        break
            else:
                for j in stat:
                    if j["name_id"] == author.id:
                        j["total"] -= data[name]["points"]
a = monster(5)
@client.event
async def on_message(message):
    global a
    if str(message.author.id) in str(stat):
        pass
    else:
        stat.append({
            "name_id":message.author.id, 
            "type1":0, 
            "type2":0, 
            "type3":0, 
            "total":0
            })
    if message.content.lower().startswith("+start in ") and message.author.guild_permissions.administrator:
        await message.channel.send(embed= discord.Embed(description="l'évènement a commencé dans les channel indiqué"))
        ghost_list.append(message.channel_mentions)
        a = monster(5)
        a.start()
    elif message.content.lower().startswith("+stop") and message.author.guild_permissions.administrator:
        a.stop = False
        await message.channel.send(embed= discord.Embed(description="fin de l'événement"))
    elif message.content.lower().startswith("+help"):
        await message.channel.send(embed= discord.Embed(description="+stat \ndonne le nombre de monstré capturé et le point\n+lb\nle leaderboard si vous rajouter un monstre vous aurez le classement pour ce monstre"))
    elif "+reset stat" in message.content.lower() and message.author.guild_permissions.administrator:
        for pseudo in stat:
            pseudo.update({ 
            "type1":0, 
            "type2":0, 
            "type3":0, 
            "total":0
            })
        await message.channel.send(embed= discord.Embed(description="ça a bien été reset"))
        json.dump(stat, open("stat", "w", encoding="utf-8"))

    elif message.content.lower().startswith("+stat "):
        azerty = 0
        for pseudo in stat:
                
            if message.mentions:
                #print(str(message.mentions[0]),pseudo[0],str(message.mentions[0])==pseudo[0])
                if message.mentions[0].id == pseudo["name_id"]:
                    print(message.mentions[0])
                    azerty = 1
                    await message.channel.send(embed= discord.Embed(description=f"""<@!{pseudo["name_id"]}> a un score total est {pseudo["total"]}. vous avez capturer {pseudo["type3"]} {type3["name"]}(s), {pseudo["type2"]} {type2["name"]} et {pseudo["type1"]} {type1["name"]}(s)."""))
                    
        if azerty != 1:
            await message.channel.send(embed= discord.Embed(description="soit je le connais pas ou soit il a pas encore dit de phrase"))

    elif message.content.lower().startswith("+stat"):
        for pseudo in stat:
            if message.author.id == pseudo["name_id"]:
                await message.channel.send(embed= discord.Embed(description=f"""<@!{pseudo["name_id"]}> votre score total est {pseudo["total"]}. vous avez capturer {pseudo["type3"]} {type3["name"]}(s), {pseudo["type2"]} {type2["name"]} et {pseudo["type1"]} {type1["name"]}(s)."""))
    
    elif message.content.lower().startswith("+lb "):
        for num, name in enumerate(data):
            if message.content.lower().startswith(f"+lb {data[name]['name']}"):
                statclass = sorted(stat, key=lambda student: int(student[name]), reverse= True)

                chn = ""
                for i in statclass:
                    chn += f"<@!{i['name_id']}> a capturé {i[name]} {data[name]['name']}(s)\n"

                await message.channel.send(embed= discord.Embed(description=chn))
                break
    elif message.content.lower().startswith("+lb"):
        statclass = sorted(stat, key=lambda student: int(student["total"]), reverse= True)

        chn = ""
        for i in statclass:
            chn += f"<@!{i['name_id']}> a {i['total']} point(s)\n"

        await message.channel.send(embed= discord.Embed(description=chn))

client.run(TOKEN)