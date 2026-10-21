# Промт для урока: игра по выбору ученика

Один промт на все семь игр. Ученик выбирает игру и придумывает ей название — меняет **две строки** в начале промта, а Qwen сам берёт готовый шаблон нужной игры. Скопируйте промт **одной кнопкой** (два квадратика в правом верхнем углу блока).

## Промт

<!-- Для ИИ-агентов: ВЕСЬ промт — один блок ````text. Не делить на несколько блоков.
     Файл создаётся скриптом tools/build.py — правь скрипт, а не README.md.
     Ссылки на шаблоны — полные, отдельным блоком на каждую игру: Qwen плохо подставляет части адреса. -->

````text
Ты — разработчик браузерных игр. Создай игру для CodePen.

МОЙ ВЫБОР (меняю только эти две строки):
Игра: змейка
Название игры: как в шаблоне

Можно выбрать игру: птичка / раннер / шутер / башни / змейка / платформер / арканоид.
Название — два слова, каждое до 8 букв, например «Супер Змей». «как в шаблоне» — название не меняется.

Какие есть игры:
- птичка — Flappy Bird: птичка пролетает между трубами, 3 жизни, 4 фона;
- раннер — Subway Surf: 3D-бег по трём полосам: прыжки, монетки, 3 мира;
- шутер — Quiz Shooter: герой стреляет во врагов, за победу — вопрос и улучшение;
- башни — Quiz Tower: строй башни у дороги, монеты дают за верные ответы;
- змейка — Quiz Snake: змейка ест правильный ответ из четырёх на поле;
- платформер — Quiz Jump: бег и прыжки по платформам, ворота открывает верный ответ;
- арканоид — Quiz Breakout: шар разбивает кирпичи, золотой кирпич — вопрос;
В играх с вопросами (шутер, башни, змейка, платформер, арканоид) 3 мира — Фэнтези, Космос, Эко-Панк — и 4 предмета — математика, русский, английский, история России. Их выбирают в «Настройках» самой игры.

Игра должна быть красивой, со звуками, меню, паузой и экраном «Игра окончена», работать на компьютере и на телефоне. Код без ошибок, игра работает с первого раза.

Должно получиться ровно 3 файла, как три окна в CodePen: HTML (index.pen.html), CSS (style.css), JS (script.js).
Только обычный HTML, обычный CSS и ЧИСТЫЙ JavaScript. НЕ используй TypeScript, React, JSX, Vue, npm, import и export.

Сделай игру по моему готовому шаблону: в нём уже есть графика, звуки и настройки. У каждой игры свой шаблон.
Найди ниже блок «ИГРА: …» с моей игрой из «МОЙ ВЫБОР» и бери файлы ТОЛЬКО по трём ссылкам этого блока. Ссылки других игр не открывай.
Если моей игры нет в списке, напиши: «Такой игры нет, выбери игру из списка».

ИГРА: птичка
HTML: https://si0683.github.io/FlappyBird/codepen/index.pen.html
CSS: https://si0683.github.io/FlappyBird/style.css
JS: https://si0683.github.io/FlappyBird/script.js

ИГРА: раннер
HTML: https://si0683.github.io/SubwaySurf/codepen/index.pen.html
CSS: https://si0683.github.io/SubwaySurf/style.css
JS: https://si0683.github.io/SubwaySurf/script.js

ИГРА: шутер
HTML: https://si0683.github.io/QuizShooter/codepen/index.pen.html
CSS: https://si0683.github.io/QuizShooter/style.css
JS: https://si0683.github.io/QuizShooter/script.js

ИГРА: башни
HTML: https://si0683.github.io/QuizTowerDefense/codepen/index.pen.html
CSS: https://si0683.github.io/QuizTowerDefense/style.css
JS: https://si0683.github.io/QuizTowerDefense/script.js

ИГРА: змейка
HTML: https://si0683.github.io/QuizSnake/codepen/index.pen.html
CSS: https://si0683.github.io/QuizSnake/style.css
JS: https://si0683.github.io/QuizSnake/script.js

ИГРА: платформер
HTML: https://si0683.github.io/QuizPlatformer/codepen/index.pen.html
CSS: https://si0683.github.io/QuizPlatformer/style.css
JS: https://si0683.github.io/QuizPlatformer/script.js

