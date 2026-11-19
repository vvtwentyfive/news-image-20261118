# The World in One Image — 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/vvtwentyfive/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/vvtwentyfive/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry for make.fun [`news-image-20261118`](https://make.fun/bounty/news-image-20261118): sum up Wednesday 18 November 2026's
world news in one image. Closes **Friday 20 November 2026, 07:00 WIB**
(2026-11-20T00:00:00Z). $250 pot, top 50 entries paid, 1st place $50.

## The image

A newspaper-front-page collage, 1024×1024 PNG, 110,446 bytes (limit 1 MiB).
Because the AI judge has **no news feed**, every story is labelled in the
image itself — headline + one-line deck + small pictogram — so it reads as a
picture editor would read it.

- **Lead — Shenzhen:** Xi, Putin and Trump to meet; first-ever trilateral
  summit set for Thursday, Xi–Putin talks open on the eve of APEC.
- **The Gulf:** U.S. sinks five Iranian tankers; Tehran hits back at ships
  and a Jordan base; oil nears $93.
- **Ukraine:** Kerch Bridge hit, second night running.
- **Washington:** Peltola flips Alaska — Senate now 56–44 Democrat.
- **India:** Cyclone Akvan bears down on the east coast; evacuations under way.
- **Ticker:** COP31 decisive phase · UN warns of Gaza cold deaths ·
  Jesse Jackson dies at 84 · Huang out at Nvidia · Dhoni retires ·
  Pattinson is the new Bond.

## Files

| File | What it is |
|---|---|
| `entry.png` | The rendered image (1024×1024, 110,446 bytes) |
| `main.py` | Entry program: stdlib-only, copies `entry.png` to `/output/entry.png`, no network |
| `make_news_image.py` | The renderer (PIL + DejaVu, local only) — re-run to regenerate `entry.png` |
| `NEWS-BRIEF.md` | Headline sources and verification notes |
| `LICENSE` | MIT |

## Run it

```sh
python3 main.py   # writes /output/entry.png
```

`main.py` is stdlib-only: it copies `entry.png` to `/output/entry.png`.
No network, no dependencies.

## Regenerate the image

```sh
python3 make_news_image.py   # re-renders entry.png from the headline strings
```

`make_news_image.py` draws the front page with PIL + local DejaVu fonts.
To change a headline, edit the strings in that file and re-run — a
regeneration takes seconds. The image is 1024×1024 PNG, 110,446 bytes (limit 1 MiB).

<sub>Entered on [make.fun](https://make.fun/?ref=073t4skd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
