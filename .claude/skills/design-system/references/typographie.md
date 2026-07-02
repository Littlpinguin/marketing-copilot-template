# Pairings typographiques — bibliothèque de fallback

> Condensé et adapté de `typography.csv` d'[ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) v2.5.0 (MIT, © 2024 Next Level Builder). 27 pairings retenus sur 73 — sélection web marketing (pairings mobile natif et scripts non latins écartés ; pour un projet multilingue non latin, retourner à la source, voir `docs/vendored-design.md`).

## La marque d'abord

`{{BRAND_FONT_PRIMARY}}` (défini dans `01-brand/style-guide.md`) est **toujours** la police de référence. Ce fichier sert à :

1. **Trouver un complément** — si la marque n'a qu'une police, choisir dans la table un pairing dont l'un des deux rôles est la police de marque (ou une voisine de même classification), et adopter l'autre rôle.
2. **Calibrer la tonalité** — vérifier que le duo retenu correspond à la tonalité du brief (colonne Tonalité).
3. **Fallback intégral** — uniquement si aucune police de marque n'est définie.

Toutes les polices sont sur Google Fonts. Import type :
`@import url('https://fonts.googleapis.com/css2?family=<Heading>:wght@400;600;700&family=<Body>:wght@400;500;600&display=swap');`
Toujours `font-display: swap` et préchargement des seules graisses réellement utilisées.

| Pairing | Titrage | Corps | Tonalité | Adapté à |
|---|---|---|---|---|
| **Classic Elegant** | Playfair Display | Inter | elegant, luxury, sophisticated, timeless, premium, editorial | Luxury brands, fashion, spa, beauty, editorial, magazines, high-end e-commerce |
| **Modern Professional** | Poppins | Open Sans | modern, professional, clean, corporate, friendly, approachable | SaaS, corporate sites, business apps, startups, professional services |
| **Tech Startup** | Space Grotesk | DM Sans | tech, startup, modern, innovative, bold, futuristic | Tech companies, startups, SaaS, developer tools, AI products |
| **Editorial Classic** | Cormorant Garamond | Libre Baskerville | editorial, classic, literary, traditional, refined, bookish | Publishing, blogs, news sites, literary magazines, book covers |
| **Minimal Swiss** | Inter | Inter | minimal, clean, swiss, functional, neutral, professional | Dashboards, admin panels, documentation, enterprise apps, design systems |
| **Bold Statement** | Bebas Neue | Source Sans 3 | bold, impactful, strong, dramatic, modern, headlines | Marketing sites, portfolios, agencies, event pages, sports |
| **Wellness Calm** | Lora | Raleway | calm, wellness, health, relaxing, natural, organic | Health apps, wellness, spa, meditation, yoga, organic brands |
| **Retro Vintage** | Abril Fatface | Merriweather | retro, vintage, nostalgic, dramatic, decorative, bold | Vintage brands, breweries, restaurants, creative portfolios, posters |
| **Geometric Modern** | Outfit | Work Sans | geometric, modern, clean, balanced, contemporary, versatile | General purpose, portfolios, agencies, modern brands, landing pages |
| **Luxury Serif** | Cormorant | Montserrat | luxury, high-end, fashion, elegant, refined, premium | Fashion brands, luxury e-commerce, jewelry, high-end services |
| **Friendly SaaS** | Plus Jakarta Sans | Plus Jakarta Sans | friendly, modern, saas, clean, approachable, professional | SaaS products, web apps, dashboards, B2B, productivity tools |
| **News Editorial** | Newsreader | Roboto | news, editorial, journalism, trustworthy, readable, informative | News sites, blogs, magazines, journalism, content-heavy sites |
| **Corporate Trust** | Lexend | Source Sans 3 | corporate, trustworthy, accessible, readable, professional, clean | Enterprise, government, healthcare, finance, accessibility-focused |
| **Fashion Forward** | Syne | Manrope | fashion, avant-garde, creative, bold, artistic, edgy | Fashion brands, creative agencies, art galleries, design studios |
| **Premium Sans** | Satoshi | General Sans | premium, modern, clean, sophisticated, versatile, balanced | Premium brands, modern agencies, SaaS, portfolios, startups |
| **Legal Professional** | EB Garamond | Lato | legal, professional, traditional, trustworthy, formal, authoritative | Law firms, legal services, contracts, formal documents, government |
| **Medical Clean** | Figtree | Noto Sans | medical, clean, accessible, professional, healthcare, trustworthy | Healthcare, medical clinics, pharma, health apps, accessibility |
| **Financial Trust** | IBM Plex Sans | IBM Plex Sans | financial, trustworthy, professional, corporate, banking, serious | Banks, finance, insurance, investment, fintech, enterprise |
| **Real Estate Luxury** | Cinzel | Josefin Sans | real estate, luxury, elegant, sophisticated, property, premium | Real estate, luxury properties, architecture, interior design |
| **Restaurant Menu** | Playfair Display SC | Karla | restaurant, menu, culinary, elegant, foodie, hospitality | Restaurants, cafes, food blogs, culinary, hospitality |
| **Magazine Style** | Libre Bodoni | Public Sans | magazine, editorial, publishing, refined, journalism, print | Magazines, online publications, editorial content, journalism |
| **Indie/Craft** | Amatic SC | Cabin | indie, craft, handmade, artisan, organic, creative | Craft brands, indie products, artisan, handmade, organic products |
| **Startup Bold** | Clash Display | Satoshi | startup, bold, modern, innovative, confident, dynamic | Startups, pitch decks, product launches, bold brands |
| **E-commerce Clean** | Rubik | Nunito Sans | ecommerce, clean, shopping, product, retail, conversion | E-commerce, online stores, product pages, retail, shopping |
| **Minimalist Portfolio** | Archivo | Space Grotesk | minimal, portfolio, designer, creative, clean, artistic | Design portfolios, creative professionals, minimalist brands |
| **Luxury Minimalist** | Bodoni Moda | Jost | luxury, minimalist, high-end, sophisticated, refined, premium | Luxury minimalist brands, high-end fashion, premium products |
| **Neubrutalist Bold** | Lexend Mega | Public Sans | bold, neubrutalist, loud, strong, geometric, quirky | Neubrutalist designs, Gen Z brands, bold marketing |
## Règles d'application

1. **Deux familles maximum** (trois si une mono est nécessaire pour données/code). Le contraste titrage/corps porte la personnalité.
2. **Échelle modulaire cohérente** : ex. 12 / 14 / 16 / 18 / 24 / 32 / 48. Corps ≥ 16 px (mobile inclus), line-height 1.5–1.75, mesure 65–75 caractères.
3. **Hiérarchie par la graisse** : titres 600–700, corps 400, labels 500. Pas de tracking serré sur le corps de texte.
4. **Chiffres tabulaires** (`font-variant-numeric: tabular-nums`) pour prix, stats et compteurs.
5. **Anti-défaut IA** : Inter-partout-en-corps + serif à fort contraste en display est devenu la signature des pages générées par IA. Si la marque laisse le choix libre, justifier le pairing par le sujet, pas par l'habitude (voir skill `design-direction`).
