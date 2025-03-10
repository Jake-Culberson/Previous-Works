


#the lore and data used in this document are not to be copied or distributed. this is incomplete and my plan is to startover from the ground up since
#the DND server i made this for has made massive changes to our documents before i could complete this document. I will be saving a copy for myself but removing the 
#token ID and channel ID's 

#this bot is for discord and can do some fun dice rolling things. please overlook the absolute horrid recursion, i did not at this time take the time to come up with a better
#alternative. since then i have thought of many ways to fix this. this was programmed back in 2023 when i was a less skilled programmer. ~Jake Culberson 3/9/2025


import datetime
import discord
import random
import asyncio
import math
from discord.ext import commands
from multiprocessing.sharedctypes import Value


Bot_Token = "" #i personally used Pylex nodes to run this bot on a live server so that it didnt require my computer to be open. shoutout to them and their amazing work offering
               #free server room for users to run a bot on. one day when i have money i could work on making many bots, maybe even bots that work together and respond.
Channel_ID = 0
CCchannel = 0

#Channel_ID = 1216830677773844671
#1214233268447346748
#646861534718590989
#1214233268447346748
intents = discord.Intents.all()
#intents.members = True
#intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)


print("Hello, World")



@bot.event
async def on_ready():
    print("Hello! Mining Bot is ready!")
    Channel = bot.get_channel(Channel_ID)
    await Channel.send("Hello! Mining Bot is Ready!")

@bot.command(name='systemhelp')
async def systemhelp(ctx):


    await ctx.send(f"---Below is a list of commands--- \n\n!hello :the bot will say hello \n!kys :tell the bot to kill itself\n!dice #amount #sides #modifier  :simple dice roller make sure to include all 3 items. if you have no modifier just put 0 \n\n---Character Related commands---\n!statsUpdate #spi #ten #dex #awa #str #int :updates your stats\n!skillroll #'name of skill' rolls a skill. for a list of skills type !skillHelp\n\n---End of Help---")

@bot.command(name='skillhelp')
async def skillhelp(ctx, skillName = "empty"):
    
    if skillName == "notice":
        await ctx.send(f"    :notice is a skill that allows you to see better. Using natural skills as well as developed ones.")
    else:
        await ctx.send(f"---Here is a list of skills--- \n\nNotice \nGrapple \nRecall")

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send("Hello")

@bot.command(name='kys')
async def kys(ctx):

    insult = random.randint(1,5)

    if (insult == 1):

        returnThreat = "Why dont you kill me yourself you bastard?"
    
    elif (insult == 2):

        returnThreat = "Sounds like a bitch baby who failed their dice checks."
    
    elif (insult == 3):

        returnThreat = "You embody small dick energy."        
    
    elif (insult == 4):

        returnThreat = "Don't care + didn't ask + you fell off + L + Cope + Mald + Seeth + Ratio"
    
    else:

        returnThreat = "Are you gonna go down with me?"       
    


    await ctx.send(f"{returnThreat}")

@bot.command(name = 'response')
async def response(ctx):
    await ctx.send("give a number int !num # format")

    num = 0
    await ctx.send(f"!{num}")
    @bot.command(name = num)
    async def num(ctx, number):
        
        await ctx.send(f"{number}")

@bot.command(name='dice')
async def dice(ctx, x, y, z = 0):

    print(ctx)

    counterOne = 0
    result = z
    arrayOne = []
    while counterOne != int(x):
        counterOne += 1
        DiceA = random.randint(1,int(y))
        round(DiceA)
        arrayOne.append(DiceA)

        endmessage = ''

        #arrayOne.append(DiceA)
        result += DiceA

    for x in arrayOne:
        
        if str(x) == f"{y}":
            endmessage += f"**{str(x)}**" + "+"
        elif str(x) == "1":
            endmessage += f"**{str(x)}**" + "+"
        else:
            endmessage += f"{str(x)}" + "+"
    endmessage += f"Bonus {z}"

    await ctx.send(f"{endmessage} = {result} \n@{ctx.author}")

@bot.command(name='resetcharactersheet')
async def resetcharactersheet(ctx):

    await ctx.send(f"Are you sure you want to reset your character sheet? Y/N")
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if message.content == "Y":
            characterName = activeprofile(ctx.author)
            f = open(f"{ctx.author}{characterName}.txt", 'w')
            f.write("0 spirit \n0 tenacity \n0 dexterity\n0 awareness\n0 strength\n0 intelligence\n")
            f.close()

            f = open(f"{ctx.author}{characterName}Skills.txt", 'w')
            f.write("0 Acrobatics\n0 Athletics\n0 Empathy\n0 Forgery\n0 Fortitude\n0 Hide\n0 Medical\n0 Notice\n0 Performance\n0 RecallInformation\n0 Silvertongue\n0 Subtlety\n0 Wilderness\n0 Willpower\n0 Relationship\n0 Nemesis\n0 Organization\n0 AnimatedCompanion\n0 AnimalHandler\n0 BeastHandler\n0 WeaponProficiency\n0 Brawling\n0 ArmorProficiency\n0 Runestone\n0 Vehicles\n0 CombatVehicles\n0 Crafting\n0 Hacking\n")
            f.close()
            await ctx.send(f"Character sheet has been Reset.")
            @bot.event
            async def on_message(message):
                await bot.process_commands(message)
        else:
            @bot.event
            async def on_message(message):
                await bot.process_commands(message)

@bot.command(name='statsupdate')
async def statsupdate(ctx, spi, ten, dex, awr, str, itg):
    

    characterName = activeprofile(ctx.author)

    await ctx.send(f"Stats Updated")
    f = open(f"{ctx.author}{characterName}.txt", "w")
    f.write(f"{spi} spirit \n{ten} tenacity \n{dex} dexterity\n{awr} awareness\n{str} strength\n{itg} intelligence\n")
    f.close()
    
@bot.command(name='skillupdate')
async def skillupdate(ctx):
    characterName = activeprofile(ctx.author)
    await ctx.send(f"Please select a skill to update")
    @bot.event
    async def on_message(message):

        if message.author == bot.user:
            return


        skill_Line = skills(message.content)
        print (skill_Line)

        if str(skill_Line) == "Notaskill":
            await ctx.send(f"{message.content} is not a skill. try checking spelling and capitalization")
            return

        if str(skill_Line) == "Notaskill":
            @bot.event
            async def on_message(message):
                if message.author == bot.user:
                    return
                await ctx.send(f"that is not a valid skill")
                await bot.process_commands(message)

        await ctx.send(f"you have chosen to update {message.content}")

        skill_name = message.content
        await ctx.send(f"what level is {skill_name}?")
        f = open(f"{ctx.author}{characterName}Skills.txt", "r")
        lines = f.readlines()
        f.close()

        @bot.event
        async def on_message(message):
            if message.author == bot.user:
                return
            

            f = open(f"{ctx.author}{characterName}Skills.txt", "w")
            lines[skill_Line] = f"{message.content} {skill_name}\n"
            f.writelines(lines)
            f.close()

            await ctx.send(f"{skill_name} has been updated to Rank:{message.content}")

            @bot.event
            async def on_message(message):
                await bot.process_commands(message)
    
@bot.command(name='skillroll')
async def skillroll(ctx, typeskill = ""):
    characterName = activeprofile(ctx.author)
    f = open(f"{ctx.author}{characterName}Skills.txt", "r")
    sklines = f.readlines()
    f.close()
    f = open(f"{ctx.author}{characterName}.txt", "r")
    
    lines = f.readlines()

    intZero = lines[0]
    intOne = lines[1]
    intTwo = lines[2]
    intThree = lines[3]
    intFour = lines[4]
    intFive = lines[5]

    spi = intZero[:2]
    ten = intOne[:2]
    dex = intTwo[:2]
    awr = intThree[:2]
    str = intFour[:2]
    itg = intFive[:2]

    
    counterOne = 0
    counterTwo = 0
    result = 0
    arrayTwo = []
    arrayThree = [2]


    match typeskill:
        case "empathy":
            statUsed = int(spi)
            skill = sklines[2]
            statName = "Spirit"
        case "performance":
            statUsed = int(spi)
            skill = sklines[8]
            statName = "Spirit"
        case "silvertongue":
            statUsed = int(spi)
            skill = sklines[10]
            statName = "Spirit"
        case "willpower":
            statUsed = int(spi)
            skill = sklines[13]
            statName = "Spirit"
        case "relationship":
            statUsed = int(spi)
            skill = sklines[14]
            statName = "Spirit"
        case "nemesis":
            statUsed = int(spi)
            skill = sklines[15]
            statName = "Spirit"
        case "animalhandler":
            statUsed = int(spi)
            skill = sklines[18]
            statName = "Spirit"
        case "beasthandler":
            statUsed = int(spi)
            skill = sklines[19]
            statName = "Spirit"
        case "athletics":
            statUsed = int(ten)
            skill = sklines[1]
            statName = "Tenacity"
        case "fortitude":
            statUsed = int(ten)
            skill = sklines[4]
            statName = "Tenacity"
        case "wilderness":
            statUsed = int(ten) 
            skill = sklines[12]
            statName = "Tenacity"
        case "acrobatics":
            statUsed = int(dex)
            skill = sklines[0]
            statName = "Dexterity"
        case "hide":
            statUsed = int(dex) 
            skill = sklines[5] 
            statName = "Dexterity"          
        case "subtlety":
            statUsed = int(dex)
            skill = sklines[11]
            statName = "Dexterity"
        case "notice":
            statUsed = int(awr)
            skill = sklines[7]
            statName = "Awareness"
        case "weaponpro":
            statUsed = int(awr)
            skill = sklines[20]
            statName = "Awareness"
        case "brawling":
            statUsed = int(awr)
            skill = sklines[21]
            statName = "Awareness"
        case "forgery":
            statUsed = int(itg) 
            skill = sklines[3]
            statName = "Intelligence"
        case "medical":
            statUsed = int(itg) 
            skill = sklines[6]
            statName = "Intelligence"
        case "recall":
            statUsed = int(itg) 
            skill = sklines[9]
            statName = "Intelligence"
        case "organization":
            statUsed = int(itg) 
            skill = sklines[16]
            statName = "Intelligence"
        case "armorproficiency":
            statUsed = int(itg) 
            skill = sklines[22]
            statName = "Intelligence"
        case "runestone":
            statUsed = int(itg) 
            skill = sklines[23]
            statName = "Intelligence"
        case "vehicles":
            statUsed = int(itg) 
            skill = sklines[24]
            statName = "Intelligence"
        case "combatvehicle":
            statUsed = int(itg) 
            skill = sklines[25]
            statName = "Intelligence"
        case "crafting":
            statUsed = int(itg) 
            skill = sklines[26]
            statName = "Intelligence"
        case "hacking":
            statUsed = int(itg) 
            skill = sklines[27]
            statName = "Intelligence"
        case "profession":
            statUsed = int(itg) 
            skill = 0
            statName = "Intelligence" 
        case "":
            await ctx.send(f"please select a skill from the skill list")  
  
    if int(skill[0]) >= 3:
            counterOne += -1
            counterTwo += -1

    while counterOne < 2:
        counterOne += 1
        DiceA = random.randint(1,10)
        round(DiceA)
        arrayTwo.append(DiceA)
        arrayThree.append(DiceA)
        print(DiceA)
        if int(skill[0]) >= 5:  
            counterTwo += 1  
            if int(DiceA) == 6:
                counterOne += -1
                
            elif int(DiceA) == 10:
                counterOne += -1

            if int(counterTwo) == 2:
                if min(arrayTwo) == 6:
                    counterOne += 1
                elif min(arrayTwo) == 10:
                    counterOne += 1

        print(f"{counterOne} counter")

        result += DiceA

    if int(skill[0]) > 0:
        diceCheck = result + statUsed + int(skill[0]) + 1
    else:    
        diceCheck = result + statUsed + int(skill[0])
    arrayFour = []
    mincounter = 0
    endmessage = ""
    RDcounter = 0
    arrayFour.append(arrayTwo[0])
    arrayFour.append(arrayTwo[1])
    if int(skill[0]) >= 3:
        arrayFour.append(arrayTwo[2])

    for x in arrayTwo:
        if RDcounter < 3:
            if int(skill[0]) >= 3:

                if x == min(arrayFour):
                    if mincounter < 1:
                        endmessage += f"~~{(x)}~~" + " + "
                        mincounter += 1
                        result += -x
                    else: 
                        endmessage += f"**{(x)}**" + " + "
                elif x == 10:
                    endmessage += f"**{(x)}**" + " + "
                elif x == 1:
                    endmessage += f"**{(x)}**" + " + "
                else:
                    endmessage += f"{(x)}" + " + "
            
            else:
                if x == 10:
                    endmessage += f"**{(x)}**" + " + "
                elif x == 1:
                    endmessage += f"**{(x)}**" + " + "
                else:
                    endmessage += f"{(x)}" + " + "
        RDcounter += 1
   
    if int(skill[0]) > 0:
        endmessage += f"{statUsed} {statName} + {int(skill[0])+1} {typeskill}"
    else:
        endmessage += f"{statUsed} {statName} + {int(skill[0])} {typeskill}"
        
    result += statUsed + int(skill[0])
    await ctx.send(f"{endmessage} = {result} \n@{ctx.author}")
    dc = 25
    if result >= dc:
        await ctx.send(f"You beat the DC of {dc}")
    else:
        await ctx.send(f"You failed the DC of {dc}")
    
    
    
    f.close()

@bot.command(name='charactersheet')
async def charactersheet(ctx):
    characterName = activeprofile(ctx.author)
    f = open(f"{ctx.author}{characterName}Skills.txt", "r")
    lines = f.readlines()
    f.close()
    f = open(f"{ctx.author}{characterName}.txt", "r")
    slines = f.readlines()
    f.close()

    await ctx.send(f"[STATS]\n\n{slines[0]}{slines[1]}{slines[2]}{slines[3]}{slines[4]}{slines[5]}\n\n[SKILLS]\n{lines[0]}{lines[1]}{lines[2]}{lines[3]}{lines[4]}{lines[5]}{lines[6]}{lines[7]}{lines[8]}{lines[9]}{lines[10]}{lines[11]}{lines[12]}{lines[13]}{lines[14]}{lines[15]}{lines[16]}{lines[17]}{lines[18]}{lines[19]}{lines[20]}{lines[21]}{lines[22]}{lines[23]}{lines[24]}{lines[25]}{lines[26]}\n") 
        
@bot.command(name='mining')
async def mining(ctx, Floor = "Zero"):
    await ctx.send(f"What floor are you on?")
    @bot.event
    async def on_message(message):

        if message.content == 0:
            @bot.event
            async def on_message(message):
                await bot.process_commands(message)

        randomstring1 = message.content
        randomstring2 =  isinstance(randomstring1, str)
        if str(randomstring2) == True:
            @bot.event
            async def on_message(message):
                await bot.process_commands(message)

        await bot.process_commands(message)
        message.content = (message.content.lower())
        flag = True
        if message.author == bot.user:
            return
        try:
            int(message.content)
        except ValueError:

            flag = False
        if flag:
            floor = int(message.content)
            await ctx.send(f"You are on Floor {floor}. \nHow many times are you rolling notice?")
            @bot.event
            async def on_message(message):
                await bot.process_commands(message)


                randomstring1 = message.content
                randomstring2 =  isinstance(randomstring1, str)
                if str(randomstring2) == True:
                    @bot.event
                    async def on_message(message):
                        await bot.process_commands(message)
                message.content = (message.content.lower())
                flagTwo = True
                if message.author == bot.user:
                    return
                


                try:

                    int(message.content)
                except ValueError:

                    flagTwo = False

                if message.author == ctx:
                    searchnum = int(message.content)
                    return searchnum
                
                if flagTwo:
                    await ctx.send(f"you are searching {int(message.content)} Times.")
                    stats(ctx.author)
                    counterTwo = 0
                    characterName = activeprofile(ctx.author)
                    f = open(f"{ctx.author}{characterName}Sheet.txt", "r")
                    lines = f.readlines()
                    f.close()
                    miningarr = []
                    while counterTwo < int(message.content):
                                               
                        counterTwo += 1
                        result = miningDice()
                        #exploding could check result and de iterate the counterTwo
                        stat = stats(ctx.author)
                        result += int(stat[3])
                        skill = lines[33]
                        result += int(skill[0]) + 1
                        if int(skill[0]) == 0:
                            result += -1
                        if result < 16:
                            amount = 2
                        elif 15 < result < 21:
                            amount = 4
                        elif 20 < result < 25:
                            amount = 5
                        else:
                            amount = 6
                        
                        material = miningFloors(int(message.content)) 
                        
                        miningarr.append(f"**#{counterTwo}**You rolled a **{result}**.You found **{amount}** **{material}**")

                    endmessage = ''
                    for x in miningarr:
                        endmessage += '\n' + x
                    await ctx.send(endmessage)
                    await ctx.send("Done")

                    if counterTwo >= int(message.content):
                        @bot.event
                        async def on_message(message):
                            await bot.process_commands(message)


@bot.command(name = "minetime")
async def timer(ctx, time, countbynum):
    minetimeuser = ctx.author
    countby = int(countbynum)

    secondint = int(time)
    while secondint >= 0:

        if secondint > 0:
            await ctx.send(f"you have {secondint} seconds left")
            if secondint >= countby:
                await asyncio.sleep(countby)
                secondint -= countby
            else:
                await asyncio.sleep(secondint)
                secondint -= secondint
        else:
            await ctx.send(f"your timer is done") 
            return        


