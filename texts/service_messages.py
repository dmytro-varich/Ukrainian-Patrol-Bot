from utils.count_files_in_directory import count_files_in_directory


'''
    #START 
'''
msg_start_in_private = """👋Привіт, <b>{0}</b>!

🤖 @ukrainian_patrol_bot створений для фільтрації <b>української мови</b> у вашій групі. 

➕ <b>Додайте бота</b> в адміністратори групи, щоб дозволити йому <b>виконувати дії</b>!

❓ Для отримання <b>додаткової інформації</b>, введіть команду /help або натисніть кнопку <code>«ℹ️ Інформація»</code>.
"""

msg_start_in_group_2 = "🔍 Бот вже працює над фільтрацією чату від російської мови."
PHRASES_START = ["""🚨 @ukrainian_patrol_bot почав свій <b>патруль у чаті</b>!

Час розпочинати фільтрацію української мови у вашій групі. Давайте зробимо ваше спілкування ще кращим! 🇺🇦💬""", 
                 """❗️<b>Увага! Увага!</b> @ukrainian_patrol_bot відтепер слідкує за Вами!

👀 Жодне російськомовне слово не пройде повз мене. Будьте уважні, бо я не сам, а разом зі своїми улюбленими адмінами. 🤗🫂""", 
                 """👮🏻‍♂️@ukrainian_patrol_bot розпочав патрулювання чату!

🚓 Він почав свій патруль, щоб переконатися, що <b>правила дотримуються</b>, і захистити нас від зловмисних повідомлень! 🚦"""
                 ] 
GIFS_START = [f"config/gif_start/gif_{n}.mp4" for n in range(count_files_in_directory("config/gif_start"))]


'''
    #HELP 
'''
help_message = """
<b>Ukrainian Patrol Bot</b> — інструмент фільтрації україномовного спілкування в групах, що автоматично блокує російську мову.

<b>Використання</b>
1️⃣ Для початку введіть команду /start в особистих.
 
2️⃣ Потім додайте бота у групу, натиснувши кнопку <code>«➕ Додати мене в групу»</code> та надайте йому права адміністратора, щоб він міг фільтрувати повідомлення. 

3️⃣ Щоб увімкнути фільтрацію, введіть команду /start, а щоб вимкнути - /stop. 

4️⃣ Якщо ви хочете додати слова, які не хочете, щоб бот їх блокував, додайте їх до списку за допомогою команди /addwords <code>слово#1</code>, <code>слово#2</code> (перераховуючи слова через кому). 

5️⃣ Якщо ви хочете видалити слова зі списку, скористайтеся командою /deletewords і виберіть слово.

❗️ Щоб увімкнути або вимкнути фільтрацію ненормативної лексики в групі, скористайтеся командою /swearcontrol.

<b>Кнопки</b>
<pre>➕ Додати мене в группу</pre>
Додає бота до вашої групи.

<pre>🔧 Підтримка</pre>
Зв'яжіться з нами для допомоги.

<pre>ℹ️ Інформація</pre>
Отримайте додаткову інформацію про бота.

<pre>💳 Донатити</pre>
Підтримайте розробку бота фінансово.

<pre>📢 Канал</pre>
Перейдіть до каналу творця для оновлень і новин.

<b>Команди в особистих</b>
/start – запустити бота
/help – переглянути інструкцію

<b>Команди в групах для адміністраторів</b>
/start – включити фільтрацію  
/stop – виключити фільтрацію
/addwords – додає слова до списку
/deletewords – видаляє слова зі списку
/swearcontrol - фільтрація ненормативної лексики

<i>⚠️ Деякі слова в українській мові мають ідентичне написання з російською мовою, тому рекомендуємо використовувати команду /addwords, щоб уникнути їх фільтрації. 

📍 Також, будь ласка, звертайтеся до служби підтримки, щоб повідомити про такі випадки та допомогти вдосконалити роботу бота</i>."""


'''
    #STOP 
'''
msg_stop_in_group_2 = "🚀 Для запуску фільтрації потрібно спочатку включити за допомогою команди /start."

PHRASES_STOP = ["""😱 <b>О ні!</b> @ukrainian_patrol_bot відключили.

🌇 <b>Мій патруль</b> на сьогодні завершено. 🛑 Проте не забувайте, що ви завжди можете <b>активувати мене</b>, введіть команду /start.""", 
                """😴 @ukrainian_patrol_bot пішов <b>спати</b>...

🛌 Залишаю <b>свою роботу</b> на вас, мої улюблені <b>адміністратори</b>. 🌟 Якщо потрібно моя допомога, Ви знаете як <b>мене включити</b>. 😉""", 
                """🔴 @ukrainian_patrol_bot відключив <b>фільтрацію.</b>

⚠️ <b>Україномовне</b> спілкування може бути <b>під загрозою</b>, тому не забувайте, що завжди можете <b>мене увімкнути</b> командою /start."""
                ] 
GIFS_STOP = [fr"config/gif_stop/gif_{n}.mp4" for n in range(count_files_in_directory("config/gif_stop"))]


'''
    #NEW MEMBER 
'''
new_members_message = """👋 Ласкаво просимо, {0}! 

🇺🇦 Будь ласка, дотримуйся цього правила групи: <code>«🚫 заборонено використовувати російську мову»</code>. 

😊 Гарного спілкування!"""


'''
    #MAINTENANCE
'''
maintenance_message = "Зачекайте, будь ласка. Бот у процесі обслуговування. ⏳🤖"


'''
    #SUPPORT
'''
support_text_begin = """<b>🔧 Підтримка</b>

📥 <b>Надсилайте повідомлення</b> про <b>проблеми</b> або <b>пропозиції</b> щодо удосконалення бота.

❕Всі запити мають бути відправлені <b>у одному повідомленні</b>. Додаткові повідомлення <b>не будуть</b> оброблені."""

support_text_confirm = """✅ Ваше повідомлення було успішно надіслано до нашої служби підтримки. 

😊 Ми з радістю відповімо на нього найближчим часом. Дякуємо за звернення!

⏳ Поки очікуєте відповідь, можете підписатися на <a href="https://t.me/varich_channel">канал</a>, щоб не пропустити оновлення."""


'''
    #SWEAR CONTROL
'''
swear_control_text_begin = """🔞 Фільтрація ненормативної лексики <b>УВІМКНЕНА. 🟢</b>

🛡 Якщо бот не відфільтрував нецензурне слово або, навпаки, відфільтрував нормативне - будь ласка, <b>зверніться до служби підтримки.</b>

💡Щоб <b>вимкнути</b> бота натисніть команду /swearcontrol."""

swear_control_text_end = """🔞 Фільтрація ненормативної лексики <b>ВИМКНЕНА. 🔴</b>

🛡 Якщо бот не відфільтрував нецензурне слово або, навпаки, відфільтрував нормативне - будь ласка, <b>зверніться до служби підтримки.</b>

💡Щоб <b>увімкнути</b> бота натисніть команду /swearcontrol."""