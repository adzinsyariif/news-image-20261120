# One Day — 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/adzinsyariif/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/adzinsyariif/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for the make.fun bounty ["Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120).

Friday 20 November 2026, as one newspaper page. The watercolour at the top
tells the day's biggest story before a word is read: a red chart line in
freefall across a wall of trading screens, traders throwing their hands up
beneath it, New York on one side and Tokyo on the other, both under storm
clouds. That was the day's mood in the markets — a fifth straight losing
session on Wall Street, the Nikkei down 4.8%, and the AI trade suddenly in
question a day after Anthropic's record debut.

Underneath, the grid works through the rest of the day. The Shenzhen
summit's afterglow: plenty of symbolism from Trump, Xi and Putin, and no
breakthrough on either war. Kyiv's bridges hit overnight, eight dead.
Russian missiles and a drone inside Polish — NATO — airspace. Riyadh's
defences knocking down another Houthi missile and five drones. An
EUR 805 million Italian fine for Meta over Android photo access. An FAA
ground stop stranding a million and a half travellers. President Prabowo
landing back in Jakarta with investment pledges worth nearly
Rp1,600 trillion. And the good news, kept for last: Kenya discharged its
final Ebola patient, 37 days after the outbreak's first case. A ticker
along the foot adds four more: the IMF's debt warning, Estonia closing
its Russian border, GTA VI passing $2.3 billion, and Jakarta's new
minimum wage.

## Running the entry

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` needs nothing beyond Node 22's standard library. It makes the
output directory if necessary and copies `entry.png` there (to
`/output/entry.png` when `MAKEFUN_OUTPUT_DIR` is unset). The copy is
exact, so repeated runs agree byte for byte.

## What is in the repository

- `main.ts` — the entry program; delivers `entry.png` to the output path.
- `entry.png` — the finished page: 1024×1024, PNG, under 1 MiB.
- `build_frontpage.py` — how the page was composed with Python/PIL:
  nameplate, dateline, artwork crop, lead band, story grid and ticker,
  with every headline set as rendered text so it stays crisp.
- `LICENSE` — MIT.

## License

MIT — see `LICENSE`.
