# Styles UI web — bibliothèque de référence

> Condensé et adapté de `styles.csv` d'[ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) v2.5.0 (MIT, © 2024 Next Level Builder). Sélection web marketing uniquement — les styles mobile natif et dashboards BI ont été écartés. **Rappel : la marque (`01-brand/style-guide.md`) prime toujours. Un style qui contredit les interdits visuels de la marque est écarté d'office.**

Comment lire : *Pour* = contextes adaptés · *Jamais* = contextes à exclure · *Signature CSS* = techniques clés · *A11y* = point de vigilance accessibilité · *Conv.* = orientation conversion.

## Styles généraux

### Minimalisme / Swiss Style
- **Pour** : SaaS, sites B2B, documentation, outils professionnels. **Jamais** : marques ludiques, portfolios créatifs.
- **Signature CSS** : grid + `gap: 2rem`, sans-serif, fort contraste, `max-width: 1200px`, pas de box-shadow superflue. Hover subtil 200-250 ms.
- **A11y** : excellent (AAA atteignable). **Conv.** : moyenne — à combiner avec un pattern CRO fort.

### Flat Design
- **Pour** : web apps, MVP, SaaS, sites corporate. **Jamais** : luxe/premium, expériences immersives.
- **Signature CSS** : couleurs pleines, `box-shadow: none`, radius 0-4 px, SVG simplifiés, transitions 150-200 ms.
- **A11y** : excellent. **Conv.** : haute. Style le plus sûr par défaut.

### Swiss Modernism 2.0
- **Pour** : corporate, éditorial, architecture, services professionnels. **Jamais** : marques enfantines, gaming, storytelling émotionnel.
- **Signature CSS** : grille 12 colonnes, base 8 px, ratios mathématiques, un seul accent, Inter/Helvetica 400-700.
- **A11y** : excellent. **Conv.** : haute.

### Glassmorphism
- **Pour** : SaaS moderne, corporate haut de gamme, overlays/navigation. **Jamais** : accessibilité critique, fonds à faible contraste, contrainte perf.
- **Signature CSS** : `backdrop-filter: blur(15px)`, `background: rgba(255,255,255,0.15)`, bordure `1px solid rgba(255,255,255,0.2)`.
- **A11y** : ⚠ vérifier 4.5:1 sur chaque surface vitrée. **Conv.** : haute.

### Aurora UI / Gradient Mesh
- **Pour** : héros de landing, marques créatives/premium, lifestyle. **Jamais** : contenu dense, accessibilité critique.
- **Signature CSS** : `conic-gradient`/`radial-gradient` multi-stops, `background-size: 200% 200%`, animation 8-12 s, `mix-blend-mode: screen`.
- **A11y** : ⚠ contraste du texte posé sur le gradient. **Conv.** : haute. S'accorde bien avec un `{{BRAND_GRADIENT}}` existant.

### Bento Box Grid
- **Pour** : pages produit, showcases de fonctionnalités, marketing « à la Apple », portfolios. **Jamais** : tableaux denses, contenu très textuel.
- **Signature CSS** : grid 4 colonnes à spans variés, `border-radius: 16-24px`, ombres douces, hover `scale(1.02)`.
- **A11y** : bon. **Conv.** : haute. Très scannable pour des propositions de valeur.

### Neubrutalism
- **Pour** : marques jeunes, startups créatives, tech blogs. **Jamais** : luxe, finance, santé, secteurs conservateurs.
- **Signature CSS** : `border: 3px solid #000`, `box-shadow: 5px 5px 0 #000`, angles droits, aplats francs, `font-weight: 700+`, pas de gradient.
- **A11y** : excellent. **Conv.** : haute.

### Brutalism (classique)
- **Pour** : portfolios design, éditorial contre-culture. **Jamais** : B2B, secteurs conservateurs, pages de conversion.
- **Signature CSS** : radius 0, `transition: none`, system-ui/monospace, couleurs primaires pures, grille visible.
- **A11y** : bon. **Conv.** : faible — réserver aux contenus de marque, pas aux pages de vente.

### Vibrant & Block-based
- **Pour** : startups, agences créatives, audiences jeunes. **Jamais** : finance, santé, institutionnel.
- **Signature CSS** : sections larges (gaps 48 px+), type 32 px+, 4-6 couleurs contrastées, motifs animés, scroll-snap.
- **A11y** : ⚠ vérifier WCAG sur couleurs vives. **Conv.** : haute.

### Exaggerated Minimalism
- **Pour** : mode, architecture, agences, luxe, éditorial. **Jamais** : catalogues, formulaires, contenus denses.
- **Signature CSS** : `font-size: clamp(3rem, 10vw, 12rem)`, `font-weight: 900`, `letter-spacing: -0.05em`, whitespace massif, un seul accent.
- **A11y** : bon. **Conv.** : haute.

