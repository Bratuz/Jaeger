# Jaeger


<h2 align="center">Introduction</h2>


   
Présentation du Problème
Le projet "LingoRank" vise à résoudre un défi majeur dans l'apprentissage des langues : trouver des textes français adaptés aux niveaux variés des apprenants anglophones. Cette difficulté à identifier des ressources adaptées à leur niveau de compétence (A1 à C2) peut freiner leur progression.

Brève Description de la Solution
Nous avons développé un modèle d'intelligence artificielle utilisant Camembert, une version française de BERT, pour classer les textes français selon leur difficulté. Notre modèle, formé sur un ensemble de données annotées et évalué sur des textes non étiquetés, prédit avec précision le niveau de difficulté d'un texte. Il offre ainsi une solution personnalisée pour améliorer l'apprentissage du français chez les anglophones, en recommandant des textes appropriés à leur niveau de compétence linguistique.
<br/>
<br/>
<br/>
<br/>
<br/>

Nous allons donc vous présenter notre application et notre model Jaeger !

<br/>

<br/>

<div align="center">
    <img src="https://github.com/Bratuz/Jaeger/assets/119636152/5c973b52-3620-4b95-8d29-86657e92d2da" width="200">
</div>

<br/>
<br/>

<h2 align="center">Our Results</h2>

<br/>

### With Basic Model

*Voici tout d'abord nos résultats avec les modèles de base que nous avons fait dans un premier temps !*

<br/>

|                      | Logistic Regression CV | Logistic Regression | kNN    | Decision Tree | Random Forest | SVC    |
|----------------------|------------------------|---------------------|--------|---------------|---------------|--------|
| Precision            | 0.4676454066489516     | 0.4434355323004604  | 0.39079983953956327 | 0.28655157769033857 | 0.39660960624031383 | 0.4508158506257017 |
| Recall               | 0.471875               | 0.4510416666666667  | 0.31875 | 0.29375       | 0.39166666666666666 | 0.4552083333333333 |
| F1-score             | 0.46733144             | 0.44297432142115906 | 0.29480639440529377 | 0.2865755980383005  | 0.37769086230428955 | 0.4509219661114091 |
| Accuracy             | 0.471875               | 0.4510416666666667  | 0.31875 | 0.29375       | 0.39166666666666666 | 0.4552083333333333 |


<br/>

### With Text Embeddings Models

<br/>

### Different hyperparameters

<br/>

| Max Length | Epoch | Learning Rate | Batch Size | Test Accuracy         | Text Embeddings | New Method                   |
|------------|-------|---------------|------------|-----------------------|-----------------|------------------------------|
| 256        | 3     | 2.00E-05      | x          | 0.54583               | Bert            | x                            |
| 128        | 6     | 5.00E-05      | x          | 0.54896               | Camembert       | x                            |
| 256        | 6     | 5.00E-05      | 16         | 0.5375                | Bert            | x                            |
| 128        | 2     | x             | x          | 0.567708              | Camembert       | x                            |
| 128        | 2     | 5.00E-05      | x          | 0.55625               | Camembert       | x                            |
| 128        | 2     | 2.00E-05      | x          | 0.5625                | Camembert       | x                            |
| 256        | 6     | x             | x          | 0.577                 | Camembert       | x                            |
| 256        | 11    | x             | x          | 0.583                 | Camembert       | Ajout de la double traduction|


<br/>

### Our Best Model

<br/>


Notre modèle le plus efficace utilise Camembert, un outil avancé pour le traitement du langage naturel en français. L'augmentation significative de notre base de données grâce à une technique de double traduction a également joué un rôle crucial dans l'amélioration de nos prédictions. Cette approche nous a permis d'obtenir des résultats plus précis dans la classification du niveau de difficulté des textes français pour les apprenants anglophones.


<br/>

(Lien vers notre model à mettre) !!!!!

<br/>

### Progress chart based on the methods added


<br/>

A FAIRE ENCORE

<br/>

### Confusion Matrix

<br/>
<br/>

<div align="center">
  <img width="300" alt="Sans titre" src="https://github.com/Bratuz/Jaeger/assets/119636152/f9d358b1-374e-40d5-a2ba-1e93be30f85a">
</div>

<br/>

Code pour [Confusion Matrix](https://github.com/Bratuz/Jaeger/blob/main/detecting-french-texts-difficulty-level-2023/Confusion_Matrix.ipynb)


<br/>


<h2 align="center">Analyse</h2>

<br/>

Expliquer un peu pourquoi ducoup pourquoi ca été notre meilleur modele, quelles ont été les fonctions méthodes qui ont permis ce score blablabl

<br/>

<h2 align="center">Streamlit</h2>

<br/>

Voici le code : 

Lien pour code : [Streamlit](https://github.com/Bratuz/Jaeger/blob/main/detecting-french-texts-difficulty-level-2023/StreamlitJaeger.py)

<br/>

<h2 align="center">Youtube Video</h2>

<br/>

Lien vidéo







