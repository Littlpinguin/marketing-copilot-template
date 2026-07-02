# Palettes sémantiques par type de produit — bibliothèque de fallback

> Condensé et adapté de `colors.csv` d'[ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) v2.5.0 (MIT, © 2024 Next Level Builder). 28 palettes retenues sur 161 — sélection web marketing. Les accents ont déjà été ajustés à la source pour un contraste WCAG ≥ 3:1.

## Quand utiliser ce fichier — et quand ne pas l'utiliser

**La marque prime.** Si `01-brand/style-guide.md` fournit des couleurs, ces palettes ne servent **jamais** à les remplacer. Usages légitimes :

1. **Calibration** — vérifier que le niveau de saturation/température des couleurs de marque est cohérent avec les usages du secteur (ex. un CTA orange vif sur un site juridique mérite discussion).
2. **Complétion des rôles manquants** — la marque donne primary/accent mais pas `muted`, `border`, `destructive` : piocher les neutres de la ligne du secteur correspondant (colonnes Muted-FG, Border, Destructive sont volontairement quasi constantes).
3. **Fallback intégral** — uniquement si la marque n'a défini aucune couleur (setup incomplet) et avec l'accord explicite de l'utilisateur.

## Rôles sémantiques

Chaque palette suit le modèle shadcn/ui : `primary` (identité, éléments dominants), `on-primary` (texte posé sur primary), `secondary` (variante de soutien), `accent` (CTA et actions — contraste ≥ 3:1 sur background), `background`/`foreground` (page), `card` (surfaces élevées), `muted-foreground` (texte secondaire, ≥ 4.5:1 requis), `border`, `destructive` (erreurs, suppressions).

