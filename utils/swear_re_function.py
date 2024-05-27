import re


def transformation_word(word: str) -> str:
    d = {'а' : ['а', 'a', 'á', 'à', 'â', 'ä', 'ã', 'å', 'ā', 'ă', 'ą', 'ǎ', 'ª', '@'],
        'б' : ['б', '6', 'b'],
        'в' : ['в', 'b', 'v'],
        'г' : ['г', 'r', 'g', 'ґ'],
        'д' : ['д', 'd', 'g'],
        'е' : ['е', 'e', 'ё', 'є', 'ė', 'ę', 'ē', 'ë', 'è', 'é', 'ê', 'ě', 'ĕ', 'э'],
        'ё' : ['ё', 'e'],
        'ж' : ['ж', 'zh', '*'],
        'з' : ['з', '3', 'z'],
        'и' : ['и', 'u', 'i'],
        'й' : ['й', 'u', 'i'],
        'к' : ['к', 'k', 'i{', '|{'],
        'л' : ['л', 'l', 'ji'],
        'м' : ['м', 'm'],
        'н' : ['н', 'h', 'n'],
        'о' : ['о', 'o', 'ó', 'ò', 'ô', 'ö', 'õ', 'ø', 'ō', 'ŏ', 'ő', 'ǒ', 'œ', '0', '0'],
        'п' : ['п', 'n', 'p'],
        'р' : ['р', 'r', 'p'],
        'с' : ['c', 'с', 'ć', 'č', 'ç', 'ĉ', 'ċ', 's', '§'],
        'т' : ['т', 'm', 't'],
        'у' : ['у', 'y', 'u', 'у́'],
        'ф' : ['ф', 'f'],
        'х' : ['х', 'x', 'h' , '}{'],
        'ц' : ['ц', 'c', 'u,'],
        'ч' : ['ч', 'ch'],
        'ш' : ['ш', 'sh'],
        'щ' : ['щ', 'sch'],
        'ь' : ['ь', 'b'],
        'ы' : ['ы', 'bi'],
        'ъ' : ['ъ'],
        'э' : ['э', 'e'],
        'ю' : ['ю', 'io'],
        'я' : ['я', 'ya']
    }

    for key, value in d.items():
        for letter in value:
            for w in word:
                if letter == w:
                    word = word.replace(w, key)
    return word

