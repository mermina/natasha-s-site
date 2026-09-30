# -*- coding: utf-8 -*-
"""Build Natasha S. site: content/ + templates/ -> _site/

Content is edited by Natasha in Pages CMS; design lives in templates/ and static/.
Run:  python3 build.py            (writes _site/)
      python3 build.py --draft    (adds a "draft" badge)
"""
import os, sys, glob, shutil, datetime
import yaml, markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "_site")
C = lambda *p: os.path.join(ROOT, "content", *p)
DRAFT = "--draft" in sys.argv

def load_yml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def load_md(path):
    """Front matter + markdown body -> dict (body rendered as .html)."""
    text = open(path, encoding="utf-8").read()
    meta, body = {}, text
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    meta["html"] = Markup(markdown.markdown(body.strip()))
    meta["slug"] = os.path.splitext(os.path.basename(path))[0]
    return meta

# ---- images: remote URLs pass through; local uploads get web-size copies ----
def img(src, width=1200):
    if not src:
        return ""
    if src.startswith(("http://", "https://")):
        return src
    rel = src.lstrip("/")
    srcpath = os.path.join(ROOT, rel)
    if not os.path.exists(srcpath):
        print("  ! missing image:", rel)
        return rel
    name = os.path.splitext(os.path.basename(rel))[0] + ".jpg"
    outrel = "media/w%d/%s" % (width, name)
    outpath = os.path.join(OUT, outrel)
    if not os.path.exists(outpath) or os.path.getmtime(outpath) < os.path.getmtime(srcpath):
        from PIL import Image, ImageOps
        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        im = ImageOps.exif_transpose(Image.open(srcpath)).convert("RGB")
        im.thumbnail((width, width))
        im.save(outpath, "JPEG", quality=82, optimize=True, progressive=True)
    return outrel

MONTHS = "January February March April May June July August September October November December".split()
def when(d, precision):
    d = d if isinstance(d, datetime.date) else datetime.date.fromisoformat(str(d))
    if precision == "year":
        return str(d.year)
    if precision == "month":
        return "%s %d" % (MONTHS[d.month - 1], d.year)
    return "%d %s %d" % (d.day, MONTHS[d.month - 1], d.year)

def main():
    site = load_yml(C("site.yml"))
    books = [b for b in load_yml(C("books.yml")).get("books", []) if b.get("show", True)]
    published = []
    for g in load_yml(C("published.yml")).get("groups", []):
        items = [i for i in g.get("items", []) if i.get("show", True)]
        if items:
            published.append({"heading": g["heading"], "items": items})
    news = [load_md(p) for p in glob.glob(C("news", "*.md"))]
    news = [n for n in news if n.get("show", True)]
    for n in news:
        n["when"] = when(n["date"], n.get("date_precision", "day"))
    news.sort(key=lambda n: str(n["date"]), reverse=True)
    galleries = [load_md(p) for p in glob.glob(C("galleries", "*.md"))]
    galleries = [g for g in galleries if g.get("show", True) and g.get("photos")]
    for g in galleries:
        g["cover"] = g.get("cover") or g["photos"][0]["image"]
    galleries.sort(key=lambda g: (g.get("order", 99), g["title"]))

    os.makedirs(OUT, exist_ok=True)
    shutil.copytree(os.path.join(ROOT, "static"), os.path.join(OUT, "static"), dirs_exist_ok=True)

    env = Environment(loader=FileSystemLoader(os.path.join(ROOT, "templates")), autoescape=select_autoescape(["html"]))
    env.filters["img"] = img
    common = dict(site=site, root="", draft=DRAFT)

    def write(name, tpl, **ctx):
        html = env.get_template(tpl).render(**common, **ctx)
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print("  wrote", name)

    write("index.html", "index.html", side=None)
    write("literature.html", "literature.html", side="literature",
          about=load_md(C("literature-about.md")), books=books, published=published, news=news)
    # Photography overview: one big cover per category, one under another (as sergeisarakhanov.com/projects).
    # Inside a gallery, two layouts for now (decision pending), switchable on draft builds:
    #   line    — photos in one sideways line (wheel / arrows / swipe)   photography-<slug>.html
    #   stacked — large photos one under another                          photography-stacked-<slug>.html
    photo_about = load_md(C("photography-about.md"))
    write("photography.html", "photography.html", side="photography",
          about=photo_about, galleries=galleries, prefix="photography-")
    G = {"line": ("photography-", "gallery.html"), "stacked": ("photography-stacked-", "gallery-stacked.html")}
    for lay, (prefix, tpl) in G.items():
        for g in galleries:
            links = [(lab.capitalize(), "%s%s.html" % (G[lab][0], g["slug"]), lab == lay) for lab in G]
            write("%s%s.html" % (prefix, g["slug"]), tpl, side="photography", g=g,
                  back="photography.html", variant_links=links)
    open(os.path.join(OUT, ".nojekyll"), "w").close()

if __name__ == "__main__":
    main()