@bot.command(name='corpMining')
async def mining(ctx, Floor = "Zero"):
    corpMiningUser = ctx.author
    await ctx.send(f"how many cargo do you gain per day for your corp?")
    @bot.event
    async def on_message(message):

        if message.author == bot.user:
            return
        if message.author != corpMiningUser:
            @bot.event
            async def on_message(message):
                await bot.process_commands(message)
                return

        if message.content == 0:
            @bot.event
            async def on_message(message):
                await bot.process_commands(message)

        randomstring1 = message.content
        randomstring2 =  isinstance(randomstring1, str)
        if str(randomstring2) == True:
            @bot.event
            async def on_message(message):
                await bot.process_commands(message)

        #await bot.process_commands(message)
        message.content = (message.content.lower())
        flag = True
        try:
            int(message.content)
        except ValueError:
            flag = False

        if flag:
            floor = 65
            
            randomstring1 = message.content
            randomstring2 =  isinstance(randomstring1, str)


            if str(randomstring2) == True:
                @bot.event
                async def on_message(message):
                    await bot.process_commands(message)
                
            message.content = (message.content.lower())
            flagTwo = True
            if message.author == bot.user:
                return
                
            try:

                int(message.content)

            except ValueError:

                flagTwo = False

            # if message.author == ctx:
            #     searchnum = int(message.content)
            #     return searchnum
                
            if flagTwo:
                #await ctx.send(f"you are searching {int(message.content)} Times.")
                #stats(ctx.author)
                counterTwo = 0
                characterName = activeprofile(ctx)
                # f = open(f"{ctx.author}{characterName}Skills.txt", "r")
                # lines = f.readlines()
                # f.close()
                miningarr = []
                while counterTwo < int(message.content):
                                           
                    counterTwo += 1
                    #result = miningDice()
                    #exploding could check result and de iterate the counterTwo
                    # stat = stats(ctx.author)
                    # result += int(stat[3])
                    # skill = lines[7]
                    # result += int(skill[0]) + 1
                    # if int(skill[0]) == 0:
                    #     result += -1
                    # if result < 16:
                    #     amount = 2
                    # elif 15 < result < 21:
                    #     amount = 4
                    # elif 20 < result < 25:
                    #     amount = 5
                    # else:
                    #     amount = 6
                    
                    material = miningFloors(65) 
                    
                    miningarr.append(f"**#{counterTwo}**.You Gained **1 Cargo** of **{material}**")
                    #await ctx.send(f"You rolled a {result} for notice {counterTwo}.You found {amount} {material}\n")
                #for i in miningarr:
                    
                #print (miningarr)
                endmessage = ''
                for x in miningarr:
                    endmessage += '\n' + x
                await ctx.send(endmessage)
                await ctx.send("Done")

                if counterTwo >= int(message.content):
                    @bot.event
                    async def on_message(message):
                        await bot.process_commands(message)

# @bot.command(name='mining')
# async def mining(ctx, Floor = "Zero"):
#     await ctx.send(f"What floor are you on?")
#     @bot.event
#     async def on_message(message):

#         if message.content == 0:
#             @bot.event
#             async def on_message(message):
#                 await bot.process_commands(message)

#         randomstring1 = message.content
#         randomstring2 =  isinstance(randomstring1, str)
#         if str(randomstring2) == True:
#             @bot.event
#             async def on_message(message):
#                 await bot.process_commands(message)

#         await bot.process_commands(message)
#         message.content = (message.content.lower())
#         flag = True
#         if message.author == bot.user:
#             return
#         try:
#             int(message.content)
#         except ValueError:

#             flag = False
#         if flag:
#             floor = int(message.content)
#             await ctx.send(f"You are on Floor {floor}. \nHow many times are you rolling notice?")
#             @bot.event
#             async def on_message(message):
#                 await bot.process_commands(message)
#                 randomstring1 = message.content
#                 randomstring2 =  isinstance(randomstring1, str)


#                 if str(randomstring2) == True:
#                     @bot.event
#                     async def on_message(message):
#                         await bot.process_commands(message)
                
#                 message.content = (message.content.lower())
#                 flagTwo = True
#                 if message.author == bot.user:
#                     return
                
#                 try:

#                     int(message.content)

#                 except ValueError:

#                     flagTwo = False

#                 if message.author == ctx:
#                     searchnum = int(message.content)
#                     return searchnum
                
#                 if flagTwo:
#                     await ctx.send(f"you are searching {int(message.content)} Times.")
#                     stats(ctx.author)
#                     counterTwo = 0
#                     characterName = activeprofile(ctx)
#                     f = open(f"{ctx.author}{characterName}Skills.txt", "r")
#                     lines = f.readlines()
#                     f.close()
#                     miningarr = []
#                     while counterTwo < int(message.content):
                                               
#                         counterTwo += 1
#                         result = miningDice()
#                         #exploding could check result and de iterate the counterTwo
#                         stat = stats(ctx.author)
#                         result += int(stat[3])
#                         skill = lines[7]
#                         result += int(skill[0]) + 1
#                         if int(skill[0]) == 0:
#                             result += -1
#                         if result < 16:
#                             amount = 2
#                         elif 15 < result < 21:
#                             amount = 4
#                         elif 20 < result < 25:
#                             amount = 5
#                         else:
#                             amount = 6
                        
#                         material = miningFloors(int(message.content)) 
                        
#                         miningarr.append(f"**#{counterTwo}**You rolled a **{result}**.You found **{amount}** **{material}**")
#                         #await ctx.send(f"You rolled a {result} for notice {counterTwo}.You found {amount} {material}\n")
#                     #for i in miningarr:
                        
#                     #print (miningarr)
#                     endmessage = ''
#                     for x in miningarr:
#                         endmessage += '\n' + x
#                     await ctx.send(endmessage)
#                     await ctx.send("Done")

#                     if counterTwo >= int(message.content):
#                         @bot.event
#                         async def on_message(message):
#                             await bot.process_commands(message)

@bot.command(name = 'testinfo')
async def createcharacter(ctx):
        testinfouser = ctx.author # this will need to be used for all commands so that only the initiator can affect the commands
        await ctx.send(f"send message\n")
        @bot.event
        async def on_message(message):
            if message.author == testinfouser: #this line to check for the author, along with the else lines will be needed alot
                channelID = f"{message.channel.id}: channel ID"
                channel = f"{message.channel}: channel"
                authorID = f"{message.author.id}: author ID"
                author = f"{message.author}: author"
                ctxuser = f"{ctx}: ctx"
                ctxUserName = f"{ctx.author}: ctx user"
                ctxUserNameID = f"{ctx.author.id}: ctx user ID"
                await ctx.send(f"INFO: \n{channelID}\n{channel}\n{authorID}\n{author}\n{ctxuser}\n{ctxUserName}\n{ctxUserNameID}")
                @bot.event
                async def on_message(message):
                    await bot.process_commands(message)
            else:
                async def on_message(message): #these lines are very important to be used for each command
                    await bot.process_commands(message)
                    return
                

@bot.command(name = 'createcharacter')
async def createcharacter(ctx):
    createcharacterUser = ctx.author
    #sheetOwner = f"{ctx.author}"
    user = f"{ctx.author}"
    await ctx.send(f"Give your Character a name")
######################################## 
    @bot.event 
    async def on_message(message):
        if message.channel.id == CCchannel:
            #ctx.send(f"{message.author}\n{ctx.author}")       
######## Protection against command locks allowing other user to use commands
            if message.author == bot.user:
                return
            if str(message.author) != str(user):#insert User string here
                await bot.process_commands(message)
                return
#############################################################################        
            await ctx.send(f"Your character's name is {message.content}")

            charlistreset(ctx.author)
            profile(ctx.author, message.content)
            characterName = message.content
            f = open(f"{ctx.author}{characterName}Sheet.txt", "a")
            f.write(f"Name: {characterName}\n")
            f.close
            
            await ctx.send(f"Age: ")

                    
######################################## 
            @bot.event
            async def on_message(message):
    
                if message.channel.id == CCchannel:


######## Protection against command locks allowing other user to use commands
                    if message.author == bot.user:
                        return
                    if str(message.author) != str(user):#insert User string here
                        await bot.process_commands(message)
                        return
#############################################################################


                    f = open(f"{ctx.author}{characterName}Sheet.txt", "a")
                    f.write(f"Age: {message.content}\n")
                    f.close
                    currentprofile = activeprofile(ctx.author)
                    sheetuser = f"{createcharacterUser}{currentprofile}Sheet"
                    if message.channel.id == CCchannel:
                        await ctx.send(f"Please Choose a Race:\n[Human]\n[Beastkin]\n[Anima Enhanced]\n[Synthetic]\n[Voidkin]\n[Elf]\n[Orc]\n[Dwarf]\n[Demon/Succubus]")
########################################                         
                        @bot.event
                        async def on_message(message):
                            if message.channel.id == CCchannel: 


######## Protection against command locks allowing other user to use commands
                                if message.author == bot.user:
                                    return
                                if str(message.author) != str(user):
                                    await bot.process_commands(message)
                                    return
#############################################################################
                                
                                answer = ""
                                global choice

                                if str(message.content) == "N":
                                    await ctx.send(f"Please Choose a Race:\n[Human]\n[Beastkin]\n[Anima Enhanced]\n[Synthetic]\n[Voidkin]\n[Elf]\n[Orc]\n[Dwarf]\n[Demon/Succubus]\n")
                                elif str(message.content) != "Y":                                        
                                    choice = race(str(message.content))
                                    if message.content == "Succubus Natural Born":
                                        await ctx.send(f"[Choose One] Tail/Horns/Wings prefixed by 'Succubus Natural Born (Choice)'")
                                    elif message.content == "Demon Natural Born":
                                        await ctx.send(f"[Choose One] Tail/Horns/Wings prefixed by 'Demon Natural Born (Choice)'")
                                    elif message.content == "Beastkin":
                                        tempOne = "Beastkin1"
                                        tempTwo = "Beastkin2"
                                        await ctx.send(f"{Lore(tempOne)}")
                                        await ctx.send(f"{Lore(tempTwo)}")

                                    else:
                                        if Lore(str(message.content)) == "DNS":
                                            await ctx.send(f"\n\nAre you sure this is the race you want? Y/N")
                                        elif message.content == "Synthetic":
                                            await ctx.send(f"{Lore(message.content)}")
                                        elif message.content == "Voidkin":
                                            await ctx.send(f"{Lore(message.content)}")
                                        elif message.content == "Elf":
                                            await ctx.send(f"{Lore(message.content)}")
                                        elif message.content == "Orc":
                                            await ctx.send(f"{Lore(message.content)}")
                                        elif message.content == "Dwarf":
                                            await ctx.send(f"{Lore(message.content)}")
                                        elif message.content == "Demon":
                                            await ctx.send(f"{Lore(message.content)}")
                                        elif message.content == "Succubus":
                                            await ctx.send(f"{Lore(message.content)}")

                                        else:
                                            await ctx.send(f"{Lore(message.content)}")
                                            await ctx.send(f"\n\nAre you sure this is the race you want? Y/N")
                                elif str(message.content) == "Y":
                                    f = open(f"{ctx.author}{characterName}Sheet.txt", "a")
                                    f.write(f"Race: {choice}\n")
                                    f.close
                                    
                                    await ctx.send(f"You have chosen {choice}\n")
                                    await ctx.send(f"Select your Heritage\n[Dux]\n[Potens]\n[Custos]\n[Elysium]\n[Libertas]\n[Vettrheim]\n[Anima Lands]\n[Dark Lands]\n[Wild]\n[The Dark Continent]\n[Military Heritage]\n[Sealed]")
################################################################################                                     
                                    @bot.event
                                    async def on_message(message):
                                        if message.channel.id == CCchannel:

######## Protection against command locks allowing other user to use commands
                                            if message.author == bot.user:
                                                return
                                            if str(message.author) != str(user):
                                                await bot.process_commands(message)
                                                return
#############################################################################


                                            global Hanswer
                                            # if message.author == bot.user:
                                            #     return
                                            if message.author != createcharacterUser:
                                                return
                                            if message.author != createcharacterUser:
                                                return

                                            if str(message.content) == "N":
                                                await ctx.send(f"Select your Heritage\n[Dux]\n[Potens]\n[Custos]\n[Elysium]\n[Libertas]\n[Vettrheim]\n[Anima Lands]\n[Dark Lands]\n[Wild]\n[The Dark Continent]\n[Military Heritage]\n[Sealed]")
                                                return
                                            elif str(message.content) != "Y":   
                                                Heritage = heritage(message.content)
                                                HeritageLore = Lore(message.content)
                                                Hanswer = str(message.content)
                                                await ctx.send(f"{HeritageLore}\n{Heritage}")

                                            elif str(message.content) == "Y":
                                                f = open(f"{ctx.author}{characterName}Sheet.txt", "a")
                                                f.write(f"Heritage: {Hanswer}\n")
                                                f.close
                                                await ctx.send(f"You have chosen {Hanswer} as your heritage.")
                                                await ctx.send("Please Choose your first background feat. [this feature is not implimented yet to just type 'Test' please]")
                                                
################################################################################                                                 
                                                @bot.event
                                                async def on_message(message):
                                                    if message.channel.id == CCchannel:

######## Protection against command locks allowing other user to use commands
                                                        if message.author == bot.user:
                                                            return
                                                        if str(message.author) != str(user):
                                                            await bot.process_commands(message)
                                                            return
#############################################################################

                                                        global BGanswer
                    #Put background info in, make a definition with all the info to compare to

                                                        if str(message.content) == "Test":
                                                            BGanswer = "[Background Place Holder]"
                                                            print(BGanswer)
                                                        
                                                        
                                                            await ctx.send(BGanswer)
                                                        f = open(f"{ctx.author}{characterName}Sheet.txt", "a")
                                                        f.write(f"Background Feat 1: {BGanswer}\nBackground Feat 2:\nBackground Feat 3:\n\n000 XP Used\n035 XP Total\n00 CCPoints Used\n20 CCPoints Max\n\n")
                                                        f.write("HP: 1\nAP: 0\nSP: 0\nPDR: 0\nMDR: 0\nSpeed: 1\n0 spirit\n0 tenacity\n0 dexterity\n0 awareness\n0 strength\n0 intelligence\n0\n")
                                                        f.write("0 Acrobatics\n0 Athletics\n0 Empathy\n0 Forgery\n0 Fortitude\n0 Hide\n0 Medical\n0 Notice\n0 Performance\n0 RecallInformation\n0 Silvertongue\n0 Subtlety\n0 Wilderness\n0 Willpower\n0 Relationship\n0 Nemesis\n0 Organization\n0 AnimatedCompanion\n0 AnimalHandler\n0 BeastHandler\n0 WeaponProficiency\n0 Brawling\n0 ArmorProficiency\n0 Runestone\n0 Vehicles\n0 CombatVehicles\n0 Crafting\n0 Hacking\n0 Profession\n")
                                                        f.close

                                                        print(choice)
                                                        print(Hanswer)
                                                        print(BGanswer)
                                                        
                                                        # raceStats(sheetuser, str(choice))
                                                        
                                                        f = open(f"{ctx.author}{characterName}sheet.txt", "r")
                                                        SLines = f.readlines()
                                                        f.close
                                                        Race = SLines[2].replace("Race: ", "")
                                                        Race = Race.replace("\n", "")
                                                        Heritage = SLines[3].replace("Heritage: ", "")
                                                        Heritage = Heritage.replace("\n", "")
                                                        statUpdater = f"{ctx.author}{characterName}sheet"
                                                        print(Race)

                                                        raceStats(statUpdater, str(Race))
                                                        heritageStats(statUpdater, str(Heritage))

                                                        raceArray = choiceRace()
                                                        heritageArray = choiceHeritage()

######## Protection against command locks allowing other user to use commands
                                                        if message.author == bot.user:
                                                            return
                                                        if str(message.author) != str(user):
                                                            await bot.process_commands(message)
                                                            return
#############################################################################

                                                        for x in raceArray:
                                                            if str(x) == str(Race):
                                                                for y in heritageArray:
                                                                    if str(y) == str(Heritage):
                                                                        await ctx.send("You have 2 choices to make. do in any order")
                                                                await ctx.send("Make your race choice either 'Race 1' or 'Race 2'")
                                                            
                                                        for x in heritageArray:
                                                            if str(x) == str(Heritage):
                                                                await ctx.send("Make your Heritage choice either 'Heritage 1' or 'Heritage 2'")
                                                            
                                                        await ctx.send("Are you ready to start stat allocation? Make sure that if you had a Race or Heritage choice to make that you make it first before you continue. When you are ready enter 'Y'")

                                                        

                                                        @bot.event
                                                        async def on_message(message):
                                                            if message.channel.id == CCchannel:

######## Protection against command locks allowing other user to use commands
                                                                if message.author == bot.user:
                                                                    return
                                                                if str(message.author) != str(user):
                                                                    await bot.process_commands(message)
                                                                    return
#############################################################################
                                                                if str(message.content) == "Race 1":
                                                                    Rchoices(statUpdater, 1, Race)
                                                                    await ctx.send("Thank you for your choice")
                                                                if str(message.content) == "Race 2":
                                                                    Rchoices(statUpdater, 2, Race)
                                                                    await ctx.send("Thank you for your choice")
                                                                if str(message.content) == "Heritage 1":
                                                                    Hchoices(statUpdater, 1, Heritage)
                                                                    await ctx.send("Thank you for your choice")
                                                                if str(message.content) == "Heritage 2":
                                                                    Hchoices(statUpdater, 2, Heritage)
                                                                    await ctx.send("Thank you for your choice")   
                                                                if str(message.content) == "Y":

                                                                    Spi = "Spirit"
                                                                    Ten = "Tenacity"
                                                                    Dex = "Dexterity"
                                                                    Awa = "Awareness"
                                                                    Str = "Strength"
                                                                    Itg = "Intelligence"
                                                                    statmsgone = (f"Welcome to Stat Allocation. unlike certain post apocolyptic games you aren't SPECIAL. Here we follow STDASI (Stacy) Which Stands for Spirit, Tenacity, Dexterity, Awareness, Strength, and Intelligence. \n{Lore(Spi)}\n\n{Lore(Ten)}\n\n{Lore(Dex)}\n\n{Lore(Awa)}\n\n{Lore(Str)}\n\n{Lore(Itg)}\n\nTo increase stat write the message as [STAT] [Amount]")
                                                                    statsret = statRetrieve(sheetuser)
                                                                    currentStat = (f"(====================)\n(Points Remaining: {statsret[3]}     )\n( Increase by 2 per point)\n(HP: {statsret[4]}                                   )\n(AP: {statsret[5]}                                  )\n( Increase by 1 per point )\n(Spirit: {statsret[10]}                              )\n(Tenacity: {statsret[11]}                         )\n(Dexterity: {statsret[12]}                      )\n(Awareness: {statsret[13]}                   )\n(Strength: {statsret[14]}                       )\n(Intelligence: {statsret[15]}                  )\n(====================)")
                                                                    await ctx.send(f"{statmsgone}\n\n{currentStat}")
                                                                    @bot.event
                                                                    async def on_message(message):
                                                                        if message.channel.id == CCchannel:

