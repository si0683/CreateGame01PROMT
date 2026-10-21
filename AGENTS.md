# AGENTS.md — правила для ИИ-агентов

Общий промт урока «Создаём игру»: ученик выбирает игру и название, Qwen берёт готовый шаблон одной из семи игр
(FlappyBird, SubwaySurf, QuizShooter, QuizTowerDefense, QuizSnake, QuizPlatformer, QuizBreakout — github.com/si0683/<имя>, папки рядом в D:\02GameBrowser).

- README.md создаёт `python tools/build.py`: правь скрипт, а не README.md. Таблицы «10 изменений» скрипт берёт из PROMPT_QWEN.md каждой игры — после изменения LAB в игре перезапусти его.
- Весь промт — ОДИН блок ````text в начале README.md. Ссылки на шаблоны — полные, отдельным блоком «ИГРА: …» на каждую игру: Qwen плохо подставляет части адреса.
- Название игры меняется только строками `titleTop` / `titleBottom` в LAB — они есть во всех семи играх.
- Похожий общий промт для сайтов — github.com/si0683/CreateSite01PROMT.
