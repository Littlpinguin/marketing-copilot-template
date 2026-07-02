# Bibliothèque de sections réutilisables — {{COMPANY_NAME}}

Source de vérité des sections HTML pour toute page produite dans `05-web-content/` (landing pages, pages de capture, outils web, pages statiques).

**Règle d'usage.** Avant d'écrire un bloc HTML : chercher ici. Si la section existe → la décliner (le contenu change, la structure reste). Si elle n'existe pas → la créer, puis **l'ajouter à ce fichier** dans la foulée. Chaque page qui réinvente sa structure crée un dialecte visuel de plus à maintenir.

Les structures ci-dessous sont des **squelettes sémantiques** : classes stables, tokens en custom properties. Le design (espacements fins, compositions, interactions) est affiné par les skills `design-direction` / `design-system` sous contrainte des tokens — jamais en changeant les couleurs ou les polices.

## Bloc de tokens de référence

À inclure dans le `<style>` de chaque page. Les valeurs viennent de `../01-brand/style-guide.md` — jamais d'autres.

```html
<style>
  :root {
    --font-primary: '{{BRAND_FONT_PRIMARY}}', system-ui, sans-serif;
    --color-primary: {{BRAND_COLOR_PRIMARY}};
    --color-accent: {{BRAND_COLOR_ACCENT}};
    --color-dark: {{BRAND_COLOR_DARK}};
    --color-light: {{BRAND_COLOR_LIGHT}};
    --gradient: {{BRAND_GRADIENT}};
    --radius: {{BRAND_BORDER_RADIUS}};
    --space-xs: 8px; --space-s: 16px; --space-m: 32px;
    --space-l: 64px; --space-xl: 96px;
    --container: 1120px;
  }
  body { font-family: var(--font-primary); color: var(--color-dark); background: var(--color-light); margin: 0; }
  .container { max-width: var(--container); margin: 0 auto; padding: 0 var(--space-s); }
  section { padding: var(--space-l) 0; }
</style>
```

Breakpoints : 900px (tablette), 600px (mobile), 400px (petit mobile). Mobile-first.

---

## 1. Hero

**Usage** : ouverture de toute page. Proposition de valeur + CTA visibles sans scroller. Test des 5 secondes obligatoire.

```html
<header class="hero">
  <div class="container">
    <p class="hero__eyebrow">{{ACCROCHE_CONTEXTE}}</p>
    <h1 class="hero__title">{{PROPOSITION_DE_VALEUR}}</h1>
    <p class="hero__subtitle">{{POUR_QUI_ET_COMMENT}}</p>
    <div class="hero__actions">
      <a href="#conversion" class="btn btn--primary" data-track="cta_click" data-cta-position="hero">{{CTA_PRIMAIRE}}</a>
      <a href="#preuve" class="btn btn--ghost">{{CTA_SECONDAIRE}}</a>
    </div>
    <p class="hero__proof">{{MICRO_PREUVE}} <!-- ex : note, nb de clients, chiffre-clé --></p>
  </div>
</header>
```

Notes CRO : un seul H1 ; le CTA primaire porte l'action de conversion de la page ; la micro-preuve désamorce le scepticisme immédiatement.

## 2. Barre de preuve sociale (logos / chiffre)

**Usage** : juste sous le hero. Crédibiliser avant d'argumenter.

```html
<section class="logos" aria-label="Ils nous font confiance">
  <div class="container">
    <p class="logos__label">{{PHRASE_CONFIANCE}}</p>
    <ul class="logos__list">
      <li><img src="assets/logo-client-1.svg" alt="{{CLIENT_1}}" loading="lazy"></li>
      <!-- 4 à 6 logos max, monochromes de préférence -->
    </ul>
  </div>
</section>
```

## 3. Problème

**Usage** : formuler les frustrations du persona dans ses mots (`../01-brand/personas.md`).

```html
<section class="problem">
  <div class="container">
    <h2>{{TITRE_PROBLEME}}</h2>
    <ul class="problem__list">
      <li class="problem__item"><h3>{{FRUSTRATION_1}}</h3><p>{{DEVELOPPEMENT_1}}</p></li>
      <!-- 2 à 3 items, pas plus -->
    </ul>
  </div>
</section>
```

