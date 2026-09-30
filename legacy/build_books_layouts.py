# -*- coding: utf-8 -*-
import os, importlib.util
here=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location("b", os.path.join(here,"build.py"))
b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)

def asym_html():
    # asymmetric placement, every cover large: 12-col grid, varied column starts
    slots=[("1","5","0"),("7","6","90"),("2","5","40"),("8","5","140"),("1","5","40"),("7","6","110")]
    out=[]
    for (title,kind,pub,prize,fid),(col,span,top) in zip(b.BOOKS,slots):
        cap = "%s \u2014 %s, %s"%(kind,pub,prize) if prize else "%s \u2014 %s"%(kind,pub)
        prize_html='<div class="prize">%s</div>'%prize if prize else ''
        out.append('<figure style="grid-column:%s / span %s;margin-top:%spx" onclick="lb(this)" data-big="%s" data-title="%s" data-meta="%s">'
          '<img loading="lazy" src="%s" alt="" onerror="ph(this)">'
          '<figcaption><div class="t">%s</div><div class="m">%s</div><div class="m">%s</div>%s</figcaption></figure>'
          %(col,span,top,b.drive(fid,1400),title,cap,b.drive(fid,1000),title,kind,pub,prize_html))
    return "\n".join(out)

def mosaic_html():
    # staggered, non-linear: varied widths and vertical offsets
    sizes=[("w-l","off-0"),("w-s","off-3"),("w-m","off-1"),("w-l","off-2"),("w-s","off-0"),("w-m","off-2")]
    out=[]
    for (title,kind,pub,prize,fid),(w,off) in zip(b.BOOKS,sizes):
        cap = "%s — %s, %s"%(kind,pub,prize) if prize else "%s — %s"%(kind,pub)
        prize_html='<div class="prize">%s</div>'%prize if prize else ''
        out.append('<figure class="%s %s" onclick="lb(this)" data-big="%s" data-title="%s" data-meta="%s">'
          '<img loading="lazy" src="%s" alt="" onerror="ph(this)">'
          '<figcaption><div class="t">%s</div><div class="m">%s</div><div class="m">%s</div>%s</figcaption></figure>'
          %(w,off,b.drive(fid,1400),title,cap,b.drive(fid,800),title,kind,pub,prize_html))
    return "\n".join(out)

EXTRA = """
.mosaic{display:flex;flex-wrap:wrap;gap:60px 56px;align-items:flex-start;margin-top:40px}
.mosaic figure{margin:0;cursor:zoom-in}
.mosaic img{width:100%;height:auto;display:block;color:transparent;background:transparent;
 box-shadow:0 1px 0 rgba(0,0,0,.08),0 22px 44px -26px rgba(0,0,0,.5);transition:transform .35s}
.mosaic figure:hover img{transform:translateY(-5px)}
.mosaic .ph{width:100%;aspect-ratio:2/3;background:#eceae5;display:flex;align-items:center;
 justify-content:center;padding:26px;text-align:center;font-size:19px;line-height:1.25}
.mosaic figcaption{margin-top:14px}
.mosaic figcaption .t{font-size:16px}
.mosaic figcaption .m{font-size:13px;color:var(--muted);margin-top:2px}
.mosaic figcaption .prize{margin-top:6px;font-size:10px;letter-spacing:.14em;text-transform:uppercase;
 font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif;color:var(--muted)}
.w-l{flex:0 0 340px}.w-m{flex:0 0 260px}.w-s{flex:0 0 200px}
.off-1{margin-top:52px}.off-2{margin-top:104px}.off-3{margin-top:150px}
.asym{display:grid;grid-template-columns:repeat(12,1fr);gap:34px;margin-top:44px}
.asym figure{margin:0;cursor:zoom-in}
.asym img{width:100%;height:auto;min-height:340px;object-fit:contain;display:block;color:transparent;background:transparent;
 box-shadow:0 1px 0 rgba(0,0,0,.08),0 26px 50px -28px rgba(0,0,0,.5);transition:transform .35s}
.asym figure:hover img{transform:translateY(-6px)}
.asym .ph{width:100%;aspect-ratio:2/3;background:#eceae5;display:flex;align-items:center;
 justify-content:center;padding:30px;text-align:center;font-size:22px;line-height:1.25}
.asym figcaption{margin-top:16px}
.asym figcaption .t{font-size:17px}
.asym figcaption .m{font-size:13px;color:var(--muted);margin-top:2px}
.asym figcaption .prize{margin-top:6px;font-size:10px;letter-spacing:.14em;text-transform:uppercase;
 font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif;color:var(--muted)}
@media(max-width:820px){.asym{grid-template-columns:1fr}.asym figure{grid-column:1/-1 !important;margin-top:0 !important}}
.switchbar{position:sticky;top:0;background:rgba(246,245,242,.94);backdrop-filter:blur(8px);
 border-bottom:1px solid var(--line);z-index:40;padding:14px 28px;display:flex;gap:26px;align-items:baseline}
.switchbar a{text-decoration:none;font-size:12px;letter-spacing:.16em;text-transform:uppercase;
 font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif;color:var(--muted)}
.switchbar a.on{color:var(--ink);border-bottom:1px solid var(--ink)}
@media(max-width:720px){.w-l,.w-m,.w-s{flex:0 0 46%;}.off-1,.off-2,.off-3{margin-top:0}}
"""

PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Option C — books, three layouts</title>
<style>%s%s</style></head><body>
<div class="switchbar"><strong style="font-size:13px;letter-spacing:.2em;text-transform:uppercase">Option C — books, three layouts</strong>
<a href="#rail" id="t1" class="on" onclick="show(1);return false">1 · Rail</a>
<a href="#staggered" id="t2" onclick="show(2);return false">2 · Staggered</a>
<a href="#asymmetric" id="t3" onclick="show(3);return false">3 · Asymmetric, all large</a></div>

<div id="v1">
<section><div class="wrap"><span class="eyebrow">Layout 1</span>
<h2>One line, scrolled sideways</h2>
<p class="lede">Mirrors the photography rail: same gesture, same rhythm. Covers whole, never cropped.
Click a cover to see it large.</p></div>
<div class="rail books">%s</div>
<p class="hint">Scroll sideways · click a cover to see it whole</p>
</section></div>

<div id="v2" style="display:none">
<section><div class="wrap"><span class="eyebrow">Layout 2</span>
<h2>Staggered, not in a row</h2>
<p class="lede">Covers at different sizes and heights, the way books sit on a table rather than on a shelf.
Nothing is cropped; click a cover to see it large.</p>
<div class="mosaic">%s</div></div>
</section></div>
<div id="v3" style="display:none">
<section><div class="wrap"><span class="eyebrow">Layout 3</span>
<h2>Asymmetric, every cover large</h2>
<p class="lede">Same refusal of the grid as layout 2, but nothing is shrunk: each cover is given
real size and its own position on the page. Click a cover to see it larger still.</p>
<div class="asym">%s</div></div>
</section></div>
%s
<script>
var HASHES=['#rail','#staggered','#asymmetric'];
function show(n,keepHash){
 for(var i=1;i<=3;i++){
   document.getElementById('v'+i).style.display=(n===i)?'block':'none';
   document.getElementById('t'+i).className=(n===i)?'on':'';
 }
 if(!keepHash && history.replaceState) history.replaceState(null,'',HASHES[n-1]);
 window.scrollTo(0,0);
}
(function(){
 var i=HASHES.indexOf(location.hash);
 if(i>-1) show(i+1,true);
})();
window.addEventListener('hashchange',function(){
 var i=HASHES.indexOf(location.hash);
 if(i>-1) show(i+1,true);
});
</script>
<div class="draft"><a href="index.html" style="color:inherit;text-decoration:none">← все варианты</a> · черновик</div>
</body></html>""" % (b.CSS, EXTRA, b.books_html(), mosaic_html(), asym_html(), b.LIGHTBOX)

open(os.path.join(here,"books-layouts.html"),"w",encoding="utf-8").write(PAGE)
print("written", len(PAGE))