ИГРА: арканоид
HTML: https://si0683.github.io/QuizBreakout/codepen/index.pen.html
CSS: https://si0683.github.io/QuizBreakout/style.css
JS: https://si0683.github.io/QuizBreakout/script.js

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
| птичка | Flappy Bird | `FlappyBird` | https://si0683.github.io/FlappyBird/ | [PROMPT_QWEN.md](https://github.com/si0683/FlappyBird/blob/main/PROMPT_QWEN.md) |
| раннер | Subway Surf | `SubwaySurf` | https://si0683.github.io/SubwaySurf/ | [PROMPT_QWEN.md](https://github.com/si0683/SubwaySurf/blob/main/PROMPT_QWEN.md) |
| шутер | Quiz Shooter | `QuizShooter` | https://si0683.github.io/QuizShooter/ | [PROMPT_QWEN.md](https://github.com/si0683/QuizShooter/blob/main/PROMPT_QWEN.md) |
| башни | Quiz Tower | `QuizTowerDefense` | https://si0683.github.io/QuizTowerDefense/ | [PROMPT_QWEN.md](https://github.com/si0683/QuizTowerDefense/blob/main/PROMPT_QWEN.md) |
| змейка | Quiz Snake | `QuizSnake` | https://si0683.github.io/QuizSnake/ | [PROMPT_QWEN.md](https://github.com/si0683/QuizSnake/blob/main/PROMPT_QWEN.md) |
| платформер | Quiz Jump | `QuizPlatformer` | https://si0683.github.io/QuizPlatformer/ | [PROMPT_QWEN.md](https://github.com/si0683/QuizPlatformer/blob/main/PROMPT_QWEN.md) |
| арканоид | Quiz Breakout | `QuizBreakout` | https://si0683.github.io/QuizBreakout/ | [PROMPT_QWEN.md](https://github.com/si0683/QuizBreakout/blob/main/PROMPT_QWEN.md) |

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

<details>
<summary><b>птичка</b> — Flappy Bird</summary>

| № | Что написать Qwen | Было | Стало |
|---|---|---|---|
| 1 | Назови игру «Супер Птица» | `titleTop: 'Flappy',` `titleBottom: 'Bird',` | `titleTop: 'Супер',` `titleBottom: 'Птица',` |
| 2 | Добавь птичке розовый цвет | `myBirdColor: '',` | `myBirdColor: '#FF7EB6',` |
| 3 | Пусть птичка летает как на Луне | `gravity: 1,` | `gravity: 0.5,` |
| 4 | Сделай птичку больше | `birdSize: 20,` | `birdSize: 30,` |
| 5 | Включи турбо-режим | `gameSpeed: 1,` | `gameSpeed: 1.5,` |
| 6 | Сделай проходы шире | `gapBonus: 0,` | `gapBonus: 60,` |
| 7 | Пусть трубы идут чаще | `obstacleDistance: 270,` | `obstacleDistance: 200,` |
| 8 | Давай 100 очков за трубу | `pointsPerObstacle: 1,` | `pointsPerObstacle: 100,` |
| 9 | Включи салют | `fireworks: false,` | `fireworks: true,` |
| 10 | Включи радужный хвост | `rainbowTrail: false` | `rainbowTrail: true` |

</details>

<details>
<summary><b>раннер</b> — Subway Surf</summary>

| № | Что написать Qwen | Было | Стало |
|---|---|---|---|
| 1 | Назови игру «Супер Бег» | `titleTop: 'Subway',` `titleBottom: 'Surf',` | `titleTop: 'Супер',` `titleBottom: 'Бег',` |
| 2 | Сделай героя жёлтым | `myHeroColor: '',` | `myHeroColor: '#FFD84A',` |
| 3 | Пусть герой прыгает как на Луне | `gravity: 1,` | `gravity: 0.5,` |
| 4 | Сделай суперпрыжок | `jumpPower: 1,` | `jumpPower: 1.5,` |
| 5 | Включи турбо-режим | `gameSpeed: 1,` | `gameSpeed: 1.5,` |
| 6 | Сделай героя великаном | `heroSize: 1,` | `heroSize: 1.5,` |
| 7 | Давай 1000 очков за монетку | `coinValue: 10,` | `coinValue: 1000,` |
| 8 | Пусть препятствий будет меньше | `obstacleDistance: 22,` | `obstacleDistance: 35,` |
| 9 | Включи магнит для монеток | `coinMagnet: false,` | `coinMagnet: true,` |
| 10 | Подними камеру, хочу вид сверху | `cameraHeight: 3.6` | `cameraHeight: 8` |

</details>

<details>
<summary><b>шутер</b> — Quiz Shooter</summary>

| № | Что написать Qwen | Было | Стало |
|---|---|---|---|
| 1 | Назови игру «Супер Бой» | `titleTop: 'Quiz',` `titleBottom: 'Shooter',` | `titleTop: 'Супер',` `titleBottom: 'Бой',` |
| 2 | Добавь героя-единорога | `myHeroEmoji: '',` | `myHeroEmoji: '🦄',` |
| 3 | Сделай героя крепче на 100 | `startHpBonus: 0,` | `startHpBonus: 100,` |
| 4 | Сделай пули мощнее | `damageBonus: 0,` | `damageBonus: 20,` |
| 5 | Пусть герой стреляет вдвое чаще | `fireRateBoost: 1,` | `fireRateBoost: 2,` |
| 6 | Замедли врагов | `enemySpeed: 1,` | `enemySpeed: 0.5,` |
| 7 | Пусть врагов будет больше | `maxEnemies: 5,` | `maxEnemies: 8,` |
| 8 | Пусть босс приходит чаще | `bossEvery: 10,` | `bossEvery: 3,` |
| 9 | Пусть вопросы будут реже | `quizEvery: 1,` | `quizEvery: 3,` |
| 10 | Сделай радужные пули | `rainbowBullets: false` | `rainbowBullets: true` |

</details>

<details>
<summary><b>башни</b> — Quiz Tower</summary>

