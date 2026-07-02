# Publishing playbook — blog {{COMPANY_NAME}}

> Comment un article validé passe du repo au blog. Le CMS est choisi pendant `/tools-setup` ({{BLOG_CMS}}) ; compléter la section correspondante à la première publication et supprimer les autres.

## Règles communes (quel que soit le CMS)

1. L'article part de `articles/YYYY-MM-DD-<slug>.md` avec un frontmatter complet et `status: ready` (voir `CLAUDE.md`, étape 8).
2. **Dry-run obligatoire** avant tout push automatisé : `python3 scripts/dry-run-push.py --target {{BLOG_CMS}} --file articles/<fichier>` — relecture du payload, confirmation humaine, puis push réel.
3. Après publication : URL finale enregistrée dans le frontmatter, `status: published`, URL soumise à Google Search Console, entrée du calendrier éditorial passée à `publié`.

## Méthode de publication (compléter selon l'outil)

### Publication manuelle (défaut, aucun connecteur requis)

1. Copier le corps de l'article dans l'éditeur du CMS.
2. Reporter meta title, meta description, slug, catégorie/pilier et tags depuis le frontmatter.
3. Téléverser les images avec leur alt-text ; vérifier le schema (Article/FAQPage) si le CMS le gère.
4. Publier, puis dérouler la règle commune n°3.

### Publication via API / webhook (si connecteur configuré)

- Connecteur : `_integrations/connectors/` (généré ou activé par `/tools-setup`).
- Variables d'environnement : voir `.env.example` (jamais de clé dans ce fichier).
- Le connecteur pousse en **brouillon** dans le CMS ; la mise en ligne finale reste une action humaine dans l'interface du CMS.

## Historique des particularités (à compléter à l'usage)

*Noter ici tout ce que la publication sur ce CMS exige de spécifique : taille d'image à la une, comportement des ancres, gestion des tableaux, plugins SEO…*
