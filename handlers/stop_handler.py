from random import choice

from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from texts.service_messages import *
from filters.chat_type import ChatTypeFilter
from databases.database import update_filter_state, check_filter_state


stop_router: Router = Router()

    
@stop_router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]),
    Command(commands=["stop"]),
)
async def cmd_stop_in_group(message: Message) -> None:
    chat_id = message.chat.id
    if await check_filter_state(chat_id, "filter_states"):
        random_gifs = choice(GIFS_STOP)
        random_caption = choice(PHRASES_STOP)
        await message.answer_animation(animation=FSInputFile(random_gifs), caption=random_caption)
        await update_filter_state(chat_id, False, "filter_states")
    else:
        await message.reply(msg_stop_in_group_2)