# -*- coding: utf-8 -*-
import os
OUT = "/Users/lordolivermyrvold/Downloads/planknorge-redesign"

TEMPLATE = r'''<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>@@TITLE@@ — Plank Norge</title>
    <meta name="description" content="@@DESC@@" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300..700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="styles.css?v=3" />
</head>
<body data-page="@@KEY@@">
    <div id="site-header"></div>

    <!-- ============ HERO ============ -->
    <section class="hero">
        <h1 class="page-title">@@H1@@</h1>

        <div class="hero-grid">
            <div class="hero-media">
                <figure class="hero-image">
                    @@HERO_MEDIA@@
                </figure>
            </div>

            <div class="hero-text">
                <p class="lead">@@LEAD@@</p>
                <p>@@BODY@@</p>

                <ul class="cta-list">
                    <li><a href="#"><span class="cta-icon">›</span> Få et tilbud</a></li>
                    <li><a href="#"><span class="cta-icon">›</span> Bestill vareprøve</a></li>
                    <li><a href="https://planknorge.no/showroom/"><span class="cta-icon">›</span> Book et møte</a></li>
                </ul>
            </div>
        </div>
    </section>

    <!-- ============ TABS ============ -->
    <section class="tabs-section">
        <div class="tabs" role="tablist">
            <button class="tab active" role="tab" data-tab="treatment">Overflatebehandling</button>
            <button class="tab" role="tab" data-tab="dimensions">Dimensjoner</button>
            <button class="tab" role="tab" data-tab="sorting">Sortering</button>
            <button class="tab" role="tab" data-tab="construction">Konstruksjon</button>
            <button class="tab" role="tab" data-tab="maintenance">Vedlikehold</button>
            <button class="tab" role="tab" data-tab="download">Last ned</button>
        </div>

        <!-- Treatment panel -->
        <div class="tab-panel active" id="treatment">
            <div class="variants-grid">
                <ul class="variants">@@VARIANTS@@
                </ul>

                <div class="variant-detail">
                    <h3>501 Light Ash <span class="thin">— Ask</span></h3>
                    <p>Overflatebehandlet med lut og hvitolje. Dette understreker den lyse, naturlige veden og skaper et balansert og rolig inntrykk.</p>
                </div>

                <figure class="variant-image">
                    <img src="assets/images/surfaces/501.jpg" alt="Overflate 501 Light Ash" />
                </figure>
            </div>

            <div class="pager">
                <button aria-label="Forrige">‹</button>
                <button aria-label="Neste">›</button>
            </div>
        </div>

        <!-- Dimensions -->
        <div class="tab-panel" id="dimensions">
            <div class="dim-grid">
                <p class="dim-intro">
                    Vi har samlet noen av våre vanligste og mest populære dimensjoner.
                    Skreddersydde dimensjoner er tilgjengelig på forespørsel.
                </p>

                <div class="dim-col">
                    <div class="dim-head">Konstruksjon</div>
                    <div class="dim-cell">Solid eik</div>
                    <div class="dim-cell">3-sjikt eik</div>
                    <div class="dim-cell">Solid ask</div>
                </div>

                <div class="dim-col">
                    <div class="dim-head">Tykkelse</div>
                    <div class="dim-cell">16 mm / 21 mm</div>
                    <div class="dim-cell">15 mm / 21 mm</div>
                    <div class="dim-cell">16 mm</div>
                </div>

                <div class="dim-col">
                    <div class="dim-head">Bredde</div>
                    <div class="dim-cell">70 mm<br/>90 mm<br/>120 mm</div>
                    <div class="dim-cell">75 mm<br/>90 mm<br/>120 mm<br/>140 mm<br/>160 mm<br/>200 mm</div>
                    <div class="dim-cell">90 mm<br/>120 mm</div>
                </div>

                <div class="dim-col">
                    <div class="dim-head">Lengder</div>
                    <div class="dim-cell">420 mm<br/>520 mm<br/>610 mm<br/>880 mm</div>
                    <div class="dim-cell">420 mm<br/>520 mm<br/>610 mm<br/>680 mm<br/>880 mm<br/>1000 mm</div>
                    <div class="dim-cell">610 mm<br/>700 mm<br/>880 mm</div>
                </div>
            </div>
        </div>

        <!-- Sorting -->
        <div class="tab-panel" id="sorting">
            <div class="char-grid">
                <div class="char-left">
                    <p class="char-intro">
                        @@SORT_INTRO@@ Hver sortering har sine egne
                        særtrekk som gir gulvet sitt distinkte uttrykk. Sorteringen indikerer fargevariasjon
                        og mengde/størrelse på kvister. I vår verden beskriver ikke sorteringen kvaliteten
                        på treet, men heller uttrykket — og bør vurderes ut fra helhetsestetikken.
                        Bildene er kun veiledende.
                    </p>

                    <ul class="char-list">
                        <li class="active" data-char="premium">Premium</li>
                        <li data-char="nature">Nature</li>
                        <li data-char="classic">Classic</li>
                    </ul>
                </div>

                <div class="char-detail">
                    <h3>Premium</h3>
                    <p>Homogent, rolig og subtilt uttrykk med minimalt med kvister.</p>
                </div>

                <div class="char-images">
                    <figure><img src="assets/images/riga-parket-chalet-hans-13.jpg" alt="Premium — bord 1" /></figure>
                    <figure class="char-image-narrow"><img src="assets/images/Gulv_interior2-2048x2048.jpg" alt="Premium — bord 2" /></figure>
                </div>
            </div>
        </div>

        <!-- Construction -->
        <div class="tab-panel" id="construction">
            <div class="constr-grid">
                <div class="constr-left">
                    <p class="constr-intro">
                        Forholdene i hvert enkelt prosjekt avgjør hvilken konstruksjon som passer best
                        for at gulvet skal vare i generasjoner. La oss veilede deg til riktig valg.
                    </p>

                    <ul class="constr-list">
                        <li class="active" data-constr="3layer">3-sjikt</li>
                        <li data-constr="solid">Solid</li>
                    </ul>
                </div>

                <div class="constr-right">
                    <p class="constr-body">
                        Et 3-sjikts gulv er en limt konstruksjon i tre lag massivt tre som gir økt
                        dimensjonsstabilitet uten å gå på kompromiss med følelsen av et heltregulv.
                        Ved bruk av gulvvarme anbefaler vi denne løsningen.
                    </p>

                    <figure class="constr-diagram">
                        <svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="3-sjikts konstruksjon">
                            <defs>
                                <pattern id="hatch" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)">
                                    <line x1="0" y1="0" x2="0" y2="6" stroke="#9c8f78" stroke-width="0.6"/>
                                </pattern>
                                <pattern id="hatch2" patternUnits="userSpaceOnUse" width="4" height="4" patternTransform="rotate(135)">
                                    <line x1="0" y1="0" x2="0" y2="4" stroke="#9c8f78" stroke-width="0.5"/>
                                </pattern>
                            </defs>
                            <g stroke="#5a4d38" stroke-width="0.8" fill="none">
                                <path d="M30 60 L240 60 L260 90 L260 130 L240 160 L30 160 Z" fill="url(#hatch)"/>
                                <line x1="30" y1="100" x2="260" y2="100"/>
                                <line x1="30" y1="120" x2="260" y2="120"/>
                            </g>
                            <g stroke="#5a4d38" stroke-width="0.6" fill="none">
                                <line x1="20" y1="60" x2="20" y2="160"/>
                                <polygon points="20,60 17,67 23,67" fill="#5a4d38"/>
                                <polygon points="20,160 17,153 23,153" fill="#5a4d38"/>
                            </g>
                            <text x="0" y="115" font-size="9" fill="#5a4d38" font-family="Source Sans 3">21 mm</text>
                            <g stroke="#5a4d38" stroke-width="0.8" fill="none">
                                <path d="M310 60 L500 60 L520 90 L520 130 L500 160 L310 160 Z" fill="url(#hatch)"/>
                                <line x1="310" y1="100" x2="520" y2="100"/>
                                <line x1="310" y1="120" x2="520" y2="120"/>
                            </g>
                            <g stroke="#5a4d38" stroke-width="0.5" fill="none">
                                <line x1="520" y1="80" x2="600" y2="80"/>
                                <line x1="520" y1="110" x2="600" y2="110"/>
                                <line x1="520" y1="140" x2="600" y2="140"/>
                            </g>
                            <text x="605" y="83" font-size="9" fill="#5a4d38" font-family="Source Sans 3">Massiv finér</text>
                            <text x="605" y="113" font-size="9" fill="#5a4d38" font-family="Source Sans 3">Massiv finér</text>
                            <text x="605" y="143" font-size="9" fill="#5a4d38" font-family="Source Sans 3">Massiv finér</text>
                            <g stroke="#5a4d38" stroke-width="0.8" fill="none">
                                <rect x="30" y="200" width="660" height="20" fill="url(#hatch2)"/>
                                <line x1="30" y1="206" x2="690" y2="206"/>
                                <line x1="30" y1="214" x2="690" y2="214"/>
                            </g>
                        </svg>
                    </figure>
                </div>
            </div>
        </div>

        <!-- Maintenance -->
        <div class="tab-panel" id="maintenance">
            <div class="maint-grid">
                <div class="maint-row">
                    <div class="maint-label">Steg 1</div>
                    <div class="maint-body">Følg alltid våre eller produsentens instruksjoner for overflatebehandling, pleie og vedlikehold.</div>
                </div>
                <div class="maint-row">
                    <div class="maint-label">Steg 2</div>
                    <div class="maint-body">Hold relativ luftfuktighet innendørs mellom 35–60 %. Dette er bra både for helsen din og for tregulvet ditt.</div>
                </div>
                <div class="maint-row">
                    <div class="maint-label">Steg 3</div>
                    <div class="maint-body">Har du gulvvarme må temperaturen reguleres etter våre anvisninger, slik at tregulvet ditt varer i generasjoner.</div>
                </div>
            </div>
        </div>

        <!-- Download -->
        <div class="tab-panel" id="download">
            <ul class="download-list">
                <li><a href="assets/docs/Plank-katalog.pdf" target="_blank" rel="noopener"><span class="cta-icon">›</span> Last ned katalog (PDF)</a></li>
            </ul>
        </div>
    </section>

    <!-- ============ REFERENCES ============ -->
    <section class="references">
        <div class="references-head">
            <h2>Historier</h2>
            <p class="references-sub">@@H1@@-gulv i prosjekter — fra private hjem til offentlige rom.</p>
        </div>
        <div class="references-track">
            <a href="#" class="reference-card">
                <figure><img src="assets/images/riga-parket-chalet-hans-1.jpg" alt="Chalet Hans, Riga" /></figure>
                <figcaption>Chalet Hans — Riga</figcaption>
            </a>
            <a href="#" class="reference-card">
                <figure><img src="assets/images/riga-parket-chalet-hans-10.jpg" alt="Chalet Hans interiør" /></figure>
                <figcaption>Chalet Hans — Salong</figcaption>
            </a>
            <a href="#" class="reference-card">
                <figure><img src="assets/images/riga-parket-chalet-hans-13.jpg" alt="Chalet Hans detalj" /></figure>
                <figcaption>Chalet Hans — Detalj</figcaption>
            </a>
            <a href="#" class="reference-card">
                <figure><img src="assets/images/Gulv_interior2-2048x2048.jpg" alt="Tregulv i bolig" /></figure>
                <figcaption>Privatbolig — Stavanger</figcaption>
            </a>
        </div>
    </section>

    <!-- ============ HOW TO ORDER ============ -->
    <section class="how-to-order">
        <h2>Slik bestiller du</h2>
        <ol class="steps">
            <li>
                <span class="step-num">1</span>
                <h3>Ta kontakt <span class="thin">—</span></h3>
                <p>Besøk et av våre showroom, book et online-møte eller ring oss. Salgsteamet vårt er klart til å diskutere drømmegulvet ditt.</p>
                <a href="kontakt.html" class="step-link">Kontakt</a>
            </li>
            <li>
                <span class="step-num">2</span>
                <h3>Velg gulvet ditt <span class="thin">—</span></h3>
                <p>Opplev og se gulvet vårt levert hjem til deg ved å bestille vareprøver gjennom kontaktpersonen din i teamet.</p>
            </li>
            <li>
                <span class="step-num">3</span>
                <h3>Klart til bestilling <span class="thin">—</span></h3>
                <p>Når du har valgt mønster, finish, dimensjoner og konstruksjon, er vi klare til å integrere gulvet i ditt prosjekt. Normal leveringstid er 5–10 uker.</p>
            </li>
        </ol>
    </section>

    <div id="site-footer"></div>
    <script src="script.js?v=3"></script>
</body>
</html>
'''