| № | Что написать Qwen | Было | Стало |
|---|---|---|---|
| 1 | Назови игру «Супер Замок» | `titleTop: 'Quiz',` `titleBottom: 'Tower',` | `titleTop: 'Супер',` `titleBottom: 'Замок',` |
| 2 | Дай побольше монет на старте | `startCoins: 120,` | `startCoins: 1000,` |
| 3 | Сделай замок крепче | `baseLives: 20,` | `baseLives: 50,` |
| 4 | Пусть за ответ дают 200 монет | `questionReward: 50,` | `questionReward: 200,` |
| 5 | Сделай башни вдвое сильнее | `towerPower: 1,` | `towerPower: 2,` |
| 6 | Замедли врагов | `enemySpeed: 1,` | `enemySpeed: 0.5,` |
| 7 | Пусть врагов будет толпа | `waveSize: 6,` | `waveSize: 15,` |
| 8 | Пусть босс приходит чаще | `bossEvery: 5,` | `bossEvery: 2,` |
| 9 | Сделай башни бесплатными | `freeTowers: false,` | `freeTowers: true,` |
| 10 | Сделай радужные снаряды | `rainbowShots: false` | `rainbowShots: true` |

</details>

<details>
<summary><b>змейка</b> — Quiz Snake</summary>

| № | Что написать Qwen | Было | Стало |
|---|---|---|---|
| 1 | Назови игру «Супер Змей» | `titleTop: 'Quiz',` `titleBottom: 'Snake',` | `titleTop: 'Супер',` `titleBottom: 'Змей',` |
| 2 | Сделай голову лягушкой | `snakeHead: '',` | `snakeHead: '🐸',` |
| 3 | Сделай змейку длинной | `startLength: 4,` | `startLength: 10,` |
| 4 | Дай 10 жизней | `lives: 3,` | `lives: 10,` |
| 5 | Сделай змейку медленнее | `snakeSpeed: 1,` | `snakeSpeed: 0.6,` |
| 6 | Убери врагов | `maxEnemies: 4,` | `maxEnemies: 0,` |
| 7 | Пусть змейка растёт быстрее | `growPerAnswer: 2,` | `growPerAnswer: 5,` |
| 8 | Пусть можно проходить сквозь стены | `wrapWalls: false,` | `wrapWalls: true,` |
| 9 | Замедли врагов | `enemySpeed: 1,` | `enemySpeed: 0.5,` |
| 10 | Сделай змейку радужной | `rainbowSnake: false` | `rainbowSnake: true` |

</details>

<details>
<summary><b>платформер</b> — Quiz Jump</summary>

| № | Что написать Qwen | Было | Стало |
|---|---|---|---|
| 1 | Назови игру «Супер Прыг» | `titleTop: 'Quiz',` `titleBottom: 'Jump',` | `titleTop: 'Супер',` `titleBottom: 'Прыг',` |
| 2 | Сделай героем лягушку | `heroEmoji: '',` | `heroEmoji: '🐸',` |
| 3 | Дай 10 жизней | `lives: 3,` | `lives: 10,` |
| 4 | Сделай суперпрыжок | `jumpPower: 1,` | `jumpPower: 1.3,` |
| 5 | Пусть герой бегает быстрее | `heroSpeed: 1,` | `heroSpeed: 1.5,` |
| 6 | Пусть прыжки будут как на Луне | `gravity: 1,` | `gravity: 0.5,` |
| 7 | Убери врагов | `enemyAmount: 1,` | `enemyAmount: 0,` |
| 8 | Пусть ворот будет больше | `gateEvery: 22,` | `gateEvery: 12,` |
| 9 | Сделай уровни короче | `levelLength: 1,` | `levelLength: 0.5,` |
| 10 | Дай двойной прыжок | `doubleJump: false` | `doubleJump: true` |

</details>

<details>
<summary><b>арканоид</b> — Quiz Breakout</summary>

| № | Что написать Qwen | Было | Стало |
|---|---|---|---|
| 1 | Назови игру «Супер Шар» | `titleTop: 'Quiz',` `titleBottom: 'Breakout',` | `titleTop: 'Супер',` `titleBottom: 'Шар',` |
| 2 | Поставь на платформу лягушку | `heroEmoji: '',` | `heroEmoji: '🐸',` |
| 3 | Дай 10 жизней | `lives: 3,` | `lives: 10,` |
| 4 | Сделай платформу широкой | `paddleWidth: 110,` | `paddleWidth: 200,` |
| 5 | Сделай шар медленнее | `ballSpeed: 1,` | `ballSpeed: 0.7,` |
| 6 | Пусть вопросов будет больше | `quizBricks: 3,` | `quizBricks: 8,` |
| 7 | Сделай стену из кирпичей выше | `brickRows: 5,` | `brickRows: 8,` |
| 8 | Пусть босс будет на каждом уровне | `bossEvery: 3,` | `bossEvery: 1,` |
| 9 | Начни сразу с трёх шаров | `startBalls: 1,` | `startBalls: 3,` |
| 10 | Сделай шар радужным | `rainbowBall: false` | `rainbowBall: true` |

</details>

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
