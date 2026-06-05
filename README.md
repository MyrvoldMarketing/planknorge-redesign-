# Plank Norge — Plankegulv prototype

Statisk HTML/CSS-prototype av en redesignet Plankegulv-side for [planknorge.no](https://planknorge.no), inspirert av [chevronparquet.com](https://www.chevronparquet.com/en/product/chevron-pattern/).

## Hva er inkludert

- **Plankegulv-side** (`index.html`) med samme struktur som Chevron-siden:
  - Header med logo, flerkolonne-meny og søk
  - Hero med produktbilde, beskrivelse og 3 CTA-er (`Få et tilbud`, `Bestill vareprøve`, `Book et møte` → `/showroom/`)
  - Tab-navigasjon: **Overflatebehandling, Dimensjoner, Sortering, Konstruksjon, Vedlikehold, Last ned**
  - Variantliste med swatches + detalj + stort produktbilde
  - "Slik bestiller du" med 3 steg
  - Footer med kontakt og CTA-knapper

## Slik kjører du

Åpne `index.html` direkte i nettleseren, eller start en lokal server:

```bash
python3 -m http.server 5500
```

og gå til <http://localhost:5500>.

## Neste steg

Samme mal kan brukes for **Chevron**, **Fiskeben** og **Heltre**-sidene — kun innhold (tittel, hero-tekst, varianter, bilder) byttes ut. Når designet er godkjent kan utvikler implementere malen i WordPress-temaet på planknorge.no.

## Filstruktur

```
planknorge-redesign/
├── index.html      # Plankegulv-siden
├── styles.css      # All styling
├── script.js       # Tab-bytte og variant-valg
└── README.md
```
