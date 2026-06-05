/* ============================================================
   Plank Norge — shared chrome + product interactions
   Header and footer are injected here so every page stays in
   sync. Set the current page via <body data-page="chevron">.
   ============================================================ */

/* ============ Smooth, weighty scrolling (Lenis) ============ */
(function loadSmoothScroll() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const s = document.createElement('script');
    s.src = 'assets/js/lenis.min.js';
    s.onload = () => {
        if (!window.Lenis) return;
        const lenis = new Lenis({
            lerp: 0.08,           // lower = heavier / more lag
            wheelMultiplier: 0.9, // a touch slower for weight
        });
        window.lenis = lenis;
        const raf = (time) => { lenis.raf(time); requestAnimationFrame(raf); };
        requestAnimationFrame(raf);
    };
    document.head.appendChild(s);
})();

const SHOWROOM_URL = 'https://planknorge.no/showroom/';

const NAV_COLUMNS = [
    [
        { label: 'Plank', href: 'plankegulv.html', key: 'plank' },
        { label: 'Chevron', href: 'chevron.html', key: 'chevron' },
        { label: 'Herringbone', href: 'herringbone.html', key: 'herringbone' },
    ],
    [
        { label: 'Rhombs', href: 'rhombs.html', key: 'rhombs' },
        { label: 'Checkerboards', href: 'checkerboards.html', key: 'checkerboards' },
        { label: 'Versailles', href: 'versailles.html', key: 'versailles' },
    ],
    [
        { label: 'Designgulv', href: 'designgulv.html', key: 'designgulv' },
        { label: 'Inspirasjon', href: 'inspirasjon.html', key: 'inspirasjon' },
        { label: 'Om oss', href: 'om.html', key: 'om' },
    ],
    [
        { label: 'Ditt Design', href: 'ditt-design.html', key: 'ditt-design' },
        { label: 'Arkitekt', href: 'arkitekt.html', key: 'arkitekt' },
    ],
    [
        { label: 'Konsultasjon', href: 'konsultasjon.html', key: 'konsultasjon' },
        { label: 'Kontakt', href: 'kontakt.html', key: 'kontakt' },
    ],
];

const SEARCH_ICON =
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>';

function buildHeader(active) {
    const cols = NAV_COLUMNS.map((col) => {
        const items = col
            .map(
                (it) =>
                    `<li><a href="${it.href}" data-label="${it.label}"${it.key === active ? ' class="active"' : ''}>${it.label}</a></li>`
            )
            .join('');
        return `<ul class="nav-col">${items}</ul>`;
    }).join('');

    return `
    <header class="site-header">
        <a href="index.html" class="logo"><img src="assets/logo/PLANK-logo-2.png" alt="Plank Norge" /></a>
        <nav class="main-nav" aria-label="Hovedmeny">${cols}</nav>
        <form class="search" role="search">
            <input type="search" placeholder="Søk..." aria-label="Søk" />
            <button type="submit" aria-label="Søk">${SEARCH_ICON}</button>
        </form>
    </header>`;
}

function buildFooter() {
    return `
    <footer class="site-footer">
        <div class="footer-inner">
            <div class="footer-brand">
                <div class="footer-logo"><img src="assets/logo/PLANK-logo-2.png" alt="Plank Norge" /></div>
                <p class="footer-tagline">Eksklusive tregulv skapt gjennom generasjoner.</p>
                <div class="footer-cta">
                    <a href="${SHOWROOM_URL}" class="btn-outline">Book et møte</a>
                    <a href="#" class="btn-outline">Bestill vareprøve</a>
                    <a href="#" class="btn-outline">Få et tilbud</a>
                </div>
            </div>

            <div class="footer-col">
                <h4>Meny</h4>
                <ul>
                    <li><a href="plankegulv.html#download">Katalog</a></li>
                    <li><a href="designgulv.html">Design</a></li>
                    <li><a href="inspirasjon.html">Inspirasjon</a></li>
                    <li><a href="konsultasjon.html">Konsultasjon</a></li>
                    <li><a href="kontakt.html">Kontakt</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Informasjon</h4>
                <ul>
                    <li><a href="https://osmo.no/" target="_blank" rel="noopener">OSMO</a></li>
                    <li><a href="https://www.rubiomonocoat.com/" target="_blank" rel="noopener">Rubio Monocoat</a></li>
                    <li><a href="om.html">Om oss</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Kontakt</h4>
                <p>Plank Norge — Showroom</p>
                <p>Fabrikkveien 10</p>
                <p>4033 Stavanger</p>
                <p class="footer-spaced">M: 404 08 996</p>
                <p>jr@planknorge.no</p>
                <p>Facebook · Instagram</p>
            </div>
        </div>

        <div class="footer-bottom">
            <span>© 2025 Plank Norge</span>
            <span>Privacy Policy</span>
        </div>
    </footer>

    <button class="chat-bubble" aria-label="Chat">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
    </button>`;
}

