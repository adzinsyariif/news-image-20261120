# One Day — 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/adzinsyariif/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/adzinsyariif/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

An entry for the make.fun bounty ["Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120).

**One Day — 20 November 2026** is a one-page newspaper for Friday 20 November
2026. The watercolour hero shows the story of the day: a glowing red chart
plunging down a wall of trading screens above panicked traders, the skylines
of New York and Tokyo under storm clouds — the global sell-off that deepened
as Wall Street fell for a fifth straight session and the Nikkei dropped 4.8%,
a day after Anthropic's record market debut. Below the fold, eight panels
carry the rest of the day: the Shenzhen summit's aftermath — big symbolism,
no breakthrough on Ukraine or Iran; Russian strikes on Kyiv's bridges that
killed eight; Russian missiles and a drone breaching Polish airspace; Saudi
defences intercepting another Houthi missile and five drones over Riyadh;
Italy's EUR 805 million fine on Meta over Android photo access; the FAA
ground stop that stranded 1.5 million travellers; President Prabowo's return
to Jakarta with nearly Rp1,600 trillion in investment pledges; and Kenya
discharging its last Ebola patient, 37 days after its first case.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only, no network) creates the output
directory when needed and copies this repository's `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). It is deterministic:
every run writes byte-identical output.

## Layout

- `main.ts` — the program: publishes `entry.png` to the output path.
- `entry.png` — the finished 1024×1024 front page (PNG, under 1 MiB).
- `build_frontpage.py` — the Python/PIL script that composed `entry.png` from
  the generated market-crash artwork: masthead, dateline, hero crop, headline
  band and the eight-story grid, with all lettering rendered as vector-sharp
  text.
- `LICENSE` — MIT.

## License

MIT — see `LICENSE`.
