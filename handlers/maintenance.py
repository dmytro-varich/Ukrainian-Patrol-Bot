from aiogram import Router, F
from aiogram.filters import MagicData, Command
from aiogram.types import Message, CallbackQuery

# from filters.chat_type import ChatTypeFilter
# from keyboards.maintenance_keyboard import maintenance_keyboard
# from config.config import OWNER_ID, maintenance_mode
from texts.service_messages import maintenance_message

# update_maintenance_router: Router = Router()


# @update_maintenance_router.message(
#     ChatTypeFilter(chat_type=["private"]),
#     Command(commands=["maintenance"]),
# )
# async def maintenance_cmd_for_owner(message: Message):
#     global maintenance_mode
#     if message.from_user.id == OWNER_ID:
#         if not maintenance_mode:
#             keyboard = await maintenance_keyboard()
#         else: 
#             keyboard = await maintenance_keyboard(switch_text="Выключить")
#         await message.answer("Выберите, если хотите идти на тех обслуживание", 
#                              reply_markup=keyboard)


# @update_maintenance_router.callback_query(F.data.startswith('switch'))
# async def maintenance_querry_button(call: CallbackQuery):
#     global maintenance_mode
#     if not maintenance_mode:
        
#         maintenance_mode = True
#         new_maintenance_kb = await maintenance_keyboard(switch_text="Выключить")
#         await call.message.edit_reply_markup(reply_markup=new_maintenance_kb)
#         await call.answer("Техническая служба включена", show_alert=True)
#     else: 
#         maintenance_mode = False
#         new_maintenance_kb = await maintenance_keyboard(switch_text="Включить")
#         await call.message.edit_reply_markup(reply_markup=new_maintenance_kb)
#         await call.answer("Техническая служба отключена", show_alert=True)
    

#---------------------------------------------------------------------------------------------
maintenance_router: Router = Router()
maintenance_router.message.filter(MagicData(F.maintenance_mode.is_(True)))
maintenance_router.callback_query.filter(MagicData(F.maintenance_mode.is_(True)))


@maintenance_router.message(
    Command(commands=["start", "help", "stop", "addwords", "deletewords"]),
)
async def any_message(message: Message):
    await message.answer(maintenance_message)


@maintenance_router.callback_query()
async def any_callback(call: CallbackQuery):
    await call.answer(
        text=maintenance_message[:-3],
        show_alert=True
    )