######## Protection against command locks allowing other user to use commands
                                                                            if message.author == bot.user:
                                                                                return
                                                                            if str(message.author) != str(user):
                                                                                await bot.process_commands(message)
                                                                                return
#############################################################################



                                                                            z = message.content
                                                                            allocate = z.split(" ")
                                                                            if str(message.content) == "Y":
                                                                                allocate.append(0)
                                                                            print(allocate)


                                                                            statsret = statRetrieve(sheetuser)
                                                                            remainingpoints = int(statsret[3])-int(statsret[2])
                                                                            print(f"{remainingpoints}: remaining points")
                                                                            
                                                                            if int(allocate[1]) > int(remainingpoints):
                                                                                await ctx.send("You are attempting to use too many points")
                                                                                return


                                                                            counter = 0
                                                                            allocationArray = ["HP", "AP", "Spirit", "Tenacity", "Dexterity", "Awareness", "Strength", "Intelligence"]
                                                                            for x in allocationArray:
                                                                                counter += 1
                                                                                if allocate[0] == str(x):
                                                                                    statUpdate(sheetuser, "CCPoint USED", int(allocate[1]))
                                                                                    counter -= 1
                                                                                elif str(allocate[0]) == "Y":
                                                                                    counter -= 1
                                                                                elif int(counter) == 8:
                                                                                    await ctx.send("That is either not a stat or you mispelled something please try again.\n~Backule")
                                                                            
                                                                            
                                                                            if allocate[0] == "HP" or allocate[0] == "AP":
                                                                                allocate[1] = int(allocate[1]) * 2  

                                                                            statUpdate(sheetuser, allocate[0], int(allocate[1]))
                                                                            statsret = statRetrieve(sheetuser)
                                                                            remainingpoints = int(statsret[3])-int(statsret[2])
                                                                            print(remainingpoints)
                                                                            
                                                                            currentStat = (f"(====================)\n(Points Remaining: {remainingpoints}     )\n( Increase by 2 per point)\n(HP: {statsret[4]}                                   )\n(AP: {statsret[5]}                                  )\n( Increase by 1 per point )\n(Spirit: {statsret[10]}                              )\n(Tenacity: {statsret[11]}                         )\n(Dexterity: {statsret[12]}                      )\n(Awareness: {statsret[13]}                   )\n(Strength: {statsret[14]}                       )\n(Intelligence: {statsret[15]}                  )\n(====================)")
                                                                            if remainingpoints > 0:
                                                                                await ctx.send(f"{currentStat}")
                                                                            elif str(message.content) != "Y":
                                                                                await ctx.send(f"Are you done with your **Point Buy**? Y/N")
                                                                            if str(message.content) == "N":
                                                                                await ctx.send(f"{currentStat}")
                                                                            elif str(message.content) == "Y":

    ######## Protection against command locks allowing other user to use commands
                                                                                if message.author == bot.user:
                                                                                    return
                                                                                if str(message.author) != str(user):
                                                                                    await bot.process_commands(message)
                                                                                    return
    #############################################################################
                                                                                f = open(f"{sheetuser}.txt", "r")

                                                                                await ctx.send(f"{f.read()}\nCongratulations on completing your character creation! Now all that is left to do is use those XP Points, create your weapons and gear, and go fuck some **shit UP!**\n\nAbove is your current lineup make sure to review and confirm everything is in order. Should you have any questions about the server or specific words you can use the Lore function by entering **!Lore [Word you want to check]**. \n\nAny and all question or complaints about the Bot should be sent to **@Backule** ")
                                                                                @bot.event
                                                                                async def on_message(message):
                                                                                    await bot.process_commands(message)




@bot.command(name = 'chooseprofile')
async def chooseprofile(ctx):

    profilelist = seeprofiles(ctx.author)
    await ctx.send(f"This is a list of profiles\n\n{profilelist}\nPlease select one")
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        f = open(f"{ctx.author}profiles.txt" , 'w')
        f.close
        for x in profilelist:
            
            #f = open(f"{ctx.author}profiles.txt" , "r")
            #linesread = f.readlines()
            #lines = linesread[int(x)]
            #f.close
            if message.content == str(x):
                

                await ctx.send(f"You have chosen {message.content}")
                f = open(f"{ctx.author}profiles.txt" , 'a')
                f.write(f"1 = {x}\n")
                f.close



                @bot.event
                async def on_message(message):
                    await bot.process_commands(message)
            
            else:

                f = open(f"{ctx.author}profiles.txt" , 'a')
                f.write(f"0 = {x}\n")
                f.close
                
                @bot.event
                async def on_message(message):
                    await bot.process_commands(message)
    
        @bot.event
        async def on_message(message):
            await bot.process_commands(message)
                
        
  #      choice = profile(ctx, message.content)
  #      print (choice)

@bot.command(name = 'checkactive')
async def checkactive(ctx):
    profilename = activeprofile(ctx.author)
    await ctx.send(f"{profilename}")
 ###############################

@bot.command(name = "mulTest")
async def mulTest(ctx):
    mulTestuser = ctx.author
    @bot.event
    async def on_message(message):
        # print(message.author)
        # print(mulTestuser)

######## Protection against command locks allowing other user to use commands
        if message.author == bot.user:
            return
        if message.author != mulTestuser:#insert User string here
            await bot.process_commands(message)
            return
 #############################################################################            

# LOOOOOOOOOORRRRRRREEEEEE ####
@bot.command(name = "Lore")
async def chooseprofile(ctx, HLore = "empty"):
    await ctx.send(f"{Lore(HLore)}")
###############################

@bot.command(name = "Stats")
async def Stats(ctx):
    statuser = ctx.author
    profile = activeprofile(ctx.author)
    user = f"{ctx.author}{profile}Sheet"

    @bot.event
    async def on_message(message):
        if message.author != statuser:
            await bot.process_commands(message)
            return
        stats = statUpdate(user, "", 0)
        counter = 0
        statment = ""
        for x in stats:
            counter += 1
            if (counter >= 1 and counter <= 5) or (counter >= 7 and counter <= 34):
                print (counter)
                print(x)

                statment = str(statment) + str(x)

            
        await ctx.send(f"{statment}")

            # if (counter >= 7 and counter <= 34):
            #     print (counter)
            #     print(x)
            #     await ctx.send(f"{x}")

@bot.command(name = "UpdateStat")
async def UpdateStat(ctx):
    UpdateStatUser = ctx.author
    await ctx.send(f"What do you want to increase?")

    # increaseStat = 0
    # statname = ""    
    
    @bot.event
    async def on_message(message):

        global increaseStat
        global statname

        statuser = ctx.author
        profile = activeprofile(ctx.author)
        user = f"{ctx.author}{profile}Sheet"

    ######## Protection against command locks allowing other user to use commands
        if message.author == bot.user:
            return
        if message.author != UpdateStatUser:
            await bot.process_commands(message)
            return
    #############################################################################            
        
        print(message.content)

        checker = message.content
        print (f"{checker.isdigit()}")
        
        if checker.isdigit() == True:
            increaseStat = int(message.content)
            await ctx.send("Are you done updating? Y/N")


        elif str(message.content) == "N":
            #print (f"{statname}\n{increaseStat}")
            statUpdate(user, statname, increaseStat)
            increaseStat = 0
            statname = ""
            await ctx.send(f"What do you want to increase?")


        elif str(message.content) != "Y":
            statname = str(message.content)
            await ctx.send(f"How much do you want to increase this?")


        else:
            print (f"{statname}\n{increaseStat}")
            sheet = statUpdate(user, statname, increaseStat)
            sheetmessage = ""
            for x in sheet:
                sheetmessage = sheetmessage + str(x)
            await ctx.send(sheetmessage)
            @bot.event
            async def on_message(message):
                await bot.process_commands(message)





def charlistreset(ctxplayer):

    f = open(f"{ctxplayer}profiles.txt" , "r")
    active = f.readlines()
    f.close
    resetarray = []
    for x in active:
        #print(x)
        x = x.replace("1 = ", "0 = ")
        resetarray.append(x)
    print(resetarray)
    
    
    f = open(f"{ctxplayer}profiles.txt", "w")
    f.writelines(resetarray)
    f.close      

def choiceRace():
    CRArray = ["Beastkin Tail", "Beastkin Eyes", "Beastkin Horns", "Voidkin Tail", "Voidkin Eyes", "Voidkin Horns", "Demon Natural Born Horns", "Demon Natural Born Tail", "Succubus Natural Born Horns", "Succubus Natural Born Tail"]
    return CRArray
    
def choiceHeritage():
    CHArray = ["Dux", "Potens", "Custos", "Elysium", "Vettrheim", "Anima Lands", "Dark Lands", "Wild", "Military Heritage", "Sealed"]
    return CHArray

def raceStats(player, race):

    if str(race) == "Human":
        statUpdate(player, "Spirit", 1)
        statUpdate(player, "Tenacity", 1)
        statUpdate(player, "CCPoint MAX", 2)
        statUpdate(player, "XP TOTAL", 5)

    elif str(race) == "Anima Enhanced":
        statUpdate(player, "Spirit", 3)
        statUpdate(player, "AP", 10)
        statUpdate(player, "Willpower", 1)

    elif str(race) == "Synthetic Genius":
        statUpdate(player, "Intelligence", 2)
    elif str(race) == "Synthetic Versatile":
        statUpdate(player, "CCPoint MAX", 2) 


#check the elves for their racial trait things. 
#activated magical armor will be interesting but will need to be done at a later time

    elif str(race) == "Elf Royal":
        statUpdate(player, "Spirit", 1)
        statUpdate(player, "Dexterity", 1)
        statUpdate(player, "Runestone", 1)
    elif str(race) == "Elf High Born":
        statUpdate(player, "Spirit", 1)
        statUpdate(player, "Dexterity", 1)
        statUpdate(player, "WeaponProficiency", 1)
    elif str(race) == "Elf Low Born":
        statUpdate(player, "Spirit", 1)
        statUpdate(player, "Dexterity", 1)
        statUpdate(player, "Wilderness", 1)

#note gonna just add a full on Def for all activated abilities so that they are 

    elif str(race) == "Orc Magic Born":
        statUpdate(player, "Tenacity", 1)
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Runestone", 1)        
    elif str(race) == "Orc Battle Born":
        statUpdate(player, "Tenacity", 1)
        statUpdate(player, "Strength", 1)
        statUpdate(player, "WeaponProficiency", 1)

    elif str(race) == "Dwarf Warrior":
        statUpdate(player, "Strength", 2)
        statUpdate(player, "WeaponProficiency", 1)
    elif str(race) == "Dwarf Smith":
        statUpdate(player, "Strength", 2)
        statUpdate(player, "Crafting", 1)

    

    #Demon/Succubus Natural born get the choice of Tail, Horn, or Wing traits from Beastkin
    elif str(race) == "Demon Summoned":
        statUpdate(player, "Runestone", 1)
    elif str(race) == "Demon Natural Born Tail":
        statUpdate(player, "Notice", 1)
    elif str(race) == "Demon Natural Born Horns":
        statUpdate(player, "Notice", 1)
    elif str(race) == "Demon Natural Born Wings":
        statUpdate(player, "Notice", 1)
        statUpdate(player, "Dexterity", 2)

    elif str(race) == "Succubus Summoned":
        statUpdate(player, "Runestone", 1)
    elif str(race) == "Succubus Natural Born Tail":
        statUpdate(player, "Notice", 1)
    elif str(race) == "Succubus Natural Born Horns":
        statUpdate(player, "Notice", 1)
    elif str(race) == "Succubus Natural Born Wings":
        statUpdate(player, "Notice", 1)
        statUpdate(player, "Dexterity", 2)
    
    
    
    elif str(race) == "Beastkin Tail":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Intelligence", 1)
        #figure out the beastkin tail abilities
    elif str(race) == "Beastkin Ears":#fix to allow choice
        statUpdate(player, "Dexterity", 2)
        statUpdate(player, "Notice", 2)
    elif str(race) == "Beastkin Eyes": #fix to allow choice
        statUpdate(player, "Awareness", 2) 
        
    elif str(race) == "Beastkin Camouflage":
        statUpdate(player, "Dexterity", 1)
        statUpdate(player, "Tenacity", 1)
    elif str(race) == "Beastkin Claws":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Strength", 1)
    elif str(race) == "Beastkin Wings":
        statUpdate(player, "Dexterity", 2)

        #these 3 get Armor based on rank
    elif str(race) == "Beastkin Exoskeleton":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)
    elif str(race) == "Beastkin Thick Hide":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)
    elif str(race) == "Beastkin Scales":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)

    #Half Cold Damage, can't be winded due to swimming
    elif str(race) == "Beastkin Gills":
        statUpdate(player, "Tenacity", 2)

    # natural light blunt 1d6+str DMG can cause winded status with hoves for 1 round
    elif str(race) == "Beastkin Hooves":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)
        statUpdate(player, "Brawling", 1)
    
    #choice with horns and get the +2 to shove/Trip/Grab Actions
    elif str(race) == "Beastkin Horns":
        statUpdate(player, "Strength", 2)
        
    elif str(race) == "Beastkin Predator":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Tenacity", 1)
        statUpdate(player, "Speed", 1)
    #allow for choice with fangs and stinger
    elif str(race) == "Beastkin Fangs":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)
    elif str(race) == "Beastkin Stinger":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)

    #Flame Breath
    elif str(race) == "Beastkin Dragon Breath":
        statUpdate(player, "Dexterity", 1)
        statUpdate(player, "Tenacity", 1)

    #can shoot and grapple up to 2 targets at a time. can be used to climb using athletics+Strength, can create
    #a sticky zone equal to ten per week. Zone has 5+Tenacity HP and takes entire turn to pass through, must used fire/cutting to destroy
    elif str(race) == "Beastkin Spider Webs":
        statUpdate(player, "Dexterity", 1)
        statUpdate(player, "Tenacity", 1)

    #
    elif str(race) == "Beastkin Drop Tail":
        statUpdate(player, "Tenacity", 1)
        statUpdate(player, "Dexterity", 1)

    elif str(race) == "Beastkin Bioluminescence":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Dexterity", 1)
    #set choice for sonar Blast and Sense
    elif str(race) == "Beastkin Sonar Sense":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Tenacity", 1)
    elif str(race) == "Beastkin Sonar Blast":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Tenacity", 1)

    
    
    
    elif str(race) == "Voidkin Tail":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Intelligence", 1)
        #figure out the beastkin tail abilities
    elif str(race) == "Voidkin Ears":#fix to allow choice
        statUpdate(player, "Dexterity", 2)
        statUpdate(player, "Notice", 2)
    elif str(race) == "Voidkin Eyes": #fix to allow choice
        statUpdate(player, "Awareness", 2) 
        
    elif str(race) == "Voidkin Camouflage":
        statUpdate(player, "Dexterity", 1)
        statUpdate(player, "Tenacity", 1)
    elif str(race) == "Voidkin Claws":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Strength", 1)
    elif str(race) == "Voidkin Wings":
        statUpdate(player, "Dexterity", 2)

        #these 3 get Armor based on rank
    elif str(race) == "Voidkin Exoskeleton":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)
    elif str(race) == "Voidkin Thick Hide":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)
    elif str(race) == "Voidkin Scales":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)

    #Half Cold Damage, can't be winded due to swimming
    elif str(race) == "Voidkin Gills":
        statUpdate(player, "Tenacity", 2)

    # natural light blunt 1d6+str DMG can cause winded status with hoves for 1 round
    elif str(race) == "Voidkin Hooves":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)
        statUpdate(player, "Brawling", 1)
    
    #choice with horns and get the +2 to shove/Trip/Grab Actions
    elif str(race) == "Voidkin Horns":
        statUpdate(player, "Strength", 2)
        
    elif str(race) == "Voidkin Predator":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Tenacity", 1)
        statUpdate(player, "Speed", 1)
    #allow for choice with fangs and stinger
    elif str(race) == "Voidkin Fangs":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)
    elif str(race) == "Voidkin Stinger":
        statUpdate(player, "Strength", 1)
        statUpdate(player, "Tenacity", 1)

    #Flame Breath
    elif str(race) == "Voidkin Dragon Breath":
        statUpdate(player, "Dexterity", 1)
        statUpdate(player, "Tenacity", 1)

    #can shoot and grapple up to 2 targets at a time. can be used to climb using athletics+Strength, can create
    #a sticky zone equal to ten per week. Zone has 5+Tenacity HP and takes entire turn to pass through, must used fire/cutting to destroy
    elif str(race) == "Voidkin Spider Webs":
        statUpdate(player, "Dexterity", 1)
        statUpdate(player, "Tenacity", 1)

    #
    elif str(race) == "Voidkin Drop Tail":
        statUpdate(player, "Tenacity", 1)
        statUpdate(player, "Dexterity", 1)

    elif str(race) == "Voidkin Bioluminescence":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Dexterity", 1)
    #set choice for sonar Blast and Sense
    elif str(race) == "Voidkin Sonar Sense":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Tenacity", 1)
    elif str(race) == "Voidkin Sonar Blast":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Tenacity", 1)

    elif str(race) == "Voidkin Despair":
        statUpdate(player, "Spirit", 1)
    elif str(race) == "Voidkin Possession":
        statUpdate(player, "Spirit", 1)
    elif str(race) == "Voidkin Power":
        statUpdate(player, "Strength", 1)

