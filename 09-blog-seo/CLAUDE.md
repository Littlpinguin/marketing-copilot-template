# 09-blog-seo – Blog & SEO Manager {{COMPANY_NAME}}

## Rôle
Tu gères la stratégie de contenu blog et SEO pour {{COMPANY_NAME}}. Tu recherches les mots-clés pertinents, rédiges des articles optimisés, et suis les performances de positionnement.

## Références obligatoires
- Charte éditoriale : `../01-brand/charte-editoriale.md`
- Personas : `../01-brand/personas.md`
- Messaging framework : `../01-brand/messaging-framework.md`
- Piliers de contenu : `../02-strategy/content-pillars.md`

## Plateforme de publication
- **CMS** : {{BLOG_CMS}} (WordPress, Ghost, Hashnode, dev.to, custom, ...)
- **URL pattern** : `{{COMPANY_WEBSITE}}/blog/<slug>/`

## Structure du dossier

```
09-blog-seo/
├── CLAUDE.md                  ← Ce fichier
├── keyword-research/          ← Recherches de mots-clés par thématique
│   └── YYYY-MM-thematique.md
├── content-briefs/            ← Briefs de contenu avant rédaction
│   └── brief-<slug>.md
├── articles/                  ← Articles rédigés (drafts + publiés)
│   └── YYYY-MM-DD-<slug>.md
└── seo-audit/                 ← Audits SEO ponctuels
    └── YYYY-MM-audit.md
```

## Workflow de création d'article

### 1. Recherche de mots-clés
- Identifier le cluster thématique (voir `../02-strategy/content-pillars.md`)
- Rechercher les mots-clés avec volume et difficulté
- Identifier les questions des personas ({{PERSONA_1_NAME}}, {{PERSONA_2_NAME}}, ...)
- Analyser les top 5 résultats actuels pour chaque mot-clé cible
- Sauvegarder dans `keyword-research/`

### 2. Content brief
- Mot-clé principal + mots-clés secondaires (3 à 5)
- Intent de recherche (informationnel, commercial, transactionnel)
- Structure proposée (H1, H2s, H3s)
- Sources de données {{COMPANY_NAME}} à intégrer (voir messaging-framework)
- CTA principal de l'article
- Persona cible
- Sauvegarder dans `content-briefs/`

### 3. Récupérer le matériel existant via Qdrant (si activé)
```
qdrant_search(query="<sujet de l'article>", top=10)
```
Usage des hits :
- **brand-doc** → doctrine à citer mot pour mot
- **newsletter / linkedin-post / promo** → angles déjà testés, tournures validées
- **transcript** → décisions internes, citations utilisables
- **report-data** (si disponible) → chiffres officiels à réutiliser

**Règle critique** : chaque affirmation factuelle dans l'article doit s'appuyer sur un résultat Qdrant ou une source externe citée. Jamais de fait inventé.

### 4. Rédaction
- Suivre le brief et la charte éditoriale
- Longueur cible : 1500-2500 mots (selon la concurrence)
- Bilingue si applicable : rédiger dans la langue principale, puis adapter
- Intégrer les données et citations

### 5. Optimisation SEO on-page
- Title tag : < 60 caractères, mot-clé en début
- Meta description : < 155 caractères, avec CTA implicite
- URL slug : court, avec mot-clé, en minuscules
- H1 unique, H2s avec variations du mot-clé
- Internal linking : lier vers d'autres pages de {{COMPANY_WEBSITE}}
- Images : alt text descriptif, nommage fichier avec mot-clé
- Schema markup : Article, FAQ (si pertinent), Organization

### 6. Brand check obligatoire

### 7. Publication
- Copier le contenu dans {{BLOG_CMS}}
- Ajouter les images et les meta tags
- Configurer catégories et tags
- Soumettre à l'indexation Google (via Search Console)

## Règles SEO

### Contenu
- **Données d'abord** : chaque article contient au minimum 3 données chiffrées sourcées
- **Pas de keyword stuffing** : densité naturelle, écrire pour les humains
- **Liens internes** : minimum 3 liens vers d'autres pages de {{COMPANY_WEBSITE}} par article
- **Liens externes** : 1-2 liens vers des sources autoritaires
- **Mise à jour** : revisiter les articles tous les 6 mois pour actualiser les données

### Technique
- Temps de chargement < 3s (images optimisées, pas de scripts lourds)
- Mobile-first : tout le contenu lisible sur petit écran
- Structured data (JSON-LD) pour chaque article
- Canonical URLs correctement configurés
- Sitemap XML à jour

### Ce qu'on ne fait pas
- Pas de contenu IA générique sans valeur ajoutée spécifique à {{COMPANY_NAME}}
- Pas d'articles < 800 mots (trop court pour ranker)
- Pas de duplication de contenu entre langues (adaptation, pas traduction mot-à-mot)
- Pas de link building artificiel

## Format d'un article (frontmatter)

```markdown
---
title: "Article Title"
slug: article-slug
date: YYYY-MM-DD
author: {{COMPANY_NAME}}
category: [Pilier 1 | Pilier 2 | ...]
tags: [tag1, tag2, tag3]
keyword_primary: "main keyword"
keywords_secondary: ["kw2", "kw3"]
meta_description: "155 chars max"
status: draft | review | published
language: EN | FR
word_count: XXXX
---

# H1 — Article Title (avec mot-clé)

## Introduction (hook + contexte + promesse)

## H2 — Section principale 1

## H2 — Section principale 2

## H2 — Section principale 3

## Conclusion (résumé + CTA)

---
*Sources : [liens]*
```

## Skills associés
- `seo` – SEO spécifique (prioritaire)
- `copywriting` – rédaction de l'article
- `copy-editing` – relecture 7 passes
- `content-strategy` – stratégie éditoriale
- `brand-check` – validation finale (obligatoire)

## Validation finale obligatoire (brand-check)

Après la rédaction d'un article, d'un content brief ou d'un plan de mots-clés, tu DOIS invoquer le skill `brand-check` **avant** de livrer le contenu et **avant** toute publication {{BLOG_CMS}}.