| Type de produit | Primary | On-Primary | Secondary | Accent (CTA) | Background | Foreground | Card | Muted-FG | Border | Destructive | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **SaaS (général)** | `#2563EB` | `#FFFFFF` | `#3B82F6` | `#EA580C` | `#F8FAFC` | `#1E293B` | `#FFFFFF` | `#64748B` | `#E2E8F0` | `#DC2626` | Trust blue + orange CTA contrast |
| **Micro-SaaS / indie** | `#6366F1` | `#FFFFFF` | `#818CF8` | `#059669` | `#F5F3FF` | `#1E1B4B` | `#FFFFFF` | `#64748B` | `#E0E7FF` | `#DC2626` | Indigo primary + emerald CTA |
| **E-commerce** | `#059669` | `#FFFFFF` | `#10B981` | `#EA580C` | `#ECFDF5` | `#064E3B` | `#FFFFFF` | `#64748B` | `#A7F3D0` | `#DC2626` | Success green + urgency orange |
| **E-commerce luxe** | `#1C1917` | `#FFFFFF` | `#44403C` | `#A16207` | `#FAFAF9` | `#0C0A09` | `#FFFFFF` | `#64748B` | `#D6D3D1` | `#DC2626` | Premium dark + gold accent |
| **Service B2B** | `#0F172A` | `#FFFFFF` | `#334155` | `#0369A1` | `#F8FAFC` | `#020617` | `#FFFFFF` | `#64748B` | `#E2E8F0` | `#DC2626` | Professional navy + blue CTA |
| **Agence créative** | `#EC4899` | `#FFFFFF` | `#F472B6` | `#0891B2` | `#FDF2F8` | `#831843` | `#FFFFFF` | `#64748B` | `#FBCFE8` | `#DC2626` | Bold pink + cyan accent |
| **Portfolio / personnel** | `#18181B` | `#FFFFFF` | `#3F3F46` | `#2563EB` | `#FAFAFA` | `#09090B` | `#FFFFFF` | `#64748B` | `#E4E4E7` | `#DC2626` | Monochrome + blue accent |
| **Fintech / crypto** | `#F59E0B` | `#0F172A` | `#FBBF24` | `#8B5CF6` | `#0F172A` | `#F8FAFC` | `#222735` | `#94A3B8` | `#334155` | `#EF4444` | Gold trust + purple tech |
| **Outil de productivité** | `#0D9488` | `#FFFFFF` | `#14B8A6` | `#EA580C` | `#F0FDFA` | `#134E4A` | `#FFFFFF` | `#64748B` | `#99F6E4` | `#DC2626` | Teal focus + action orange |
| **Plateforme IA / chatbot** | `#7C3AED` | `#FFFFFF` | `#A78BFA` | `#0891B2` | `#FAF5FF` | `#1E1B4B` | `#FFFFFF` | `#64748B` | `#DDD6FE` | `#DC2626` | AI purple + cyan interactions |
| **Base de connaissances / docs** | `#475569` | `#FFFFFF` | `#64748B` | `#2563EB` | `#F8FAFC` | `#1E293B` | `#FFFFFF` | `#64748B` | `#E2E8F0` | `#DC2626` | Neutral grey + link blue |
| **Beauté / spa / bien-être** | `#EC4899` | `#FFFFFF` | `#F9A8D4` | `#8B5CF6` | `#FDF2F8` | `#831843` | `#FFFFFF` | `#64748B` | `#FBCFE8` | `#DC2626` | Soft pink + lavender luxury |
| **Marque luxe / premium** | `#1C1917` | `#FFFFFF` | `#44403C` | `#A16207` | `#FAFAF9` | `#0C0A09` | `#FFFFFF` | `#64748B` | `#D6D3D1` | `#DC2626` | Premium black + gold accent |
| **Restauration / food** | `#DC2626` | `#FFFFFF` | `#F87171` | `#A16207` | `#FEF2F2` | `#450A0A` | `#FFFFFF` | `#64748B` | `#FECACA` | `#DC2626` | Appetizing red + warm gold |
| **Immobilier** | `#0F766E` | `#FFFFFF` | `#14B8A6` | `#0369A1` | `#F0FDFA` | `#134E4A` | `#FFFFFF` | `#64748B` | `#99F6E4` | `#DC2626` | Trust teal + professional blue |
| **Voyage / tourisme** | `#0EA5E9` | `#0F172A` | `#38BDF8` | `#EA580C` | `#F0F9FF` | `#0C4A6E` | `#FFFFFF` | `#64748B` | `#BAE6FD` | `#DC2626` | Sky blue + adventure orange |
| **Services juridiques** | `#1E3A8A` | `#FFFFFF` | `#1E40AF` | `#B45309` | `#F8FAFC` | `#0F172A` | `#FFFFFF` | `#64748B` | `#CBD5E1` | `#DC2626` | Authority navy + trust gold |
| **Formation en ligne** | `#0D9488` | `#FFFFFF` | `#2DD4BF` | `#EA580C` | `#F0FDFA` | `#134E4A` | `#FFFFFF` | `#64748B` | `#5EEAD4` | `#DC2626` | Progress teal + achievement orange |
| **Association / non-profit** | `#0891B2` | `#FFFFFF` | `#22D3EE` | `#EA580C` | `#ECFEFF` | `#164E63` | `#FFFFFF` | `#64748B` | `#A5F3FC` | `#DC2626` | Compassion blue + action orange |
| **Recrutement / job board** | `#0369A1` | `#FFFFFF` | `#0EA5E9` | `#16A34A` | `#F0F9FF` | `#0C4A6E` | `#FFFFFF` | `#64748B` | `#BAE6FD` | `#DC2626` | Professional blue + success green |
| **Média / actualités** | `#DC2626` | `#FFFFFF` | `#EF4444` | `#1E40AF` | `#FEF2F2` | `#450A0A` | `#FFFFFF` | `#64748B` | `#FECACA` | `#DC2626` | Breaking red + link blue |
| **Magazine / blog** | `#18181B` | `#FFFFFF` | `#3F3F46` | `#EC4899` | `#FAFAFA` | `#09090B` | `#FFFFFF` | `#64748B` | `#E4E4E7` | `#DC2626` | Editorial black + accent pink |
| **Agence marketing** | `#EC4899` | `#FFFFFF` | `#F472B6` | `#0891B2` | `#FDF2F8` | `#831843` | `#FFFFFF` | `#64748B` | `#FBCFE8` | `#DC2626` | Bold pink + creative cyan |
| **Événementiel** | `#7C3AED` | `#FFFFFF` | `#A78BFA` | `#EA580C` | `#FAF5FF` | `#4C1D95` | `#FFFFFF` | `#64748B` | `#DDD6FE` | `#DC2626` | Excitement purple + action orange |
| **Communauté / membership** | `#7C3AED` | `#FFFFFF` | `#A78BFA` | `#16A34A` | `#FAF5FF` | `#4C1D95` | `#FFFFFF` | `#64748B` | `#DDD6FE` | `#DC2626` | Community purple + join green |
| **Newsletter** | `#0369A1` | `#FFFFFF` | `#0EA5E9` | `#EA580C` | `#F0F9FF` | `#0C4A6E` | `#FFFFFF` | `#64748B` | `#BAE6FD` | `#DC2626` | Trust blue + subscribe orange |
| **Produits digitaux** | `#6366F1` | `#FFFFFF` | `#818CF8` | `#16A34A` | `#EEF2FF` | `#312E81` | `#FFFFFF` | `#64748B` | `#C7D2FE` | `#DC2626` | Digital indigo + buy green |
| **CRM / gestion clients** | `#2563EB` | `#FFFFFF` | `#3B82F6` | `#059669` | `#F8FAFC` | `#0F172A` | `#FFFFFF` | `#64748B` | `#E4ECFC` | `#DC2626` | Professional blue + deal green |
## Règles d'application

1. **Ne jamais poser un hex brut dans un composant** — toujours passer par les tokens `--primary`, `--accent`, etc.
2. **Le CTA utilise `accent`, pas `primary`** — le contraste CTA/fond doit rester le plus fort de la page.
3. **`muted-foreground` `#64748B` sur fond blanc = 4.6:1** — ne pas l'éclaircir davantage pour du texte porteur de sens.
4. **Dark mode** : ne pas inverser mécaniquement — désaturer les couleurs vives, éclaircir les textes, re-tester chaque paire.
5. **Vérification finale** : chaque paire fond/texte du système passe 4.5:1 (texte normal) ou 3:1 (texte large ≥ 24 px / composants UI).