def Rchoices(player, CCchoice, race):
    
    if int(CCchoice) == 1:
        if str(race) == "Beastkin Tail": 
            statUpdate(player, "Spirit", 0)
        if str(race) == "Beastkin Eyes": 
            statUpdate(player, "Athletics", 1)
        if str(race) == "Beastkin Horns":
            statUpdate(player, "Performance", 2)
        if str(race) == "Voidkin Tail":
            statUpdate(player, "Spirit", 0)
        if str(race) == "Voidkin Eyes":
            statUpdate(player, "Athletics", 1)
        if str(race) == "Voidkin Horns":
            statUpdate(player, "Performance", 2)
        if str(race) == "Demon Natural Born Tail": 
            statUpdate(player, "Spirit", 0)
        if str(race) == "Demon Natural Born Horns": 
            statUpdate(player, "Performance", 2)
        if str(race) == "Succubus Natural Born Tail": 
            statUpdate(player, "Spirit", 0)
        if str(race) == "Succubus Natural Born Horns":
            statUpdate(player, "Performance", 2)

    elif int(CCchoice) == 2:
        if str(race) == "Beastkin Tail": 
            statUpdate(player, "Spirit", 0)
        if str(race) == "Beastkin Eyes": 
            statUpdate(player, "Notice", 2)
        if str(race) == "Beastkin Horns":
            statUpdate(player, "Athletics", 1)
        if str(race) == "Voidkin Tail":
            statUpdate(player, "Spirit", 0)
        if str(race) == "Voidkin Eyes":
            statUpdate(player, "Notice", 2)
        if str(race) == "Voidkin Horns":
            statUpdate(player, "Athletics", 1)
        if str(race) == "Demon Natural Born Tail": 
            statUpdate(player, "Spirit", 0)
        if str(race) == "Demon Natural Born Horns": 
            statUpdate(player, "Athletics", 1)
        if str(race) == "Succubus Natural Born Tail": 
            statUpdate(player, "Spirit", 0)
        if str(race) == "Succubus Natural Born Horns":
            statUpdate(player, "Athletics", 1)

    else:
        error1 = "You did not make a choice, please notify the @Server_helper/DM role for help"
        return error1

def heritageStats(player, heritage):               #make voidkin despair possession and power

    if str(heritage) == "Dux":               #Needs choice 
        statUpdate(player, "Spirit", 1)
    if str(heritage) == "Potens":               #Needs choice 
        statUpdate(player, "Tenacity", 1)
    if str(heritage) == "Custos":               #Needs choice 
        statUpdate(player, "Strength", 1)
    if str(heritage) == "Elysium":               #Needs choice 
        statUpdate(player, "Intelligence", 1)
    if str(heritage) == "Libertas":
        statUpdate(player, "Awareness", 1)
        statUpdate(player, "Wilderness", 2)
    if str(heritage) == "Vettrheim":               #Needs choice 
        statUpdate(player, "Tenacity", 1)
    if str(heritage) == "Anima Lands":               #Needs choice 
        statUpdate(player, "Dexterity", 1)
    if str(heritage) == "Dark Lands":               #Needs choice 
        statUpdate(player, "Tenacity", 1)
    if str(heritage) == "Wild":               #Needs choice 
        statUpdate(player, "Dexterity", 1)
    if str(heritage) == "The Dark Continent":
        statUpdate(player, "Silvertongue", 1)
        statUpdate(player, "HP", 4)
    if str(heritage) == "Military Heritage":               #Needs choice 
        statUpdate(player, "Tenacity", 1)
    if str(heritage) == "Sealed":               #Needs choice 
        statUpdate(player, "CCPoint MAX", 1)

def Hchoices(player, CCchoice, heritage):
    if int(CCchoice) == 1:
        if str(heritage) == "Dux": 
            statUpdate(player, "Willpower", 1)
        if str(heritage) == "Potens": 
            statUpdate(player, "Brawling", 1)
        if str(heritage) == "Custos":
            statUpdate(player, "Notice", 2)
        if str(heritage) == "Elysium":
            statUpdate(player, "Runestone", 1)
        if str(heritage) == "Libertas":
            statUpdate(player, "Spirit", 0)
        if str(heritage) == "Vettrheim":
            statUpdate(player, "WeaponProficiency", 1)
        if str(heritage) == "Anima Lands": #Gains Essence domain/augmentation 1
            statUpdate(player, "Spirit", 0)
        if str(heritage) == "Dark Lands": 
            statUpdate(player, "Fortitude", 1)
        if str(heritage) == "Wild": 
            statUpdate(player, "Fortitude", 1)
        if str(heritage) == "The Dark Continent":
            statUpdate(player, "Spirit", 0)
        if str(heritage) == "Military Heritage": 
            statUpdate(player, "CombatVehicles", 1)
        if str(heritage) == "Sealed": 
            statUpdate(player, "Wilderness", 1)
    elif int(CCchoice) == 2:
        if str(heritage) == "Dux": 
            statUpdate(player, "Performance", 2)
        if str(heritage) == "Potens": 
            statUpdate(player, "WeaponProficiency", 1)
        if str(heritage) == "Custos":
            statUpdate(player, "Silvertongue", 1)
        if str(heritage) == "Elysium":
            statUpdate(player, "Profession", 1)
        if str(heritage) == "Libertas":
            statUpdate(player, "Spirt", 0)
        if str(heritage) == "Vettrheim":
            statUpdate(player, "Runestone", 1)
        if str(heritage) == "Anima Lands":
            statUpdate(player, "AnimatedCompanion", 1)
        if str(heritage) == "Dark Lands": 
            statUpdate(player, "Willpower", 1)
        if str(heritage) == "Wild": 
            statUpdate(player, "Hide", 2)
        if str(heritage) == "The Dark Continent":
            statUpdate(player, "Spirit", 0)
        if str(heritage) == "Military Heritage": 
            statUpdate(player, "Organization", 1)
        if str(heritage) == "Sealed":  #Gains Essence domain/augmentation 1
            statUpdate(player, "Spirit", 0)
    else:
        error1 = "You did not make a choice, please notify the @Server_helper/DM role for help"
        return error1


def statRetrieve(player):
    statarray = []
    XParray = []
    CCSTATS = []
    f = open(f"{player}.txt", "r")
    stats = f.readlines()
    f.close
    counter = 0
    for x in stats:
        counter += 1
        if counter >= 9 and counter <=12:
            XParray.append(x)
        if counter >= 14:
            statarray.append(x)
    
    for x in XParray:
        xp = x
        xp = xp.replace(" XP Used", "")
        xp = xp.replace(" XP Total", "")
        xp = xp.replace(" CCPoints Used", "")
        xp = xp.replace(" CCPoints Max", "")
        xp = xp.replace("\n", "")

        CCSTATS.append(xp)
    
    for x in statarray:
        num = x
        num = num.replace("HP: ", "")
        num = num.replace("AP: ", "")
        num = num.replace("SP: ", "")
        num = num.replace("PDR: ", "")
        num = num.replace("MDR: ", "")
        num = num.replace("Speed: ", "")
        
        num = num.replace(" spirit", "")
        num = num.replace(" tenacity", "")
        num = num.replace(" dexterity", "")
        num = num.replace(" awareness", "")
        num = num.replace(" strength", "")
        num = num.replace(" intelligence", "")
        num = num.replace(" Acrobatics", "")
        num = num.replace(" Athletics", "")
        num = num.replace(" Empathy", "")
        num = num.replace(" Forgery", "")
        num = num.replace(" Fortitude", "")
        num = num.replace(" Hide", "")
        num = num.replace(" Medical", "")
        num = num.replace(" Notice", "")
        num = num.replace(" Performance", "")
        num = num.replace(" RecallInformation", "")
        num = num.replace(" Silvertongue", "")
        num = num.replace(" Subtlety", "")
        num = num.replace(" Wilderness", "")
        num = num.replace(" Willpower", "")
        num = num.replace(" Relationship", "")
        num = num.replace(" Nemesis", "")
        num = num.replace(" Organization", "")
        num = num.replace(" AnimatedCompanion", "")
        num = num.replace(" AnimalHandler", "")
        num = num.replace(" BeastHandler", "")
        num = num.replace(" WeaponProficiency", "")
        num = num.replace(" Brawling", "")
        num = num.replace(" ArmorProficiency", "")
        num = num.replace(" Runestone", "")
        num = num.replace(" Vehicles", "")
        num = num.replace(" CombatVehicles", "")
        num = num.replace(" Crafting", "")
        num = num.replace(" Hacking", "")
        num = num.replace(" Profession", "")
        num = num.replace("\n", "")

        CCSTATS.append(num)
    
    print (f"{CCSTATS}")
    
    return CCSTATS

def statUpdate(player, Stat = "", Amount = 0):

    #print(f"{player}\n{Stat}\n{Amount}")
    statarray = []
    statnum = []
    XParray = []
    XPnum = []
    f = open(f"{player}.txt", "r")
    stats = f.readlines()
    f.close
    counter = 0
    for x in stats:
        counter += 1
        if counter >= 9 and counter <=12:
            XParray.append(x)
        if counter >= 14:
            statarray.append(x)
    #        print(x)
    
    for x in XParray:
        xp = x
        xp = xp.replace(" XP Used", "")
        xp = xp.replace(" XP Total", "")
        xp = xp.replace(" CCPoints Used", "")
        xp = xp.replace(" CCPoints Max", "")
        xp = xp.replace("\n", "")

        XPnum.append(xp)
    
    for x in statarray:
        num = x
        num = num.replace("HP: ", "")
        num = num.replace("AP: ", "")
        num = num.replace("SP: ", "")
        num = num.replace("PDR: ", "")
        num = num.replace("MDR: ", "")
        num = num.replace("Speed: ", "")
        
        num = num.replace(" spirit", "")
        num = num.replace(" tenacity", "")
        num = num.replace(" dexterity", "")
        num = num.replace(" awareness", "")
        num = num.replace(" strength", "")
        num = num.replace(" intelligence", "")
        num = num.replace(" Acrobatics", "")
        num = num.replace(" Athletics", "")
        num = num.replace(" Empathy", "")
        num = num.replace(" Forgery", "")
        num = num.replace(" Fortitude", "")
        num = num.replace(" Hide", "")
        num = num.replace(" Medical", "")
        num = num.replace(" Notice", "")
        num = num.replace(" Performance", "")
        num = num.replace(" RecallInformation", "")
        num = num.replace(" Silvertongue", "")
        num = num.replace(" Subtlety", "")
        num = num.replace(" Wilderness", "")
        num = num.replace(" Willpower", "")
        num = num.replace(" Relationship", "")
        num = num.replace(" Nemesis", "")
        num = num.replace(" Organization", "")
        num = num.replace(" AnimatedCompanion", "")
        num = num.replace(" AnimalHandler", "")
        num = num.replace(" BeastHandler", "")
        num = num.replace(" WeaponProficiency", "")
        num = num.replace(" Brawling", "")
        num = num.replace(" ArmorProficiency", "")
        num = num.replace(" Runestone", "")
        num = num.replace(" Vehicles", "")
        num = num.replace(" CombatVehicles", "")
        num = num.replace(" Crafting", "")
        num = num.replace(" Hacking", "")
        num = num.replace(" Profession", "")
        num = num.replace("\n", "")

        statnum.append(num)

    if Stat == "XP USED":
        XPnum[0] = int(XPnum[0]) + Amount
    if Stat == "XP TOTAL":
        XPnum[1] = int(XPnum[1]) + Amount
    if Stat == "CCPoint USED":
        XPnum[2] = int(XPnum[2]) + Amount
    if Stat == "CCPoint MAX":
        XPnum[3] = int(XPnum[3]) + Amount
    
    if Stat == "HP":
        statnum[0] = int(statnum[0]) + Amount
    if Stat == "AP":
        statnum[1] = int(statnum[1]) + Amount
    if Stat == "Speed":
        statnum[5] = int(statnum[5]) + Amount
    if Stat == "Spirit":
        statnum[6] = int(statnum[6]) + Amount
    if Stat == "Tenacity":
        statnum[7] = int(statnum[7]) + Amount
    if Stat == "Dexterity":
        statnum[8] = int(statnum[8]) + Amount
    if Stat == "Awareness":
        statnum[9] = int(statnum[9]) + Amount
    if Stat == "Strength":
        statnum[10] = int(statnum[10]) + Amount
    if Stat == "Intelligence":
        statnum[11] = int(statnum[11]) + Amount
    if Stat == "Acrobatics":
        statnum[13] = int(statnum[13]) + Amount
    if Stat == "Athletics":
        statnum[14] = int(statnum[14]) + Amount
    if Stat == "Empathy":
        statnum[15] = int(statnum[15]) + Amount
    if Stat == "Forgery":
        statnum[16] = int(statnum[16]) + Amount
    if Stat == "Fortitude":
        statnum[17] = int(statnum[17]) + Amount
    if Stat == "Hide":
        statnum[18] = int(statnum[18]) + Amount
    if Stat == "Medical":
        statnum[19] = int(statnum[19]) + Amount
    if Stat == "Notice":
        statnum[20] = int(statnum[20]) + Amount
    if Stat == "Performance":
        statnum[21] = int(statnum[21]) + Amount
    if Stat == "RecallInformation":
        statnum[22] = int(statnum[22]) + Amount
    if Stat == "Silvertongue":
        statnum[23] = int(statnum[23]) + Amount
    if Stat == "Subtlety":
        statnum[24] = int(statnum[24]) + Amount
    if Stat == "Wilderness":
        statnum[25] = int(statnum[25]) + Amount
    if Stat == "Willpower":
        statnum[26] = int(statnum[26]) + Amount
    if Stat == "Relationship":
        statnum[27] = int(statnum[27]) + Amount
    if Stat == "Nemesis":
        statnum[28] = int(statnum[28]) + Amount
    if Stat == "Organization":
        statnum[29] = int(statnum[29]) + Amount
    if Stat == "AnimatedCompanion":
        statnum[30] = int(statnum[30]) + Amount
    if Stat == "AnimalHandler":
        statnum[31] = int(statnum[31]) + Amount
    if Stat == "BeastHandler":
        statnum[32] = int(statnum[32]) + Amount
    if Stat == "WeaponProficiency":
        statnum[33] = int(statnum[33]) + Amount
    if Stat == "Brawling":
        statnum[34] = int(statnum[34]) + Amount
    if Stat == "ArmorProficiency":
        statnum[35] = int(statnum[35]) + Amount
    if Stat == "Runestone":
        statnum[36] = int(statnum[36]) + Amount
    if Stat == "Vehicles":
        statnum[37] = int(statnum[37]) + Amount
    if Stat == "CombatVehicles":
        statnum[38] = int(statnum[38]) + Amount
    if Stat == "Crafting":
        statnum[39] = int(statnum[39]) + Amount
    if Stat == "Hacking":
        statnum[40] = int(statnum[40]) + Amount
    if Stat == "Profession":
        statnum[41] = int(statnum[40]) + Amount

    #print(stats)
    counterTwo = 0
    for x in statnum:
        stats[counterTwo+13] = statnum[counterTwo]
        counterTwo += 1 
    
    PhysicalDR = int(statnum[7])
    PhysicalDR = PhysicalDR/2
    MetaDR = int(statnum[6])
    MetaDR = MetaDR/2
    MetaDR = math.ceil(MetaDR)
    PhysicalDR = math.ceil(PhysicalDR)

    #print(PhysicalDR)
    #print(MetaDR)

    stats[8] = str(XPnum[0]) + " XP Used\n"
    stats[9] = str(XPnum[1]) + " XP Total\n"    
    stats[10] = str(XPnum[2]) + " CCPoints Used\n"
    stats[11] = str(XPnum[3]) + " CCPoints Max\n"

    stats[13] = "HP: " + str(statnum[0])
    stats[14] = "\nAP: " + str(statnum[1])
    stats[15] = "\nSP: " + str(statnum[6]) 
    stats[16] = "\nPDR " + str(PhysicalDR) 
    stats[17] = "\nMDR: " + str(MetaDR)
    stats[18] = "\nSpeed: " + str(statnum[5])
    stats[19] = "\n" + str(statnum[6]) + " spirit\n"
    stats[20] = str(statnum[7]) + " tenacity\n"
    stats[21] = str(statnum[8]) + " dexterity\n"
    stats[22] = str(statnum[9]) + " awareness\n"
    stats[23] = str(statnum[10]) + " strength\n"
    stats[24] = str(statnum[11]) + " intelligence\n"
    stats[25] = "0\n"

    stats[26] = str(statnum[13]) + " Acrobatics\n"
    stats[27] = str(statnum[14]) + " Athletics\n"
    stats[28] = str(statnum[15]) + " Empathy\n"
    stats[29] = str(statnum[16]) + " Forgery\n"
    stats[30] = str(statnum[17]) + " Fortitude\n"
    stats[31] = str(statnum[18]) + " Hide\n"
    stats[32] = str(statnum[19]) + " Medical\n"
    stats[33] = str(statnum[20]) + " Notice\n"
    stats[34] = str(statnum[21]) + " Performance\n"
    stats[35] = str(statnum[22]) + " RecallInformation\n"
    stats[36] = str(statnum[23]) + " Silvertongue\n"
    stats[37] = str(statnum[24]) + " Subtlety\n"
    stats[38] = str(statnum[25]) + " Wilderness\n"
    stats[39] = str(statnum[26]) + " Willpower\n"
    stats[40] = str(statnum[27]) + " Relationship\n"
    stats[41] = str(statnum[28]) + " Nemesis\n"
    stats[42] = str(statnum[29]) + " Organization\n"
    stats[43] = str(statnum[30]) + " AnimatedCompanion\n"
    stats[44] = str(statnum[31]) + " AnimalHandler\n"
    stats[45] = str(statnum[32]) + " BeastHandler\n"
    stats[46] = str(statnum[33]) + " WeaponProficiency\n"
    stats[47] = str(statnum[34]) + " Brawling\n"
    stats[48] = str(statnum[35]) + " ArmorProficiency\n"
    stats[49] = str(statnum[36]) + " Runestone\n"
    stats[50] = str(statnum[37]) + " Vehicles\n"
    stats[51] = str(statnum[38]) + " CombatVehicles\n"
    stats[52] = str(statnum[39]) + " Crafting\n"
    stats[53] = str(statnum[40]) + " Hacking\n"
    stats[54] = str(statnum[41]) + " Profession\n"
    
    f = open(f"{player}.txt", "w")
    f.writelines(stats)
    f.close

    

    #print(stats)
            
            



    #print(statarray)
    #print(f"\n\n")
    #print(statnum)
    return stats