PRODUCTS = [
    {
        "FILE": "chevron.html",
        "KEY": "chevron",
        "TITLE": "Chevron",
        "DESC": "Chevron — rytmisk og tidløst. Eksklusive chevron-gulv fra Plank Norge, utviklet i samspill med arkitekter og designere.",
        "H1": "Chevron",
        "TAGLINE": "— rytmisk og tidløst",
        "HERO_IMG": "assets/images/chevron-floor.jpg",
        "HERO_ALT": "Chevron-gulv i moderne interiør",
        "TEXTURE_IMG": "assets/images/riga-parket-chalet-hans-10.jpg",
        "LEAD": "Et vinkelmønster med europeiske røtter — presist, rytmisk og tidløst.",
        "BODY": "I møte med nordisk minimalisme får Chevron et nytt liv. De skarpe vinklene og rene linjene skaper et moderne, rolig uttrykk, samtidig som den historiske elegansen ligger som et subtilt lag under overflaten.",
        "SORT_INTRO": "Chevron-gulvene våre leveres i tre ulike sorteringer.",
    },
    {
        "FILE": "plankegulv.html",
        "KEY": "plank",
        "TITLE": "Plank",
        "DESC": "Plankegulv — brede og lange planker for en sømløs, minimalistisk eleganse. Eksklusive tregulv fra Plank Norge.",
        "H1": "Plank",
        "TAGLINE": "— sømløst og levende",
        "HERO_IMG": "assets/images/Gulv_interior2-2048x2048.jpg",
        "HERO_ALT": "Plankegulv i moderne interiør",
        "TEXTURE_IMG": "assets/images/riga-parket-chalet-hans-13.jpg",
        "LEAD": "Brede, lange planker for en sømløs, minimalistisk eleganse.",
        "BODY": "Produsert i flere ulike treslag — eik, ask, douglas-gran, furu og valnøtt. Velg gulvet ditt: kom innom et av våre showroom, book et online-møte eller bestill en vareprøve.",
        "SORT_INTRO": "Plankegulvene våre leveres i tre ulike sorteringer.",
    },
    {
        "FILE": "fiskeben.html",
        "KEY": "fiskeben",
        "TITLE": "Fiskeben",
        "DESC": "Fiskeben (sildebensmønster) — klassisk parkett med tidløs karakter. Eksklusive tregulv fra Plank Norge.",
        "H1": "Fiskeben",
        "TAGLINE": "— klassisk og karakterfull",
        "HERO_IMG": "assets/images/fiskeben-floor.jpg",
        "HERO_ALT": "Fiskebensgulv i interiør",
        "TEXTURE_IMG": "assets/images/riga-parket-chalet-hans-10.jpg",
        "LEAD": "Det ikoniske sildebensmønsteret — rytme, dybde og en varm, klassisk atmosfære.",
        "BODY": "Et tidløst mønster med røtter i europeisk håndverkstradisjon, foredlet med nordisk presisjon. Velg treslag, sortering og overflate som passer ditt rom.",
        "SORT_INTRO": "Fiskebensgulvene våre leveres i tre ulike sorteringer.",
    },
    {
        "FILE": "heltre.html",
        "KEY": "heltre",
        "TITLE": "Heltre",
        "DESC": "Heltregulv — massivt tre i hele bordets tykkelse, gulvet i sin reneste form. Eksklusive tregulv fra Plank Norge.",
        "H1": "Heltre",
        "TAGLINE": "— massivt og ekte",
        "HERO_IMG": "assets/images/riga-parket-chalet-hans-10.jpg",
        "HERO_ALT": "Heltregulv i interiør",
        "TEXTURE_IMG": "assets/images/Gulv_interior2-2048x2048.jpg",
        "LEAD": "Massivt tre i hele bordets tykkelse — gulvet i sin reneste form.",
        "BODY": "Den naturlige veden lever med rommet og får en vakker patina over tid. Et bevisst valg for deg som verdsetter ekthet og varighet.",
        "SORT_INTRO": "Heltregulvene våre leveres i tre ulike sorteringer.",
    },
    {
        "FILE": "herringbone.html",
        "KEY": "herringbone",
        "TITLE": "Herringbone",
        "DESC": "Herringbone (sildebensmønster) — klassisk parkett med tidløs karakter. Eksklusive tregulv fra Plank Norge.",
        "H1": "Herringbone",
        "TAGLINE": "— klassisk og karakterfull",
        "HERO_IMG": "assets/images/fiskeben-floor.jpg",
        "HERO_ALT": "Herringbone-gulv i interiør",
        "TEXTURE_IMG": "assets/images/riga-parket-chalet-hans-10.jpg",
        "LEAD": "Det ikoniske sildebensmønsteret — rytme, dybde og en varm, klassisk atmosfære.",
        "BODY": "Et tidløst mønster med røtter i europeisk håndverkstradisjon, foredlet med nordisk presisjon. Velg treslag, sortering og overflate som passer ditt rom.",
        "SORT_INTRO": "Herringbone-gulvene våre leveres i tre ulike sorteringer.",
    },
    {
        "FILE": "rhombs.html",
        "KEY": "rhombs",
        "TITLE": "Rhombs",
        "DESC": "Rhombs — geometriske rhombeformer som skaper dybde og et grafisk, moderne uttrykk. Eksklusive tregulv fra Plank Norge.",
        "H1": "Rhombs",
        "TAGLINE": "— geometrisk og grafisk",
        "HERO_IMG": "assets/images/rhombes-floor.jpg",
        "HERO_ALT": "Rhombs-gulv i interiør",
        "TEXTURE_IMG": "assets/images/riga-parket-chalet-hans-13.jpg",
        "LEAD": "Geometriske rhomber som skaper dybde og et grafisk, moderne uttrykk i tre.",
        "BODY": "Rhombemønsteret leker med lys og vinkler og gir gulvet en skulpturell karakter. Et dristig valg for rom som tåler et tydelig uttrykk.",
        "SORT_INTRO": "Rhombs-gulvene våre leveres i tre ulike sorteringer.",
    },
    {
        "FILE": "checkerboards.html",
        "KEY": "checkerboards",
        "TITLE": "Checkerboards",
        "DESC": "Checkerboards — kvadratiske paneler i et rolig rutemønster, balansert og arkitektonisk. Eksklusive tregulv fra Plank Norge.",
        "H1": "Checkerboards",
        "TAGLINE": "— rolig og arkitektonisk",
        "HERO_IMG": "assets/images/squares-floor.jpg",
        "HERO_ALT": "Checkerboard-gulv i interiør",
        "TEXTURE_IMG": "assets/images/Gulv_interior2-2048x2048.jpg",
        "LEAD": "Kvadratiske paneler i et rolig rutemønster — balansert, arkitektonisk og diskret.",
        "BODY": "Et klassisk rutemønster som gir rommet struktur og ro. Spill på kontrast eller harmoni mellom feltene for ditt eget uttrykk.",
        "SORT_INTRO": "Checkerboard-gulvene våre leveres i tre ulike sorteringer.",
    },
    {
        "FILE": "versailles.html",
        "KEY": "versailles",
        "TITLE": "Versailles",
        "DESC": "Versailles — storslåtte paneler med diagonalt fletteverk, opprinnelig skapt for de franske slottene. Eksklusive tregulv fra Plank Norge.",
        "H1": "Versailles",
        "TAGLINE": "— storslått og symmetrisk",
        "HERO_IMG": "assets/images/versailles-floor.jpg",
        "HERO_ALT": "Versailles-gulv i interiør",
        "TEXTURE_IMG": "assets/images/riga-parket-chalet-hans-13.jpg",
        "LEAD": "Klassiske Versailles-paneler — kvadrater med diagonalt fletteverk, opprinnelig skapt for de franske slottene.",
        "BODY": "Et av historiens mest forseggjorte parkettmønstre, gjenskapt med moderne presisjon. Storslått, symmetrisk og tidløst elegant.",
        "SORT_INTRO": "Versailles-gulvene våre leveres i tre ulike sorteringer.",
    },
]

