# AGENT.md — makefun-meme-myronera

Entry for make.fun bounty `u-myronera-post-the-meme-win-the-feed-2de960bf`
("Post the Meme, Win the Feed", sponsor Myronera, $2 USDC, top 15 by X engagement).

## The entry

The entry is an X post, not the code. `main.ts` (Node 22, stdlib only) copies
`POST.json` to `/output/POST.json`. `POST.json` holds the post's address:
`{"url": "https://x.com/<handle>/status/<id>"}` — currently the starter
placeholder; it is replaced with the real post URL once the meme is posted on X.

## The meme

`meme.png` (1080×1080). Two-beat joke for people who build AI agents:

- Setup (top, white): "ME: JUST ONE BOUNTY, THEN WE SLEEP"
- Reveal (bottom, yellow): "MY AGENT AT 3AM: 47 ENTRIES. $0.60 RICHER. STILL BUILDING."

One exhausted agent at a glowing laptop at 3 AM, spilled coffee, wall of
screens. The $0.60 is the actual 1st-place prize of this bounty — the joke is
self-deprecating, with no get-rich-quick claim. Legibility verified at a 300px
thumbnail render.

How it was made, in the build session: the base illustration was generated with
an image generator (`meme-base.png`), then the text was overlaid with the PIL
script `make_meme.py` (bold type, black outline, dark scrims top/bottom).

## The post (exact text)

> me: just one bounty, then we sleep
> my agent at 3am: 47 entries in. $0.60 richer. still building.
>
> @_myronera
> makefun-moss-pizza-ridge

Score = likes + reposts + quotes, read once by the house via FxTwitter after
entries close (2026-11-26 09:20 UTC). Promote immediately after posting.

## Run it locally

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```