def race(player):

    if str(player) == "Human":
        choice = "Human"
        return choice
    
    elif str(player) == "Beastkin":
        choice = "Beastkin"
        return choice
    elif str(player) == "Beastkin Tail":
        choice = "Beastkin Tail"
        return choice
    elif str(player) == "Beastkin Ears":
        choice = "Beastkin Ears"
        return choice
    elif str(player) == "Beastkin Eyes":
        choice = "Beastkin Eyes"
        return choice
    elif str(player) == "Beastkin Camouflage":
        choice = "Beastkin Camouflage"
        return choice
    elif str(player) == "Beastkin Claws":
        choice = "Beastkin Claws"
        return choice
    elif str(player) == "Beastkin Wings":
        choice = "Beastkin Wings"
        return choice
    elif str(player) == "Beastkin Exoskeleton":
        choice = "Beastkin Exoskeleton"
        return choice
    elif str(player) == "Beastkin Thick Hide":
        choice = "Beastkin Thick Hide"
        return choice
    elif str(player) == "Beastkin Scales":
        choice = "Beastkin Scales"
        return choice
    elif str(player) == "Beastkin Gills":
        choice = "Beastkin Gills"
        return choice
    elif str(player) == "Beastkin Hooves":
        choice = "Beastkin Hooves"
        return choice
    elif str(player) == "Beastkin Horns":
        choice = "Beastkin Horns"
        return choice
    elif str(player) == "Beastkin Predator":
        choice = "Beastkin Predator"
        return choice
    elif str(player) == "Beastkin Fangs":
        choice = "Beastkin Fangs"
        return choice
    elif str(player) == "Beastkin Stinger":
        choice = "Beastkin Stinger"
        return choice
    elif str(player) == "Beastkin Dragon Breath":
        choice = "Beastkin Dragon Breath"
        return choice
    elif str(player) == "Beastkin Webbing":
        choice = "Beastkin Webbing"
        return choice
    elif str(player) == "Beastkin Drop Tail":
        choice = "Beastkin Drop Tail"
        return choice
    elif str(player) == "Beastkin Bioluminescence":
        choice = "Beastkin Bioluminescence"
        return choice 
    elif str(player) == "Beastkin Mimicry":
        choice = "Beastkin Mimicry"
        return choice
    elif str(player) == "Beastkin Sonar Sense":
        choice = "Beastkin Sonar Sense"
        return choice
    elif str(player) == "Beastkin Sonar Blast":
        choice = "Beastkin Sonar Blast"
        return choice
    
    elif str(player) == "Anima Enhanced":
        choice = "Anima Enhanced"
        return choice
    
    elif str(player) == "Elf Royal":
        choice = "Elf Royal"
        return choice
    elif str(player) == "Elf High Born":
        choice = "Elf High Born"
        return choice
    elif str(player) == "Elf Low Born":
        choice = "Elf Low Born"
        return choice
    
    elif str(player) == "Orc Magic Born":
        choice = "Orc Magic Born"
        return choice
    elif str(player) == "Orc Battle Born":
        choice = "Orc Battle Born"
        return choice
    
    elif str(player) == "Synthetic":
        choice = "Synthetic"
        return choice
    elif str(player) == "Synthetic Genius":
        choice = "Synthetic Genius"
        return choice
    elif str(player) == "Synthetic Versatile":
        choice = "Synthetic Versatile"
        return choice
    
    elif str(player) == "Voidkin":
        choice = "Voidkin"
        return choice
    elif str(player) == "Voidkin Tail":
        choice = "Voidkin Tail"
        return choice
    elif str(player) == "Voidkin Ears":
        choice = "Voidkin Ears"
        return choice
    elif str(player) == "Voidkin Eyes":
        choice = "Voidkin Eyes"
        return choice
    elif str(player) == "Voidkin Camouflage":
        choice = "Voidkin Camouflage"
        return choice
    elif str(player) == "Voidkin Claws":
        choice = "Voidkin Claws"
        return choice
    elif str(player) == "Voidkin Wings":
        choice = "Voidkin Wings"
        return choice
    elif str(player) == "Voidkin Exoskeleton":
        choice = "Voidkin Exoskeleton"
        return choice
    elif str(player) == "Voidkin Thick Hide":
        choice = "Voidkin Thick Hide"
        return choice
    elif str(player) == "Voidkin Scales":
        choice = "Voidkin Scales"
        return choice
    elif str(player) == "Voidkin Gills":
        choice = "Voidkin Gills"
        return choice
    elif str(player) == "Voidkin Hooves":
        choice = "Voidkin Hooves"
        return choice
    elif str(player) == "Voidkin Horns":
        choice = "Voidkin Horns"
        return choice
    elif str(player) == "Voidkin Predator":
        choice = "Voidkin Predator"
        return choice
    elif str(player) == "Voidkin Fangs":
        choice = "Voidkin Fangs"
        return choice
    elif str(player) == "Voidkin Stinger":
        choice = "Voidkin Stinger"
        return choice
    elif str(player) == "Voidkin Dragon Breath":
        choice = "Voidkin Dragon Breath"
        return choice
    elif str(player) == "Voidkin Webbing":
        choice = "Voidkin Webbing"
        return choice
    elif str(player) == "Voidkin Drop Tail":
        choice = "Voidkin Drop Tail"
        return choice
    elif str(player) == "Voidkin Bioluminescence":
        choice = "Voidkin Bioluminescence"
        return choice 
    elif str(player) == "Voidkin Mimicry":
        choice = "Voidkin Mimicry"
        return choice
    elif str(player) == "Voidkin Sonar":
        choice = "Voidkin Sonar"
        return choice
    elif str(player) == "Voidkin Sonar Blast":
        choice = "Voidkin Sonar Blast"
        return choice
    elif str(player) == "Voidkin Despair":
        choice = "Voidkin Despair"
        return choice
    elif str(player) == "Voidkin Possession":
        choice = "Voidkin Possession"
        return choice
    elif str(player) == "Voidkin Power":
        choice = "Voidkin Power"
        return choice

    elif str(player) == "Dwarf Warrior":
        choice = "Dwarf Warrior"
        return choice
    elif str(player) == "Dwarf Smith":
        choice = "Dwarf Smith"
        return choice
    
    elif str(player) == "Succubus":
        choice = "Succubus"
        return choice
    elif str(player) == "Succubus Summoned":
        choice = "Succubus Summoned"
        return choice
    elif str(player) == "Succubus Natural Born Tail":
        choice = "Succubus Natural Born Tail"
        return choice
    elif str(player) == "Succubus Natural Born Horns":
        choice = "Succubus Natural Born Horns"
        return choice
    elif str(player) == "Succubus Natural Born Wings":
        choice = "Succubus Natural Born Wings"
        return choice
    
    elif str(player) == "Demon":
        choice = "Demon"
        return choice
    elif str(player) == "Demon Summoned":
        choice = "Demon Summoned"
        return choice
    elif str(player) == "Demon Natural Born Tail":
        choice = "Demon Natural Born Tail"
        return choice
    elif str(player) == "Demon Natural Born Horns":
        choice = "Demon Natural Born Horns"
        return choice
    elif str(player) == "Demon Natural Born Wings":
        choice = "Demon Natural Born Wings"
        return choice

def heritage(player):

    Hanswer = "You either misspelled the Heritage name or did not choose one, make sure to always capitalize your answers"

    if player == "Dux":
        Hanswer = "Dux"
        print(Hanswer)
    if player == "Potens":
        Hanswer = "Potens"
        print(Hanswer)
    if player == "Custos":
        Hanswer = "Custos"
        print(Hanswer)
    if player == "Elysium":
        Hanswer = "Elysium"
        print(Hanswer)
    if player == "Libertas":
        Hanswer = "Libertas"
        print(Hanswer)
    if player == "Vettrheim":
        Hanswer = "Vettrheim"
        print(Hanswer)
    if player == "Anima Lands":
        Hanswer = "Anima Lands"
        print(Hanswer)
    if player == "Dark Lands":
        Hanswer = "Dark Lands"
        print(Hanswer)
    if player == "Wild":
        Hanswer = "Wild"
        print(Hanswer)
    if player == "The Dark Continent":
        Hanswer = "The Dark Continent"
        print(Hanswer)
    if player == "Military Heritage":
        Hanswer = "Military Heritage"
        print(Hanswer)
    if player == "Sealed":
        Hanswer = "Sealed"
        print(Hanswer)

    heritage = (f"{Hanswer}\n\nAre you sure this is the Heritage you want? Y/N")
    return heritage

