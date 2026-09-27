# -*- coding: utf-8 -*-
import os
OUT = os.path.dirname(os.path.abspath(__file__))

PHOTOS = [
 ("Portraits","https://photos.smugmug.com/Masha/i-f45Ks4N/0/MjwG6bckgThmcWb588cpVxTmJ6Gk4zfwG8pJgD485/L/DSCF1171-L.jpg","Masha"),
 ("Portraits","https://photos.smugmug.com/Jelena/i-CrLDH3D/0/Nb6sfHxKPRNdspMB39Cm96fNC9mXZBVRF4TwBgTQh/L/DSCF0114-L.jpg","Jelena"),
 ("Portraits","https://photos.smugmug.com/Alina/i-cN35KvW/0/LKPktMcq9P4hXsjMRZqZ97PVGWLGbsTrktGhshmr8/L/DSCF8828-2-L.jpg","Alina"),
 ("Portraits","https://photos.smugmug.com/Nastja/i-wjz58wm/0/LGPc5QBc5QjcFTRJt66wbqDBZPGHTLt5WkwwbPGLj/L/DSCF3643-L.jpg","Nastja"),
 ("Portraits","https://photos.smugmug.com/El%C3%ADn-%C3%93sk/i-pN666c8/0/MBwsd7gDHr7sQgXnpxFcj3v4nNzRqSK5HfVSFT7gz/L/DSCF7649-L.jpg","Elín Ósk"),
 ("Portraits","https://photos.smugmug.com/Anastasia-studio/i-MbvWPjm/0/NZTFQ9Gj6HwP25jqCwmSczkH9qthzJ2wcNRR9RMvv/X2/DSCF4068-X2.jpg","Anastasia, studio"),
 ("Literary events","https://photos.smugmug.com/Olga-Tokarczuk/i-Dnhv8x4/0/MCznbXnq9zkvr38t78bZq2rw8jXM85wVN9ZpM8JSW/L/DSCF3307-L.jpg","Olga Tokarczuk"),
 ("Literary events","https://photos.smugmug.com/Upplestur-27-mars/i-dzBVNxR/0/MwZPkPRLHNThvhDjnDJsjcjcghhRwCZXx92RGDZbp/X2/DSCF0159-2-X2.jpg","Upplestur, 27 March"),
 ("Literary events","https://photos.smugmug.com/Fischersund-upplestur/i-NJJhxvh/0/KWhdhpR7sgfhMF6L3zHR69SDsF2jzMC2Dhb9hgsDS/XL/DSCF5805-XL.jpg","Fischersund, reading"),
 ("Literary events","https://photos.smugmug.com/Lj%C3%B3%C3%B0sk%C3%B3gur/i-S25NQwP/0/NhKL94fskDBr7vvJTk5qDrKDHZHpgvGNShbtCGDwb/L/DSCF9243-L.jpg","Ljóðskógur"),
 ("Events","https://photos.smugmug.com/Extra-Time-Jazz-Band/i-kpGnXv3/0/KVHWPchJgDR8dpvWs3c5xBLFvjP3crfz3dt7d8S4T/L/DSCF6347-L.jpg","Extra Time Jazz Band"),
 ("Events","https://photos.smugmug.com/Kynvillingagrill/i-hTZkPk5/0/KFTjBnJ2FtLN3T225WS3nwJ2jT3GJW86C4md628bT/L/DSCF0078-L.jpg","Kynvillingagrill"),
 ("Events","https://photos.smugmug.com/Vi%C3%B0ey-S%C3%B6guhringur/i-dV5w2wZ/0/McJNThh4HhM74mf3MrmvhccjP9DkQCjxQLQhC8fBF/L/DSCF8187-2-L.jpg","Viðey, Söguhringur"),
 ("Events","https://photos.smugmug.com/Fr%C3%AD%C3%B0a-T%C3%B3mas-Eyborg/i-x3jqPpj/0/KsQg6JRPxbB7XpdxL8n7jQ8fPhh5bJhFhCkpwvd72/XL/DSCF0589-3-XL.jpg","Fríða, Tómas, Eyborg"),
 ("Personal work","https://photos.smugmug.com/%D0%94%D0%BE%D0%BC%D0%B0/i-3DvgwRV/0/KmtNZwfpNNcV2r82j3Rk4cP6JK4Q8BxG9mBZS4GZH/XL/DSCF9285-XL.jpg","Дома"),
 ("Personal work","https://photos.smugmug.com/H%C3%BAsi%C3%B0/i-hvCbjQH/0/NN9PHsb8FJ6jn2X7r6qXFpghh7pGzfZg2rZZMwKDm/L/DSCF1169-L.jpg","Húsið"),
 ("Personal work","https://photos.smugmug.com/K%C3%A6ri-f%C3%A1viti/i-VwBpmGL/0/MFWq6fGC9Fkd3NwGhKRMZvqpXt3XNv8VwmR5LBnxx/XL/DSCF8803-2-XL.jpg","Kæri fáviti"),
 ("Personal work","https://photos.smugmug.com/Ertu-a%C3%B0-hugsa-um-t%C3%ADmann/i-5kRGbRt/0/MwfVTkZ5R5J5ffVFXvfBDsJrBVStDmQj5CX2FWTkL/L/DSCF9742-L.jpg","Ertu að hugsa um tímann"),
 ("Personal work","https://photos.smugmug.com/Undanbr%C3%B6g%C3%B0/i-nhggQt6/0/NgqV8Q7LMJP5g6cNvmZMDHKwGFhZDkFvH5qnv6pVb/L/DSCF1442-L.jpg","Undanbrögð"),
 ("Personal work","https://photos.smugmug.com/%C3%93/i-vPmfGSQ/0/LPt4cBVpBjT6TS9j5N5j5FxmC4fz2JfTCbZKJh63Q/X2/DSCF6016-X2.jpg","Ó"),
]

