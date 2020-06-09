import sys

invalid_input = True

def start() :
    print("Discord Python Bot Editor V.1 created by ALEXDIEU !")
    print("Please choose an option : ")
    print("1 : create a new bot")
    print("2 : edit a bot (soon)")
    print("3 : exit")

    in_pick = input("Choice :  ")


    if in_pick == '1':
        invalid_input = False
        namefile = input("okay , what should be the main file bot title ? \n")
        PREFIX = input("Before starting , what should be the bot prefix ? \n")
        token = input('What is the bot token ? \n')
        start = f"import discord\nfrom io import BytesIO\nimport maths\nfrom discord.ext import commands\nimport asyncio\nimport aiohttp\nfrom discord.ext.commands import Bot\nimport os\nimport platform\nfrom platform import python_version\n\n\nbot = commands.Bot(command_prefix='{PREFIX}')\nBLACKLIST = []\nTOKEN = '{token}'"
        with open(namefile+".py", 'w') as f:
            f.write('{}'.format(start))
            print('Bot succesfully created ! Now let\'s do the starting events !')
            personnal = input('Now , would you like to print a personnal message when the bot is ready ?(That will print it in your python console , it\'s recommended you keep the default(say no to keep the default) wich is : \nregistred as (bot name)\nDiscord.py version = (version)\nPython Version (version) \nRunning on (OS)\nSo ?  ')
            if personnal == 'yes' :
                print('to mention the bot name add anywhere in your message {BOTNAME}')
                OnreadyMsgP = input('Please enter your new message wich the bot will display in the console when it is ready (if you want to write this carcter : \' please do \ then \' thanks (if not your bot will not working  thanks !) :')
                BOTNAME = client.user.name
                OnreadyMsg = (f'@client.event\nasync def on_ready():\n    client.loop.create_task(status_task())\n    print(\'{OnreadyMsgP}\')\n')
                f.write('{}'.format(OnreadyMsg))
            if personnal == 'no' :
                print('On ready message set as default !')
                OnreadyMsg =  ('@client.event\nasync def on_ready():\n    client.loop.create_task(status_task())\n    print(\'Registred as \' + client.user.name)\n    print(\"API version of discord.py :\", discord.version\n    print(\"Python version :\", platform.python_version())\n    print(\"Running on :\", platform.system(), platform.release(), \"(\" + os.name + \")\")\n    print(\'-------------------\')')
                f.write('{}'.format(OnreadyMsg))
            else:
                print('Answer by yes or no please !')


    if in_pick == '2':
        print("soon , if you want it now , come help us on my github !")

    if in_pick == '3':
        invalid_input = False
        sys.exit()

    else:
        print('This Option doesn\'t exist (may be yet) sorry')

while invalid_input :
    start()