def Lore(player):

    Dux = """**[Dux]:**\nA province within the United Government. Dux is known for its diverse Landscapes, including vast forests, open plains, and majestic mountains. It is a region dotted with 
numerous towns and villages, making it a sprawling and thriving country. the inhabitants of Duc have developed exceptional trenacity and possess stornger wills, which translates into better career performances.
**+1 Spirit**
[Choose One] [Dux Option 1]: +1 Willpower Rank [Dux Option 2]: +2 Performance Ranks"""
    Potens = """**[Potens]:**\nThe Country of Sand and Rock, is a harsh and unforgiving land where little thrives except for conflict and crime. Life here revoles around constant struggles, 
with the looming threat of the Void-Taken and the ever present menace of bandits. The people of Potens have adapted to this brutal environment, becoming highly skilled in combat to survive and protect their homeland.
+1 Tenacity
[Choose One] [Potens Option 1]: +1 Brawling Skill [Potens Option 2]: +1 Weapon Pro Skill"""
    Custos = """**[Custos]:**\nCustos is a group of individuals known for their exceptional climbing abilities nad keen powers of observation. They possess eagle-like vision, making them highly perceptive and adept at spotting even the smallest details.
They are renowned for their persuasive nature, often being described as master negotiators and smooth talkers. Whether it's finding the best deals in markets, scaling treacherous mountains, or convincing others to agree with them, Custians excel in these endeavors.
+1 Strength
[Choose One] [Custos Option 1] +2 Notice Skill [Custos Option 2] +1 Silvertongue Skill"""
    Elysium = """**[Elysium]:**\nElysium Engineering stands as a testament to unparalleled brilliance in the world. They are renowned for createing the first synthetic being, an achievement that echoes through history. 
Elysians are exceptionally intelligent, possessing sharp minds capable of tackling the most complex challenges. Their expertise in the mystical art of Runestone is unmatched, and they excell in their chosen careers, becoming true masters in their fields.
+1 Intelligence
[Choose One] [Elysium Option 1] +1 Runestone Skill [Elysium Option 2] +1 Profession Skill"""
    Libertas = """**[Libertas]:**\nIt is a paradise island, a place of unparalleled beauty and tranquility. However, this serenity is occasionally disrupted by the dreaded Voidtaken attacks. Despite these challenges, the inhabitants of Libertas, known as Beastkin, 
possess exceptional abilities that aid them in times of crisis. Beastkin have heightened awareness, being able to detect Voidtaken from afar and strike them with remarkable accuracy in combat. Moreover, their survival skills in the wilderness are unmatched, making them true masters of their environment.
+1 Awareness
+2 Wilderness Skill"""
    Vettrheim = """**[Vettrheim]:**\nThe minor Country of Vettrheim is unique in the world, having existed long as a Independent territory even before the Rise of Independents, they hold several key locations important for Elysium and as such have a very important Alliance with Elysium. The people while typically Anima Enhanced are also very honorable and more simple in their lifestyles.
+1 Tenacity
[Choose One][Vettrhiem Option 1]+1 Weapon Pro skill [Vettrhiem Option 2] +1 Runestone skill"""
    AnimaLands = """**[Anima Lands]:**\nThe Anima Lands are unique regions in the world, brimming with vibrant and living energies. These lands seem almsot alive, and those who dwell within them must navigate with utmost precision and understanding of their own Essence. In the Anima Lands, some individuals are blessed with loyal companions, either selfmade creations or AI entities.
+1 Dexterity
[Choose One][Anima Lands Option 1] +1 Essence Domain/Augmentation SKILL [Anima Lands Option 2] +1 Animated Companion Skill"""
    DarkLands = """**[Dark Lands]:**\nThe Dark Lands are regions tainted by darkness, whether it be the touch of death, the presence of the Voidtaken, or ancient and unknown malevolence. These lands instill fear in the hearts of many, for they carry the risk of death or worse - Corruption. However some individuals choose to brave these treacherous lands, becoming true survivors.
+1 Tenacity
[Choose One][Dark Lands Option 1] +1 Fortitude Skill [Dark Lands Option 2] +1 Willpower Skill"""
    Wild = """**[Wild]:**\nWildlings, free spirits living outside the confines of towns or cities, often encounter skepticism and distrust from the more sttled folks. But their way of life has honed their abilities, making them adept at avoiding danger and finding refuge when needed. while some excel at hiding in the shadows, others rely on their endurance to weather the trials of the wilderness.
+1 Dexterity
[Choose One] [Wild Option 1] +1 Fortitude Skill [Wild Option 2] +2 Hide Skill"""
    TheDarkContinent = """**[The Dark Continent]:**\nA land shrouded in mystery and peril, is the realm of the Voidkin. For humans, living her e is deemed insanity, but for the Voidkin, it becomes their home. Embracing their tribe's principles is the key to finding acceptance and belonging in this enigmatic realm.
+4 HP
+1 Silvertongue skill"""
    MilitaryHeritage = """**[Military Heritage]:**\n Born into a distinguished Military family of one of the 5 major Countries, you were destined for a life intertwined with the military. From a young age, you were enrolled in military programs, instilling in you discipline, respect, honor, and rigorous physical training.
+1 Tenacity
[Choose One] [Military Option 1] +1 Combat Vehicles skill [Military Option 2 (Country of Origin)] +1 Organization skill(Restricted to country of origin)"""
    Sealed = """**[Sealed]:**\nRestricted to: Elves, Orcs, Dwarfs, Demon/Succubus. Born of a race previously lost to the world of Vesper, you are one of many now released from the dimension your kind was imprisoned in. Why it is only now happening is still unknown but one thing is for sure. That the lands your race once held are gone but your place in the world is not lost. Now is the new time for learning and exploring this new world.
+1 Attribute Point
[Choose One] [Sealed Option 1] +1 Wilderness Skill [Sealed Option 2] +1 Essence Domain/Augmentation SKILL"""
    
    Human = """**[Human]:**\nDespite lacking natural advantages, humans have proven their tenacity and spirit throughout history,
        establishing the four Countries to protect the world from the relentless threat of the Void-Taken. Their  ability to unite and 
        support each other through 'Strength in Numbers' sets them apart as resilient and strategic fighters.\n**+1 Spirit**\n**+1 Tenacity**
        **+2 Character Creation Points**\n**+5 Starting XP**\n\n**Strength in Numbers:** Humans have the unique ability to buff themselves and allies 
        in combat Increasing attack to hit, defence chance, and damage by +1 up to a max of 4 for each creature within 5 zones. The creature 
        Max goes up by 1 per B Rank. 1B, 2B, 3B, 4B.
        **Activation:** 1 use per mission
        **Group Activation:** Stacks with other 'Strength in Numbers'
        **Duration and Aftermath:** Lasts 6 Rounds, once the 6 rounds are over character is at disadvantage for 10 rounds."""                
    BeastKin1 = """[Beastkin]\nWith their Dark vision, Beastkin can confidently navigate dark environments without hindrance. Additionally,
their chosen Beaskin trait and Primal Instinct grant them distinct advantages in various situations, making them formidable adventurers and 
valuable members of any party
\nDark Vision: Cannot be inflicted with the 'Obstructed' Status Condition when in dark or low-light conditions.
**Primal Instinct:** Beastkin tap into their primal instincts, gaining a boost ot their physical-based rolls. This includes attacking with weapons 
or hands, dodging attacks, resisting damage, performing athletic feats, and moving stealthily. +1 per B rank. 1B, 2B, 3B, 4B.
**Activation:** 1 use per mission
**Duration and Aftermath:** Lasts 6 Rounds, once the 6 rounds are over character is at disadvantage for 10 rounds.
Beastkin Trait: Each Beastkin can choose one of the following
**Tail:** +1 Awareness, +1 Intelligence, [Choose One] 1. Use tail to hold items 2. use tail to climb without needing to roll
**Beast Ears:** +2 Dexterity, hearing rolls ADV, Ignore Sneak Attack Debuff so long as you are within hearing range, +2 Notice Ranks
**Beast Eyes:** +2 Awareness, Sight rolls ADV, Sight range Doubled, Immune to Obstructed Status, [Choose] +1 Athletics Rank, +2 Notice Rank.
**Camouflage:** +1 Dexterity, +1 Tenacity, as a Free action, you can give yourself the Hidden status for rounds equal to Tenacity
**Claws:** +1 Awareness, +1 Strength, You have 2x claws[Natural Weapon, Light, Edged] that deal a 1d6+Strength DMG, +1 Brawling skill, claws can activate Bleeding for 1 round
"""
    BeastKin2 = """**Wings:** +2 Dexterity, Immune to 'Lame' status and dont suffer drawbacks from leg injury, can move Vertically, ya know... FLY
**Exoskeleton/Thick Hide/Scales:** +1 Strength, +1 Tenacity, Gain armor that increases strength based on rank, Rank 4: Light Rank 3: Medium Rank 2: Heavy Rank 1: SuperHeavy can regain half missing AD for 1 SP.
**Gills:** +2 Tenacity, Water Breathing, take half Cold damage, cant become winded due to swimming
**Hooves:** +1 Strength, +1 Tenacity, +1 Brawling Rank for Hooves[Natural, Light, Blunt] Deal 1d6+Strength Damage DMG, can cause Winded status with Hooves for 1 Round
**Horns:** +2 Strength, +2 to Shove/Trip/Grab Actions, [Choose One] 1. +2 Performance Ranks 2. +1 Athletics Rank
**Predator:** +1 Awareness, +1 Tenacity, +1 Speed
**Fangs/Stinger:** +1 Strength, +1 Tenacity, Fangs or Stinger[Natural, Precise or Edged] that deal a 1d6+strength, [Choose one] 1. Precise 2 Edged, can give poisoned status up to Tenacity times per week
**Dragon Breath:** +1 Dexterity, +1 Tenacity, Flame Breath[Natural, Precise] Deal 1d6+Dexterity, can cause on Fire Status to target for 6 rounds taking half attacks Damage. can activate times equal to Tenacity per week
**Spider Webs:** +1 Dexterity, +1 Tenacity, can shoot and grapple up to 2 targets at a time. can be used to climb using Athletics+Strength, can create a sticky zone equal to tenacity per week. zone has 5+Tenacity HP and takes entire turn to pass through, msut use fire/cutting to destroy
**Drop Tail:** +1 Tenacity, +1 Dexterity, can negate an injury by losing your tail until it regrows in a week.
**Bioluminescence:** +1 Awareness, +1 Dexterity, create a light spanning a 2 Zone radius for minutes equal to Tenacity per week.
**Sonar:** +1 Awareness, +1 Tenacity, [Choose One] 1.Sonar Sense(Immune to Blindness) 2. Sonar Blast [Natural, Blunt] deals 1d6+Tenacity DMG, can do equal to Tenacity times a week
**Must Format as Beastkin (Trait)**
"""
    #Note Give beastkin their background info
    AnimaEnhanced = """**[AnimaEnhanced]**\nAnima enhanced look like either a human or beastkin including cosmetic features but benefit from neither race.
instead their eyes match their anima color. Once known as the chosen, Anima Enhanced now have a deep connection to the magical energies of the world.
their 'Hero Mode' ability allows them to become formidable adversaries against the forces of darkness, but it comes with risks and consequences.
\n**Hero Mode:** Gain a +2 to rolls against Void-taken and Creatures of darkness including damage. Gain +1 per B rank 1B, 2B, 3B, 4B
**Activation:** this ability can be activated Once per mission
**Duration and aftermath:** 'Hero Mode' Lasts for 6 rounds, afterwards they are at disadvantage for 10 rounds
+3 Spirit
+10 Anima max of 20 at Character Creation
+1 Willpower Rank"""
    Synthetic = """**[Synthetic]**\nAs a synthetic, you possess a remarkable blend of humanoid appearance and advanced mechanical capabilities. Your ability to blend 
in with other races and your arsenal of built-in equipment make you a formidable force in the world.
[Choose One] **[Synthetic Genius]** +2 Intelligence **[Synthetic Versatile]** +1 to any 2 attributes
**no need for food**
**advantage to blend in with Humans or Beastkin**
**Natural Light armor:** 4 AD against Cutting Damage you take. if you reduce damage to 0 you do not lose any AD. Can spend 1 SP to regain all expended AD from this armor
**Can have modifications or weapons built into your body equal to your tenacity.** you do not suffer the weight increase effect on built in equipment."""            
    Elf = """**[Elves]**\nA once-thriving race, Elves have endured hardship due to the malevolent sorceress Eclipse. Sealed away by her dark magic, they're marked 
by their graceful presence and heightened senses, including double the visual range, Elves can choose different paths, such as the noble Royal Descendants, 
Martially skilled High Born, or nature-connected Low Born. in combat, they can unleash the 'Magic Cloak' to harness elemental power.
\nHeritage Predetermined: Sealed for heritage
Magic Cloak: During combat choose an Elemental damage type. gain 2DR against that damage type and deal 1d6+spirit to enemies in your zone. +1 DR and +2 sides on DMG Dice per B rank
1B, 2B, 3B, 4B. start->1d6->1d8->1d10->1d12->1d14
+1 Spirit
+1 Dexterity
2x vision distance
[Choose One] [Elf Royal]: +1 Runestone skill [Elf High Born]: +1 Weapon pro Skill [Elf Low Born]: +1 Wilderness Rank"""
    Orc = """**[Orc]**\nOrcs, a resilient race, faced Eclipse's wrath but emerged with unwavering strength. Their powerful bodies recieve a permanent boost in Senacity 
and Strength, while innate dark vision grants them the ability to navigate darkness effortlessly. ORcs follow paths as Magic Born with runic powers or Battle Born as foprmidable Warriros.
They can tap into 'Berserking' during combat, enhancing their combat prowess. 
Orcs typically have dark skin tones: Black,Brown, Charcoal or yellow color in rare cases.
[Berserking] Orcs can activate 'Berserking' during combat, +2DR and +1 to all combat based checks. these each go up by +1 for every B rank. This lasts 6 rounds, afterwards gain the 'Winded' status efect for 6 rounds
**+1 Tenacity**
**+1 Strength**
**Dark Vision:** can't be inflicted with the 'Obstructed status condition when in dark or low-light conditions.
**[Choose One] [Orc Magic Born]:** +1 Runestone Skill  **[Orc Battle Born]** +1 Weapon Pro Rank"""
    Dwarf = """**[Dwarves]**\nknown for their craftsmanship, Dwarves struggled against Eclypse's curse. their sturdy bodies are fortified with a permanent increase in strength. 
Dwarves often tread the path of a skilled Warriro Class or a masterful Smtih class, crafting goods from ores. Their unique ability,'Smith's Eye' allows them to blend metals when crafting equipment, 
combining their strengths to create formidable gear.
**Smith's Eye(Passive)**: when crafting a piece of equipment, instead of aonly being able to forge it out of 1 metal to gain a bonus, instead upon a 50/50 split you can add 2 bonus's from metals
**+2 Strength**
**[Choose One] [Dwarf Warrior]:** +1 Weapon pro rank **[Dwarf Smith]:** +1 crafting rank.
"""
    Demon = """**[Demon/Succubus]**\n Demons and Succubi are enigmatic beings, torn from their own shadowy realms by sorcerers' incantations. Their essence is stepped in darkness and allure, 
Hailing from a world shrouded in Mysteries beyond moratl comprehension. Sealed away by the malevolent sorceress Eclipse, their history and true nature were conceald from the world, erased from memory until 
only recently. In the past, They were often mistaken as mere magical summons of eclipse. Unlike the other races Demons and Succubi were forced into servitude as foot soldiers for Eclipse. Some resisted her control, 
their loyalty forged in the fires of rebellion, while others found a perverse pride in serving under her dark banner. Their existence remains an unsettling reminder of Eclipse's reing and the hidden realms from which they
were forcibly drawn. unlike the other races, this race appears nearly Human except for markings around their body and a noticeable snake like eyes.
**Magic Eye(Passive):** When casting Spells or cantrips. the DC required to cast them is lowered by 2. this increases every B rank. 1B, 2B, 3B, 4B
**+2 Spirit**
**Dark vision:** Demons/Succubus possess innate dark vision, whihc means they cannot be inflicted with the 'Obstructed' Status Condition when in dark or low light conditions.
[Choose One] **Demon Summoned:** +1 Runestone skill, **Demon Natural Born:** +1 notice rank, and can take the Tail, Horn, Or Wing traits from Beastkin."""
    Succubus = """**[Demon/Succubus]**\n Demons and Succubi are enigmatic beings, torn from their own shadowy realms by sorcerers' incantations. Their essence is stepped in darkness and allure, 
Hailing from a world shrouded in Mysteries beyond moratl comprehension. Sealed away by the malevolent sorceress Eclipse, their history and true nature were conceald from the world, erased from memory until 
only recently. In the past, They were often mistaken as mere magical summons of eclipse. Unlike the other races Demons and Succubi were forced into servitude as foot soldiers for Eclipse. Some resisted her control, 
their loyalty forged in the fires of rebellion, while others found a perverse pride in serving under her dark banner. Their existence remains an unsettling reminder of Eclipse's reing and the hidden realms from which they
were forcibly drawn. unlike the other races, this race appears nearly Human except for markings around their body and a noticeable snake like eyes.
**Magic Eye(Passive):** When casting Spells or cantrips. the DC required to cast them is lowered by 2. this increases every B rank. 1B, 2B, 3B, 4B
**+2 Spirit**
**Dark vision:** Demons/Succubus possess innate dark vision, whihc means they cannot be inflicted with the 'Obstructed' Status Condition when in dark or low light conditions.
[Choose One] **Succubus Summoned:** +1 Runestone skill, **Succubus Natural Born:** +1 notice rank, and can take the Tail, Horn, Or Wing traits from Beastkin."""
    Voidkin = """**[Voidkin]**\nA race of monster that come from negative energies in the World. They possess a blend of humanoid and animal traits. Each Voidkin takes on a Human-like 
appearance with a single prominent animal trait. One of their most remarkable abilities is their night vision, granting them an advantage in low light conditions.
However, their presence in history has not been long nor challenges. From a rapid evolution from their mindless states they've adopted a society that believes in strength. Now with 
a entire continent to themselves and the ability to integrate into human society. a voidkin looks like any other person but they have grey skintones. 
Their eyes have a dark color They may pick any one Beastkin trait or Voidkin trait. [See beastkin for their traits and return]
Traits include: Voidkin Tail, Voidkin Ears, Voidkin Eyes, Voidkin Camouflage, Voidkin Claws, Voidkin Wings, Voidkin Exoskeleton/Thick Hide/ Scales, Voidkin Gills, Voidkin Hooves, Voidkin Horns, Voidkin Predator, 
Voidkin Fangs/Stinger(if fangs (edged), if stinger (Precise)), Voidkin Dragon Breath, Voidkin Spider Webs, Voidkin Drop Tail, Voidkin Bioluminescence, Voidkin Sonar Sense, Voidkin Sonar Blast.
Dark Vision: cannot be inflicted with the 'Obstructed' Status Condition due to being in the dark.
[Choose One]
**Any Beastkin Trait:**
**Voidkin Despair:** +1 Spirit, as an action attack with your natural weapon, deal damage normally as well as cause the 'Horrified' status condition. cna only use this 1 time per week
**Voidkin Possession:** +1 Spirit, as an action you make a ability roll with your voidkin race ability. if the roll beats the DC determined by the DM you take control over said object. you can only use this once per week
**Voidkin Power:** +1 Strength, you start with Rank 1 Terrain Domain. The terrain is pre-selected for Darklands. this takes upa  domain slot. You have the ability to do this without SP cost equal to Spirit times per week"""                   

    Spirit = """Spirit - Measures a character's soul potency, ability to channel Essence, mental resilience, and charisma with others."""
    Tenacity = """Tenacity - Determines a character's physical toughness and ability to withstand damage and exhaustion"""
    Dexterity = """Dexterity - Reflects a character's nimbleness and skill with ranged weapons like guns, bows, and throwing knives."""
    Awareness = """Awareness - Represents a character's situational awareness and precision in landing blows with weapons, along with ability to notice clues and entities"""
    Strength = """Strength - Measures a character's physical pwoer, influencing their melee attack damage, grappling abilities, and carry capacity."""
    Intelligence = """Intelligence - Indicates a character's knowledge, understanding of the world, and proficiency with technology."""


    if player == "Dux":
        return Dux
    elif player == "Potens":
        return Potens
    elif player == "Custos":
        return Custos
    elif player == "Elysium":
        return Elysium
    elif player == "Libertas":
        return Libertas
    elif player == "Vettrheim":
        return Vettrheim
    elif player == "Anima Lands":
        return AnimaLands
    elif player == "AnimaLands":
        return AnimaLands
    elif player == "Dark Lands":
        return DarkLands
    elif player == "DarkLands":
        return DarkLands
    elif player == "Wild":
        return Wild
    elif player == "The Dark Continent":
        return TheDarkContinent
    elif player == "TheDarkContinent":
        return TheDarkContinent
    elif player == "Military Heritage":
        return MilitaryHeritage
    elif player == "MilitaryHeritage":
        return MilitaryHeritage
    elif player == "Sealed":
        return Sealed
    
    
    
    elif player == "Human":
        return Human
    elif player == "Beastkin":
        temp = "there are 2 Beaskin lists, make sure to put 'Beastkin1' or 'Beastkin2'"
        return temp
    elif player == "Beastkin1":
        return BeastKin1
    elif player == "Beastkin2":
        return BeastKin2
    elif player == "Anima Enhanced":
        return AnimaEnhanced
    elif player == "Synthetic":
        return Synthetic
    elif player == "Elf":
        return Elf
    elif player == "Elf Royal":
        return "DNS"
    elif player == "Elf High Born":
        return "DNS"
    elif player == "Elf Low Born":
        return "DNS"
    
    elif player == "Demon Natural Born Tail":
        return "DNS"
    elif player == "Demon Natural Born Horns":
        return "DNS"
    elif player == "Demon Natural Born Wings":
        return "DNS"
    elif player == "Succubus Natural Born Tail":
        return "DNS"
    elif player == "Succubus Natural Born Horns":
        return "DNS"
    elif player == "Succubus Natural Born Wings":
        return "DNS"
    
    elif player == "Synthetic Genius":
        return "DNS"
    elif player == "Synthetic Versatile":
        return "DNS"
    
    elif player == "Beastkin Tail":
        return "DNS"
    elif player == "Beastkin Ears":
        return "DNS"
    elif player == "Beastkin Eyes":
        return "DNS"
    elif player == "Beastkin Camouflage":
        return "DNS"
    elif player == "Beastkin Claws":
        return "DNS"
    elif player == "Beastkin Wings":
        return "DNS"
    elif player == "Beastkin Exoskeleton":
        return "DNS"
    elif player == "Beastkin Thick Hide":
        return "DNS"
    elif player == "Beastkin Scales":
        return "DNS"
    elif player == "Beastkin Gills":
        return "DNS"
    elif player == "Beastkin Hooves":
        return "DNS"
    elif player == "Beastkin Horns":
        return "DNS"
    elif player == "Beastkin Predator":
        return "DNS"
    elif player == "Beastkin Fangs":
        return "DNS"
    elif player == "Beastkin Stinger":
        return "DNS"
    elif player == "Beastkin Dragon Breath":
        return "DNS"
    elif player == "Beastkin Spider Webs":
        return "DNS"
    elif player == "Beastkin Drop Tail":
        return "DNS"
    elif player == "Beastkin Bioluminescence":
        return "DNS"
    elif player == "Beastkin Sonar Blast":
        return "DNS"
    elif player == "Beastkin Sonar Sense":
        return "DNS"
    
    elif player == "Voidkin Tail":
        return "DNS"
    elif player == "Voidkin Ears":
        return "DNS"
    elif player == "Voidkin Eyes":
        return "DNS"
    elif player == "Voidkin Camouflage":
        return "DNS"
    elif player == "Voidkin Claws":
        return "DNS"
    elif player == "Voidkin Wings":
        return "DNS"
    elif player == "Voidkin Exoskeleton":
        return "DNS"
    elif player == "Voidkin Thick Hide":
        return "DNS"
    elif player == "Voidkin Scales":
        return "DNS"
    elif player == "Voidkin Gills":
        return "DNS"
    elif player == "Voidkin Hooves":
        return "DNS"
    elif player == "Voidkin Horns":
        return "DNS"
    elif player == "Voidkin Predator":
        return "DNS"
    elif player == "Voidkin Fangs":
        return "DNS"
    elif player == "Voidkin Stinger":
        return "DNS"
    elif player == "Voidkin Dragon Breath":
        return "DNS"
    elif player == "Voidkin Spider Webs":
        return "DNS"
    elif player == "Voidkin Drop Tail":
        return "DNS"
    elif player == "Voidkin Bioluminescence":
        return "DNS"
    elif player == "Voidkin Sonar Blast":
        return "DNS"
    elif player == "Voidkin Sonar Sense":
        return "DNS"
    elif player == "Voidkin Despair":
        return "DNS"
    elif player == "Voidkin Possession":
        return "DNS"
    elif player == "Voidkin Power":
        return "DNS"
    
    elif player == "Orc":
        return Orc
    elif player == "Orc Magic Born":
        return "DNS"
    elif player == "Orc Battle Bonr":
        return "DNS"
    
    elif player == "Dwarf":
        return Dwarf
    elif player == "Dwarf Warrior":
        return "DNS"
    elif player == "Dwarf Smith":
        return "DNS"
    
    elif player == "Demon":
        return Demon
    elif player == "Demon Summoned":
        return "DNS"
    elif player == "Demon Tail":
        return "DNS"
    elif player == "Demon Horn":
        return "DNS"
    elif player == "Demon Wing":
        return "DNS"
    
    elif player == "Succubus":
        return Succubus
    elif player == "Succubus Summoned":
        return "DNS"
    elif player == "Succubus Tail":
        return "DNS"
    elif player == "Succubus Horn":
        return "DNS"
    elif player == "Succubus Wing":
        return "DNS"
    
    elif player == "Voidkin":
        return Voidkin


    elif player == "Spirit":
        return Spirit
    elif player == "Tenacity":
        return Tenacity
    elif player == "Dexterity":
        return Dexterity
    elif player == "Awareness":
        return Awareness
    elif player == "Strength":
        return Strength
    elif player == "Intelligence":
        return Intelligence


    else:
        return f"You may have misspelled something, please make sure to capitalize each word. Thank you in advance. Backule 10.1.11.5.0.3.21.12.2.5.18.19.15.14"

def seeprofiles(player):
    profiles = []
    f = open(f"{player}profiles.txt", "r")
    for x in f:

        tempstring = str(x)
        print (tempstring)
        tempstring = tempstring.replace('1 = ', '')
        tempstring = tempstring.replace('0 = ', '')
        tempstring = tempstring.replace('\n', '')
        print (tempstring)

        profiles.append(tempstring)
        print (profiles)
    f.close
    return profiles

def profile(player, profileNames):
    
#    f = open(f"{player}profiles.txt", "w")
#    f.write(f"")
#    f.close
    f = open(f"{player}profiles.txt", "a")
    f.write(f"1 = {profileNames}\n")
    f.close

    profiles = []
    f = open(f"{player}profiles.txt", "r")
    for x in f:
        profiles.append(x)
    
    print (profiles)
    return profiles

def profilechoice(player, profileNames):


    profiles = []
    f = open(f"{player}profiles.txt", 'r')
    for x in f:

        profiles.append(x)
        print (profiles)
    f.close
    f = open(f"{player}profiles.txt", 'w')
    for x in f:
        x = f"0 = {profiles[x]}"

    
    for x in f:
        if f"0 = {profileNames}" == f"0 = {profiles[x]}":
            x = f"1 = {profiles[x]}"
            
    for x in f:
        if x[0] == "1":
            profilechoice = f"{profiles[x]}"
            print (profilechoice)
        
def activeprofile(player):

    f = open(f"{player}profiles.txt" , "r")
    active = f.readlines()
    f.close
    for x in active:
        #print(x)
        if x[0] == "1":
            #print(x)
            x = x.replace("1 = ", "")
            x = x.replace("\n", "")
            return (x)

def skills(skillname):

    match skillname: 
        case "Acrobatics":
            file_line = 0
        case "Athletics":
            file_line = 1    
        case "Empathy":
            file_line = 2
        case "Forgery":
            file_line = 3
        case "Fortitude":
            file_line = 4
        case "Hide":
            file_line = 5
        case "Medical":
            file_line = 6
        case "Notice":
            file_line = 7
        case "Performance":
            file_line = 8
        case "RecallInformation":
            file_line = 9
        case "Silvertongue":
            file_line = 10
        case "Subtlety":
            file_line = 11
        case "Wilderness":
            file_line = 12
        case "Willpower":
            file_line = 13
        case "Relationship":
            file_line = 14
        case "Nemesis":
            file_line = 15
        case "Organization":
            file_line = 16
        case "AnimatedCompanion":
            file_line = 17
        case "AnimalHandler":
            file_line = 18
        case "BeastHandler":
            file_line = 19
        case "WeaponProficiency":
            file_line = 20
        case "Brawling":
            file_line = 21
        case "ArmorProficiency":
            file_line = 22
        case "Runestone":
            file_line = 23
        case "Vehicles":
            file_line = 24
        case "CombatVehicles":
            file_line = 25
        case "Crafting":
            file_line = 26
        case "Hacking":
            file_line = 27
        case _:
            file_line = "Notaskill"

    return file_line

