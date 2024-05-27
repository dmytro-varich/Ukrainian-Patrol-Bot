from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats, BotCommandScopeAllChatAdministrators
from aiogram.methods.set_my_commands import SetMyCommands


async def set_commands(bot):
    await bot(SetMyCommands(commands=[
        BotCommand(command="start", description="запустити"),
        BotCommand(command="help", description="інструкція"),
    ], scope=BotCommandScopeAllPrivateChats()))

    # await bot(SetMyCommands(commands=[
    #     # BotCommand(command="help", description="інструкція"),
    # ], scope=BotCommandScopeAllGroupChats()))
    
    await bot(SetMyCommands(commands=[
        BotCommand(command="start", description="запустити"),
        BotCommand(command="stop", description="зупинити"),
        BotCommand(command="addwords", description="додати слова"),
        BotCommand(command="deletewords", description="видалити слова"),
        BotCommand(command="swearcontrol", description="фільтрувати лайливі слова")
    ], scope=BotCommandScopeAllChatAdministrators()))