## 4. Solution / bénéfices

**Usage** : 3-4 blocs, bénéfice avant fonctionnalité, chaque bloc ancré dans un chiffre du messaging framework.

```html
<section class="benefits">
  <div class="container">
    <h2>{{TITRE_SOLUTION}}</h2>
    <div class="benefits__grid">
      <article class="benefit">
        <div class="benefit__icon" aria-hidden="true"><!-- SVG inline charté --></div>
        <h3>{{BENEFICE_1}}</h3>
        <p>{{PREUVE_OU_MECANISME_1}}</p>
      </article>
      <!-- ×3-4, grid responsive : 1 col mobile, 2 tablette, 3-4 desktop -->
    </div>
  </div>
</section>
```

## 5. Stats showcase

**Usage** : les chiffres en héros — un grand nombre bat un paragraphe.

```html
<section class="stats" id="preuve">
  <div class="container">
    <dl class="stats__grid">
      <div class="stat"><dt>{{LIBELLE_1}}</dt><dd class="stat__number">{{CHIFFRE_1}}</dd></div>
      <!-- 3 stats max ; chaque chiffre vérifié contre messaging-framework.md ou source citée -->
    </dl>
  </div>
</section>
```

## 6. Témoignages

**Usage** : preuve incarnée. Nom + contexte obligatoires, portrait si disponible ; jamais de témoignage inventé.

```html
<section class="testimonials">
  <div class="container">
    <h2>{{TITRE_TEMOIGNAGES}}</h2>
    <div class="testimonials__grid">
      <figure class="testimonial">
        <blockquote>{{CITATION}}</blockquote>
        <figcaption>
          <img src="assets/portrait-1.webp" alt="" class="testimonial__avatar" loading="lazy">
          <span class="testimonial__name">{{NOM}}</span>
          <span class="testimonial__role">{{FONCTION_ENTREPRISE}}</span>
        </figcaption>
      </figure>
    </div>
  </div>
</section>
```

## 7. Étude de cas

**Usage** : résultat concret en trois temps — situation, action, résultat chiffré.

```html
<section class="case-study">
  <div class="container">
    <h2>{{TITRE_CAS}}</h2>
    <div class="case-study__body">
      <p class="case-study__context">{{SITUATION}}</p>
      <p class="case-study__action">{{CE_QUI_A_ETE_FAIT}}</p>
      <p class="case-study__result"><strong>{{RESULTAT_CHIFFRE}}</strong></p>
    </div>
    <a href="{{URL_CAS_COMPLET}}" class="btn btn--ghost">{{CTA_LIRE_LE_CAS}}</a>
  </div>
</section>
```

## 8. Timeline / process

**Usage** : rassurer sur le « comment ça se passe » en 3-5 étapes.

```html
<section class="process">
  <div class="container">
    <h2>{{TITRE_PROCESS}}</h2>
    <ol class="process__steps">
      <li class="process__step"><span class="process__num">1</span><h3>{{ETAPE_1}}</h3><p>{{DETAIL_1}}</p></li>
      <!-- 3 à 5 étapes -->
    </ol>
  </div>
</section>
```

## 9. Pricing

**Usage** : pages offre. 1 à 3 plans, plan recommandé mis en avant, prix ancrés dans l'offre validée — jamais improvisés.

```html
<section class="pricing">
  <div class="container">
    <h2>{{TITRE_PRICING}}</h2>
    <div class="pricing__grid">
      <article class="plan plan--featured">
        <h3 class="plan__name">{{PLAN}}</h3>
        <p class="plan__price">{{PRIX}}<span class="plan__period">{{PERIODE}}</span></p>
        <ul class="plan__features"><li>{{INCLUS_1}}</li></ul>
        <a href="#conversion" class="btn btn--primary" data-track="cta_click">{{CTA_PLAN}}</a>
      </article>
    </div>
    <p class="pricing__reassurance">{{GARANTIE_OU_CONDITION}}</p>
  </div>
</section>
```

