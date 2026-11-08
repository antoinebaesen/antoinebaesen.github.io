# Publier plusieurs sites sur antoinebaesen.github.io

L’export est entièrement statique : HTML, CSS, JavaScript, données, images et polices locales. Aucun serveur applicatif, compte ChatGPT, Node.js ou installation n’est nécessaire sur GitHub Pages. Il faut un hébergement HTTP ; ouvrir `index.html` par double-clic avec `file://` ne permet pas au navigateur de charger les données.

## Première publication

1. Créer un dépôt **public** nommé exactement `antoinebaesen.github.io` sur le compte `antoinebaesen`, ou utiliser ce dépôt s’il existe déjà.
2. Extraire `exports/askallor-premiere-installation.zip`. Copier **son contenu** à la racine du dépôt, sans le dossier englobant daté.
3. Dans **Settings → Pages**, choisir **Deploy from a branch**, puis la branche `main`, dossier `/ (root)`, et enregistrer.
4. Après la publication GitHub, ouvrir **https://antoinebaesen.github.io/** pour l’accueil, ou **https://antoinebaesen.github.io/askallor-wiki/** pour le wiki.

Arborescence attendue :

```text
antoinebaesen.github.io/
├── .nojekyll
├── index.html
├── projects.json
├── README.md
├── askallor-wiki/
│   ├── index.html
│   ├── .nojekyll
│   ├── app.js
│   ├── style.css
│   ├── map-cells.css
│   ├── data.json
│   ├── source.md
│   ├── fonts/
│   └── media/
└── autre-projet/
    └── index.html
```

`.nojekyll` désactive le traitement Jekyll pour servir les fichiers tels quels. Le ZIP le contient ; si l’outil de transfert masque ce fichier, créer un fichier vide `.nojekyll` à la racine.

Si le dépôt possède déjà une page d’accueil ou d’autres sites, **conserver ces fichiers** : ajouter seulement le dossier `askallor-wiki` et `.nojekyll`, puis ajouter un lien vers `./askallor-wiki/` dans l’accueil existant. L’accueil fourni est facultatif.

## Ajouter un autre projet

Déposer le site statique dans un autre dossier, par exemple `mon-jeu/`. Avec l’accueil fourni, ajouter une entrée à `projects.json` :

```json
[
  {
    "name": "Wiki Askallor",
    "description": "Les Chroniques de l’Empire.",
    "path": "./askallor-wiki/"
  },
  {
    "name": "Mon jeu",
    "description": "Un autre projet.",
    "path": "./mon-jeu/"
  }
]
```

Chaque dossier sert de point d’entrée : aucun routeur commun n’est nécessaire. Askallor gère ensuite ses pages avec des fragments, par exemple `/askallor-wiki/#/cartes` et `/askallor-wiki/#/fiche/neuchwander`. Les liens directs et le rafraîchissement fonctionnent sans réécriture ni page 404 spéciale.

Tous les sites de ce dépôt partagent le domaine. Chaque futur projet doit employer des chemins relatifs pour ses fichiers et ses propres clés de stockage dans le navigateur.

## Mettre le wiki à jour

Dans le projet source local :

```powershell
npm.cmd ci
npm.cmd run export:pages
```

Ou double-cliquer sur **Exporter-GitHubPages.cmd**. Le script vérifie les données, les images et les polices locales, régénère tous les fichiers, puis crée des ZIP standards avec .NET, sans entrée racine `./`. Il les extrait avec Windows PowerShell `Expand-Archive` et compare les empreintes SHA-256 de tous les fichiers extraits aux fichiers générés avant de valider la publication. Les fichiers `.nojekyll` sont inclus. Chaque génération crée un nouveau dossier daté et deux archives datées dans `exports/`, sans remplacer les exports précédents.

Après une génération réussie, les fichiers pratiques suivants sont actualisés :

- **`exports/askallor-publication.zip`** : le ZIP à utiliser pour les mises à jour suivantes. Il contient uniquement `askallor-wiki/` et `.nojekyll`. L’extraire à la racine du dépôt GitHub Pages pour remplacer les fichiers du wiki, en conservant l’accueil, `projects.json` et les autres projets.
- **`exports/askallor-premiere-installation.zip`** : le wiki et son accueil multi-projets, pour la première publication.
- **`exports/derniere-publication.json`** : les chemins, la date de génération, les nombres de fiches/événements/régions et les empreintes SHA-256 des ZIP.

La génération ne contacte pas GitHub et n’effectue aucun commit ou envoi : elle prépare les fichiers à publier. Si une validation échoue, le script s’arrête avant d’actualiser les ZIP de dernière publication. Le double-clic installe les dépendances si elles sont absentes ; les générations ordinaires n’utilisent pas le réseau quand elles sont déjà installées.

Le contenu des fiches se modifie toujours dans le projet source, notamment `content/wiki.md` et `public/media/`, puis se régénère. Un fichier supprimé de la source n’est pas inclus dans le nouvel export. Si l’ancien fichier existe dans le dépôt GitHub, sa suppression éventuelle reste à faire dans le dossier `askallor-wiki/` du dépôt.

Le ZIP contient seulement le site généré et l’accueil. Il n’embarque ni `oldData`, ni dépendances Node, ni configuration d’hébergement Sites, ni historique Git. `source.md` est la source éditoriale nécessaire à l’atelier et reste accessible aux visiteurs, comme les données publiques du wiki. Les modifications de l’atelier sont des brouillons locaux et ne changent pas les fichiers publiés sur GitHub.

## Vérifier l’export localement

Depuis le projet source, en remplaçant le chemin par celui du dossier exporté :

```powershell
node scripts/preview-pages.mjs "exports/github-pages-…"
```

Ouvrir **http://127.0.0.1:4390/askallor-wiki/**. Le chemin reproduit celui de GitHub Pages. Arrêter le serveur avec `Ctrl+C`.

## Autre organisation possible

GitHub permet également un dépôt par projet : un dépôt `askallor-wiki`, avec Pages activé, donne la même adresse `https://antoinebaesen.github.io/askallor-wiki/`. Pour cette variante, déposer le **contenu** de `askallor-wiki/` à la racine de ce dépôt. Choisir une seule organisation pour éviter de servir deux projets au même chemin.

Références : [types de sites GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages), [création d’un site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).