function renderChrome() {
    const active = document.body.dataset.page || '';
    const headerMount = document.getElementById('site-header');
    const footerMount = document.getElementById('site-footer');
    if (headerMount) headerMount.outerHTML = buildHeader(active);
    if (footerMount) footerMount.outerHTML = buildFooter();
}

renderChrome();

/* ============ Tab switching ============ */
const tabs = document.querySelectorAll('.tab');
const panels = document.querySelectorAll('.tab-panel');

tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
        const target = tab.dataset.tab;
        tabs.forEach((t) => t.classList.remove('active'));
        panels.forEach((p) => p.classList.remove('active'));
        tab.classList.add('active');
        const panel = document.getElementById(target);
        if (panel) panel.classList.add('active');
    });
});

/* ============ Character (Sortering) selection ============ */
const charItems = document.querySelectorAll('.char-list li');
const charDetail = document.querySelector('.char-detail');

const charData = {
    premium: {
        title: 'Premium',
        body: 'Homogent, rolig og subtilt uttrykk med minimalt med kvister.',
    },
    nature: {
        title: 'Nature',
        body: 'Naturlig uttrykk med synlige kvister og fargevariasjon — gulvet får liv og karakter.',
    },
    classic: {
        title: 'Classic',
        body: 'Markant uttrykk med tydelige kvister og stor fargevariasjon — et levende og rustikt gulv.',
    },
};

charItems.forEach((item) => {
    item.addEventListener('click', () => {
        charItems.forEach((i) => i.classList.remove('active'));
        item.classList.add('active');
        const key = item.dataset.char;
        if (charDetail && charData[key]) {
            charDetail.innerHTML = `<h3>${charData[key].title}</h3><p>${charData[key].body}</p>`;
        }
    });
});

/* ============ Variant selection ============ */
const variants = document.querySelectorAll('.variants li');
const detailTitle = document.querySelector('.variant-detail h3');
const variantImg = document.querySelector('.variant-image img');

variants.forEach((variant) => {
    variant.addEventListener('click', () => {
        variants.forEach((v) => v.classList.remove('active'));
        variant.classList.add('active');
        if (detailTitle) {
            const name = variant.querySelector('.variant-name')?.textContent ?? '';
            const type = variant.querySelector('.variant-type')?.textContent ?? '';
            detailTitle.innerHTML = `${name} <span class="thin">${type}</span>`;
        }
        if (variantImg && variant.dataset.img) variantImg.src = variant.dataset.img;
    });
});

