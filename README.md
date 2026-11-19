# Sum up 18 November's world news in one image

Entry for the make.fun bounty
[Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118)
— $250, 50 places paid. Deadline: Friday 20 November 2026, 00:00 UTC
(08:00 WITA).

## The image

A 1024×1024 infographic, "WORLD NEWS — Wednesday 18 November 2026",
summarising the day in five stories across five regions:

1. **Summit in Shenzhen** — Xi meets Putin ahead of talks with Trump
2. **Strikes in the Gulf** — Iran hits Kuwait and Bahrain after US strike
3. **Kerch Bridge hit** — Ukraine attack collapses part of Crimea bridge
4. **US Senate flips** — Peltola wins Alaska; Democrats reach 56–44
5. **Ebola surges in Congo** — Outbreak passes 11,000 cases in DR Congo

The image was drawn from scratch for this entry (no copied photo or
artwork). It names the date twice, in the header and the footer.

## How it runs

`main.py` is Python 3.13, standard library only. It copies the
`entry.png` shipped in this repository to `/output/entry.png`
(or `$MAKEFUN_OUTPUT_DIR/entry.png` when that is set, for local runs):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network, no third-party packages, deterministic — two runs write
byte-identical output.

## Files

- `main.py` — entrypoint, stdlib only
- `entry.png` — the image, 1024×1024, 90,456 bytes (< 1 MiB)
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
