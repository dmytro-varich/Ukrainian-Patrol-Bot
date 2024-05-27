from aiogram import Router, Bot
from aiogram.filters import IS_MEMBER, IS_NOT_MEMBER, ChatMemberUpdatedFilter
from aiogram.types import ChatMemberUpdated

from texts.service_messages import new_members_message


new_member_router: Router = Router()


@new_member_router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def new_member(event: ChatMemberUpdated, bot: Bot):
    if event.new_chat_member.user.username :
        await event.answer(new_members_message.format('@' + event.new_chat_member.user.username))
    else:
        await event.answer(new_members_message.format(event.new_chat_member.user.first_name))