rules = """
/ban - отправляет "Бан"
/bylo - отправляет "Было"
/ne_bylo - отправляет "Не было"
/da_net - отправит Да или Нет
/random - генерирует время вашего бана
/random_putin - когда уйдет Обнуленец?
/random_lukash - койда уйдет Лукашеску?

======== Математика ========
/calc - Выполнить одну арифметическую операцию (числа и операторы писать раздельно)
/sqrt - Квадрат от числа

======== Онлайн-ресурсы ========
/wiki2 - Для работы надо ввести /wiki + код страны (ru, uk, en, de) и название статьи
/wiki_langs - языки википедии, которые бот поддерживает
/wget - Информация о скорости загрузки страницы
/lurk - Луркоморье
/preview - Качает превью с ютуба по ссылке

======== Работа с текстом ========
/title - все слова с большой буквы
/upper - все слова капсом
/lower - все слова с маленькой буквы

======== Работа с изображениями ========
/resize - Изменить размер фото по пропорциям
/text - Нанести на фото текст
/rectangle - Нарисовать квадрат

======== Команды для бота ========
/delete - удаляет сообщение, если на него ответить
/to_json - переводит обычный python объект (str) в json
/status - Статус бота

======== Шифровая херня ========
/sha256 - хеширует ваш текст в sha256
/generate_password - генерирует пароль, можно указать количество символов (по стандарту 256)

======== Мемы ========
/rzaka - отправляет короткий вариант "РЖАКА-СМЕЯКА..."
/rzaka_full - отправляет полный вариант "РЖАКА-СМЕЯКА..."
/fake - отправляет фото с джонами/поляками
/pizda - отправляет мем "пизда"
/net_pizdy - отправляет мем "нет пизда"
/xui - отправляет мем "хуй"
"""

rzaka_time = 848393938347292929647492918363739304964682010

rzaka_full = """РЖАКА-СМЕЯКА 🤣🤣🤣🤣😋😋😋😋😋😋СРАЗУ ВИДНО РУССКОГО ЧЕЛОВЕКА😃😃😃😃😃🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺👍👍👍👍ТУПЫЕ ПЕНДОСЫ В СВОЕЙ ОМЕРИКЕ ДО ТАКОГО БЫ НЕ ДОДУМАЛИСЬ😡😡😡😡😡😡👎👎👎👎👎🇺🇸🇺🇸🇺🇸🇺🇸🇺🇸🇺🇸РОССИЯ ВПЕРЕД😊😊😊😊😊😊😃😃😃😃😃😃😋😋😋😋🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺АХАХАХАХАХ😃😃😃😃😃СМЕШНО ПОШУТИЛ ЧУВАЧОК👉👋👍👍👍👍👍ТАКОЕ МОЖНО УВИДЕТЬ ТОЛЬКО В РОССИИ ✌️✌️😲😲😲 ХААХАХА ВОТ УМОРА🤣🤣🤣🤣АЖ АМЕРИКА ВЗОРВАЛАСЬ ОТ СМЕХА😜😜😜😜😜😜😜ВСЯ ЕВРОПА В ШОКЕ🤙🤙🤙🤙🤙🤙🤙АХХАХАХАХА БЛИН НЕ МОГУ ОСТАНОВИТЬСЯ СМЕЮСЬ КАТАЮСЬ ПО ПОЛУ😬😬😬😵😵😵😵😵ВОТ ЭТО ШУТКА РЖАКА СМЕЯЛИСЬ ВСЕЙ МАРШРУТКОЙ РЖАЛА 848393938347292929647492918363739304964682010 ЧАСОВ РЖОМБА ПРЯМА НЕРЕАЛЬНАЯ РЖАКА ШУТКА 😂😂😂😂😂😂😂😂🤔😂😂😹😹😹😹😹😹😹😹😹😂😂😂😂👍👍👍👍👍👍👍👍👍👍АХАХА , КАК СМЕШНО !!!!! Я НЕ МОГУ, ПОМОГИТЕ , ЗАДЫХАЮСЬ ОТ СМЕХА 😂🤣🤣😄🤣😂🤣🤣🤣 СПАСИБО , ВЫ СДЕЛАЛИ МОЙ ДЕНЬ !!! КАК ЖЕ ОРИГИНАЛЬНО !!! Я В ВОСТОРГЕ!!!!!!😀😃😀😃🤣😁🤣🤣🤣🤣🤣😀🤣😀😀🤣🤣😀🤣😀🤣😀🤣😀🤣😀🤣😀😀🤣😀🤣😁🤣😁🤣😁🤣😁😁🤣😁"""

