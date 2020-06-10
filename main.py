import sys

invalid_input = True
invalid_inputCHOICE = True
invalid_inputCHOICE2 = True


def debut():
    print("Discord Python Bot Editor V.1.1 created by ALEXDIEU !")
    print("Please choose an option : ")
    print("1.create a new bot")
    print("2.edit a bot(soon)")
    print("3.exit")


def pick_one():
    global f
    global ID
    invalid_input = False
    ID = input('Before all , can you tell me your profil ID(NOT THE BOT!) please ?\n')
    namefile = input("okay , what should be the main file bot title ? \n")
    PREFIX = input("Before starting , what should be the bot prefix ? \n")
    token = input('What is the bot token ? \n')
    start = f'import discord\nfrom io import BytesIO\nfrom discord.ext import commands\nimport asyncio\nimport aiohttp\nfrom discord.ext.commands import Bot\nimport os\nimport platform\nfrom platform import python_version\n\n\nbot = commands.Bot(command_prefix=\'{PREFIX}\')\nOWNER = [{ID}]\nBLACKLIST = []\nTOKEN = \'{token}\''
    with open(namefile + ".py", 'w') as f:
        f.write('{}'.format(start))
        print('Bot succesfully created ! Now let\'s do the starting events !')
        startEvent()
        choice2()

def startEvent():
    global f
    invalid_inputCHOICE = False
    personnal = input('Now , would you like to print a personnal message when the bot is ready ?(That will print it in your python console , it\'s recommended you keep the default(say no to keep the default) wich is : \nregistred as (bot name)\nDiscord.py version = (version)\nPython Version (version) \nRunning on (OS)\nSo ?  ')
    if personnal == 'yes':
        print('The bot name is metionned at the end of your message !')
        OnreadyMsgP = input(f'Please enter your new message wich the bot will display in the console when it is ready (if you want to write this caracter : \' please do \ then \' thanks (if not your bot will not working  thanks !) :')
        OnreadyMsg = (f'\n\n@bot.event\nasync def on_ready():\n    print(\'{OnreadyMsgP}\'+ bot.user.name )\n    print(\'Created by DISCORDBOTMAKER(by alexdieu)\')\n')
        f.write('{}'.format(OnreadyMsg))
        choice2()
    if personnal == 'no':
        print('On ready message set as default !')
        OnreadyMsg = ('\n\n@bot.event\nasync def on_ready():\n    print(\'Registred as \' + bot.user.name)\n    print(\'Created by DISCORDBOTMAKER(by alexdieu)\')\n    print(\"API version of discord.py :\"), discord.__version__\n    print(\"Python version :\", platform.python_version())\n    print(\"Running on :\", platform.system(), platform.release(), \"(\" + os.name + \")\")\n    print(\'-------------------\')')
        f.write('{}'.format(OnreadyMsg))
        choice2()
    else:
        print('Please answer by yes or no !')
        invalid_inputCHOICE = False
        startEvent()



def start() :
    debut()

    in_pick = input("Your choice : ")

    if in_pick == '1':
       pick_one()
    else:
        print('Answer by yes or no please !')

    if in_pick == '2':
        print("soon , if you want it now , come help us on my github !")

    if in_pick == '3':
        print('Created by Alexdieu')
        time.sleep(1)
        invalid_input = False
        debut()
    else:
        print('This Option doesn\'t exist (may be yet) sorry')

def choice2():
    global f
    invalid_inputCHOICE2 = False
    choice1 = input('Now what do you want see next ? events , commands ,plugins(soon!) or exit ?(commands written by community or Alexdieu(Credits of the plugin at the end)\nPLEASE ANSWER by the choices proposed : events , commands ,exit(finish the file and compile it) or plugins(integred functiinalities or Precommands) !\nYour answer :')
    if choice1 == 'events':
        print('events')
        choiceEV = input('What event do you want ?\n1.On member join \n2.On reaction add\n3.On member leave\nChoice :')
        if choiceEV == '1':
            onmemberjoin()


    if choice1 == 'commands':
        commands()

    if choice1 == 'plugins' :
        print('plugins(soon!)')
        choice2()
    if choice1 == ('exit'):
        print('credits: Alexdieu . Maybe Others with the time ;)')
        END = '\n\nbot.run(TOKEN)'
        f.write('{}'.format(END))
        f.close()
        start()
    else:
        print('PLEASE ANSWER by the choices proposed : events , commands , exit or plugins !')
        invalid_inputCHOICE2 = True
        choice2()