### Kinetic Typography
- **Pour** : héros de landing, storytelling, portfolios créatifs. **Jamais** : contenu long, audiences sensibles au mouvement, formulaires.
- **Signature CSS** : `@keyframes` sur le texte, `background-clip: text`, split text, révélations au scroll.
- **A11y** : ❌ faible — `prefers-reduced-motion` obligatoire avec fallback statique. **Conv.** : très haute en héros.

### Motion-Driven
- **Pour** : storytelling, expériences interactives, portfolios. **Jamais** : dashboards, contenu dense, appareils modestes.
- **Signature CSS** : Intersection Observer, `transform: translateY/X`, `will-change: transform`, parallax 3-5 couches, 300-400 ms.
- **A11y** : ⚠ `prefers-reduced-motion` obligatoire. **Conv.** : haute.

### Parallax Storytelling
- **Pour** : storytelling de marque, lancements, études de cas, rapports annuels. **Jamais** : e-commerce, SEO-critique, mobile-first strict.
- **Signature CSS** : `position: sticky`, `perspective`, scroll-snap, couches z-index, déclencheurs Intersection Observer.
- **A11y** : ❌ faible — fallback statique obligatoire. **Conv.** : haute.

### Organic Biophilic / Nature Distilled
- **Pour** : bien-être, durabilité, produits artisanaux/bio, spa-beauté. **Jamais** : tech, gaming, finance corporate.
- **Signature CSS** : tons terre, radius organiques variés (16-24 px), formes SVG « blob », grain/texture subtils, ombres naturelles.
- **A11y** : bon. **Conv.** : haute.

### Editorial Grid / Magazine
- **Pour** : blogs, articles longs, contenus éditoriaux, médias. **Jamais** : dashboards, catalogues, temps réel.
- **Signature CSS** : grid à zones nommées, `column-count`, lettrines `::first-letter`, `figure/figcaption`, serif pour le corps.
- **A11y** : excellent. **Conv.** : moyenne — pensé pour la lecture, pas la conversion.

### Vintage Analog / Retro Film
- **Pour** : photo, musique/vinyle, nostalgie, cafés. **Jamais** : SaaS moderne, santé, enterprise.
- **Signature CSS** : `filter: sepia() contrast() saturate(0.8)`, grain SVG, light leaks, cadres polaroid.
- **A11y** : bon. **Conv.** : haute sur les audiences ciblées.

### Liquid Glass
- **Pour** : SaaS premium, e-commerce haut de gamme, expériences de marque. **Jamais** : budget serré, perf limitée, accessibilité critique.
- **Signature CSS** : morphing SVG 400-600 ms, `backdrop-filter: blur + saturate`, gradients iridescents.
- **A11y** : ⚠ contraste. **Conv.** : haute. Complexité élevée — ne choisir que si l'équipe peut l'exécuter proprement.

## Styles orientés landing page

| Style | Pour | Jamais | Signature |
|---|---|---|---|
| **Hero-Centric** | Landing SaaS/produit, lancements | Navigation complexe, contenu dense | Hero 60-80 % au-dessus du pli, `min-height: 100vh` flex centré, un seul CTA primaire, reveal doux |
| **Conversion-Optimized** | Essai gratuit, lead gen, pricing | Explications complexes | CTA sticky, formulaire `max-width: 600px`, focus rings, états loading/succès |
| **Feature-Rich Showcase** | SaaS enterprise, produits complexes | Produits simples | Grid `auto-fit minmax(280px, 1fr)`, cartes hover lift, fonds alternés |
| **Minimal & Direct** | Services simples, indie, consulting | Produits riches en features | Colonne unique `max-width: 680px`, corps 18-20 px, quasi aucune animation |
| **Social Proof-Focused** | B2B, services pro, marques établies | Produits sans utilisateurs | Témoignages avatar+nom+rôle, grille de logos grayscale, compteurs animés |
| **Interactive Product Demo** | SaaS, outils, produits dev | Services non digitaux | Vidéo/mockup interactif, indicateurs d'étapes, lightbox screenshots |
| **Trust & Authority** | Santé, finance, legal, enterprise | Produits casual/viraux | Badges, certifications, métriques, palette bleu/gris, ombres discrètes |
| **Storytelling-Driven** | Marques à mission, premium/lifestyle | Enterprise classique | Sections scroll-snap, reveals, alternance image-texte, timeline |

## Règles transverses

1. **Un style par site.** Ne pas mélanger flat et glassmorphism au hasard ; les effets (ombres, blur, radius) découlent du style choisi.
2. **La marque d'abord.** Couleurs et police viennent de `01-brand/style-guide.md` ; le style ne fournit que la grammaire (layout, effets, rythme).
3. **Complexité = coût.** Kinetic/Parallax/Liquid Glass exigent une exécution parfaite ; en cas de doute, choisir Flat, Swiss 2.0 ou Bento.
4. **Motion = opt-in.** Tout style animé embarque `prefers-reduced-motion` avec fallback complet.