/* ============ Floor-type slider — name reveals when you navigate ============ */
const floorSlider = document.querySelector('.floor-slider');
if (floorSlider) {
    const track = floorSlider.querySelector('.floor-track');
    const slides = [...floorSlider.querySelectorAll('.floor-slide')];
    const dotsWrap = floorSlider.querySelector('.floor-dots');
    let index = 0;

    // Expandable "more info" box that reflects the current floor.
    const infoBox = document.querySelector('.floor-info');
    const FLOOR_INFO = {
        'Versailles': 'Klassiske Versailles-paneler — kvadrater med diagonalt fletteverk. Storslått og symmetrisk, opprinnelig skapt for de franske slottene.',
        'Chevron': 'Skarpe vinkler i et presist sikksakk. Fransk eleganse møter nordisk ro — rytmisk og tidløst.',
        'Fiskeben': 'Det ikoniske sildebensmønsteret, lagt i 90° vinkel. Et levende, klassisk gulv med varme og karakter.',
        'Rhombes': 'Geometriske rhombeformer som skaper dybde og et grafisk, moderne uttrykk i tre.',
        'Squares': 'Kvadratiske paneler i et rolig rutemønster — balansert, arkitektonisk og diskret.',
    };
    const syncInfo = () => {
        if (!infoBox) return;
        const name = slides[index].querySelector('.floor-overlay').textContent.trim();
        const nameEl = infoBox.querySelector('.floor-info__name');
        const patEl = infoBox.querySelector('.floor-info__pattern');
        const descEl = infoBox.querySelector('.floor-info__desc');
        if (nameEl) nameEl.textContent = name;
        if (patEl) patEl.textContent = name;
        if (descEl) descEl.textContent = FLOOR_INFO[name] || '';
    };
    if (infoBox) {
        const infoToggle = infoBox.querySelector('.floor-info__toggle');
        infoToggle?.addEventListener('click', () => {
            const open = infoBox.getAttribute('data-open') === 'true';
            infoBox.setAttribute('data-open', String(!open));
            infoToggle.setAttribute('aria-expanded', String(!open));
        });
    }

    const updateDots = () => {
        if (dotsWrap) [...dotsWrap.children].forEach((d, i) => d.classList.toggle('active', i === index));
    };

    // Show the current floor's name, then let it slowly fade out.
    const revealName = () => {
        slides.forEach((s) => {
            const o = s.querySelector('.floor-overlay');
            if (o) { o.classList.remove('is-visible'); clearTimeout(o._hideTimer); }
        });
        const overlay = slides[index].querySelector('.floor-overlay');
        if (!overlay) return;
        overlay.classList.add('is-visible');
        overlay._hideTimer = setTimeout(() => overlay.classList.remove('is-visible'), 2200);
    };

    const update = () => {
        track.style.transform = `translateX(-${index * 100}%)`;
        updateDots();
        syncInfo();
    };

    // Navigating (arrows + dots) moves to the slide AND reveals its name.
    const goTo = (i) => {
        index = (i + slides.length) % slides.length;
        update();
        revealName();
    };

    if (dotsWrap) {
        slides.forEach((_, i) => {
            const dot = document.createElement('button');
            dot.className = 'floor-dot';
            dot.setAttribute('aria-label', `Gå til gulv ${i + 1}`);
            dot.addEventListener('click', () => goTo(i));
            dotsWrap.appendChild(dot);
        });
    }

    floorSlider.querySelector('.floor-prev')?.addEventListener('click', () => goTo(index - 1));
    floorSlider.querySelector('.floor-next')?.addEventListener('click', () => goTo(index + 1));

    update(); // initial position only — no name shown until you navigate
}

/* ============ Hero tiles — soft light that trails the cursor on hover ============ */
document.querySelectorAll('.home-hero .hero-tile').forEach((tile) => {
    const fig = tile.querySelector('figure');
    if (!fig) return;
    let tx = 50, ty = 50, cx = 50, cy = 50, raf = null;
    const EASE = 0.1; // lower = more lag / bigger delay

    const tick = () => {
        cx += (tx - cx) * EASE;
        cy += (ty - cy) * EASE;
        fig.style.setProperty('--mx', `${cx}%`);
        fig.style.setProperty('--my', `${cy}%`);
        if (Math.abs(tx - cx) > 0.1 || Math.abs(ty - cy) > 0.1) {
            raf = requestAnimationFrame(tick);
        } else {
            raf = null;
        }
    };

    const toPct = (e) => {
        const r = fig.getBoundingClientRect();
        return [((e.clientX - r.left) / r.width) * 100, ((e.clientY - r.top) / r.height) * 100];
    };

    tile.addEventListener('mouseenter', (e) => {
        [tx, ty] = toPct(e);
        cx = tx; cy = ty; // start under the cursor (no jump from centre)
        fig.style.setProperty('--mx', `${cx}%`);
        fig.style.setProperty('--my', `${cy}%`);
    });

    tile.addEventListener('mousemove', (e) => {
        [tx, ty] = toPct(e);
        if (!raf) raf = requestAnimationFrame(tick);
    });
});
