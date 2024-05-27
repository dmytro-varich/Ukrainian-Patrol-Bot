from asyncio import sleep

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ChatMemberAdministrator
from aiogram.filters import Command

from config.config import OWNER_ID, FILE_PATH
from filters.chat_type import ChatTypeFilter
from databases.database import set_last_active_keyboard_id, get_last_active_keyboard_id
from databases.words_storage import get_allowed_words, delete_allowed_words
from keyboards.delete_keyboards import pagination
from utils.file_operations import load_homographs_list, remove_words_to_file
from texts.general_messages import *


delete_allowed_words_router: Router = Router()


@delete_allowed_words_router.message(
    ChatTypeFilter(chat_type=["private"]),
    Command(commands=["deletewords"]),
)
async def cmd_delete_allowed_words_in_private(message: Message):
    await message.answer("👥 Цю команду можна використовувати лише в групі.")


# Owner Command
@delete_allowed_words_router.message(
        ChatTypeFilter(chat_type=["private"]),
        Command(commands=["deleteglobalwords"]),
)
async def cmd_delete_global_words_in_private(message: Message):
    user_id = message.from_user.id
    if user_id == OWNER_ID:
        allowed_words = load_homographs_list(FILE_PATH)
        if len(allowed_words) != 0:
            keyboard_id = f'{user_id} {message.date}'
            keyboard = await pagination(words=allowed_words, keyboard_id=keyboard_id, mode="owner_to_remove")
            await message.answer(msg_delete_for_owner, 
                                reply_markup=keyboard)
            await set_last_active_keyboard_id(chat_id=user_id, last_active_keyboard_id=keyboard_id)
        else: 
            await message.answer(msg_delete_add_word_again)


@delete_allowed_words_router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]),
    Command(commands=["deletewords"]),
)
async def cmd_delete_allowed_words_in_group(message: Message):
    chat_id = message.chat.id
    allowed_words = await get_allowed_words(chat_id)
    # print(allowed_words)
    if len(allowed_words) != 0:
        keyboard_id = f'{chat_id} {message.date}'
        keyboard = await pagination(words=allowed_words, keyboard_id=keyboard_id, mode="other")
        await message.answer(msg_delete_main_text.format(message.chat.title), 
                             reply_markup=keyboard)
        await set_last_active_keyboard_id(chat_id=chat_id, last_active_keyboard_id=keyboard_id)
    else: 
        await message.answer(msg_delete_add_word_again)


@delete_allowed_words_router.callback_query(F.data.startswith(('#')))
async def select_words_buttons(call: CallbackQuery): 
    chat_id = call.message.chat.id
    from main import bot
    user_status = await bot.get_chat_member(chat_id=chat_id, user_id=call.message.from_user.id)

    if isinstance(user_status, ChatMemberAdministrator) or chat_id == OWNER_ID:
        data = call.data.split('#')
        i, keyboard_id, mode = data[1], data[2], data[3]
        
        # print("word", word, type(word))
        if keyboard_id == await get_last_active_keyboard_id(chat_id=chat_id):
            if mode == "other":
                words = await get_allowed_words(chat_id)
                word = words[int(i)]
                await delete_allowed_words(chat_id, word)
                await call.answer(text=f"Видалено!")
                allowed_words = await get_allowed_words(chat_id)
            elif mode == "owner_to_remove":
                words = load_homographs_list(FILE_PATH)
                remove_words_to_file(words[int(i)], FILE_PATH)
                await call.answer(text=f"Видалено!")
                allowed_words = load_homographs_list(FILE_PATH)

            if len(allowed_words) != 0:
                await process_pagination_buttons(call)
            else: 
                await call.message.edit_text(msg_delete_add_word_again)
        else: 
            await call.answer("Список застарів")
    else: 
        await call.answer(text="Ви не адмін")


@delete_allowed_words_router.callback_query(F.data.startswith(('prev_page', 'next_page')))
async def process_pagination_buttons(call: CallbackQuery):
    chat_id=call.message.chat.id
    # print("Callback.data:", call.data)
    data = call.data.split("#")
    data = [x for x in data if x.strip()]
    # print(data)
    action, keyboard_id, mode = data[0], data[1], data[2]
    # print("keyboard", keyboard_id)
    # print("action", action, "mode", mode)
    if keyboard_id == await get_last_active_keyboard_id(chat_id=chat_id):
        if mode == "other":
            allowed_words = await get_allowed_words(chat_id)
        elif mode == "owner_to_remove":
            allowed_words = load_homographs_list(FILE_PATH)

        # print(allowed_words)
        current_page = int(call.message.reply_markup.inline_keyboard[-2][1].text.split('/')[0])
        if action == 'prev_page':
            current_page -= 1
        elif action == 'next_page':
            current_page += 1
        new_keyboard = await pagination(words=allowed_words, keyboard_id=keyboard_id, mode=mode, current_page=current_page)
        await call.message.edit_reply_markup(reply_markup=new_keyboard)
            
    else: 
        await call.answer("Список застарів")


@delete_allowed_words_router.callback_query(F.data.startswith('stop&page_number'))
async def stop_pagination_buttons(call: CallbackQuery):
    chat_id = call.message.chat.id
    keyboard_id = call.data.split("stop&page_number")[1]
    # print(keyboard_id)
    if keyboard_id == await get_last_active_keyboard_id(chat_id=chat_id):
        await call.answer(text="Сюди не можна")
    else: 
        await call.answer("Список застарів")

@delete_allowed_words_router.callback_query(F.data == 'finish')
async def btn_finish_delete_keyboard(call: CallbackQuery):
    await call.answer("Завершити!")
    await sleep(3)
    await call.message.delete()