LOCAL = {
 "1kEqq9FwawiDllqJW6RjRZ0D1_syT5_AA":"img/mara-cover.jpg",
 "1LC6AjpxIW5vZYOul0otzyo-QNkKqaYwR":"img/skaldreki-cover.jpg",
 "1QJbDG1_gnBajHfMWM48tz0cYZWMLr-4X":"img/maltaka-cover.jpg",
 "1PRlQVM2-pqzLuX6fDTOfBQcABqiGvOdz":"img/polifonia-cover.jpg",
 "1xuNv1bJBMcy7Besaz32hfG1S21Moe-01":"img/magma-cover.jpg",
 "1jxL9Z2jdy6k9P1HhVAfg7zvmx9YCP7A9":"img/odnoi-tsepyu-cover.jpg",
 "1ffFYhKE6KkFz6YqRhSMbB6yFAg-oTHWe":"img/natasha-portrait.jpg",
}

def local(fid):
    return LOCAL.get(fid,"")

def drive(fid, w=1200):
    return "https://drive.google.com/thumbnail?id=%s&sz=w%d" % (fid, w)

PORTRAIT_ID = "1ffFYhKE6KkFz6YqRhSMbB6yFAg-oTHWe"

BOOKS = [
 ("Mara kemur í heimsókn","Poetry","Benedikt, 2025","Maístjarnan 2026","1kEqq9FwawiDllqJW6RjRZ0D1_syT5_AA"),
 ("Skáldreki // Writers adrift","Essays — editor, co-author","Una útgáfuhús, 2023","","1LC6AjpxIW5vZYOul0otzyo-QNkKqaYwR"),
 ("Máltaka á stríðstímum","Poetry","Una útgáfuhús, 2022","Tómas Guðmundsson Prize 2022","1QJbDG1_gnBajHfMWM48tz0cYZWMLr-4X"),
 ("Polífonía af erlendum uppruna","Poetry anthology — editor, co-author","Una útgáfuhús, 2021","","1PRlQVM2-pqzLuX6fDTOfBQcABqiGvOdz"),
 ("Магма / Kvika","Translation of Þóra Hjörleifsdóttir","Дримбук, 2022","","1xuNv1bJBMcy7Besaz32hfG1S21Moe-01"),
 ("Одной цепью","Short story — «Ис в эфтирретт»","Есть смысл, 2021","","1jxL9Z2jdy6k9P1HhVAfg7zvmx9YCP7A9"),
]

