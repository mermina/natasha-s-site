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
| `legacy/` | the 26 Sept prototypes (options A/B/C) | archive |

## Build locally

    pip install pyyaml jinja2 markdown pillow
    python3 build.py --draft      # open _site/index.html

## Status (30 Sept 2026)

Demo content: photos are SmugMug stand-ins sorted by Marina, not Natasha's selection;
book covers come from Drive links that only load for Marina; the photography bio is a placeholder.
