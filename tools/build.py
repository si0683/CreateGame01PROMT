"""Собирает README.md — промты урока «Создаём игру»: любая игра на ArcadeJS и 7 готовых игр.

Запускать после любого изменения игр (их LAB или PROMPT_QWEN.md):

    python tools/build.py

Таблицы «10 изменений» берутся из PROMPT_QWEN.md каждой игры
(папки рядом: D:\\02GameBrowser\\<Игра>), поэтому общий промт не расходится с играми.
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')  # русский текст в консоли Windows

ROOT = Path(__file__).resolve().parent.parent
GAMES_DIR = ROOT.parent
GH = 'https://si0683.github.io'

# Слово для выбора, папка-шаблон, название в меню, что за игра
GAMES = [
    ('птичка', 'FlappyBird', 'Flappy Bird', 'птичка пролетает между трубами, 3 жизни, 4 фона'),
    ('раннер', 'SubwaySurf', 'Subway Surf', '3D-бег по трём полосам: прыжки, монетки, 3 мира'),
    ('шутер', 'QuizShooter', 'Quiz Shooter', 'герой стреляет во врагов, за победу — вопрос и улучшение'),
    ('башни', 'QuizTowerDefense', 'Quiz Tower', 'строй башни у дороги, монеты дают за верные ответы'),
    ('змейка', 'QuizSnake', 'Quiz Snake', 'змейка ест правильный ответ из четырёх на поле'),
    ('платформер', 'QuizPlatformer', 'Quiz Jump', 'бег и прыжки по платформам, ворота открывает верный ответ'),
    ('арканоид', 'QuizBreakout', 'Quiz Breakout', 'шар разбивает кирпичи, золотой кирпич — вопрос'),
]


ARCADE_VERSION = '1.1.0'
ARCADE = f'https://cdn.jsdelivr.net/gh/si0683/ArcadeJS@{ARCADE_VERSION}'

# Промт 1: любая игра на фреймворке ArcadeJS (главный). ARCADE_URL заменяется адресом версии
ARCADE_PROMPT = '''# Промты для урока: создаём игру

Здесь два промта для Qwen (или другой нейросети):

1. **Любая игра на ArcadeJS** — ученик сам придумывает игру, нейросеть пишет её на нашем движке [ArcadeJS](https://github.com/si0683/ArcadeJS). Меню, очки, жизни, звуки, кнопки для телефона, физика и 3D уже в движке, поэтому код короткий и работает с первого раза.
2. **Готовая игра из шаблона** — одна из семи наших игр, Qwen берёт её по ссылкам без изменений (запасной вариант, если нужен гарантированный результат).

Скопируйте промт **одной кнопкой** (два квадратика в правом верхнем углу блока).

# Промт 1: любая игра на ArcadeJS

<!-- Для ИИ-агентов: ВЕСЬ промт — один блок ````text. Шпаргалка API внутри промта нужна, если нейросеть не откроет ссылку на AI.md.
     Версия ArcadeJS в ссылках — ARCADE_VERSION в tools/build.py. -->

````text
Ты — разработчик браузерных игр. Сделай игру для CodePen на моём игровом движке ArcadeJS.

МОЯ ИГРА (меняю только эти строки):
Название: Космический кот
Идея: кот летает на ракете, ловит рыбок и уворачивается от метеоритов
Управление: стрелки влево-вправо, на телефоне кнопки
Мир: космос

Миры: небо (sky), космос (space), лес (forest), океан (ocean), ночь (night), сладости (candy), пустыня (desert), город (city).
В идею можно добавить: вопросы по математике, русскому, английскому или истории; физику (всё падает и сталкивается); 3D.

Должно получиться ровно 3 файла, как три окна в CodePen: HTML, CSS, JS.
Только обычный HTML, CSS и ЧИСТЫЙ JavaScript. НЕ используй TypeScript, React, JSX, Vue, npm, import и export, свой <canvas>, requestAnimationFrame и setInterval.

Полный справочник движка: ARCADE_URL/AI.md
Запасная ссылка: https://raw.githubusercontent.com/si0683/ArcadeJS/main/AI.md
Готовые примеры: https://github.com/si0683/ArcadeJS/tree/main/examples

Если ссылки не открываются, вот главное:
- HTML — ровно эти 3 строки:
<link rel="stylesheet" href="ARCADE_URL/arcade.css">
<script src="ARCADE_URL/arcade.js"></script>
<div id="game"></div>
- CSS — почти пустой, можно свой цвет кнопок: .arc-root { --arc-accent: #ff4d6d; }
- JS: сначала const LAB = { ... } — 6–10 настроек для детей с комментариями (название, герой-эмодзи, скорость, жизни…), потом
  Arcade.create({ title, emoji, subtitle, help, world, worlds: true, lives, buttons: ['left', 'right', 'action'], quiz, physics, mode, setup(game) { ... }, update(game, dt) { ... } })
  и ниже свои функции. Свои переменные храни в game.data. Меню, настройки, отсчёт, пауза, «Игра окончена», рекорд, панель очков и жизней уже есть — не пиши их.
- Объекты: const hero = game.add({ emoji: '🐱', x, y, size: 60, vx, vy, gravity, tag: 'hero', inside: true }); враги и предметы — с tag и removeOffscreen: true.
  Свойства: x, y (центр), size или w, h, emoji / image / text / shape: 'rect' | 'circle', color, vx, vy, gravity, spin, angle, flip, bounce, wrap, inside, life, blink, hitbox.
- obj.remove(), game.all('tag'), game.first('tag'), game.count('tag'), game.hit(a, b), game.hitAny(a, 'tag'), game.collide(a, 'ground') — твёрдые платформы (a.onGround), game.follow(hero) — камера.
- Управление: game.key.left / right / up / down / action — зажато; game.pressed('action') — нажато сейчас (пробел, касание); game.pressed('left') — стрелка или свайп; game.pointer.x / y / down — мышь и палец.
- game.addScore(10, x, y), game.loseLife(), game.addLife(), game.nextLevel(), game.over(), game.win(), game.message('Текст'), game.hud('⏱', 30).
- game.every(1.5, fn), game.after(2, fn) — таймеры; game.burst(x, y, { emoji: '✨' }), game.popup(x, y, '+10'), game.shake().
- Звуки: game.sound('coin') — jump, coin, crash, flap, hit, score, start, tick, bonus, lose, click, win; звуки Kenney — laser, explosion, boom, powerup, coins, sword, punch, door, zap, step, error, confirm, jingle-nes…; 8-битные — retro-jump, retro-coin, retro-laser, retro-explosion, retro-powerup, retro-win… Фоновая музыка: music: 'adventure' (action, boss, calm, menu) в Arcade.create.
- Графика: эмодзи (emoji: '🐱', рисуются картинками) или готовые спрайты (image: 'knight'). Персонажи с анимацией ходьбы и прыжка: adventurer, explorer, robot, zombie, woman, man; пиксельные: alien-green, slime, bat, knight, wizard, orc, skeleton, ghost; блоки: grass, dirt, crate, plank, spikes, coin, gem, heart, flag, door, key; космос: ship-blue, ufo-red, enemy-red, meteor, laser-blue, powerup-star; животные: panda, penguin, rabbit, monkey, pig. Полный список — в справочнике.
- game.rand(a, b), game.randInt(a, b), game.pick(list), game.chance(0.3), game.clamp(v, a, b).
- Вопросы (quiz: true): game.ask().then(ok => { ... }). Выбор улучшения: game.choose([{ icon, title, text, apply }]).then(card => card.apply()).
- Физика (physics: { walls: true, drag: true }): game.add({ ..., body: true }) или body: 'static'; game.velocity(obj, vx, vy), game.onCollide('a', 'b', fn), game.link(a, b).
- 3D (mode: '3d'): game.add3d({ shape: 'box' | 'sphere' | 'emoji', emoji, x, y, z, size, vz, gravity, color, tag }), пол — shape: 'plane'; game.follow(hero, { offset: { x: 0, y: 3.5, z: 7 } }).

Пример игры целиком:
const LAB = { title: 'Фруктопад', hero: '🧺', speed: 500, lives: 3 };
Arcade.create({
  title: LAB.title, emoji: '🍉', subtitle: 'Лови фрукты', world: 'sky', worlds: true, lives: LAB.lives, buttons: ['left', 'right'],
  setup(game) {
    game.data.hero = game.add({ emoji: LAB.hero, x: game.width / 2, y: game.height - 60, size: 70, inside: true });
    game.every(0.7, g => g.add({ emoji: g.pick(['🍎', '🍌', '💣']), x: g.rand(40, g.width - 40), y: -30, size: 48, vy: 220, tag: 'item', removeOffscreen: true }));
  },
  update(game, dt) {
    const hero = game.data.hero;
    hero.vx = game.key.left ? -LAB.speed : game.key.right ? LAB.speed : 0;
    if (game.pointer.down) hero.x = game.pointer.x;
    const item = game.hitAny(hero, 'item');
    if (item) { item.remove(); if (item.emoji === '💣') game.loseLife(); else { game.addScore(1, item.x, item.y); game.sound('coin'); } }
  }
});

Как выдавать код:
- Сначала одной строкой опиши, какой будет игра. Потом файлы, без долгих рассуждений.
- По одному файлу за ответ: HTML, после моего «дальше» — CSS, после следующего «дальше» — JS.
- Перед каждым блоком кода одна строка: «Файл 1 из 3 — HTML. Вставьте в окно HTML и напишите: дальше» (так же для CSS и JS).
- Комментарии в коде на русском. Код без ошибок, игра работает с первого раза.

Когда игра будет готова, я буду просить изменения. Меняй по возможности только объект LAB в начале JS и отвечай коротко: строка «было» и строка «стало». Если я напишу «настройки», перечисли настройки LAB с номерами.

Начинай.
````

> **Только для преподавателя.** Здесь нейросеть действительно пишет игру сама, но на нашем движке: ей не нужно писать меню, физику, звуки и экраны, поэтому код короткий и почти всегда работает с первого раза. Если игра не заработала, скопируйте красную ошибку из консоли CodePen и отправьте Qwen: «Исправь ошибку: …». Для гарантированного результата есть промт 2 ниже.

## Как менять игру на уроке

1. Вставьте промт в Qwen, **не отправляя**, и вместе с учеником перепишите четыре строки «МОЯ ИГРА»: название, идею одним предложением, управление и мир.
2. Режим Qwen: ❌ без «Web Dev» и «Мышления», ✅ с «Поиском» (чтобы открыть справочник).
3. Три ответа Qwen вставьте в окна **HTML**, **CSS**, **JS** на [codepen.io/pen](https://codepen.io/pen/).
4. Идеи для учеников: «рыцарь в подземелье собирает зелья» (спрайты и музыка), «кот ловит рыбок в космосе», «змейка в лесу ест ягоды и отвечает на вопросы по математике», «башня из ящиков, которую надо сбить мячом» (физика), «гонка по 3D-трассе» (3D).

Готовые примеры игр на ArcadeJS: [Фруктопад](https://si0683.github.io/ArcadeJS/examples/starter/) · [Флаппи](https://si0683.github.io/ArcadeJS/examples/flappy/) · [Змейка-умник](https://si0683.github.io/ArcadeJS/examples/snake/) · [Космо-арканоид](https://si0683.github.io/ArcadeJS/examples/breakout/) · [Лисёнок](https://si0683.github.io/ArcadeJS/examples/platformer/) · [Звёздный патруль](https://si0683.github.io/ArcadeJS/examples/shooter/) · [Злые эмодзи](https://si0683.github.io/ArcadeJS/examples/angry/) · [Космо-раннер 3D](https://si0683.github.io/ArcadeJS/examples/runner3d/) · [Приключение](https://si0683.github.io/ArcadeJS/examples/adventure/)
'''.replace('ARCADE_URL', ARCADE)


def changes_table(folder):
    """Строки таблицы «10 изменений» из PROMPT_QWEN.md игры: (просьба, было, стало)."""
    text = (GAMES_DIR / folder / 'PROMPT_QWEN.md').read_text(encoding='utf-8')
    block = text.split('## 10 изменений', 1)[1].split('\n---', 1)[0]
    rows = []
    for line in block.split('\n'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if cells and cells[0].isdigit():
            rows.append((cells[0], cells[-3], cells[-2], cells[-1]))  # №, просьба, было, стало
    if len(rows) != 10:
        raise SystemExit(f'{folder}: в таблице изменений {len(rows)} строк вместо 10')
    return rows


def build():
    choice_words = ' / '.join(g[0] for g in GAMES)
    about = '\n'.join(f'- {word} — {title}: {desc};' for word, folder, title, desc in GAMES)
    links = '\n\n'.join(
        f'ИГРА: {word}\n'
        f'HTML: {GH}/{folder}/codepen/index.pen.html\n'
        f'CSS: {GH}/{folder}/style.css\n'
        f'JS: {GH}/{folder}/script.js' for word, folder, title, desc in GAMES)
    games_table = '\n'.join(
        f'| {word} | {title} | `{folder}` | {GH}/{folder}/ | [PROMPT_QWEN.md](https://github.com/si0683/{folder}/blob/main/PROMPT_QWEN.md) |'
        for word, folder, title, desc in GAMES)
    details = []
    for word, folder, title, desc in GAMES:
        rows = '\n'.join(f'| {n} | {ask} | {old} | {new} |' for n, ask, old, new in changes_table(folder))
        details.append(f'''<details>
<summary><b>{word}</b> — {title}</summary>

| № | Что написать Qwen | Было | Стало |
|---|---|---|---|
{rows}

</details>''')
    details = '\n\n'.join(details)

    return ARCADE_PROMPT + f'''
---

# Промт 2: готовая игра из шаблона

Один промт на все семь готовых игр. Ученик выбирает игру и придумывает ей название — меняет **две строки** в начале промта, а Qwen сам берёт готовый шаблон нужной игры. Скопируйте промт **одной кнопкой** (два квадратика в правом верхнем углу блока).

## Промт

<!-- Для ИИ-агентов: ВЕСЬ промт — один блок ````text. Не делить на несколько блоков.
     Файл создаётся скриптом tools/build.py — правь скрипт, а не README.md.
     Ссылки на шаблоны — полные, отдельным блоком на каждую игру: Qwen плохо подставляет части адреса. -->

````text
Ты — разработчик браузерных игр. Создай игру для CodePen.

МОЙ ВЫБОР (меняю только эти две строки):
Игра: змейка
Название игры: как в шаблоне

Можно выбрать игру: {choice_words}.
Название — два слова, каждое до 8 букв, например «Супер Змей». «как в шаблоне» — название не меняется.

Какие есть игры:
{about}
В играх с вопросами (шутер, башни, змейка, платформер, арканоид) 3 мира — Фэнтези, Космос, Эко-Панк — и 4 предмета — математика, русский, английский, история России. Их выбирают в «Настройках» самой игры.

Игра должна быть красивой, со звуками, меню, паузой и экраном «Игра окончена», работать на компьютере и на телефоне. Код без ошибок, игра работает с первого раза.

Должно получиться ровно 3 файла, как три окна в CodePen: HTML (index.pen.html), CSS (style.css), JS (script.js).
Только обычный HTML, обычный CSS и ЧИСТЫЙ JavaScript. НЕ используй TypeScript, React, JSX, Vue, npm, import и export.

Сделай игру по моему готовому шаблону: в нём уже есть графика, звуки и настройки. У каждой игры свой шаблон.
Найди ниже блок «ИГРА: …» с моей игрой из «МОЙ ВЫБОР» и бери файлы ТОЛЬКО по трём ссылкам этого блока. Ссылки других игр не открывай.
Если моей игры нет в списке, напиши: «Такой игры нет, выбери игру из списка».

{links}

Как выдавать код:
- Первой строкой первого ответа напиши проверку: «Игра: …, шаблон: …, название: …». В «шаблон» впиши слово из ссылки, например QuizSnake.
- Код каждого файла возьми из шаблона полностью, без сокращений и без изменений. Шаблон уже на чистом JavaScript — не переводи его на TypeScript или React. Звуки шаблон сам берёт из интернета — пути к ним не меняй.
- Если в «Название игры» не «как в шаблоне», поменяй только две строки в самом начале JS, в блоке LAB:
  titleTop: '…',    — первое слово названия
  titleBottom: '…', — второе слово названия
- Отвечай сразу, без долгих рассуждений и без объяснений кода.
- По одному файлу за ответ: сначала HTML, после моего «дальше» — CSS, после следующего «дальше» — JS.
- Перед каждым блоком кода напиши одну строку:
  «Файл 1 из 3 — HTML (index.pen.html). Вставьте в окно HTML и напишите: дальше»
  «Файл 2 из 3 — CSS (style.css). Вставьте в окно CSS и напишите: дальше»
  «Файл 3 из 3 — JS (script.js). Вставьте в окно JS — игра готова!»
- JS длинный: если он не помещается в один ответ, остановись в конце строки. После «дальше» продолжи со следующей строки новым блоком кода.
- Если шаблон не открывается, напиши «Не могу открыть шаблон».

Когда игра будет готова, я буду просить изменения. В начале JS есть блок LAB «Лаборатория игры» из 10 настроек: меняй только его, одно значение на одну просьбу. Отвечай сразу и коротко: строка «было» и строка «стало» в блоке кода javascript.
Если я напишу «настройки», перечисли 10 настроек LAB моей игры: номер, что делает (из комментария) и пример нового значения. Потом я выберу по номеру.

Начинай: строка проверки и файл 1 — HTML.
````

> **Только для преподавателя.** Для детей промт выглядит как задание разработчику с выбором игры. На самом деле в нём ссылки на «шаблоны проекта» — готовые игры, и Qwen берёт нужную без изменений. Поэтому он отвечает за минуты, а игра гарантированно работает.

---

## Как менять выбор на уроке

1. Вставьте промт в поле ввода Qwen, но **не отправляйте**.
2. Вместе с учеником поменяйте две строки в блоке «МОЙ ВЫБОР» — игру пишите **словом из списка**:
   ```
   Игра: арканоид
   Название игры: Супер Шар
   ```
3. Отправьте. Первая строка ответа Qwen — проверка «Игра: …, шаблон: …». Шаблон должен совпадать с таблицей:

| Игра | Название | Шаблон | Готовая игра (запасной вариант) | Урок по одной игре |
|---|---|---|---|---|
{games_table}

## На уроке

**Шаг 1.** Откройте [chat.qwen.ai](https://chat.qwen.ai), новый чат.

**Шаг 2. Режим — самое важное для скорости:**
- ❌ **не включайте «Web Dev» / «Веб-разработка» / «Artifacts»**: там Qwen переписывает всё на React (`.tsx`);
- ❌ **выключите «Мышление» (Thinking)**: иначе долгие рассуждения;
- ✅ **включите «Поиск» (Search / веб-доступ)**: без него Qwen не откроет ссылки.

**Шаг 3.** Вставьте промт, поменяйте «МОЙ ВЫБОР», отправьте.

**Шаг 4.** Откройте [codepen.io/pen](https://codepen.io/pen/) и соберите игру из трёх ответов:

| Ответ Qwen | Куда вставить в CodePen | Что написать Qwen потом |
|---|---|---|
| Файл 1 из 3 — HTML | окно **HTML** (в CodePen 2.0 — файл `index.pen.html`) | `дальше` |
| Файл 2 из 3 — CSS | окно **CSS** (файл `style.css`) | `дальше` |
| Файл 3 из 3 — JS | окно **JS** (файл `script.js`) | `дальше`, пока JS не закончится |

> Файл JS большой (1300–1600 строк), Qwen печатает его несколько минут. В это время можно рассказать, как устроена игра: разделы кода подписаны комментариями.

**Шаг 5. Проверьте название.** Если ученик придумал название, в самом начале окна JS должны стоять строки `titleTop: '…',` и `titleBottom: '…',` с его словами. Если Qwen оставил старые — поправьте сами.

**Шаг 6. Меняем игру.** Ученик пишет Qwen `настройки` — Qwen перечислит 10 настроек его игры. Ученик выбирает номер или пишет просьбу своими словами (готовые идеи — в таблицах ниже). Qwen отвечает «было → стало»: в окне JS нажмите `Ctrl+F`, найдите строку «было» и замените на «стало».

## 10 изменений для каждой игры

Все изменения — одна строка в блоке **«0. ЛАБОРАТОРИЯ ИГРЫ 🧪»** в начале JS. Если Qwen ответит неточно, поменяйте значение сами.

{details}

---

## Если что-то пошло не так

| Что случилось | Что сделать |
|---|---|
| В строке проверки не тот шаблон | Напишите: `Ты взял не тот шаблон. Моя игра — арканоид: возьми три ссылки из блока «ИГРА: арканоид» и начни заново с HTML.` |
| Название не поменялось | Поправьте строки `titleTop:` и `titleBottom:` в начале окна JS сами. |
| Qwen долго «думает» | Выключите «Мышление», начните новый чат. |
| «Не могу открыть шаблон» | Включите «Поиск» и отправьте промт заново. |
| Qwen выдал `.tsx`, React или TypeScript | Выключите «Web Dev», новый чат. Или: `Нужен чистый JavaScript — возьми script.js из шаблона как есть.` |
| Qwen остановился посреди файла JS | Напишите `дальше` и вставьте продолжение в конец окна JS. |
| Qwen пишет свой код или «улучшает» | Напишите: `Возьми код из шаблона без изменений.` |
| В CodePen ошибка `has already been declared` | В окно HTML попал лишний `<script>`. Вставьте файл 1 заново. |
| Ничего не помогает | Покажите готовую игру из таблицы выше. |
'''


def framework_prompt_md():
    """PROMPT.md для репозитория ArcadeJS: только промт «любая игра», без шаблонов."""
    body = '<!--' + ARCADE_PROMPT.split('<!--', 1)[1]
    body = body.replace(' Для гарантированного результата есть промт 2 ниже.', '')
    head = (
        '# Промт: любая игра на ArcadeJS\n\n'
        'Шаблон промта для быстрой разработки: ученик (или вы) меняет строки «МОЯ ИГРА» — название, идею, управление и мир, '
        'а нейросеть (Qwen, ChatGPT, GigaChat, DeepSeek…) пишет игру на ArcadeJS. Получается 3 файла — HTML, CSS, JS — для CodePen. '
        'Скопируйте промт **одной кнопкой** (два квадратика в правом верхнем углу блока).\n\n'
        'Полный справочник движка — [AI.md](AI.md), примеры — [examples](examples).\n\n'
        '<!-- Файл создаётся скриптом CreateGame01PROMT/tools/build.py (D:\\02GameBrowser\\CreateGame01PROMT) — правьте там. -->\n\n'
    )
    return head + body


if __name__ == '__main__':
    (ROOT / 'README.md').write_text(build(), encoding='utf-8', newline='\n')
    print('README.md: общий промт обновлён')
    arcade = GAMES_DIR / 'ArcadeJS'
    if arcade.exists():
        (arcade / 'PROMPT.md').write_text(framework_prompt_md(), encoding='utf-8', newline='\n')
        print('ArcadeJS/PROMPT.md: обновлён')
