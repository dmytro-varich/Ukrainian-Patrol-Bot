from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from filters.chat_type import ChatTypeFilter
from databases.database import update_filter_state, check_filter_state
from texts.service_messages import swear_control_text_begin, swear_control_text_end

swear_words_router: Router = Router()


@swear_words_router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]),
    Command(commands=["swearcontrol"]),
)
async def swear_words_cmd(message: Message) -> None:
    chat_id = message.chat.id
    if not await check_filter_state(chat_id, "swear_state_control"):
        await message.answer(swear_control_text_begin)
        await update_filter_state(chat_id, True, "swear_state_control")
    else: 
        await message.answer(swear_control_text_end)
        await update_filter_state(chat_id, False, "swear_state_control")