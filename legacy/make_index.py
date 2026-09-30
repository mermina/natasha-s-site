# -*- coding: utf-8 -*-
import os, importlib.util
here=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location("b", os.path.join(here,"build.py"))
b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)

CARDS = [
 ("option-a-one-site.html", "Вариант A — один сайт",
  "Обычный сайт с меню сверху: книги, фотография, тексты, об авторе. Всё на одной странице, листается вниз.",
  "Посмотри: не теряется ли фотография рядом с книгами."),
 ("option-b-two-sides.html", "Вариант B — две половины",
  "Твоя идея: вход разделён пополам, слева фотография, справа литература. Выбираешь сторону — попадаешь в свою часть. Сверху остаётся переключатель и ссылка Entrance назад на вход.",
  "Посмотри: не мешает ли лишний шаг перед тем, как увидеть работы."),
 ("books-layouts.html", "Вариант C — три раскладки книг",
  "Не сайт, а сравнение. Сверху три вкладки, по каждой надо нажать: <b>1 · Rail</b> — обложки одной строкой, <b>2 · Staggered</b> — разного размера и высоты, <b>3 · Asymmetric, all large</b> — без сетки, но все крупные.",
  "Выбери один из трёх — он пойдёт в сайт."),
]

def cards():
    out=[]
    for href,title,desc,ask in CARDS:
        out.append('<a class="card" href="%s"><h3>%s</h3><p>%s</p><p class="ask">%s</p>'
                   '<span class="go">Открыть →</span></a>'%(href,title,desc,ask))
    return "\n".join(out)

PAGE = """<!DOCTYPE html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Сайт Наташи — черновики</title>
<style>%s
.hero{padding:96px 0 40px}
.hero h1{font-size:clamp(32px,5vw,58px);line-height:1.05;max-width:18ch}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:26px;margin:40px 0 10px}
.card{display:block;text-decoration:none;border:1px solid var(--line);padding:28px 26px;
 background:#fffdfa;transition:transform .25s,box-shadow .25s}
.card:hover{transform:translateY(-3px);box-shadow:0 20px 40px -28px rgba(0,0,0,.45)}
.card h3{font-size:21px;margin-bottom:10px}
.card p{font-size:15px;margin:0 0 10px}
.card .ask{color:var(--muted);font-size:14px}
.card .go{font-size:12px;letter-spacing:.16em;text-transform:uppercase;
 font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif;color:var(--muted)}
.note{max-width:62ch}
.note h3{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);
 font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif;margin-bottom:12px}
.note li{margin-bottom:10px;font-size:15px}
</style></head><body>
<section class="hero"><div class="wrap">
 <span class="eyebrow">Черновики сайта · сентябрь 2026</span>
 <h1>Три страницы, которые надо посмотреть</h1>
 <p class="lede">Это не готовый сайт, а два варианта его устройства и одно сравнение раскладок.
 Нужно выбрать направление, а не оценивать детали.</p>
 <div class="cards">%s</div>
</div></section>

<section><div class="wrap note">
 <h3>Что здесь ненастоящее</h3>
 <ul>
  <li><b>Фотографии временные.</b> Они взяты с твоего SmugMug наугад, ты их не отбирала.
   Смотри на то, как они показаны, а не на то, какие именно снимки.</li>
  <li><b>Язык — английский только для черновика.</b> На каком языке будет сайт, ещё не решено.</li>
  <li><b>Тексты и книги</b> взяты из твоего CV. Если где-то ошибка или чего-то не хватает — скажи.</li>
  <li><b>Цен нигде нет</b> и пока не планируется.</li>
  <li><b>Серые прямоугольники</b> на месте обложек или портрета означают, что картинка не загрузилась. Это чинится.</li>
 </ul>
 <h3 style="margin-top:34px">Как смотреть</h3>
 <ul>
  <li>Ленты фотографий и обложек прокручиваются вбок.</li>
  <li>Клик по любому снимку или обложке открывает её крупно. Esc или клик — закрыть.</li>
  <li>Слева внизу есть ссылка «все варианты» — возвращает сюда.</li>
 </ul>
</div></section>
<footer><div class="wrap">Черновик. Собрано Мариной с помощью Claude.</div></footer>
</body></html>""" % (b.CSS, cards())

open(os.path.join(here,"index.html"),"w",encoding="utf-8").write(PAGE)
print("index written", len(PAGE))
