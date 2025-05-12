# 📦 Auto-Mods Downloader pour Factorio

Ce script Python permet de télécharger automatiquement les versions de certains mods Factorio, en utilisant un miroir (`re146.dev`). Il a été conçu pour permettre de télécharger des mods sans compte Factorio.

## ✅ Fonctionnalités

- Télécharge automatiquement les fichiers `.zip` des mods listés
- Récupère la version disponible via l'API `re146.dev`
- Crée un dossier `modspack/` avec tous les fichiers prêts à l'emploi
- Aucun besoin de compte Factorio ou d’authentification

## ⚙️ Pré-requis

- Python 3.7 ou supérieur
- Module Python `requests` (installé par défaut dans beaucoup de distributions, sinon voir ci-dessous)

## 🔧 Installation

Clone ou télécharge ce dépôt :

```bash
git clone https://github.com/ton-utilisateur/auto-factorio-mods.git
cd auto-factorio-mods

```
## 🚀 Utilisation

La liste des mods à télécharger est à modifier en haut directement dans le script :

Exempple : 
```python
mods = [
    "Krastorio2",
    "Krastorio2Assets",
    "krastorio-2-compat",
    "FluidMustFlow",
    "nach0_modpack_alienbiomes",
    "ArmouredBiters",
]
```

⚠️ Remarques
Ce script repose sur un miroir communautaire (re146.dev) et n’est pas affilié à Wube Software ou Factorio.

Il est possible que certains mods n’y soient pas disponibles, ou que les versions soient différentes de celles sur le portail officiel.

🪪 Licence
Code placé dans le domaine public ou sous licence MIT — fais-en ce que tu veux.