def miningDice():


    counterOne = 0
    result = 0
    arrayOne = []
    while counterOne != int(1):
        counterOne += 1
        DiceA = random.randint(1,10)
        DiceB = random.randint(1,10)
        round(DiceA)
        round(DiceB)
        arrayOne.append(DiceA)
        result += DiceA+DiceB
        print (f"{DiceA} + {DiceB}")
        return result
    
def miningFloors(FloorDC): #This is gonna be a minute

    Layer = myround(FloorDC)

    match int(Layer):
            case 5:
                layername = "Top layer down to layer"
                Mineral = Omnidice(1, 12)
                match Mineral:
                    case 1|2|3|4|5|6:
                        return "Coal"
                    case 7|8:
                        return "Tin"
                    case 9|10:
                        return "Nickel"
                    case 11|12:
                        return "Copper"

            case 10:
                layername = "First Layer"
                Mineral = Omnidice(1, 20)            
                match Mineral:
                    case 1|2|3|4|5|6|7:
                        return "Coal"
                    case 8|9|10:
                        return "Tin"
                    case 11|12|13:
                        return "Nickel"
                    case 14|15|16|17|18:
                        return "Iron"
                    case 19: 
                        return "Aluminum"
                    case 20:
                        return "Magnesium"

            case 15:
                layername = "Upper Caves"
                Mineral = Omnidice(1, 32)            
                match Mineral:
                    case 1|2|3|4|5|6|7|8:
                        return "Coal"
                    case 9|10|11|12:
                        return "Tin"
                    case 13|14|15|16:
                        return "Nickel"
                    case 17|18|19|20:
                        return "Iron"
                    case 21|22|23|24: 
                        return "Aluminum"
                    case 25|26|27:
                        return "Magnesium"
                    case 28:
                        return "Copper"
                    case 29:
                        return "Corundum"
                    case 30:
                        return "Lead"
                    case 31:
                        return "Jaunstite"
                    case 32:
                        return "Zinc"

            case 20:
                layername = "Mid Caves"
                Mineral = Omnidice(1, 51)            
                match Mineral:
                    case 1|2|3|4|5|6|7|8|9:
                        return "Coal"
                    case 10|11|12|13|14:
                        return "Tin"
                    case 15|16|17|18|19:
                        return "Nickel"
                    case 20|21|22|23|24|25:
                        return "Iron"
                    case 26|27|28|29|30:
                        return "Aluminum"
                    case 31|32|33|34|35:
                        return "Magnesium"
                    case 36|37:
                        return "Copper"
                    case 38|39:
                        return "Corundum"
                    case 40|41:
                        return "Lead"
                    case 42|43:
                        return "Jaunstite"
                    case 44|45:
                        return "Zinc"
                    case 46|47:
                        return "Silver"
                    case 48:
                        return "Tungsten"
                    case 49:
                        return "Silicon"
                    case 50:
                        return "Malachite"
                    case 51:
                        return "Yellorite"

            case 25:
                layername = "Low Caves"
                Mineral = Omnidice(1, 73)            
                match Mineral:
                    case 1|2|3|4|5|6|7|8|9|10:
                        return "Coal"
                    case 11|12|13|14|15|16:
                        return "Tin"
                    case 17|18|19|20|21|22:
                        return "Nickel"
                    case 23|24|26|27|28|29:
                        return "Iron"
                    case 30|31|32|33|34|35|36:
                        return "Aluminum"
                    case 37|38|39|40|41|42|43:
                        return "Magnesium"
                    case 44|45|46:
                        return "Copper"
                    case 47|48|49:
                        return "Corundum"
                    case 50|51|52:
                        return "Lead"
                    case 53|54|55:
                        return "Jaunstite"
                    case 56|57|58:
                        return "Zinc"
                    case 59|60|61:
                        return "Silver"
                    case 62|63|64:
                        return "Tungsten"
                    case 65|66:
                        return "Silicon"
                    case 67|68:
                        return "Malachite"
                    case 69|70:
                        return "Yellorite"
                    case 71:
                        return "Gems"
                    case 72:
                        return "Dwarven"
                    case 73:
                        return "Ebony"

            case 30:
                layername = "Upper Caverns"
                Mineral = Omnidice(1, 99)            
                match Mineral:
                    case 1|2|3|4|5|6|7|8|9|10|11:
                        return "Coal"
                    case 12|13|14|15|16|17|18:
                        return "Tin"
                    case 19|20|21|22|23|24|25:
                        return "Nickel"
                    case 26|27|28|29|30|31|32|33:
                        return "Iron"
                    case 34|35|36|37|38|39|40|41|42:
                        return "Aluminum"
                    case 43|44|45|46|47|48|49|50|51:
                        return "Magnesium"
                    case 52|53|54|55:
                        return "Copper"
                    case 56|57|58|59:
                        return "Corundum"
                    case 60|61|62|63:
                        return "Lead"
                    case 64|65|66|67:
                        return "Jaunstite"
                    case 68|69|70|71:
                        return "Zinc"
                    case 72|73|74|75:
                        return "Silver"
                    case 76|77|78|79|80:
                        return "Tungsten"
                    case 81|82|83:
                        return "Silicon"
                    case 84|85|86:
                        return "Malachite"
                    case 87|88|89:
                        return "Yellorite"
                    case 90|91:
                        return "Gems"
                    case 92|93:
                        return "Dwarven"
                    case 94|95:
                        return "Ebony"
                    case 96:
                        return "Cobalt"
                    case 97:
                        return "Orichalcum"
                    case 98:
                        return "Gold"
                    case 99:
                        return "Titanium"

            case 35:
                layername = "Mid Caverns"
                Mineral = Omnidice(1, 127)            
                match Mineral:
                    case 1|2|3|4|5|6|7|8|9|10|11|12:
                        return "Coal"
                    case 13|14|15|16|17|18|19|20:
                        return "Tin"
                    case 21|22|23|24|25|26|27|28:
                        return "Nickel"
                    case 29|30|31|32|33|34|35|36|37|38:
                        return "Iron"
                    case 39|40|41|42|43|44|45|46|47|48:
                        return "Aluminum"
                    case 49|50|51|52|53|54|55|56|57|58|59:
                        return "Magnesium"
                    case 60|61|62|63|64:
                        return "Copper"
                    case 65|66|67|68|69:
                        return "Corundum"
                    case 70|71|72|73|74:
                        return "Lead"
                    case 75|76|77|78|79:
                        return "Jaunstite"
                    case 80|81|82|83|84:
                        return "Zinc"
                    case 85|86|87|88|89|90:
                        return "Silver"
                    case 91|92|93|94|95|96:
                        return "Tungsten"
                    case 97|98|99|100:
                        return "Silicon"
                    case 101|102|103|104:
                        return "Malachite"
                    case 105|106|107|108:
                        return "Yellorite"
                    case 109|110|111:
                        return "Gems"
                    case 112|113|114:
                        return "Dwarven"
                    case 115|116|117:
                        return "Ebony"
                    case 118|119:
                        return "Cobalt"
                    case 120|121:
                        return "Orichalcum"
                    case 122|123:
                        return "Gold"
                    case 124|125:
                        return "Titanium"
                    case 126:
                        return "Platinum"
                    case 127:
                        return "Adamantium"

            case 40:
                layername = "Low Caverns"
                Mineral = Omnidice(1, 143)            
                match Mineral:
                    case 1|2|3|4|5|6|7|8|9|10|11:
                        return "Coal"
                    case 12|13|14|15|16|17|18:
                        return "Tin"
                    case 19|20|21|22|23|24|25:
                        return "Nickel"
                    case 26|27|28|29|30|31|32|33|34:
                        return "Iron"
                    case 35|36|37|38|39|40|41|42|43:
                        return "Aluminum"
                    case 44|45|46|47|48|49|50|51|52|53|54|55:
                        return "Magnesium"
                    case 56|57|58|59|60|61:
                        return "Copper"
                    case 62|63|64|65|66|67:
                        return "Corundum"
                    case 68|69|70|71|72|73:
                        return "Lead"
                    case 74|75|76|77|78|79:
                        return "Jaunstite"
                    case 80|81|82|83|84|85:
                        return "Zinc"
                    case 86|87|88|89|90|91|92|93:
                        return "Silver"
                    case 94|95|96|97|98|99|100:
                        return "Tungsten"
                    case 101|102|103|104|105:
                        return "Silicon"
                    case 106|107|108|109|110:
                        return "Malachite"
                    case 111|112|113|114|115:
                        return "Yellorite"
                    case 116|117|118|119:
                        return "Gems"
                    case 120|121|122|123:
                        return "Dwarven"
                    case 124|125|126|127:
                        return "Ebony"
                    case 128|129|130:
                        return "Cobalt"
                    case 131|132|133:
                        return "Orichalcum"
                    case 135|136:
                        return "Gold"
                    case 137|138|139:
                        return "Titanium"
                    case 140|141:
                        return "Platinum"
                    case 142|143:
                        return "Adamantium"

            case 45:
                layername = "Deepest Cavern"
                Mineral = Omnidice(1, 143)            
                match Mineral:
                    case 1|2|3|4|5|6|7|8|9|10:
                        return "Coal"
                    case 11|12|13|14|15|16:
                        return "Tin"
                    case 17|18|19|20|21|22:
                        return "Nickel"
                    case 23|24|25|26|27|28|29:
                        return "Iron"
                    case 30|31|32|33|34|35|36:
                        return "Aluminum"
                    case 37|38|39|40|41|42|43|44|45:
                        return "Magnesium"
                    case 46|47|48|49|50:
                        return "Copper"
                    case 51|52|53|54|55:
                        return "Corundum"
                    case 56|57|58|59|60:
                        return "Lead"
                    case 61|62|63|64|65:
                        return "Jaunstite"
                    case 66|67|68|69|70:
                        return "Zinc"
                    case 71|72|73|74|75|76|77|78|79:
                        return "Silver"
                    case 80|81|82|83|84|85|86|87|88:
                        return "Tungsten"
                    case 89|90|91|92|93|94:
                        return "Silicon"
                    case 95|96|97|98|99|100:
                        return "Malachite"
                    case 101|102|103|104|105|106:
                        return "Yellorite"
                    case 107|108|109|110|111:
                        return "Gems"
                    case 112|113|114|115|116:
                        return "Dwarven"
                    case 117|118|119|120|121:
                        return "Ebony"
                    case 122|123|124|125:
                        return "Cobalt"
                    case 126|127|128|129:
                        return "Orichalcum"
                    case 130|131|132|133:
                        return "Gold"
                    case 134|135|136|137:
                        return "Titanium"
                    case 138|139|140:
                        return "Platinum"
                    case 141|142|143:
                        return "Adamantium"

            case 50:
                layername = "Deep"
                Mineral = Omnidice(1, 133)            
                match Mineral:
                    case 1|2|3|4|5:
                        return "Coal"
                    case 6|7|8|9|10|11:
                        return "Sulfur"
                    case 12|13|14:
                        return "Tin"
                    case 15|16|17|18|19:
                        return "Nickel"
                    case 20|21|22|23|24|25:
                        return "Iron"
                    case 26|27|28|29|30:
                        return "Aluminum"
                    case 31|32|33|34|35|36|37:
                        return "Magnesium"
                    case 38|39|40|41:
                        return "Copper"
                    case 42|43|44|45:
                        return "Corundum"
                    case 46|47|48|49:
                        return "Lead"
                    case 50|51|52|53:
                        return "Jaunstite"
                    case 54|55|56|57:
                        return "Zinc"
                    case 58|59|60|61|62|63|64|65:
                        return "Silver"
                    case 66|67|68|69|70|71|72:
                        return "Tungsten"
                    case 73|74|75|76|77:
                        return "Silicon"
                    case 78|79|81|82:
                        return "Malachite"
                    case 83|84|85|86|87:
                        return "Yellorite"
                    case 88|89|90|91|92|93:
                        return "Gems"
                    case 94|95|96|97|98|99:
                        return "Dwarven"
                    case 100|101|102|103|104|105:
                        return "Ebony"
                    case 106|107|108|109|110:
                        return "Cobalt"
                    case 111|112|113|114|115:
                       return "Orichalcum"
                    case 116|117|118|119|120:
                        return "Gold"
                    case 121|122|123|124|125:
                        return "Titanium"
                    case 126|127|128|129:
                        return "Platinum"
                    case 130|131|132|133:
                        return "Adamantium"

            case 55:
                layername = "Deeper"
                Mineral = Omnidice(1, 117)            
                match Mineral:
                    case 1|2|3|4:
                        return "Coal"
                    case 5|6|7|8|9:
                        return "Sulfur"
                    case 10|11|12:
                        return "Tin"
                    case 13|14|15|16:
                        return "Nickel"
                    case 17|18|19:
                        return "Iron"
                    case 20|21|22|23|24:
                        return "Aluminum"
                    case 25|26|27|28|29:
                        return "Magnesium"
                    case 30|31|32:
                        return "Copper"
                    case 33|34|35:
                        return "Corundum"
                    case 36|37|38:
                        return "Lead"
                    case 39|40|41:
                        return "Jaunstite"
                    case 42|43|44:
                        return "Zinc"
                    case 45|46|47|48|49|50:
                        return "Silver"
                    case 51|52|53|54|55|56:
                        return "Tungsten"
                    case 57|58|59|60:
                        return "Silicon"
                    case 61|62|63|64:
                        return "Malachite"
                    case 65|66|67|68:
                        return "Yellorite"
                    case 69|70|71|72|73:
                        return "Gems"
                    case 74|75|76|77|78:
                        return "Dwarven"
                    case 79|80|81|82|83:
                        return "Ebony"
                    case 84|85|86|87|88|89:
                        return "Cobalt"
                    case 90|91|92|93|94|95:
                        return "Orichalcum"
                    case 96|97|98|99|100|101:
                        return "Gold"
                    case 102|103|104|105|106|107:
                        return "Titanium"
                    case 108|109|110|111|112:
                        return "Platinum"
                    case 113|114|115|116|117:
                        return "Adamantium"

            case 60:
                layername = "Deepest"
                Mineral = Omnidice(1, 113)            
                match Mineral:
                    case 1|2|3:
                        return "Coal"
                    case 4|5|6|7|8|9:
                        return "Sulfer"
                    case 10|11:
                        return "Tin"
                    case 12|13:
                        return "Nickel"
                    case 14|15|16:
                        return "Iron"
                    case 17|18|19|20|21|22:
                        return "Aluminum"
                    case 23|24|25|26|27|28|29:
                        return "Magnesium"
                    case 30|31|32|33|34|35:
                        return "Copper"
                    case 36|37|38|39:
                        return "Corundum"
                    case 40|41|42|43:
                        return "Lead"
                    case 44|45|46|47:
                        return "Jaunstite"
                    case 48|49|50|51:
                        return "Zinc"
                    case 52|53|54|55|56:
                        return "Silver"
                    case 57|58|59|60:
                        return "Tungsten"
                    case 61|62|63:
                        return "Silicon"
                    case 64|65|66:
                        return "Malachite"
                    case 67|68|69:
                        return "Yellorite"
                    case 70|71|72|73:
                        return "Gems"
                    case 74|75|76|77:
                        return "Dwarven"
                    case 78|79|80|81:
                        return "Ebony"
                    case 82|83|84|85|86:
                        return "Cobalt"
                    case 87|88|89|90|91:
                        return "Orichalcum"
                    case 92|93|94|95|96:
                        return "Gold"
                    case 97|98|99|100|101:
                        return "Titanium"
                    case 102|103|104|105|106|107:
                        return "Platinum"
                    case 108|109|110|111|112|113:
                        return "Adamantium"

            case 65:
                layername = "Deepester"
                Mineral = Omnidice(1, 107)            
                match int(Mineral):
                    case 1|2:
                        return "Coal"
                    case 3|4:
                        return "Sulfur"
                    case 5|6:
                        return "Iron"
                    case 7|8:
                        return "Aluminum"
                    case 9|10|11|12|13:
                        return "Magnesium"
                    case 14|15|16:
                        return "Copper"
                    case 17|18|19:
                        return "Corundum"
                    case 20|21|22:
                        return "Lead"
                    case 23|24|25:
                        return "Jaunstite"
                    case 26|27|28:
                        return "Zinc"
                    case 29|30|31|32|33|34:
                        return "Silver"
                    case 35|36|37|38|39|40:
                        return "Tungsten"
                    case 41|42|43|44:
                        return "Silicon"
                    case 45|46|47|48:
                        return "Malachite"
                    case 49|50|51|52:
                        return "Yellorite"
                    case 53|54|55|56|57:
                        return "Gems"
                    case 58|59|60|61|62:
                        return "Dwarven"
                    case 63|64|65|66|67:
                        return "Ebony"
                    case 68|69|70|71|72|73:
                        return "Cobalt"
                    case 74|75|76|77|78|79:
                        return "Orichalcum"
                    case 80|81|82|83|84|85:
                        return "Gold"
                    case 86|87|88|89|90|91:
                        return"Titanium"
                    case 92|93|94|95|96|97|98|99:
                        return "Platinum"
                    case 100|101|102|103|104|105|106|107:
                        return "Adamantium"
            
            case 70:
                Mineral = Omnidice(1,3)
                match int(Mineral):
                    case 1|2|3:
                        return "test"
                #1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34
                #35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61
                #62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85
                #86|87|88|89|90|91|92|93|94|95|96|97|98|99|100|101|102|103|104|105
                #106|107|108|109|110|111|112|113|114|115|116|117|118|119|120|121|122|123
#592 lines later I was right it was gonna be a minute
def myround(x, base=5):
    return base * round((int(x)+5)/base)