## 10. Tableau comparatif

**Usage** : audience en phase de comparaison. Rester factuel et vérifiable — pas de dénigrement.

```html
<section class="compare">
  <div class="container">
    <h2>{{TITRE_COMPARAISON}}</h2>
    <table class="compare__table">
      <thead><tr><th scope="col"></th><th scope="col">{{COMPANY_NAME}}</th><th scope="col">{{ALTERNATIVE}}</th></tr></thead>
      <tbody>
        <tr><th scope="row">{{CRITERE_1}}</th><td>{{VALEUR_NOUS}}</td><td>{{VALEUR_EUX}}</td></tr>
      </tbody>
    </table>
  </div>
</section>
```

## 11. Pour qui (blocs personas)

**Usage** : quand la page s'adresse à plusieurs personas — un bloc par persona, message principal de `personas.md`.

```html
<section class="for-whom">
  <div class="container">
    <h2>{{TITRE_POUR_QUI}}</h2>
    <div class="for-whom__grid">
      <article class="persona-card">
        <h3>{{PERSONA_1}}</h3>
        <p>{{MESSAGE_PRINCIPAL_PERSONA_1}}</p>
      </article>
    </div>
  </div>
</section>
```

## 12. FAQ (accordéon natif)

**Usage** : traitement des objections. Questions réelles des personas, pas du remplissage SEO.

```html
<section class="faq">
  <div class="container">
    <h2>{{TITRE_FAQ}}</h2>
    <details class="faq__item">
      <summary class="faq__question">{{OBJECTION_1}}</summary>
      <p class="faq__answer">{{REPONSE_1}}</p>
    </details>
    <!-- 4 à 8 questions ; <details>/<summary> natif : accessible, zéro JS -->
  </div>
</section>
```

## 13. Formulaire de capture

**Usage** : lead magnets et pages de capture. Règles : skill `cro-form` (fallback : email seul, bouton en bénéfice, RGPD). Voir skill `lead-magnet` pour le circuit complet (n8n → emailing → nurturing).

```html
<section class="capture" id="conversion">
  <div class="container">
    <h2>{{PROMESSE_LEAD_MAGNET}}</h2>
    <form class="capture__form" method="post" action="{{FORM_ENDPOINT}}" data-track="generate_lead">
      <label for="email" class="capture__label">{{LABEL_EMAIL}}</label>
      <input type="email" id="email" name="email" required autocomplete="email" placeholder="{{PLACEHOLDER_EMAIL}}">
      <button type="submit" class="btn btn--primary">{{CTA_BENEFICE}}</button>
      <p class="capture__rgpd">{{MENTION_RGPD}} <a href="{{URL_CONFIDENTIALITE}}">{{LIEN_CONFIDENTIALITE}}</a></p>
    </form>
  </div>
</section>
```

## 14. CTA final

**Usage** : clôture de toute landing page. Reformule la proposition de valeur ; CTA identique au hero (même action, même libellé). Fond gradient signature.

```html
<section class="final-cta" style="background: var(--gradient);">
  <div class="container">
    <h2 class="final-cta__title">{{REFORMULATION_PROPOSITION}}</h2>
    <p class="final-cta__subtitle">{{DERNIERE_REASSURANCE}}</p>
    <a href="#conversion" class="btn btn--light" data-track="cta_click" data-cta-position="final">{{CTA_PRIMAIRE}}</a>
  </div>
</section>
```

## 15. Footer

**Usage** : toute page. Vient de `templates/` — ne jamais réimplémenter par page. Minimum : logo, mentions légales, politique de confidentialité, contact. Sur une landing page de campagne : pas de navigation complète (fuites de conversion).

---

## Ajouter une section à la bibliothèque

1. Vérifier qu'aucune section existante ne couvre le besoin (y compris en la déclinant).
2. Écrire le squelette avec classes stables (`bloc__element`), tokens en custom properties, HTML sémantique et accessible.
3. Documenter : usage, notes CRO, contraintes.
4. L'ajouter ici avec un numéro, et signaler l'ajout dans le message de livraison.
