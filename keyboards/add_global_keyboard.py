from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def add_global_pagination(words: list, current_page :int = 1) -> InlineKeyboardMarkup:
    buttons = []
    page_size = 5
    total_pages = (len(words) + page_size - 1) // page_size

    start_index = (current_page - 1) * page_size
    end_index = min(start_index + page_size, len(words))
    for i in range(start_index, end_index):
        word_button = InlineKeyboardButton(text=words[i], callback_data=f"global#{words[i]}")
        buttons.append([word_button])
       
    bottom_buttons = []

    if current_page > 1:
        bottom_buttons.append(InlineKeyboardButton(text=f'⬅️', callback_data=f'global_prev_page'))
    else:
        bottom_buttons.append(InlineKeyboardButton(text=f'⛔️', callback_data=f'global_stop'))

    bottom_buttons.append(
        InlineKeyboardButton(text=f'{current_page}/{total_pages}', callback_data=f'global_stop'))

    if current_page == total_pages:
        bottom_buttons.append(InlineKeyboardButton(text=f'⛔️', callback_data=f'global_stop'))
    else:
        bottom_buttons.append(InlineKeyboardButton(text=f'➡️', callback_data=f'global_next_page'))

    buttons.append(bottom_buttons)

    buttons.append([InlineKeyboardButton(text=f'Закончить', callback_data=f'global_finish')])

    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=buttons)

    return keyboard 