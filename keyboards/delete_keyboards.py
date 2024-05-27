from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def pagination(words: list, keyboard_id: str, mode: str, current_page :int = 1) -> InlineKeyboardMarkup:
    buttons = []
    page_size = 5
    total_pages = (len(words) + page_size - 1) // page_size

    start_index = (current_page - 1) * page_size
    end_index = min(start_index + page_size, len(words))
    for i in range(start_index, end_index):
        word_button = InlineKeyboardButton(text=words[i], callback_data=f"#{i}#{keyboard_id}#{mode}")   # word[i]
        buttons.append([word_button])
       
    bottom_buttons = []

    if current_page > 1:
        bottom_buttons.append(InlineKeyboardButton(text=f'⬅️', callback_data=f'prev_page#{keyboard_id}#{mode}'))
    else:
        bottom_buttons.append(InlineKeyboardButton(text=f'⛔️', callback_data=f'stop&page_number{keyboard_id}'))

    bottom_buttons.append(
        InlineKeyboardButton(text=f'{current_page}/{total_pages}', callback_data=f'stop&page_number{keyboard_id}'))

    if current_page == total_pages:
        bottom_buttons.append(InlineKeyboardButton(text=f'⛔️', callback_data=f'stop&page_number{keyboard_id}'))
    else:
        bottom_buttons.append(InlineKeyboardButton(text=f'➡️', callback_data=f'next_page#{keyboard_id}#{mode}'))

    buttons.append(bottom_buttons)
    buttons.append([InlineKeyboardButton(text=f'Завершити', callback_data=f'finish')])
    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=buttons)

    return keyboard 