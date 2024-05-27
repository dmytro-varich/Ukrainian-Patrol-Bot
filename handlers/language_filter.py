from aiogram import Router, F
from aiogram.types import Message

from databases.database import check_filter_state
from databases.words_storage import get_allowed_words
from utils.file_operations import load_homographs_list
from config.config import FILE_PATH, API_KEY
from texts.general_messages import msg_language_filter, swear_control_text_main
from filters.chat_type import ChatTypeFilter
from utils.nlp_technologies import translate_to_ukrainian, tokenization, lemmatize_word, \
detect_language, single_detection, text_no_punct_func, homografs_control_pattern
from utils.swear_re_function import is_obscene


lang_router: Router = Router()


async def language_filter(message: Message, chat_id: int):
    msg = message.text
    print(msg)

    text = tokenization(msg)
    print(text)
    print("TEST", translate_to_ukrainian(text))

    try: 
        sngl_det_lang = single_detection(text, api_key=API_KEY)
    except:
        sngl_det_lang = text

    print("TEST", sngl_det_lang)

    word_ru_msg = list()
    word_trans_ua_msg = list()
    flag_ru_word = False

    # 1 methods: 
    if sngl_det_lang == 'ru':
        language_pairs = await detect_language(text)
        for word, lang, sngle_lng in language_pairs:
            if lang == 'ru' and word.lower() != translate_to_ukrainian(word.lower()) or sngle_lng == 'ru' and word.lower() != translate_to_ukrainian(word.lower()) or await lemmatize_word(word.lower()) != translate_to_ukrainian(await lemmatize_word(word.lower())):
                if word.lower() not in load_homographs_list(FILE_PATH) \
                and word.lower() not in await get_allowed_words(chat_id):
                    if not homografs_control_pattern(word.lower()):
                        flag_ru_word = True
                        
                        word_ru_msg.append(word)
                        word_trans_ua_msg.append(translate_to_ukrainian(word))             

    if flag_ru_word:
        await message.reply(msg_language_filter.format(', '.join(word_ru_msg), ', '.join(word_trans_ua_msg)))


@lang_router.message(F.text, ChatTypeFilter(chat_type=["group", "supergroup"]))
async def language_detect_filter(message: Message):
    chat_id = message.chat.id
    if await check_filter_state(chat_id, "swear_state_control"):
        text = message.text
        text_no_punct = text_no_punct_func(text)
        words = text_no_punct.split() 
        swear_words_list = list()
        flag = False
        for word in words:
            # print(word)
            if is_obscene(word.lower()):
                swear_words_list.append(word)
                flag = True
        
        # print(flag)
        # print("Check swear word: ", swear_words_list)  
        if flag:
            await message.reply(swear_control_text_main.format(', '.join(swear_words_list)))
            flag = False
        elif await check_filter_state(chat_id, "filter_states"):
            await language_filter(message, chat_id)
    elif await check_filter_state(chat_id, "filter_states"):
        await language_filter(message, chat_id)