VARIANTS = [
    ("501", "501 Light Ash", "Ask"),
    ("101", "101 Falsterbo", "Eik"),
    ("102", "102 Sandhammaren", "Eik"),
    ("103", "103 Brantevik", "Eik"),
    ("104", "104 Smygehuk", "Eik"),
    ("105", "105 Mälarhusen", "Eik"),
    ("201", "201 Ljunghusen", "Eik"),
    ("202", "202 Norr Mälarstrand", "Eik"),
    ("203", "203 Sjöorona", "Eik"),
    ("301", "301 Abbekås", "Eik"),
    ("302", "302 Skurusundet", "Eik"),
    ("303", "303 Winchester", "Eik"),
]
_vrows = []
for _i, (_key, _name, _wood) in enumerate(VARIANTS):
    _active = ' class="active"' if _i == 0 else ''
    _img = "assets/images/surfaces/%s.jpg" % _key
    _vrows.append(
        '                    <li%s data-img="%s"><span class="swatch" style="background-image:url(\'%s\')"></span>'
        '<span class="variant-name">%s</span><span class="variant-type">— %s</span></li>'
        % (_active, _img, _img, _name, _wood)
    )
TEMPLATE = TEMPLATE.replace("@@VARIANTS@@", "\n" + "\n".join(_vrows))

for p in PRODUCTS:
    # default hero media is an <img>; chevron overrides with a looping <video>
    if "HERO_MEDIA" not in p:
        p["HERO_MEDIA"] = '<img src="%s" alt="%s" />' % (p["HERO_IMG"], p["HERO_ALT"])
    out = TEMPLATE
    for k, v in p.items():
        if k == "FILE":
            continue
        out = out.replace("@@" + k + "@@", v)
    path = os.path.join(OUT, p["FILE"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", p["FILE"], len(out), "bytes")
