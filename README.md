# Natasha S. — website (v2)

Static site: content files + templates → `_site/`, published by GitHub Pages.
Natasha edits the content in **Pages CMS**; the design lives in `templates/` and `static/`.

## Layout

| Path | What | Who edits |
|---|---|---|
| `content/` | all texts, books, publications, news, galleries | Natasha (Pages CMS) |
| `media/` | uploaded photos (originals) | Natasha (Pages CMS) |
| `templates/`, `static/` | design | Marina |
| `build.py` | content + templates → `_site/`, resizes photos | Marina |
| `.pages.yml` | what Natasha sees in the editor | Marina |
| `.github/workflows/deploy.yml` | rebuild + publish on every save | — |
| `design/` | private, not pushed: logo, previews, 26 Sept prototypes | Marina |

## Build locally

    pip install pyyaml jinja2 markdown pillow
    python3 build.py --draft            # what the public preview shows; open _site/index.html
    python3 build.py --draft --local    # + press photos awaiting permission (Marina's Mac only — never deploy)

## Status (1 Oct 2026)

Live preview: https://mermina.github.io/natasha-s-site/ — the v2 site (split entrance, Literature, Photography),
with a draft badge and yellow questions for Natasha. Option C, the book-cover layouts, is at `books-layouts.html`
(linked from the draft badge). Options A and B are retired (still in git history).

News: 21 items from Natasha's «Новостная полоса»; several source links per item; one sideways rail that loops.
Press photos (Vísir, RÚV, Grapevine) need permission: until `image_permission: true` they appear only in
`--local` builds, and files in `media/pending/` are git-ignored — the repo is public.

Demo content: gallery photos are SmugMug stand-ins, not Natasha's selection; book covers come from her Drive;
the photography bio is a placeholder.
