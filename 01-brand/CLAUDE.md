# 01-brand – Gardien de la marque {{COMPANY_NAME}}

## Rôle
Ce dossier est la **source unique de vérité** pour l'identité, le ton, le messaging et l'identité visuelle de {{COMPANY_NAME}}. Il ne produit rien : il est consulté par tous les autres rôles (`02-strategy/` à `09-blog-seo/`) avant toute création de contenu.

**Règle absolue** : en cas de contradiction entre `01-brand/` et un autre dossier, `01-brand/` fait foi. Si tu détectes une contradiction, signale-la avant d'agir.

## Accès rapide via Qdrant (si activé)

Si Qdrant est activé (`qdrant.enabled: true` dans `config.yaml`), les fichiers de ce dossier sont indexés dans la collection configurée. Pour toute question sur le ton, le vocabulaire, les chiffres, les personas ou la doctrine, la recherche sémantique est plus rapide qu'une lecture complète :

```
mcp__qdrant__qdrant_search(
  query="<ta question en langage naturel>",
  top=5,
  filter_source_key="brand"
)
```

**Règle** : quand une information est disponible via `qdrant_search`, préfère cette route à un `Read` long. Tu économises du contexte et tu remontes précisément le passage pertinent. La lecture complète d'un fichier reste justifiée pour `charte-editoriale.md` (courte, souvent lue en entier) ou pour vérifier l'absence d'un mot interdit.

Si Qdrant est désactivé, lire directement les fichiers ci-dessous.

## Quand consulter ce dossier

| Tu dois… | Lis en priorité |
|---|---|
| Rédiger un post, email, page, script d'événement | `charte-editoriale.md` + `messaging-framework.md` |
| Cibler une audience spécifique | `personas.md` |
| Choisir un chiffre ou une preuve | `messaging-framework.md` (section chiffres clés) |
| Utiliser une tagline, citation, formule signature | `charte-editoriale.md` (section formules signature) |
| Créer un visuel, choisir une couleur, une typo | `style-guide.md` |
| Comprendre le contexte stratégique global | `plateforme-de-marque.md` |
| Identifier un interlocuteur interne | `parties-prenantes.md` |
| Utiliser un asset visuel (logo, bannière, illustration) | `assets/` |

## Inventaire des fichiers

Ces fichiers sont créés pendant le bootstrap (Phase 1 – Identity validation). Si certains sont vides ou absents, c'est que la phase n'est pas terminée ou que l'utilisateur a marqué des gaps à compléter plus tard (`_gaps.md`).

| Fichier | Contenu | Quand s'en servir |
|---|---|---|
| `charte-editoriale.md` | Ton, vocabulaire de marque, mots interdits, règles par canal, bilinguisme, valeurs, formules signature | **À lire avant toute rédaction** |
| `messaging-framework.md` | Message central, messages par audience, top 10 chiffres clés, CTA types, hiérarchie des preuves | **Avant toute création de contenu qui convertit** |
| `personas.md` | 2-4 personas avec enjeux, frustrations, attentes, canaux, message principal | **Avant tout contenu ciblé** |
| `plateforme-de-marque.md` | Document stratégique complet (mission, vision, positionnement, valeurs, architecture) | Pour le contexte profond |
| `style-guide.md` | Identité visuelle : logos, palette, typographie, composants, illustration style, banned visuals | Avant toute création visuelle |
| `parties-prenantes.md` | Fondateurs, équipe, rôles fonctionnels | Pour citer un membre, assigner une action |
| `assets/` | Logos, bannières, illustrations, photos, visuels publiés | Réutiliser un visuel existant |

## Règles universelles de marque (rappel condensé)

Ces règles sont la synthèse de `charte-editoriale.md`. Si tu n'as qu'une minute, c'est ce qu'il faut retenir.

### Ton
{{BRAND_VOICE_POSITION}}

### Vocabulaire
- ✅ **Préférer** : {{BRAND_VOCABULARY_PREFERRED}}
- ❌ **Éviter / interdire** : {{BRAND_VOCABULARY_BANNED}}

### Typographie et couleurs
- **Police principale** : {{BRAND_FONT_PRIMARY}}
- **Primary** : `{{BRAND_COLOR_PRIMARY}}`
- **Accent** : `{{BRAND_COLOR_ACCENT}}`
- **Dark** : `{{BRAND_COLOR_DARK}}`
- **Light** : `{{BRAND_COLOR_LIGHT}}`
- **Gradient signature** : `{{BRAND_GRADIENT}}`
- **Border-radius** : {{BRAND_BORDER_RADIUS}}

### Visuels
- ✅ **Préférer** : {{BRAND_ILLUSTRATION_STYLE}}
- ❌ **Interdire** : {{BRAND_BANNED_VISUALS}}

### Taglines et formules de référence (réutilisables)
{{BRAND_TAGLINES}}

### Top chiffres clés
{{BRAND_TOP_NUMBERS}}

## Workflow de vérification de cohérence de marque

Avant de livrer tout contenu, l'agent qui le produit doit passer ce filtre (5 points) :

1. **Vocabulaire** – Aucun mot interdit ? Vocabulaire préféré utilisé ?
2. **Ton** – Aligné avec `{{BRAND_VOICE_POSITION}}` ?
3. **Preuve** – Chaque affirmation majeure adossée à un chiffre ou fait issu de `messaging-framework.md` ?
4. **Audience** – Persona cible identifié ? Message principal correspond à son attente ?
5. **Visuel** – Couleurs, police, border-radius conformes à `style-guide.md` ?

Si un point échoue → retour en rédaction, pas de publication. C'est exactement ce que fait le skill `brand-check`.

## Conflits et mises à jour

- **Si un autre CLAUDE.md contredit ce dossier** : `01-brand/` fait foi. Signale le conflit.
- **Si une règle manque** : ne pas inventer. Remonter à {{COMPANY_MAIN_CONTACT}}.
- **Si un chiffre devient obsolète** : mettre à jour `messaging-framework.md` ET `plateforme-de-marque.md` en même temps.

## Ce que ce dossier ne fait PAS

- ❌ Produire du contenu (→ rôles 03 à 09)
- ❌ Gérer le calendrier éditorial (→ `02-strategy/` + {{EDITORIAL_CALENDAR_TOOL}})
- ❌ Créer les visuels (→ `06-graphic-design/` + skill `image-generation`)
- ❌ Les skills spécialisés (→ `.agents/skills/`) — mais ceux-ci doivent tous lire `01-brand/` avant d'agir.