def stats(filename):

    character = activeprofile(filename)

    f = open(f"{filename}{character}Sheet.txt", "r")
    
    lines = f.readlines()

    # intZero = lines[0]
    # intOne = lines[1]
    # intTwo = lines[2]
    # intThree = lines[3]
    # intFour = lines[4]
    # intFive = lines[5]

    # spi = intZero[0]
    # ten = intOne[0]
    # dex = intTwo[0]
    # awr = intThree[0]
    # str = intFour[0]
    # itg = intFive[0]

    intZero = lines[19]
    intOne = lines[20]
    intTwo = lines[21]
    intThree = lines[22]
    intFour = lines[23]
    intFive = lines[24]

    spi = intZero[0]
    ten = intOne[0]
    dex = intTwo[0]
    awr = intThree[0]
    str = intFour[0]
    itg = intFive[0]

    statarray = [spi, ten, dex, awr, str, itg]
    f.close()
    return statarray
   
def Omnidice(x, y):


    counterOne = 0
    result = 0
    arrayOne = []
    while counterOne != int(x):
        counterOne += 1
        DiceA = random.randint(1,int(y))
        round(DiceA)
        arrayOne.append(DiceA)
        result += DiceA
    
    return result
     
bot.run(Bot_Token)

























############# DEAD ZONE FOR DEAD CODES THAT IM TOO AFRAID TO DELETE IN CASE I NEED THEM###############


                                        #CURRENTLY WORKING ON THIS SECTION############## \/ \/ \/
                                        #CURRENTLY WORKING ON THIS SECTION############## /\ /\ /\













                                            # if str(message.content) == "Dux":
                                            #     Hanswer = "Dux"
                                            #     await ctx.send(f"{Dux}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "Potens":
                                            #     Hanswer = "Potens"
                                            #     await ctx.send(f"{Potens}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "Custos":
                                            #     Hanswer = "Custos"
                                            #     await ctx.send(f"{Custos}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "Elysium":
                                            #     Hanswer = "Elysium"
                                            #     await ctx.send(f"{Elysium}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "Libertas":
                                            #     Hanswer = "Libertas"
                                            #     await ctx.send(f"{Libertas}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "Vettrheim":
                                            #     Hanswer = "Vettrheim"
                                            #     await ctx.send(f"{Vettrheim}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "Anima Lands":
                                            #     Hanswer = "Anima Lands"
                                            #     await ctx.send(f"{AnimaLands}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "Dark Lands":
                                            #     Hanswer = "Dark Lands"
                                            #     await ctx.send(f"{DarkLands}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "Wild":
                                            #     Hanswer = "Wild"
                                            #     await ctx.send(f"{Wild}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "The Dark Continent":
                                            #     Hanswer = "The Dark Continent"
                                            #     await ctx.send(f"{TheDarkContinent}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "Military Heritage":
                                            #     Hanswer = "Military Heritage"
                                            #     await ctx.send(f"{MilitaryHeritage}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            # if str(message.content) == "Sealed":
                                            #     Hanswer = "Sealed"
                                            #     await ctx.send(f"{Sealed}\n\nAre you sure this is the Heritage you want? Y/N")
                                            #     print(Hanswer)
                                            
                                            
                                            # if str(message.content) == "Y":
                                            #     f = open(f"{ctx.author}{characterName}Sheet.txt", "a")
                                            #     f.write(f"Heritage: {Hanswer}\n")
                                            #     f.close
                                            #     await ctx.send(f"You have chosen {Hanswer} as your heritage.")
                                            #     await ctx.send("Please Choose your first background feat")













        #             if 0 == 0:
        #                 Human = """**[Human]:**\nDespite lacking natural advantages, humans have proven their tenacity and spirit throughout history,
        # establishing the four Countries to protect the world from the relentless threat of the Void-Taken. Their  ability to unite and 
        # support each other through 'Strength in Numbers' sets them apart as resilient and strategic fighters.\n**+1 Spirit**\n**+1 Tenacity**
        # **+2 Character Creation Points**\n**+5 Starting XP**\n\n**Strength in Numbers:** Humans have the unique ability to buff themselves and allies 
        # in combat Increasing attack to hit, defence chance, and damage by +1 up to a max of 4 for each creature within 5 zones. The creature 
        # Max goes up by 1 per B Rank. 1B, 2B, 3B, 4B.
        # **Activation:** 1 use per mission
        # **Group Activation:** Stacks with other 'Strength in Numbers'
        # **Duration and Aftermath:** Lasts 6 Rounds, once the 6 rounds are over character is at disadvantage for 10 rounds."""                
        #                 BeastKin1 = """[Beastkin]\nWith their Dark vision, Beastkin can confidently navigate dark environments without hindrance. Additionally,
        # their chosen Beaskin trait and Primal Instinct grant them distinct advantages in various situations, making them formidable adventurers and 
        # valuable members of any party
        # \nDark Vision: Cannot be inflicted with the 'Obstructed' Status Condition when in dark or low-light conditions.
        # **Primal Instinct:** Beastkin tap into their primal instincts, gaining a boost ot their physical-based rolls. This includes attacking with weapons 
        # or hands, dodging attacks, resisting damage, performing athletic feats, and moving stealthily. +1 per B rank. 1B, 2B, 3B, 4B.
        # **Activation:** 1 use per mission
        # **Duration and Aftermath:** Lasts 6 Rounds, once the 6 rounds are over character is at disadvantage for 10 rounds.
        # Beastkin Trait: Each Beastkin can choose one of the following
        # **Tail:** +1 Awareness, +1 Intelligence, [Choose One] 1. Use tail to hold items 2. use tail to climb without needing to roll
        # **Beast Ears:** +2 Dexterity, hearing rolls ADV, Ignore Sneak Attack Debuff so long as you are within hearing range, +2 Notice Ranks
        # **Beast Eyes:** +2 Awareness, Sight rolls ADV, Sight range Doubled, Immune to Obstructed Status, [Choose] +1 Athletics Rank, +2 Notice Rank.
        # **Camouflage:** +1 Dexterity, +1 Tenacity, as a Free action, you can give yourself the Hidden status for rounds equal to Tenacity
        # **Claws:** +1 Awareness, +1 Strength, You have 2x claws[Natural Weapon, Light, Edged] that deal a 1d6+Strength DMG, +1 Brawling skill, claws can activate Bleeding for 1 round
        # """
        #                 BeastKin2 = """**Wings:** +2 Dexterity, Immune to 'Lame' status and dont suffer drawbacks from leg injury, can move Vertically, ya know... FLY
        # **Exoskeleton/Thick Hide/Scales:** +1 Strength, +1 Tenacity, Gain armor that increases strength based on rank, Rank 4: Light Rank 3: Medium Rank 2: Heavy Rank 1: SuperHeavy can regain half missing AD for 1 SP.
        # **Gills:** +2 Tenacity, Water Breathing, take half Cold damage, cant become winded due to swimming
        # **Hooves:** +1 Strength, +1 Tenacity, +1 Brawling Rank for Hooves[Natural, Light, Blunt] Deal 1d6+Strength Damage DMG, can cause Winded status with Hooves for 1 Round
        # **Horns:** +2 Strength, +2 to Shove/Trip/Grab Actions, [Choose One] 1. +2 Performance Ranks 2. +1 Athletics Rank
        # **Predator:** +1 Awareness, +1 Tenacity, +1 Speed
        # **Fangs/Stinger:** +1 Strength, +1 Tenacity, Fangs or Stinger[Natural, Precise or Edged] that deal a 1d6+strength, [Choose one] 1. Precise 2 Edged, can give poisoned status up to Tenacity times per week
        # **Dragon Breath:** +1 Dexterity, +1 Tenacity, Flame Breath[Natural, Precise] Deal 1d6+Dexterity, can cause on Fire Status to target for 6 rounds taking half attacks Damage. can activate times equal to Tenacity per week
        # **Spider Webs:** +1 Dexterity, +1 Tenacity, can shoot and grapple up to 2 targets at a time. can be used to climb using Athletics+Strength, can create a sticky zone equal to tenacity per week. zone has 5+Tenacity HP and takes entire turn to pass through, msut use fire/cutting to destroy
        # **Drop Tail:** +1 Tenacity, +1 Dexterity, can negate an injury by losing your tail until it regrows in a week.
        # **Bioluminescence:** +1 Awareness, +1 Dexterity, create a light spanning a 2 Zone radius for minutes equal to Tenacity per week.
        # **Sonar:** +1 Awareness, +1 Tenacity, [Choose One] 1.Sonar Sense(Immune to Blindness) 2. Sonar Blast [Natural, Blunt] deals 1d6+Tenacity DMG, can do equal to Tenacity times a week
        # **Must Format as Beastkin (Trait)**
        # """
        #                 #Note Give beastkin their background info
        #                 AnimaEnhanced = """**[AnimaEnhanced]**\nAnima enhanced look like either a human or beastkin including cosmetic features but benefit from neither race.
        # instead their eyes match their anima color. Once known as the chosen, Anima Enhanced now have a deep connection to the magical energies of the world.
        # their 'Hero Mode' ability allows them to become formidable adversaries against the forces of darkness, but it comes with risks and consequences.
        # \n**Hero Mode:** Gain a +2 to rolls against Void-taken and Creatures of darkness including damage. Gain +1 per B rank 1B, 2B, 3B, 4B
        # **Activation:** this ability can be activated Once per mission
        # **Duration and aftermath:** 'Hero Mode' Lasts for 6 rounds, afterwards they are at disadvantage for 10 rounds
        # +3 Spirit
        # +10 Anima max of 20 at Character Creation
        # +1 Willpower Rank"""
        #                 Synthetic = """**[Synthetic]**\nAs a synthetic, you possess a remarkable blend of humanoid appearance and advanced mechanical capabilities. Your ability to blend 
        # in with other races and your arsenal of built-in equipment make you a formidable force in the world.
        # [Choose One] **[Synthetic Genius]** +2 Intelligence **[Synthetic Versatile]** +1 to any 2 attributes
        # **no need for food**
        # **advantage to blend in with Humans or Beastkin**
        # **Natural Light armor:** 4 AD against Cutting Damage you take. if you reduce damage to 0 you do not lose any AD. Can spend 1 SP to regain all expended AD from this armor
        # **Can have modifications or weapons built into your body equal to your tenacity.** you do not suffer the weight increase effect on built in equipment."""            
        #                 Elf = """**[Elves]**\nA once-thriving race, Elves have endured hardship due to the malevolent sorceress Eclipse. Sealed away by her dark magic, they're marked 
        # by their graceful presence and heightened senses, including double the visual range, Elves can choose different paths, such as the noble Royal Descendants, 
        # Martially skilled High Born, or nature-connected Low Born. in combat, they can unleash the 'Magic Cloak' to harness elemental power.
        # \nHeritage Predetermined: Sealed for heritage
        # Magic Cloak: During combat choose an Elemental damage type. gain 2DR against that damage type and deal 1d6+spirit to enemies in your zone. +1 DR and +2 sides on DMG Dice per B rank
        # 1B, 2B, 3B, 4B. start->1d6->1d8->1d10->1d12->1d14
        # +1 Spirit
        # +1 Dexterity
        # 2x vision distance
        # [Choose One] [Elf Royal]: +1 Runestone skill [Elf High Born]: +1 Weapon pro Skill [Elf Low Born]: +1 Wilderness Rank"""
        #                 Orc = """**[Orc]**\nOrcs, a resilient race, faced Eclipse's wrath but emerged with unwavering strength. Their powerful bodies recieve a permanent boost in Senacity 
        # and Strength, while innate dark vision grants them the ability to navigate darkness effortlessly. ORcs follow paths as Magic Born with runic powers or Battle Born as foprmidable Warriros.
        # They can tap into 'Berserking' during combat, enhancing their combat prowess. 
        # Orcs typically have dark skin tones: Black,Brown, Charcoal or yellow color in rare cases.
        # [Berserking] Orcs can activate 'Berserking' during combat, +2DR and +1 to all combat based checks. these each go up by +1 for every B rank. This lasts 6 rounds, afterwards gain the 'Winded' status efect for 6 rounds
        # **+1 Tenacity**
        # **+1 Strength**
        # **Dark Vision:** can't be inflicted with the 'Obstructed status condition when in dark or low-light conditions.
        # **[Choose One] [Orc Magic Born]:** +1 Runestone Skill  **[Orc Battle Born]** +1 Weapon Pro Rank"""
        #                 Dwarf = """**[Dwarves]**\nknown for their craftsmanship, Dwarves struggled against Eclypse's curse. their sturdy bodies are fortified with a permanent increase in strength. 
        # Dwarves often tread the path of a skilled Warriro Class or a masterful Smtih class, crafting goods from ores. Their unique ability,'Smith's Eye' allows them to blend metals when crafting equipment, 
        # combining their strengths to create formidable gear.
        # **Smith's Eye(Passive)**: when crafting a piece of equipment, instead of aonly being able to forge it out of 1 metal to gain a bonus, instead upon a 50/50 split you can add 2 bonus's from metals
        # **+2 Strength**
        # **[Choose One] [Dwarf Warrior]:** +1 Weapon pro rank **[Dwarf Smith]:** +1 crafting rank.
        # """
        #                 Demon = """**[Demon/Succubus]**\n Demons and Succubi are enigmatic beings, torn from their own shadowy realms by sorcerers' incantations. Their essence is stepped in darkness and allure, 
        # Hailing from a world shrouded in Mysteries beyond moratl comprehension. Sealed away by the malevolent sorceress Eclipse, their history and true nature were conceald from the world, erased from memory until 
        # only recently. In the past, They were often mistaken as mere magical summons of eclipse. Unlike the other races Demons and Succubi were forced into servitude as foot soldiers for Eclipse. Some resisted her control, 
        # their loyalty forged in the fires of rebellion, while others found a perverse pride in serving under her dark banner. Their existence remains an unsettling reminder of Eclipse's reing and the hidden realms from which they
        # were forcibly drawn. unlike the other races, this race appears nearly Human except for markings around their body and a noticeable snake like eyes.
        # **Magic Eye(Passive):** When casting Spells or cantrips. the DC required to cast them is lowered by 2. this increases every B rank. 1B, 2B, 3B, 4B
        # **+2 Spirit**
        # **Dark vision:** Demons/Succubus possess innate dark vision, whihc means they cannot be inflicted with the 'Obstructed' Status Condition when in dark or low light conditions.
        # [Choose One] **Demon Summoned:** +1 Runestone skill, **Demon Natural Born:** +1 notice rank, and can take the Tail, Horn, Or Wing traits from Beastkin."""
        #                 Succubus = """**[Demon/Succubus]**\n Demons and Succubi are enigmatic beings, torn from their own shadowy realms by sorcerers' incantations. Their essence is stepped in darkness and allure, 
        # Hailing from a world shrouded in Mysteries beyond moratl comprehension. Sealed away by the malevolent sorceress Eclipse, their history and true nature were conceald from the world, erased from memory until 
        # only recently. In the past, They were often mistaken as mere magical summons of eclipse. Unlike the other races Demons and Succubi were forced into servitude as foot soldiers for Eclipse. Some resisted her control, 
        # their loyalty forged in the fires of rebellion, while others found a perverse pride in serving under her dark banner. Their existence remains an unsettling reminder of Eclipse's reing and the hidden realms from which they
        # were forcibly drawn. unlike the other races, this race appears nearly Human except for markings around their body and a noticeable snake like eyes.
        # **Magic Eye(Passive):** When casting Spells or cantrips. the DC required to cast them is lowered by 2. this increases every B rank. 1B, 2B, 3B, 4B
        # **+2 Spirit**
        # **Dark vision:** Demons/Succubus possess innate dark vision, whihc means they cannot be inflicted with the 'Obstructed' Status Condition when in dark or low light conditions.
        # [Choose One] **Succubus Summoned:** +1 Runestone skill, **Succubus Natural Born:** +1 notice rank, and can take the Tail, Horn, Or Wing traits from Beastkin."""
        #                 Voidkin = """**[Voidkin]**\nA race of monster that come from negative energies in the World. They possess a blend of humanoid and animal traits. Each Voidkin takes on a Human-like 
        # appearance with a single prominent animal trait. One of their most remarkable abilities is their night vision, granting them an advantage in low light conditions.
        # However, their presence in history has not been long nor challenges. From a rapid evolution from their mindless states they've adopted a society that believes in strength. Now with 
        # a entire continent to themselves and the ability to integrate into human society. a voidkin looks like any other person but they have grey skintones. 
        # Their eyes have a dark color They may pick any one Beastkin trait or Voidkin trait. [See beastkin for their traits and return]
        # Traits include: Voidkin Tail, Voidkin Ears, Voidkin Eyes, Voidkin Camouflage, Voidkin Claws, Voidkin Wings, Voidkin Exoskeleton/Thick Hide/ Scales, Voidkin Gills, Voidkin Hooves, Voidkin Horns, Voidkin Predator, 
        # Voidkin Fangs/Stinger(if fangs (edged), if stinger (Precise)), Voidkin Dragon Breath, Voidkin Spider Webs, Voidkin Drop Tail, Voidkin Bioluminescence, Voidkin Sonar Sense, Voidkin Sonar Blast.
        # Dark Vision: cannot be inflicted with the 'Obstructed' Status Condition due to being in the dark.
        # [Choose One]
        # **Any Beastkin Trait:**
        # **Voidkin Despair:** +1 Spirit, as an action attack with your natural weapon, deal damage normally as well as cause the 'Horrified' status condition. cna only use this 1 time per week
        # **Voidkin Possession:** +1 Spirit, as an action you make a ability roll with your voidkin race ability. if the roll beats the DC determined by the DM you take control over said object. you can only use this once per week
        # **Voidkin Power:** +1 Strength, you start with Rank 1 Terrain Domain. The terrain is pre-selected for Darklands. this takes upa  domain slot. You have the ability to do this without SP cost equal to Spirit times per week"""                   




# @bot.command(name = 'testinfo')
# async def createcharacter(ctx):
#         if ctx.author == bot.user:
#             return
#         channelID = f"{ctx.channel.id}: channel ID"
#         channel = f"{ctx.channel}: channel"
#         authorID = f"{ctx.author.id}: author ID"
#         author = f"{ctx.author}: author"
#         ctxuser = f"{ctx}: ctx"
#         ctxUserName = f"{ctx.author}: ctx user"
#         ctxUserNameID = f"{ctx.author.id}: ctx user ID"
#         await ctx.send(f"INFO: \n{channelID}\n{channel}\n{authorID}\n{author}\n{ctxuser}\n{ctxUserName}\n{ctxUserNameID}")