WRITING = [
 ("Journalism &amp; essays", [
   "Heimildin — columns, 2023–2024",
   "Víðsjá (RÚV) — columns, 2022",
   "Tímarit Máls og menningar — poetry and essays, 2022–2025",
   "Iceland Review — poetry in English, 2023",
   "Ós pressan — poetry, 2022, 2025",
   "stelkur.is — 2026",
   "gorky.media, batenka.ru, literatice.ru — essays in Russian, 2019–2021",
 ]),
 ("Translation from Icelandic", [
   "Kristín Eiríksdóttir, <em>Tól</em> — into Russian, 2025 (unpublished)",
   "Þóra Hjörleifsdóttir, <em>Kvika</em> — into Russian, Дримбук, 2022",
   "Einar Kári Jóhannesson, «Mávurinn» — into Russian, 2022",
   "Eva Rún Snorradóttir — poetry, into Russian, 2021",
 ]),
 ("Her work in translation", [
   "German — <em>Ein Alb kommt zu Besuch</em>, ELIF Verlag, 2027 (forthcoming)",
   "Swedish — <em>Mara kommer på besök</em>, Ramús förlag, 2026, translated by the author",
   "Italian — poems in <em>Internazionale</em>, 2026",
   "English — essay on Literary Hub, 2023, tr. Larissa Kyzer",
 ]),
]

BIO = """Natasha S. is a poet, translator, journalist and editor. Born in Russia, she has
lived in Iceland since 2012. She holds a BA in journalism from Moscow and a BA in Icelandic as
a second language, with Swedish, from the University of Iceland.
Her first collection of poetry, <em>Máltaka á stríðstímum</em> (2022), received the
Tómas Guðmundsson Literary Prize and was nominated for the Maístjarnan Award. Her second,
<em>Mara kemur í heimsókn</em> (2025), won the Maístjarnan Award in 2026. She edited and
co-authored two anthologies of writing by authors of foreign origin, and in 2023 received
the Icelandic Language Committee's recognition for extending Icelandic as a literary language
to those who did not grow up with it. She photographs writers, readings and people at home."""

CSS = """
:root{--paper:#f6f5f2;--ink:#14110f;--muted:#6b6560;--line:#ddd9d2;--accent:#14110f}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);
 font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
 font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:inherit}
.wrap{max-width:1180px;margin:0 auto;padding:0 28px}
.eyebrow{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);
 font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif}
h1,h2,h3{font-weight:400;letter-spacing:-.01em;margin:0}
h2{font-size:clamp(24px,3.2vw,34px);margin-bottom:6px}
p{margin:0 0 18px}
section{padding:86px 0;border-top:1px solid var(--line)}
section:first-of-type{border-top:none}
.lede{font-size:clamp(19px,2.2vw,23px);line-height:1.5;max-width:46ch;color:var(--ink)}
.meta{font-size:14px;color:var(--muted)}
/* single-line gallery */
.rail{display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;
 padding:6px 28px 26px;scrollbar-width:thin}
.rail figure{margin:0;flex:0 0 auto;scroll-snap-align:center}
.rail img{height:64vh;min-height:340px;width:auto;display:block;background:#e9e6e1;color:transparent;min-width:220px}
.rail figcaption{margin-top:10px;font-size:13px;color:var(--muted);display:flex;
 justify-content:space-between;gap:16px}
.rail figcaption .series{letter-spacing:.14em;text-transform:uppercase;font-size:10px;
 font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif}
.hint{font-size:12px;color:var(--muted);padding:0 28px}
/* books — rail mirroring the photo rail */
.rail.books figure{max-width:46vw;cursor:zoom-in}
.rail figure{cursor:zoom-in}
.rail.books img{height:52vh;min-height:300px;width:auto;object-fit:contain;background:transparent;
 box-shadow:0 1px 0 rgba(0,0,0,.08),0 18px 38px -22px rgba(0,0,0,.45);transition:transform .35s}
.rail.books figure:hover img{transform:translateY(-4px)}
.rail.books .ph{height:52vh;min-height:300px;width:340px;background:#eceae5;display:flex;
 align-items:center;justify-content:center;padding:34px;text-align:center;font-size:21px;line-height:1.25}
.rail.books figcaption{display:block;max-width:340px;margin-top:14px}
.rail.books figcaption .t{font-size:16px}
.rail.books figcaption .m{font-size:13px;color:var(--muted);margin-top:2px}
.rail.books figcaption .prize{margin-top:6px;font-size:10px;letter-spacing:.14em;text-transform:uppercase;
 font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif;color:var(--muted)}
/* lightbox */
.lb{position:fixed;inset:0;background:rgba(20,17,15,.94);display:none;z-index:80;
 align-items:center;justify-content:center;flex-direction:column;gap:22px;padding:5vh 5vw;cursor:zoom-out}
.lb.on{display:flex}
.lb img{max-height:74vh;max-width:88vw;object-fit:contain;box-shadow:0 30px 70px -30px #000}
.lb .cap{color:#f6f5f2;text-align:center;max-width:52ch}
.lb .cap .m{font-size:13px;opacity:.65;margin-top:4px}
.lb .x{position:absolute;top:22px;right:28px;color:#f6f5f2;font-size:13px;letter-spacing:.16em;
 text-transform:uppercase;font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif;opacity:.7}
/* writing */
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:44px;margin-top:34px}
.cols ul{list-style:none;margin:14px 0 0;padding:0}
.cols li{padding:9px 0;border-bottom:1px solid var(--line);font-size:15px}
.cols h3{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);
 font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif}
/* about */
.about{display:grid;grid-template-columns:minmax(240px,340px) 1fr;gap:56px;align-items:start}
.about img{width:100%;min-height:380px;display:block;background:#e9e6e1;filter:grayscale(1);color:transparent}
.about .body{max-width:60ch}
footer{padding:60px 0 80px;border-top:1px solid var(--line);font-size:14px;color:var(--muted)}
footer a{text-decoration:none;border-bottom:1px solid var(--line)}
.draft a:hover{text-decoration:underline !important}
.draft{position:fixed;left:0;bottom:0;background:var(--ink);color:var(--paper);
 font-size:10px;letter-spacing:.18em;text-transform:uppercase;padding:6px 12px;z-index:50;
 font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif}
@media(max-width:720px){.about{grid-template-columns:1fr;gap:28px}.rail img{height:46vh;min-height:0}}
"""

