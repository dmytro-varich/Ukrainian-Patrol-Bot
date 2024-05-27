from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


deeplinks = [
    "tg://resolve?domain=ukrainian_patrol_bot&startgroup=botstart&admin=post_messages+edit_messages+delete_messages+restrict_members+invite_users", 
    "https://t.me/ukrainian_patrol_bot?startgroup&admin=post_messages", 
    "https://t.me/ukrainian_patrol_bot?startgroup=start"
    ]


start_builder_in_private = InlineKeyboardBuilder()
add_to_group = types.InlineKeyboardButton(text="➕ Додати мене в групу", url=deeplinks[0])
support_btn = types.InlineKeyboardButton(text="🔧 Підтримка", callback_data="support")
payment_btn = types.InlineKeyboardButton(text="💳 Донатити", url="https://send.monobank.ua/jar/5UmqUmjrvA")
go_to_channel = types.InlineKeyboardButton(text="📢 Канал", url="https://t.me/varich_channel")
info_btn = types.InlineKeyboardButton(text="ℹ️ Інформація", callback_data="help")

start_builder_in_private.row(add_to_group).row(support_btn, info_btn).row(payment_btn, go_to_channel)


cancel_builder_for_states = InlineKeyboardBuilder()
cancel_builder_for_states.add(
    types.InlineKeyboardButton(
        text="Відмінити", callback_data="cancel"
    )
)