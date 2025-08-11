Risk-Mapper : Prototype d'Outil de Pré-évaluation et Visualisation des Risques Industriels

Un prototype d'application web pour assister les consultants en risques dans la modélisation, la visualisation et la communication des premières phases d'une étude de dangers.

Lien vers la démo live : 
<br>
Auteur : MFOUM MINKO Daniel
<br>
Technologies principales : Python (Flask), JavaScript (Leaflet.js), PostgreSQL (PostGIS)

1. Contexte du Projet et Objectifs

Dans le cadre des missions de conseil en maîtrise des risques industriels, la réalisation d'études de dangers pour des sites (notamment des Installations Classées pour la Protection de l'Environnement - ICPE) est une activité centrale. La phase initiale de ces études implique la collecte de données, l'identification des phénomènes dangereux et la délimitation des périmètres de sécurité (zones d'effets thermiques, toxiques, de surpression...).

Ce processus peut être complexe et le rendu final difficile à appréhender pour les non-spécialistes.

Risk-Mapper a été conçu comme un outil d'aide à la décision visant à :

Accélérer la phase de pré-évaluation en centralisant les données clés d'un site.

Faciliter la communication avec les clients et les autorités en offrant une visualisation cartographique interactive des enjeux.

Fournir une base de travail standardisée pour les consultants, garantissant la cohérence des données pour la rédaction du plan d'urgence (POI).

2. Fonctionnalités Clés


Saisie Structurée des Données : Formulaire permettant d'enregistrer les informations essentielles d'un site :

Coordonnées géographiques (adresse convertie en latitude/longitude).

Type d'activité (chimie, pétrochimie, logistique...).

Principaux produits dangereux et seuils associés.

Scénarios de risques identifiés (ex: BLEVE, fuite toxique, incendie...).

Cartographie Interactive (Leaflet.js) :

Positionnement automatique du site sur une carte.

Visualisation dynamique des zones d'effets (cercles de danger) paramétrables en fonction du phénomène dangereux et de son intensité (ex: Seuil des Effets Létaux, Seuil des Effets Irréversibles).

Modélisation Simplifiée des Risques :

Permet d'associer un ou plusieurs scénarios de risque à un site.

Calcule et affiche les rayons des zones d'impact sur la carte, offrant un aperçu immédiat des enjeux territoriaux.

Génération de Fiches de Synthèse :

Exportation des données du site et de la carte en une fiche synthétique (format web ou PDF), servant de support pour les réunions ou d'annexe au rapport d'étude d'impact.

3. Stack Technique et Architecture

Ce projet a été développé pour démontrer la maîtrise d'un écosystème full-stack moderne et pertinent.

Backend :

Langage : Python 3

Framework : Flask (ou FastAPI) pour sa légèreté et sa robustesse.

API : Architecture RESTful pour la communication entre le frontend et le backend.

Frontend :

Langages : HTML5, CSS3, JavaScript (ES6+)

Librairie de Cartographie : Leaflet.js, un standard open-source pour les cartes interactives.

Requêtes API : Fetch API ou Axios.

Base de Données :

SGBD : PostgreSQL

Extension Géospatiale : PostGIS pour le stockage et l'interrogation efficace des coordonnées géographiques. Ce choix démontre une compréhension des besoins spécifiques à la manipulation de données spatiales.

(Alternative possible : MongoDB pour sa flexibilité avec les documents JSON)

Déploiement :

Hébergement : Heroku / PythonAnywhere / Render

Contrôle de Version : Git & GitHub


4. Installation et Lancement Local

Pour lancer ce projet sur votre machine locale, suivez ces étapes :

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# 1. Cloner le repository
git clone https://github.com/danie2minko/risk-mapper.git
cd risk-mapper

# 2. Créer et activer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer la base de données
#    - Assurez-vous d'avoir PostgreSQL et PostGIS installés.
#    - Créez une base de données.
#    - Copiez .env.example en .env et remplissez les informations de connexion.
#      DATABASE_URL="postgresql://user:password@host:port/database"

# 5. Lancer l'application backend
flask run

# 6. Ouvrir votre navigateur
#    Accédez à http://127.0.0.1:5000
5. Guide d'Utilisation

Sur la page d'accueil, cliquez sur "Ajouter un nouveau site".

Remplissez le formulaire avec les informations du site (ex: "Usine de production d'ammoniac, Grand-Couronne"). L'adresse sera automatiquement géocodée.

Ajoutez un ou plusieurs scénarios de risque en spécifiant le type de danger et le rayon d'effet en mètres.

Cliquez sur "Enregistrer". Vous serez redirigé vers la page de visualisation où le site et ses zones de danger sont affichés sur la carte.

Cliquez sur "Générer la Fiche" pour obtenir une synthèse imprimable.

6. Axes d'Amélioration Possibles (Roadmap)

Ce prototype est une base solide qui pourrait être étendue avec des fonctionnalités à plus forte valeur ajoutée :

Intégration de données externes : Connexion à des API pour superposer des couches d'information (ex: densité de population, zones naturelles protégées, conditions météorologiques en temps réel).

Modèles de calcul plus complexes : Implémentation de modèles de dispersion atmosphérique ou de flux thermiques plus précis que de simples cercles.

Gestion des utilisateurs et des projets : Authentification pour permettre à plusieurs consultants de gérer leurs propres portefeuilles de sites.

Module de "Mise à disposition de personnel" : Une fonctionnalité innovante qui pourrait faire le lien avec l'autre mission de l'entreprise : suggérer des profils d'experts (ingénieurs sécurité, auditeurs) disponibles dans la base de données de recrutement en fonction de la localisation et du type de risque d'un site.