def rail_html():
    out=[]
    for series,url,cap in PHOTOS:
        out.append('<figure onclick="lb(this)" data-big="%s" data-title="%s" data-meta="%s">'
                   '<img loading="lazy" src="%s" alt="%s">'
                   '<figcaption><span>%s</span><span class="series">%s</span></figcaption></figure>'
                   %(url,cap,series,url,cap,cap,series))
    return "\n".join(out)

def books_html():
    out=[]
    for title,kind,pub,prize,fid in BOOKS:
        big = local(fid) or drive(fid,1400)
        cap = "%s \u2014 %s, %s" % (kind, pub, prize) if prize else "%s \u2014 %s" % (kind, pub)
        img = '<img loading="lazy" src="%s" data-fallback="%s" alt="" onerror="fb(this)">'%(local(fid),drive(fid,700))
        prize_html = '<div class="prize">%s</div>'%prize if prize else ''
        out.append('<figure onclick="lb(this)" data-big="%s" data-title="%s" data-meta="%s">%s'
                   '<figcaption><div class="t">%s</div><div class="m">%s</div><div class="m">%s</div>%s</figcaption></figure>'
                   %(big,title,cap,img,title,kind,pub,prize_html))
    return "\n".join(out)

def writing_html():
    out=[]
    for head,items in WRITING:
        lis="".join("<li>%s</li>"%i for i in items)
        out.append('<div><h3>%s</h3><ul>%s</ul></div>'%(head,lis))
    return "\n".join(out)

PHOTO_SECTION = """<section id="photography">
  <div class="wrap"><span class="eyebrow">Photography</span>
    <h2>Writers, readings, people at home</h2>
    <p class="lede">Portraits, literary events and personal series. Commissions taken in Reykjav&iacute;k &mdash; portraits, readings and events, family sessions at home.</p>
  </div>
  <div class="rail">%s</div>
  <p class="hint">Scroll sideways. Full archive: <a href="https://natashas.smugmug.com/">natashas.smugmug.com</a></p>
</section>""" % rail_html()

BOOKS_SECTION = """<section id="books">
  <div class="wrap"><span class="eyebrow">Books</span>
    <h2>Poetry, anthologies, translation</h2>
  </div>
  <div class="rail books">%s</div>
  <p class="hint">Scroll sideways \u00b7 click a cover to see it whole</p>
</section>

""" % books_html()

