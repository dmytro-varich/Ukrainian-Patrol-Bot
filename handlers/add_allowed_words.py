from asyncio import sleep

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject

from filters.chat_type import ChatTypeFilter
from handlers.language_filter import lemmatize_word
from utils.file_operations import append_words_to_file
from databases.database import set_last_active_keyboard_id
from databases.words_storage import add_allowed_words
from config.config import OWNER_ID, FILE_PATH
from main import bot
from keyboards.add_global_keyboard import add_global_pagination
from texts.general_messages import *


# Global variable 
word_list_confirm = []
word_list_from_chat = []


# Initialization Router
add_allowed_words_router: Router = Router()


@add_allowed_words_router.message(
    ChatTypeFilter(chat_type=["private"]),
    Command(commands=["addwords"]),
)
async def cmd_add_allowed_words_in_private(message: Message, command: CommandObject):
    await message.answer("👥 Цю команду можна використовувати лише в групі.")


@add_allowed_words_router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]),
    Command(commands=["addwords"]),
)
async def cmd_add_allowed_words_in_group(message: Message, command: CommandObject):
    global word_list_from_chat
    chat_id = message.chat.id
    if command.args is None:
        await message.reply(msg_addwords_incorrect_1.format("addwords"))
        return
    
    try:
        await set_last_active_keyboard_id(chat_id=chat_id)
        words = command.args.split(",")
        words = [word.strip() for word in words if word != '']
        # print(words)
        for word in words:
            if ' ' in word:
                await message.reply(msg_addwords_incorrect_2.format("addwords"))
                return 
    except ValueError:
        await message.reply(msg_addwords_incorrect_2.format("addwords"))
        return      

    await add_allowed_words(chat_id, await lemmatize_word(words)) 
    word_list_from_chat = words
    keyboard = await add_global_pagination(words=word_list_from_chat)  
    await bot.send_message(chat_id=OWNER_ID, text=msg_addwords_to_confirm_for_own_1.format(message.chat.title), 
                           reply_markup=keyboard) # Owner confirm
    await message.reply(msg_addwords_main_text.format(message.chat.title, ', '.join(words)))


@add_allowed_words_router.message(
    ChatTypeFilter(chat_type=["private"]),
    Command(commands=["addglobalwords"]),
)
async def cmd_add_allowed_for_owner(message: Message, command: CommandObject):
    if OWNER_ID == message.from_user.id:
        if command.args is None:
            await message.answer(msg_addwords_incorrect_1.format("addglobalwords"))
            return
        try:
            words = command.args.split(",")
            words = [word.strip() for word in words if word != '']
        except ValueError:
            await message.answer(msg_addwords_incorrect_2.format("addglobalwords"))
            return 

        append_words_to_file(words, FILE_PATH)
        await message.answer(msg_addwords_to_confirm_for_own_2.format(', '.join(words)))


@add_allowed_words_router.callback_query(F.data.startswith(('global#')))
async def select_global_word_btn(call: CallbackQuery): 
    global word_list_confirm
    word = call.data.split("global#")[1]
    await call.answer(f"{word}")
     
    buttons = call.message.reply_markup.inline_keyboard
    for row in buttons:
        for button in row:
            if button.text == word or button.text.startswith('✅ ' + word) or button.text.startswith('❌ ' + word):
                if word not in word_list_confirm: 
                    button.text = '✅ ' + word
                    word_list_confirm.append(word)
                else: 
                    button.text = word
                    word_list_confirm.remove(word)
                break
    
    await call.message.edit_reply_markup(reply_markup=call.message.reply_markup)


@add_allowed_words_router.callback_query(F.data.startswith(('global_next_page', 'global_prev_page')))
async def select_global_pages_btn(call: CallbackQuery): 
    global word_list_from_chat
    action = call.data
    current_page = int(call.message.reply_markup.inline_keyboard[-2][1].text.split('/')[0])
    
    if action == 'global_prev_page':
        current_page -= 1
    elif action == 'global_next_page':
        current_page += 1
    new_keyboard = await add_global_pagination(words=word_list_from_chat, current_page=current_page)
    await call.message.edit_reply_markup(reply_markup=new_keyboard)


@add_allowed_words_router.callback_query(F.data == "global_finish")
async def select_finish_btn(call: CallbackQuery):
    global word_list_confirm, word_list_from_chat
    append_words_to_file(word_list_confirm, FILE_PATH)
    await call.answer("Зроблено!")
    await sleep(3)
    await call.message.edit_text(msg_addwords_to_confirm_for_own_2.format(", ".join(word_list_confirm)))
    word_list_confirm = []
    word_list_from_chat = []
    # new_keyboard = await finish_global_keyboard()
    # await call.message.edit_reply_markup(reply_markup=new_keyboard)


@add_allowed_words_router.callback_query(F.data == "global_stop")
async def select_stop_btn(call: CallbackQuery):
    await call.answer(text="Сюди не можна")