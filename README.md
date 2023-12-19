# Jaeger


<h2 align="center">Introduction</h2>

 
   
Presentation of the problem, our project aims to solve a major challenge in language learning: finding French texts adapted to the varying levels of English-speaking learners. This difficulty in identifying resources adapted to their level of proficiency (A1 to C2) can hinder their progress.

Brief description of our solution: We have developed a text embedding model, Camembert, a French version of BERT, to classify French texts according to their difficulty. Our model, trained on an annotated dataset and evaluated on unlabelled texts, accurately predicts the level of difficulty of a text. It thus offers a personalised solution for improving the learning of French by English speakers, by recommending texts appropriate to their level of linguistic competence.
<br/>
<br/>
<br/>
<br/>
<br/>

<table>
   <tr>
      <td>
         We will introduce and delineate our model, detailing the processes and evaluations we conducted to refine it. Ultimately, we will showcase our Streamlit application that incorporates the model.
      </td>
      <td>
         <img src="https://github.com/Bratuz/Jaeger/assets/119636152/5c973b52-3620-4b95-8d29-86657e92d2da" width="200">
      </td>
   </tr>
</table>


<br/>
<br/>

<h2 align="center">Our Results</h2>

<br/>

### With Basic Model

*First of all, here are our results with the basic models we made!*

<br/>

|                      | [Logistic Regression CV](https://github.com/Bratuz/Jaeger/blob/main/detecting-french-texts-difficulty-level-2023/Test/LogisticRegressionCV.ipynb) | [Logistic Regression](https://github.com/Bratuz/Jaeger/blob/main/detecting-french-texts-difficulty-level-2023/Test/LogisticRegression.ipynb) | [kNN](https://github.com/Bratuz/Jaeger/blob/main/detecting-french-texts-difficulty-level-2023/Test/KNN.ipynb) | [Decision Tree](https://github.com/Bratuz/Jaeger/blob/main/detecting-french-texts-difficulty-level-2023/Test/Decision_tree.ipynb) | [Random Forest](https://github.com/Bratuz/Jaeger/blob/main/detecting-french-texts-difficulty-level-2023/Test/Random_forest.ipynb) | [SVC](https://github.com/Bratuz/Jaeger/blob/main/detecting-french-texts-difficulty-level-2023/Test/SVC.ipynb) |
|----------------------|------------------------|---------------------|--------|---------------|---------------|--------|
| Precision            | 0.467645               | 0.443436            | 0.390799 | 0.286552     | 0.396609     | 0.450816 |
| Recall               | 0.471875               | 0.451042            | 0.31875  | 0.29375      | 0.391667     | 0.455208 |
| F1-score             | 0.467331               | 0.442974            | 0.294806 | 0.286576     | 0.377691     | 0.450922 |
| Accuracy             | 0.471875               | 0.451042            | 0.31875  | 0.29375      | 0.391667     | 0.455208 |


<br/>

### With Text Embeddings Models

<br/>



### Our Best Model

<br/>


Our best-performing model is based on Camembert, a cutting-edge technology for automatic natural language processing specifically designed for French. In addition, we have considerably enriched our dataset by applying a double translation technique, which has considerably improved the accuracy of our predictions. Thanks to this innovative strategy, we were able to classify the difficulty level of French texts more accurately, making it easier for English speakers to learn.


<br/>

(Lien vers notre model à mettre) !!!!!

<br/>



### Progress chart based on the methods added


<br/>

A FAIRE ENCORE

<br/>



<h2 align="center">Analyse</h2>

<br/>

Expliquer un peu pourquoi ducoup pourquoi ca été notre meilleur modele, quelles ont été les fonctions méthodes qui ont permis ce score blablabl

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

*Class 0 (Level A1): Out of 311 predictions for this class, 282 were correctly classified, while 29 were incorrectly classified as belonging to higher levels (mainly A2 and B1). This indicates strong performance for this basic level.*

*Class 1 (Level A2): Out of 327 predictions, 257 were correctly classified. However, 23 texts of level A2 were classified as A1, and 46 as B1, suggesting some confusion between these adjacent levels.*

*Class 2 (Level B1): Of 323 predictions, 267 were correctly classified. The model had difficulties with 30 texts of level B1 wrongly classified as A2 and 14 as A1. Moreover, there is some confusion with level B2 (10 cases).*

*Class 3 (Level B2): Out of 344 predictions, 293 were correct. There is notable confusion with level C1 (61 cases), which might indicate a linguistic or structural similarity between these two levels.*

*Class 4 (Level C1): This class saw 233 out of its 317 predictions correctly classified. The most significant confusion is with level B2 (61 cases), reciprocating the confusion observed for class B2.*

*Class 5 (Level C2): Out of 298 predictions, 216 were correctly classified. However, there is notable confusion with levels B2 (32 cases) and C1 (39 cases).*

<br/>

**General Observations:**


The model is quite effective in distinguishing the basic levels (A1 and A2) from more advanced levels.
There is notable confusion between adjacent levels, particularly between B1 and B2, and between B2 and C1. This might be due to overlaps in linguistic complexity or similar characteristics at these language levels.
The higher levels (B2, C1, C2) show more significant confusion among themselves, which is understandable given the gradual nature of linguistic skill progression.

<br/>

### Different hyperparameters

*Here are the hyperparameter adjustments and additional methods we have incorporated into our model*

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
| 256        | 11    | x             | x          | 0.583                 | Camembert       | Double translation added|


<br/>

**Observations**

A longer maximum length and a greater number of epochs seem beneficial, particularly with Camembert and additional methods such as double translation.
The choice of learning rate and batch size is less clear and merits further testing.
The use of Camembert, particularly with additional techniques, seems to be a winning strategy for improving model accuracy.

<br/>

<h2 align="center">Streamlit</h2>

<br/>

Voici le code : 

Lien pour code : [Streamlit](https://github.com/Bratuz/Jaeger/blob/main/detecting-french-texts-difficulty-level-2023/StreamlitJaeger.py)

<br/>

<h2 align="center">Youtube Video</h2>

<br/>

Lien vidéo