LIGHTBOX = """<div class="lb" id="lb" onclick="this.classList.remove('on')">
  <span class="x">Close</span>
  <img id="lb-img" src="" alt="">
  <div class="cap"><div id="lb-title"></div><div class="m" id="lb-meta"></div></div>
</div>

<script>
function fb(img){
  var alt=img.getAttribute('data-fallback');
  if(alt && img.src.indexOf('drive.google.com')===-1){ img.removeAttribute('data-fallback'); img.src=alt; return; }
  ph(img);
}
function ph(img){
  var f=img.closest('figure');
  var d=document.createElement('div');
  d.className='ph';
  d.textContent=f?f.getAttribute('data-title'):'';
  img.replaceWith(d);
}
function lb(fig){
  var big=fig.getAttribute('data-big');
  if(!fig.querySelector('img')) return;
  document.getElementById('lb-img').src=big;
  document.getElementById('lb-title').textContent=fig.getAttribute('data-title');
  document.getElementById('lb-meta').textContent=fig.getAttribute('data-meta');
  document.getElementById('lb').classList.add('on');
}
document.addEventListener('keydown',function(e){if(e.key==='Escape'){var l=document.getElementById('lb');if(l)l.classList.remove('on');}});
</script>"""

WRITING_SECTION = """<section id="writing">
  <div class="wrap"><span class="eyebrow">Writing</span>
    <h2>Published work</h2>
    <div class="cols">%s</div>
  </div>
</section>""" % writing_html()

ABOUT_SECTION = """<section id="about">
  <div class="wrap"><span class="eyebrow">About</span>
    <div class="about" style="margin-top:28px">
      <img src="%s" data-fallback="%s" alt="Natasha S." onerror="fb(this)">
      <div class="body"><h2 style="margin-bottom:18px">Natasha S.</h2><p>%s</p>
      <p class="meta">Reykjav&iacute;k &middot; Icelandic, Russian, English<br>
      <a href="mailto:natasha.s.writer@gmail.com">natasha.s.writer@gmail.com</a></p></div>
    </div>
  </div>
</section>""" % (local(PORTRAIT_ID), drive(PORTRAIT_ID,1000), BIO)

FOOTER = """<footer><div class="wrap">Natasha S. &mdash; Reykjav&iacute;k &middot;
<a href="mailto:natasha.s.writer@gmail.com">natasha.s.writer@gmail.com</a> &middot;
<a href="https://natashas.smugmug.com/">Photo archive</a></div></footer>
<div class="draft"><a href="index.html" style="color:inherit;text-decoration:none">&larr; все варианты</a> &middot; черновик</div>"""

# ---------- OPTION A ----------
A = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Natasha S. &mdash; option A, one site</title>
<style>%s
header.top{position:sticky;top:0;background:rgba(246,245,242,.93);backdrop-filter:blur(8px);
 border-bottom:1px solid var(--line);z-index:40}
header.top .wrap{display:flex;justify-content:space-between;align-items:baseline;padding-top:16px;padding-bottom:16px}
header.top nav a{margin-left:26px;text-decoration:none;font-size:12px;letter-spacing:.16em;
 text-transform:uppercase;font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif;color:var(--muted)}
header.top nav a:hover{color:var(--ink)}
.name{font-size:17px;letter-spacing:.2em;text-transform:uppercase}
.hero{padding:120px 0 96px}
.hero h1{font-size:clamp(38px,7vw,82px);line-height:1.02;max-width:14ch}
.hero p{margin-top:26px}
@media(max-width:720px){header.top .wrap{flex-direction:column;gap:10px}header.top nav a{margin:0 20px 0 0}}
</style></head><body>
<header class="top"><div class="wrap"><span class="name">Natasha S.</span>
<nav><a href="#books">Books</a><a href="#photography">Photography</a><a href="#writing">Writing</a><a href="#about">About</a></nav>
</div></header>
<section class="hero"><div class="wrap">
  <h1>Poet, translator and photographer in Reykjav&iacute;k</h1>
  <p class="lede">Two poetry collections in Icelandic, translations from Icelandic into Russian,
  and photographs of writers, readings and people at home.</p>
