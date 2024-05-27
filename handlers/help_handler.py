from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from texts.service_messages import help_message
from filters.chat_type import ChatTypeFilter


help_router: Router = Router()


@help_router.message(
    ChatTypeFilter(chat_type=["private"]),
    Command('help'),
)
async def command_help_handler(message: Message, state: FSMContext) -> None:
    await message.answer(text=help_message)


@help_router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]),
    Command('help')
)
async def command_help_handler(message: Message) -> None:
    await message.reply(help_message)


@help_router.callback_query(F.data == 'help')
async def help_slct_btn(call: CallbackQuery, state: FSMContext) -> None:
    help_builder_in_private = InlineKeyboardBuilder()
    back_btn = InlineKeyboardButton(text="🔙 Назад", callback_data='back_to_start')
    help_builder_in_private.row(back_btn)
    await call.message.edit_text(text=help_message, reply_markup=help_builder_in_private.as_markup())