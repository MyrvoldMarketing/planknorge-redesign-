# Plank Norge redesign — handoff

Static HTML/CSS/JS prototype of a redesigned **planknorge.no** (Norwegian premium wood-flooring co., Stavanger).
Brief: match **chevronparquet.com** layout/aesthetic, but with **Plank's own fonts/branding**. Deploys via cPanel (`.cpanel.yml`).

## Run / preview
- No-cache dev server on **port 5500**: `python3 devserver.py` (project root). Sends `no-store` so every refresh is fresh.
- Claude Code preview: launch config **`planknorge`** in `~/CC/.claude/launch.json` runs `devserver.py`.
- Open `http://localhost:5500/index.html`. The preview screenshot tool has been unreliable for the home page (stale/scaled frames) — trust live DOM evals / the real browser over screenshots.

## Pages (12)
`index.html` (home) · `chevron.html` `plankegulv.html`(=“Plank”) `fiskeben.html` `heltre.html` (4 products) · `arkitekt.html` `designgulv.html` `inspirasjon.html` `om.html` `ditt-design.html` `konsultasjon.html` `kontakt.html`.

## Architecture
- **Shared header + footer + chat bubble** are injected by `script.js` into `<div id="site-header">` / `<div id="site-footer">`. Active nav item via `<body data-page="…">`. Edit nav/footer in **one place** (`NAV_COLUMNS` / `buildFooter()` in script.js).
- **Product pages are generated** from one template: `tools/gen_products.py` (PRESERVED here; was in /tmp). It builds chevron/plankegulv/fiskeben/heltre identically except hero copy/image. To change all 4 product pages, edit the template + re-run: `python3 tools/gen_products.py`. (Surface swatches + the 12-variant list live in this template.)
- `styles.css` — all styling. `script.js` — chrome injection, floor slider, info box, tabs, variant swatch swap, cursor-light, Lenis init.

## Design system
- **Type:** one sans everywhere — **Source Sans 3** (variable, loaded `wght@300..700`). Playfair Display was tried then removed (owner wanted all-sans / wanted titles to match the slider names). Headings use `--font-display` (currently = the body sans).
- **Palette:** cream `#EEEDE7`, ink `#161513`, secondary `#5f5b52`, lines `#c9c5ba`/`#d8d5cc`.
- **Side padding:** 30px (matches chevronparquet; was 40 → changed site-wide).
- **Header:** logo left (PLANK png, height 60px, `margin-left:-28px` to offset the PNG's transparent left padding so the “P” aligns to content edge). Nav = **4 columns** (`grid-template-columns:46.4% auto 1fr` → starts ~44–46%, right-aligned), font 14.5px, light, slightly condensed (`transform:scaleX(1.07) scaleY(.93)`), col gap 56px, tight rows. Search right.
- **cta-icon:** circle with a crisp CSS-border chevron (`.cta-icon::before`, rotated). Applies site-wide.
- **Scroll:** smooth/weighty via **Lenis** (vendored `assets/js/lenis.min.js`, init in script.js, `lerp:0.08`; disabled for reduced-motion).
- Cache-busting `?v=2` on css/js `<link>`/`<script>` in all pages (bump if needext).

## Home (index.html)
- **Hero grid:** 4 tiles, `grid-template-columns:2.08fr 2.08fr 1fr 1fr`, gap 18px, all images **4:5**, top-aligned, captions ABOVE (`.hero-caption` 15px/weight 450). Tile 1 = looping **`nature-hero.mp4`** (reindeer drone). Tile 2 = `tregulv-rom.jpg`. Cursor-following **soft light** overlay on hover (`.hero-tile figure::after`, JS lerps `--mx/--my`).
- **Collab section** (`.collab`, full-viewport-height, image full-bleed to right edge): left text indented `padding-left:48px`, title **“MØNSTRE I TRE”** (`.collab-mark`, sans uppercase 0.16em — matches slider names), lead, 4 CTAs grouped (Se mer/Få et tilbud/Bestill vareprøve/Book et møte), and an expandable **“Mer om <floor>” info box** (`.floor-info`, ~338×~324 open) that **syncs to the slider** (name + description from `FLOOR_INFO` in script.js).
- **Floor slider** (`.floor-slider`, right side, height `100vh` desktop / `60vh` mobile): 5 slides **Versailles · Chevron · Fiskeben · Rhombes · Squares** (real interior photos `*-floor.jpg`/`versailles-floor.jpg`). Prev/next arrows + dots. Navigating reveals that floor's **name overlay** (uppercase, fades in then slowly out ~2.2s). Easy to add slides: add a `<figure class="floor-slide">` in index.html; JS auto-builds dots.

## Product pages — “Overflatebehandling” tab
- 12 surface variants (501 Light Ash → 303 Winchester) shown light→dark. Each `<li data-img="assets/images/surfaces/{key}.jpg">` with a wood-image swatch; clicking swaps the big preview (`.variant-image img`). Logic in script.js.
- **Surfaces** live in `assets/images/surfaces/501.jpg … 303.jpg` (12). They are the owner's AI-rendered oak photos, **re-sorted by brightness** into the slots (501 lightest → 303 darkest). Original source extraction came from `Plank-katalog.pdf` pages 4–5 (catalog “Overflater”). A reference folder of named copies was created at `~/Downloads/plank-overflater/`.

## OPEN ITEMS / TODO
1. **201 Ljunghusen surface = catalog placeholder.** The owner sent 12 surfaces across 3 batches but only **11 distinct files** downloaded — the light-medium tan one (eye-knot + butterfly repair) from the middle batch never saved. `201.jpg` currently uses a low-res catalog texture to keep the gradient. **When the owner re-sends it:** convert to web JPG (`sips -s format jpeg -s formatOptions 88 --resampleWidth 800 SRC --out assets/images/surfaces/201.jpg`) — but note surfaces are sorted by tone, so confirm it belongs at the 201 tonal position (~brightness 144) or re-run a brightness sort of all 12.
2. **Not committed / not deployed.** Repo is on `main` with a GitHub remote + `.cpanel.yml`. Owner hasn't asked to commit/push/deploy yet — wait for explicit ask.
3. `assets.zip` (~23 MB) is a redundant duplicate of `assets/` — safe to delete.
4. Owner image-drop workflow: they paste images in chat AND they land in `~/Downloads` with hash names. Match newest files by appearance; convert with `sips … --resampleWidth 800`.

## Recent owner-driven tweaks (so you know the “why”)
All-sans typography; text-led product hero; 30px margins; nav → 4 cols, right-aligned, 14.5px, condensed; logo “P” alignment; collab section full-frame then sized then made responsive (`100vh`); floor slider + click-reveal-name; smooth heavy scroll (Lenis); cursor light on hero tiles; surfaces from the catalog PDF + owner's AI renders, sorted by color.