</div></section>
%s
%s
%s
%s
%s
%s
</body></html>""" % (CSS, BOOKS_SECTION, PHOTO_SECTION, WRITING_SECTION, ABOUT_SECTION, FOOTER, LIGHTBOX)

# ---------- OPTION B ----------
B = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Natasha S. &mdash; option B, two sides</title>
<style>%s
.gate{position:fixed;inset:0;display:flex;z-index:60;background:var(--paper)}
.gate .half{flex:1;position:relative;display:flex;flex-direction:column;align-items:center;
 justify-content:center;cursor:pointer;transition:flex .55s cubic-bezier(.4,0,.2,1);overflow:hidden}
.gate .half:hover{flex:1.25}
.gate .half.photo{background:#14110f;color:#f6f5f2}
.gate .half.photo img{position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;
 opacity:.5;filter:grayscale(1);transition:opacity .55s}
.gate .half.photo:hover img{opacity:.72}
.gate .half .label{position:relative;text-align:center;padding:24px}
.gate .half h2{font-size:clamp(28px,4.6vw,54px)}
.gate .half .sub{margin-top:12px;font-size:12px;letter-spacing:.2em;text-transform:uppercase;
 font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif;opacity:.7}
.gate .who{position:absolute;top:30px;left:0;right:0;text-align:center;font-size:12px;
 letter-spacing:.3em;text-transform:uppercase;z-index:2;mix-blend-mode:difference;color:#888}
.site{display:none}
.site.on{display:block}
header.top{position:sticky;top:0;background:rgba(246,245,242,.93);backdrop-filter:blur(8px);
 border-bottom:1px solid var(--line);z-index:40}
header.top .wrap{display:flex;justify-content:space-between;align-items:baseline;padding:16px 28px}
.switch a{margin-left:22px;text-decoration:none;font-size:12px;letter-spacing:.16em;
 text-transform:uppercase;font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif;color:var(--muted)}
.switch a.on{color:var(--ink);border-bottom:1px solid var(--ink)}
.name{font-size:16px;letter-spacing:.2em;text-transform:uppercase}
.hero{padding:96px 0 70px}
.hero h1{font-size:clamp(34px,6vw,68px);line-height:1.04;max-width:15ch}
.hero p{margin-top:24px}
@media(max-width:720px){.gate{flex-direction:column}}
</style></head><body>

<div class="gate" id="gate">
  <div class="who">Natasha S.</div>
  <div class="half photo" onclick="enter('photography')">
    <img src="%s" alt="">
    <div class="label"><h2>Photography</h2><div class="sub">Portraits &middot; readings &middot; events</div></div>
  </div>
  <div class="half" onclick="enter('literature')">
    <div class="label"><h2>Literature</h2><div class="sub">Poetry &middot; essays &middot; translation</div></div>
  </div>
</div>

<div class="site" id="site">
<header class="top"><div class="wrap"><span class="name">Natasha S.</span>
<nav class="switch"><a href="#" id="tab-photography" onclick="enter('photography');return false">Photography</a><a href="#" id="tab-literature" onclick="enter('literature');return false">Literature</a><a href="#" onclick="document.getElementById('gate').style.display='flex';return false">Entrance</a></nav>
</div></header>

<div id="side-photography">
  <section class="hero"><div class="wrap">
    <h1>Writers, readings, people at home</h1>
    <p class="lede">Portraits and documentary work in Reykjav&iacute;k. Commissions: portraits,
    readings and literary events, family sessions at home.</p>
  </div></section>
  %s
  %s
</div>

<div id="side-literature">
  <section class="hero"><div class="wrap">
    <h1>Poet, translator, editor</h1>
    <p class="lede">Two poetry collections in Icelandic, two edited anthologies, and translation
    from Icelandic into Russian.</p>
  </div></section>
  %s
  %s
  %s
</div>
%s
</div>
%s

<script>
function enter(side){
  document.getElementById('gate').style.display='none';
  document.getElementById('site').classList.add('on');
  var p=side==='photography';
  document.getElementById('side-photography').style.display=p?'block':'none';
  document.getElementById('side-literature').style.display=p?'none':'block';
  document.getElementById('tab-photography').className=p?'on':'';
  document.getElementById('tab-literature').className=p?'':'on';
  window.scrollTo(0,0);
}
</script>
</body></html>""" % (CSS, PHOTOS[6][1], PHOTO_SECTION, ABOUT_SECTION, BOOKS_SECTION, WRITING_SECTION, ABOUT_SECTION, FOOTER, LIGHTBOX)

open(os.path.join(OUT,"option-a-one-site.html"),"w",encoding="utf-8").write(A)
open(os.path.join(OUT,"option-b-two-sides.html"),"w",encoding="utf-8").write(B)
print("written", len(A), len(B))