def is_obscene(word: str) -> bool:
    word = transformation_word(word)

    obscene_pattern = r'(?iu)(?<![а-яёeě])(?:(?:(?:у|[нз]а|(?:хитро|не)?вз?[ыьъ]|с[ьъ]|(?:и|ра)[зс]ъ?|(?:о[тб]|п[оа]д)[ьъ]?|(?:\S(?=[а-яёeě]))+?[оаeеěи-])-?)?(?:[еeё](?:б(?!о[рй]|рач)|п[уа](?:ц|тс))|и[пб][ае][тцд][ьъ]).*?|(?:(?:н[иеа]|ра[зс]|[зд]?[ао](?:т|дн[оа])?|с(?:м[еи])?|а[пб]ч)-?)?хуе(?!дин).*?|бл(?:[эя]|еа?)(?:[дт][ьъ]?)?|\S*?(?:п(?:[иеё]зд|ид[аое]?р|ед(?:р(?!о)|[аое]р|ик)|охую)|бля(?:[дбц]|тс)|[ое]ху[яйиеё]|хуйн).*?|(?:о[тб]?|про|на|вы)?м(?:анд(?:[ауеыи](?:л(?:и[сзщ])?[ауеиы])?|ой|[ао]в.*?|юк(?:ов|[ауи])?|е[нт]ь|ища)|уд(?:[яаиое].+?|е?н(?:[ьюия]|ей))|[ао]л[ао]ф[ьъ](?:[яиюе]|[еёо]й))|елд[ауые].*?|ля[тд]ь|(?:[нз]а|по)х)(?![а-яёěe])|(\bзалуп[ао]?[чк]?[аие]?[сьть]?|залупина\b)'

    # Patterns for the first set:
    # pattern1 = r'[уyоoаa](?=[еёeєэхx])'
    # pattern2 = r'[вvbсc](?=[хпбмгжxpmgj])'
    # pattern3 = r'[вvbсc][ъь](?=[еёeєэ])'
    # pattern4 = r'ё(?=[бb6])'

    # Patterns for the second set:
    # pattern5 = r'[вvb][ыi]'
    # pattern6 = r'[зz3][аa]'
    # pattern7 = r'[нnh][аaеeиi]'
    # pattern8 = r'[вvb][сc](?=[хпбмгжxpmgj])'
    # pattern9 = r'[оo][тtбb6](?=[хпбмгжxpmgj])'
    # pattern10 = r'[оo][тtбb6][ъь](?=[еёe])'
    # pattern11 = r'[иiвvb][зz3](?=[хпбмгжxpmgj])'
    # pattern12 = r'[иiвvb][зz3][ъь](?=[еёe])'
    # pattern13 = r'[иi][сc](?=[хпбмгжxpmgj])'
    # pattern14 = r'[пpдdg][оo](?>[бb6](?=[хпбмгжxpmgj])|[бb6][ъь](?=[еёe])|[зz3][аa])?'

    # Patterns for the thirty set:
    # pattern15 = r'[пp][рr][оoиi]'
    # pattern16 = r'[зz3][лl][оo]'
    # pattern17 = r'[нnh][аa][дdg](?=[хпбмгжxpmgj])'
    # pattern18 = r'[нnh][аa][дdg][ъь](?=[еёe])'
    # pattern19 = r'[пp][оoаa][дdg](?=[хпбмгжxpmgj])'
    # pattern20 = r'[пp][оoаa][дdg][ъь](?=[еёe])'
    # pattern21 = r'[рr][аa][зz3сc](?=[хпбмгжxpmgj])'
    # pattern22 = r'[рr][аa][зz3сc][ъь](?=[еёe])'
    # pattern23 = r'[вvb][оo][зz3сc](?=[хпбмгжxpmgj])'
    # pattern24 = r'[вvb][оo][зz3сc][ъь](?=[еёe])'

    # Patterns for the fourth set:
    # pattern25 = r'[нnh][еe][дdg][оo]'
    # pattern26 = r'[пp][еe][рr][еe]'
    # pattern27 = r'[oо][дdg][нnh][оo]'
    # pattern28 = r'[кk][oо][нnh][оo]'
    pattern29 = r'(?!mydas)[мm][уy][дdg][oоaа]'
    # pattern30 = r'[oо][сc][тt][оo]'
    # pattern31 = r'[дdg][уy][рpr][оoаa]'
    pattern32 = r'\b[ш][ао][б][ао][л][д][уаіиыое]'

    # Patterns for the fifth set:
    pattern33 = r'\b[ш][а][л][а][в][уаіиыоeэ]'
    pattern34 = r'\b[гgґ][аa@о0][нn][дd][оo0][нn]'
    pattern35 = r'\b[бb][лl][яa][хx][аa]'
    pattern36 = r'\b[еёeě][bб6][а@a][tт]'
    pattern37 = r'\b[еeєě][бbpп][тt][oоаaeěеуyыиi]'
    pattern38 = r'\bйо[бb6][аa]'
    pattern39 = r'(?!(?:hue|hueso|Hueso|Хуедин|Hyundai))\b[hхx][уyu][ийiеeёяюju]'

    # Patterns for the sixth set:
    pattern40 = r'\b[гg][оo][вvb][нnh][оoаaуy]'
    pattern41 = r'\b[f][uа][cсk][кk]'
    pattern41_1 = r'\b[fa][uа][cсk][кk]'
    pattern41_2 = r'\b[fa][uа][cсk]'
    pattern42 = r'\b[лl][о0o][хhx]'
    pattern43 = r'\b[^р][scс][yуu][kк][aаiи]'
    pattern44 = r'\b[cссs][уyуu][ч4ч][кk]'
    pattern45 = r'\b[хx][еee][рpr]([нnh](я|ya)|)'
    pattern46 = r'\b[зz3][аa][лl][уy][пp][аa]'

    pattern47 = r'(?<![eеєёэе])[еєёэєэе]б(?=[уyиi]|[^уyиiоoaаеeeэєёуыиоoaа]|[еєeэєэeеэё]|[_ebo][kt]|[^ллооааыиия]|[нn][уy]|[кk][аa]|[сc][тt])'
    pattern48 = r'\bсу[кч](?:[аи]?(?:[н])?)?[аоуеиы]?'
    pattern49 = r'\b[жz][o0о][pп][aаyěуыу́iеeoо]'
    pattern49_1 = r'\bzh[o0о][pп][aаyуěыiеу́eoо]'

    # patterns = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7, pattern8, pattern9,
    #             pattern10, pattern11, pattern12, pattern13, pattern14, pattern15, pattern16, pattern17,
    #             pattern18, pattern19, pattern20, pattern21, pattern22, pattern23, pattern24, pattern25,
    #             pattern26, pattern27, pattern28, pattern29, pattern30, pattern31, pattern32, pattern33,
    #             pattern34, pattern35, pattern36, pattern37, pattern38, pattern39, pattern40, pattern41, pattern41_1, pattern41_2,
    #             pattern42, pattern43, pattern44, pattern45, pattern46, pattern47, pattern48, pattern49, pattern49_1]
    patterns = [pattern29, pattern32, pattern33, pattern34, pattern35, pattern36, pattern37, pattern38, pattern39, pattern40, pattern41, pattern41_1, pattern41_2,
                pattern42, pattern43, pattern44, pattern45, pattern46, pattern48, pattern49, pattern49_1]

    print("check swear word:", word)
    if re.search(obscene_pattern, word, re.IGNORECASE):
        return True
    else:
        for pattern in patterns:
            matches = re.findall(pattern, word, re.IGNORECASE)
            if matches:
                # print("matches: ", matches)
                print(pattern)
                return True
            
        return False