rzaka = """РЖАКА-СМЕЯКА 🤣🤣🤣🤣😋😋😋😋😋😋СРАЗУ ВИДНО РУССКОГО ЧЕЛОВЕКА😃😃😃😃😃🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺👍👍👍👍ТУПЫЕ ПЕНДОСЫ В СВОЕЙ ОМЕРИКЕ ДО ТАКОГО БЫ НЕ ДОДУМАЛИСЬ😡😡😡😡😡😡👎👎👎👎👎🇺🇸🇺🇸🇺🇸🇺🇸🇺🇸🇺🇸"""

greatings = [
    "Поляк",
    "Джон",
    "Александр Гомель",
    "Иван",
    "УберКац",
    "Яблочник",
    "Электрическая Говноварка",
    "Кацебот",
    "Кацекот",
    "Кац",
    "Голосовал против"
]

ban_list = [
    "Вы запостили информацию о бане, если вы не забаненны, то к вам приедут с [ДАННЫЕ ЗАБАНЕННЫ] сроком на 1 минуту",
    "Бан не плох, особенно на одну минуту",
    "Бан",
    "Анб",
    "Я из Баннии приехать, бан привез :/",
    "Выборы не признаю, но бан да",
    "Помолчи)))",
    "Я приватизировал бан",
    "⚡️⚡️⚡️ Ты получил бан на 1 минуту",
    "‼️‼️‼️ ТЫ ПОЛУЧАЕШЬ БАН)))",
    "Бан бану рознь, но этот лучший",
    "Пора бы за бан и заплатить",
    "Бань людей — спасай планету"
]

langs_list = """
`Поддерживаемые языки
├─🇷🇺 (ab) Абхазский
├─🇬🇧 (en) Английский
├─🇸🇱 (ba) Башкирский
├─🇧🇾 (be) Беларуский
│⠀└─🇧🇾 (bet) Тарашкевица
├─🇮🇱 (he) Иврит
├─🇪🇸 (es) Испанский
├─🇿🇦 (xh) Коса
├─🇩🇪 (de) Немецкий
├─🇵🇱 (pl) Польский
├─🇷🇺 (ru) Русский
├─🇧🇾 (tt) Татарский
├─🇺🇦 (uk) Украинский
└─🇧🇾 (ce) Чеченский`

[Предложите](t.me/jdan734) свой язык!
"""

langs = """
Чтобы вызвать википедию нужно ввести 
    `/w[язык] [запрос]`:
Например для русского (`ru`) команда будет такой:
    `/wru Википедия`

Узнать домен (индекс языка) - /langs
"""

keep = """
`🇷🇺 Русский язык`
`├─`/wikiru
`├─`/wikiru2
`├─`/wru
`├─`/wiki
`└─`/w

`🇬🇧 Английский`
`├─`/wikien
`├─`/van
`└─`/wen

`🇩🇪 Немецкий`
`├─`/wikide
`└─`/wde

`🇵🇱 Польский`
`├─`/wikipl
`└─`/wpl

`🇺🇦 Украинский`
`├─`/wikiua
`├─`/wikiuk
`├─`/wuk
`└─`/pawuk

`🇧🇾 Беларуский`
`├─`/wikibe
`├─`/wbe
`├─`/tarakanwiki
`├─`/lukaswiki
`├─`/potato
`└─`/potatowiki

`🇪🇸 Испанский`
`├─`/wes
`└─`/wikies

`🇧🇾 Тарашкевица`
`├─`/wbet
`└─`/xbet

`🇮🇱 Иврит`
`├─`/wikihe
`└─`/whe
"""