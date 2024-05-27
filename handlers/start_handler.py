from random import choice

from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from texts.service_messages import *
from filters.chat_type import ChatTypeFilter
from keyboards.start_keyboards import start_builder_in_private, cancel_builder_for_states
from databases.database import update_filter_state, check_filter_state
from states.support_states import SupportStates
from handlers.help_handler import help_router
from config.config import OWNER_ID


start_router: Router = Router()


@start_router.message(
    ChatTypeFilter(chat_type="private"),
    CommandStart(),
)
async def cmd_start_in_private(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(msg_start_in_private.format(message.from_user.first_name), 
                         reply_markup=start_builder_in_private.as_markup())
        
    
@start_router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]),
    CommandStart(),
)
async def cmd_start_in_group(message: Message) -> None:
    chat_id = message.chat.id
    if not await check_filter_state(chat_id, "filter_states"):
        random_gifs = choice(GIFS_START)
        random_caption = choice(PHRASES_START)
        await message.answer_animation(animation=FSInputFile(random_gifs), caption=random_caption)
        await update_filter_state(chat_id, True, "filter_states")
    else:
        await message.reply(msg_start_in_group_2)


@start_router.callback_query(F.data == "cancel")
@help_router.callback_query(F.data == 'back_to_start')
async def cmd_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(msg_start_in_private.format(call.from_user.first_name), 
                         reply_markup=start_builder_in_private.as_markup())


@start_router.callback_query(F.data == "support")
async def select_support_btn(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text=support_text_begin, 
                                 reply_markup=cancel_builder_for_states.as_markup())
    await state.set_state(SupportStates.start_support)


@start_router.message(SupportStates.start_support)
async def user_dialogue_for_support(message: Message, state: FSMContext):
    from main import bot
    user_name = message.from_user.full_name
    user_tag = message.from_user.username
    await message.answer(support_text_confirm)
    await bot.send_message(chat_id=OWNER_ID, 
                           text=f"""<b>🔧Служба підтримки</b>
👤 Користувач {user_name}(@{user_tag}) відправив <i>Вам повідомлення</i>!

📩 <b>Повідомлення:</b> 
{message.text}""")
    await bot.pin_chat_message(chat_id=OWNER_ID, message_id=message.message_id)