def commands():
    print('availaibles commands categorys :')
    print('1.personalised commands')
    print('2.moderations commands')
    print('3.Back')
    print('For community commands , it\'s in plugins !')
    commands_choice = input('Your choice : ')

    if commands_choice == '1':
        perso_com()


def perso_com():
    global f
    print('personnalised commands !')
    print('Options :')
    print('1.Create a personnalised answer to a personnal command for the bot !')
    print('2.Create an Embed(SOON)!')
    print('3.Back')
    CHOICEPERSO = input('Okay , what do you want to do ? \n')

def onmemberjoin():
    global f
    print('event on member join choosed !')
    print('Did the bot say your message in DM or in the same channel as the person send the message ?(To answer , \nPlease say 1 for DM , \n2.In a specific channel(need the channel ID), \n3.DM and specific channel\n4.back )')
    answer2 = input('Your choice : ')
    if answer2 == '1':
        DMsg = input('\n Use Tutorial : \nTo type \' do \\\' \nYou have to write or copy/paste :\n{ID} to mention member who just joined\n{SERVERNAME} to mention the server !\nAnd **To write in bold** or \ and \' to write \' !\nWhat should be the DM message ?\n')
        DMNEW = (f'\n@client.event\nasync def on_member_join(member):\n    ID = f\'<@{{member.id}}>\'\n    SERVERNAME = member.guild.name\'\n    await member.create_dm()\n    await member.dm_channel.send(f\'{DMsg}\')')
        f.write('{}'.format(DMNEW))
        print('succes')
        choice2()
    if answer2 == '2':
        print('Specific channel')
        CHANNELID = input('What is the welcome channel ID ?\n')
        MMSSGG = input('What is the welcome message ?\nTo type \' do \\\' \nTo mention user , please copy/paste {ID} in your message, and to mention server it\'s {SERVERNAME} \n')
        SpecificCHAN = (f'\n@bot.event\nasync def on_member_join(member):\n    print(f\'{{member.id}}, {{member}}Join the server!\')\n    ID = \'<@{{member.id}}>\'\n    SERVERNAME = member.guild.name\n    channel = bot.get_channel(date[\'{CHANNELID}\'])\n    await channel.send(f\'{MMSSGG}\')')
        f.write('{}'.format(SpecificCHAN))
        print('succes')
        choice2()
    if answer2 == '3':
        print('You requested DM + Specific channel')
        CHANELID1 = input('What is the channel ID ?\n')
        CHANNELMSG = input('What is the welcome message ?\nTo type \' do \\\' \nTo mention user , please copy/paste {ID} in your message, and to mention server it\'s {SERVERNAME} \n')
        DNEWM = input('What will be your welcome Dm message ?\nTo type \' do \\\' \nTo mention user , please copy/paste {ID} in your message, and to mention server it\'s {SERVERNAME}\n')
        ALLINONE = (f'\n@client.event\nasync def on_member_join(member):\n    ID = f\'<@{{member.id}}>\'\n    SERVERNAME = member.guild.name\'\n    await member.create_dm()\n    await member.dm_channel.send(f\'{DNEWM}\')\n    channel = bot.get_channel(date[\'{CHANELID1}\'])\n    await channel.send(f\'{CHANNELMSG}\')')
        f.write('{}'.format(ALLINONE))
        print('succes')
        choice2()
    if answer2 == '4':
        choice2()
    else:
        print('Please choose 1 , 2 ,3 or 4 !')
        onmemberjoin()



while invalid_input :
    start()

