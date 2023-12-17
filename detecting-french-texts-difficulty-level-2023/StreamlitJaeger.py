import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import numpy as np
import random
from PIL import Image
import io
import base64

# Charger et encoder le logo
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string


# Charger et encoder le logo et l'image d'arrière-plan
logo = load_image("/Users/hugopierazzi/Downloads/DALL·E 2023-12-06 00.05.49 - A modern, professional logo for a language learning application named 'Jaeger'. The logo should symbolize language proficiency, education, and advance.png")



# CSS personnalisé pour positionner et redimensionner le logo
logo_css = f"""
<style>
.logo-img {{
    position: fixed;
    right: 30px;
    top: 70px;
    height: 50px;  /* Taille du logo */
}}
</style>
"""

# Créer l'interface utilisateur principale avec un style personnalisé
st.markdown(logo_css, unsafe_allow_html=True)
st.markdown(
    f'<img src="data:image/png;base64,{logo}" class="img-fluid logo-img" alt="logo">',
    unsafe_allow_html=True
)


def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Convertissez votre image d'arrière-plan
background_image = get_img_as_base64("/Users/hugopierazzi/Downloads/streamlitbackground.png") # Mettez à jour le chemin d'accès

# Définissez le CSS pour l'arrière-plan
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{background_image}");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
}}
</style>
"""

# Injectez le CSS dans votre application
st.markdown(page_bg_img, unsafe_allow_html=True)

def go_to_forme_toi_en_ligne():
    st.session_state['current_page'] = 'Forme toi en ligne'

def get_audio_exercises(level):
    audio_links = {
        'A1': ['https://apprendre.tv5monde.com/fr/exercices/a1-debutant/bonjour', 'https://apprendre.tv5monde.com/fr/exercices/a1-debutant/noel'],
        'A2': ['https://apprendre.tv5monde.com/fr/exercices/a2-elementaire/comment-traiter-le-conflit-israelo-palestinien', 'https://apprendre.tv5monde.com/fr/exercices/a2-elementaire/haut-potentiel-intellectuel-revoir-les-prejuges'],
        'B1': ['https://apprendre.tv5monde.com/fr/exercices/b1-intermediaire/france-des-maisons-en-palettes-recyclees', 'https://apprendre.tv5monde.com/fr/exercices/b1-intermediaire/entre-helsinki-et-moscou-des-relations-glaciales'],
        'B2': ['https://apprendre.tv5monde.com/fr/exercices/b2-avance/les-objectifs-de-la-cedeao-sont-ils-atteints', 'https://apprendre.tv5monde.com/fr/exercices/b2-avance/marisol-figure-enigmatique-du-pop-art'],
        'C1': ['https://www.lepointdufle.net/p/comprehensionaudio.htm#C1C2'],
        'C2': ['https://www.lepointdufle.net/p/comprehensionaudio.htm#C1C2'],
        # Ajoutez des liens pour les autres niveaux (B1, B2, C1, C2)
    }
    return audio_links.get(level, ["Aucun lien audio trouvé pour ce niveau."])



# Charger le tokenizer
tokenizer = AutoTokenizer.from_pretrained('camembert-base')

def load_model():
    model_path = '/Users/hugopierazzi/Streamlit1.py/model'
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    return model

def predict(text):
    model = load_model()
    encoding = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=256)
    encoding = {k: v.to(model.device) for k, v in encoding.items()}

    with torch.no_grad():
        outputs = model(**encoding)

    logits = outputs.logits
    softmax = torch.nn.Softmax(dim=-1)
    probs = softmax(logits.squeeze().cpu()).numpy()
    predicted_class = np.argmax(probs, axis=-1)
    difficulty_mapping = {0: 'A1', 1: 'A2', 2: 'B1', 3: 'B2', 4: 'C1', 5: 'C2'}
    return difficulty_mapping[predicted_class.item()]

def get_recommended_texts(level):
    example_links = {
        'A1': [
            'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/A1/A1_Junior/2018_uploads/delf-dalf-a1-sj-candidat-coll-sujet-demo.pdf',
            'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/A1/A1_Junior/2022_uploads/sujetdemodelfjsexemple2candidat.pdf',
            'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/A1/A1_TP/2018_uploads/delf-dalf-a1-tp-candidat-coll-sujet-demo.pdf',
            'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/A1/A1_TP/2022_uploads/delfa1toutpubliccandidatexemple2.pdf'
        ],
        'A2': ['https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/A2/A2_Prim/2018_uploads/DELF__Prim_A2_Livret_candidat.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/A2/A2_Junior/2022_uploads/delf-sj-a2-coll-candidat.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/A2/A2_Junior/2018_uploads/delf-dalf-a2-sj-candidat-coll-sujet-demo.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/A2/A2_TP/A2_TP_nouv.format_2019/sujet_demo_2019_tp_a2_candidat_2.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/A2/A2_TP/a2_ex1_tp_candidat.pdf'],  # Remplissez ces listes pour les autres niveaux
        'B1': ['https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/B1/B1_Junior/2022_uploads/delf-sj-b1-exemple1-coll-candidat.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/B1/B1_Junior/2018_uploads/delf-dalf-b1-sj-candidat-coll-sujet-demo.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/B1/B1_TP/B1_TP_nouv.format_2019/Sujet_demo_2019_TP_B1_candidat.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/B1/B1_TP/2018_uploads/delf-dalf-b1-tp-candidat-coll-sujet-demo.pdf'],
        'B2': ['https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/B2/B2_Junior/2022_uploads/delf-sj-b2-exemple1-coll-candidat.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/B2/B2_Junior/2018_uploads/delf-dalf-b2-sj-candidat-coll-sujet-demo.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/B2/B2_TP/B2_TP_nouv.format_2019/Sujet_demo_2019_TP_B2_candidat.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/B2/B2_TP/b2_example1_tp_candidat.pdf'],
        'C1': ['https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/C1/2021/dalf-c1_sujet-demo-candidat-coll.pdf'],
        'C2': ['https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/C2/2018_uploads/C2_LSH/c2-nouveau_example1_LSH_candidat_PO.pdf',
        'https://delfdalf.ch/fileadmin/user_upload/Unterlagen/Exemples_examens/C2/2018_uploads/C2_SC/c2-nouveau_example2_SC_candidat_PO.pdf']
        # ...
    }
    return example_links.get(level, ["Aucun lien trouvé pour ce niveau."])



def analyze_text(text):
    # Diviser le texte en mots ou phrases
    words = text.split()
    analyzed_words = []

    for word in words:
        # Prédire le niveau de difficulté de chaque mot ou petite phrase
        predicted_level, _ = predict(word)  # Utiliser la fonction de prédiction existante
        analyzed_words.append((word, predicted_level))

    return analyzed_words


def generate_quiz_questions(level, num_questions=8):
    # Exemple de questions fictives par niveau
    questions_dict = {
        'A1': [("How do you say 'Hello' in French ?", ["Bonjour", "Au revoir", "Merci"], "Bonjour"),
("What is the French word for 'apple' ?", ["Pomme", "Banane", "Orange"], "Pomme"),
("How do you say 'yes' in French ?", ["Non", "Oui", "Peut-être"], "Oui"),
("What does 'merci' mean in English ?", ["Hello", "Goodbye", "Thank you"], "Thank you"),
("What is the French word for 'dog' ?", ["Chat", "Chien", "Souris"], "Chien"),
("How do you say 'please' in French ?", ["S'il vous plaît", "Merci", "Excusez-moi"], "S'il vous plaît"),
("What is the translation of 'car' in French ?", ["Vélo", "Avion", "Voiture"], "Voiture"),
("How do you say 'I am tired' in French ?", ["Je suis fatigué", "Je suis content", "J'ai soif"], "Je suis fatigué"),
("What does 'au revoir' mean in English ?", ["Hello", "Goodbye", "Thank you"], "Goodbye"),
("What is the French word for 'table' ?", ["Chaise", "Lit", "Table"], "Table"),
("How do you say 'water' in French ?", ["Feu", "Eau", "Air"], "Eau"),
("What is the translation of 'bread' in French ?", ["Pain", "Pomme", "Lait"], "Pain"),
("How do you say 'I am hungry' in French ?", ["Je suis fatigué", "Je suis content", "J'ai faim"], "J'ai faim"),
("What is the French word for 'book' ?", ["Livre", "Table", "Chaise"], "Livre"),
("How do you say 'no' in French ?", ["Oui", "Non", "Peut-être"], "Non"),
("What is the translation of 'cat' in French ?", ["Chien", "Chat", "Maison"], "Chat"),
("How do you say 'Thank you' in French ?", ["Merci", "Eau", "Nourriture"], "Merci"),
("What is the French word for 'house' ?", ["Chien", "Maison", "Ami"], "Maison"),
("How do you say 'I am happy' in French ?", ["Je suis fatigué", "Je suis content", "J'ai faim"], "Je suis content"),
("What is the translation of 'water' in French ?", ["Ami", "Eau", "Mer"], "Eau")],
        'A2': [("What is the French word for 'bicycle' ?", ["Voiture", "Vélo", "Avion"], "Vélo"),
("How do you say 'good morning' in French ?", ["Bonsoir", "Bonjour", "Bon appétit"], "Bonjour"),
("What is the translation of 'computer' in French ?", ["Ordinateur", "Téléphone", "Télévision"], "Ordinateur"),
("How do you say 'I like it' in French ?", ["Je n'aime pas ça", "J'adore ça", "Ça va"], "J'adore ça"),
("What is the French word for 'movie' ?", ["Musique", "Livre", "Film"], "Film"),
("How do you say 'I don't understand' in French ?", ["Je ne parle pas français", "Je ne comprends pas", "Je suis fatigué"], "Je ne comprends pas"),
("What is the translation of 'friend' in French ?", ["Famille", "Ami", "Animal"], "Ami"),
("How do you say 'to eat' in French ?", ["Manger", "Boire", "Cuisiner"], "Manger"),
("What is the French word for 'city' ?", ["Village", "Ville", "Campagne"], "Ville"),
("How do you say 'tomorrow' in French ?", ["Hier", "Aujourd'hui", "Demain"], "Demain"),
("What is the translation of 'shirt' in French ?", ["Chapeau", "Pantalon", "Chemise"], "Chemise"),
("How do you say 'to drink' in French ?", ["Manger", "Boire", "Cuisiner"], "Boire"),
("What is the French word for 'beach' ?", ["Forêt", "Plage", "Montagne"], "Plage"),
("How do you say 'to read' in French ?", ["Écrire", "Lire", "Parler"], "Lire"),
("What is the translation of 'breakfast' in French ?", ["Dîner", "Petit déjeuner", "Déjeuner"], "Petit déjeuner"),
("How do you say 'to travel' in French ?", ["Voyager", "Travailler", "Étudier"], "Voyager"),
("What is the French word for 'watch' ?", ["Horloge", "Montre", "Télévision"], "Montre"),
("How do you say 'I am going' in French ?", ["Je suis venu", "Je vais", "Je suis allé"], "Je vais"),
("What is the translation of 'shoes' in French ?", ["Chapeau", "Manteau", "Chaussures"], "Chaussures"),
("How do you say 'to swim' in French ?", ["Nager", "Courir", "Marcher"], "Nager")],
'B1': [("What is the French word for 'environment' ?", ["Environnement", "Éducation", "Évolution"], "Environnement"),
("How do you say 'to understand' in French ?", ["Comprendre", "Apprendre", "Entendre"], "Comprendre"),
("What is the translation of 'history' in French ?", ["Histoire", "Géographie", "Mathématiques"], "Histoire"),
("How do you say 'to succeed' in French ?", ["Échouer", "Réussir", "Perdre"], "Réussir"),
("What is the French word for 'culture' ?", ["Nature", "Société", "Culture"], "Culture"),
("How do you say 'to celebrate' in French ?", ["Célébrer", "Fêter", "Voyager"], "Célébrer"),
("What is the translation of 'freedom' in French ?", ["Paix", "Liberté", "Égalité"], "Liberté"),
("How do you say 'to dream' in French ?", ["Rêver", "Penser", "Dormir"], "Rêver"),
("What is the French word for 'politics' ?", ["Politique", "Économie", "Science"], "Politique"),
("How do you say 'to discover' in French ?", ["Décider", "Découvrir", "Devenir"], "Découvrir"),
("What is the translation of 'art' in French ?", ["Sport", "Musique", "Art"], "Art"),
("How do you say 'to express' in French ?", ["Expliquer", "Exprimer", "Écouter"], "Exprimer"),
("What is the French word for 'economy' ?", ["Économie", "Société", "Environnement"], "Économie"),
("How do you say 'to travel' in French ?", ["Travailler", "Voyager", "Rêver"], "Voyager"),
("What is the translation of 'society' in French ?", ["Culture", "Société", "Nature"], "Société"),
("How do you say 'to communicate' in French ?", ["Communiquer", "Parler", "Écouter"], "Communiquer"),
("What is the French word for 'problem' ?", ["Solution", "Question", "Problème"], "Problème"),
("How do you say 'to participate' in French ?", ["Participer", "Gagner", "Perdre"], "Participer"),
("What is the translation of 'education' in French ?", ["Éducation", "Formation", "Connaissance"], "Éducation"),
("How do you say 'to collaborate' in French ?", ["Coopérer", "Travailler", "Étudier"], "Coopérer")],
'B2': [("What is the French word for 'technology' ?", ["Technique", "Technologie", "Télévision"], "Technologie"),
("How do you say 'to analyze' in French ?", ["Analyser", "Étudier", "Comparer"], "Analyser"),
("What is the translation of 'environmental' in French ?", ["Environnemental", "Éducatif", "Économique"], "Environnemental"),
("How do you say 'to innovate' in French ?", ["Innover", "Révolutionner", "Améliorer"], "Innover"),
("What is the French word for 'globalization' ?", ["Globalisation", "Mondialisation", "Internationalisation"], "Mondialisation"),
("How do you say 'to adapt' in French ?", ["Adapter", "Modifier", "Changer"], "Adapter"),
("What is the translation of 'communication' in French ?", ["Communauté", "Communication", "Conversation"], "Communication"),
("How do you say 'to negotiate' in French ?", ["Négocier", "Discuter", "Résoudre"], "Négocier"),
("What is the French word for 'development' ?", ["Évolution", "Développement", "Progression"], "Développement"),
("How do you say 'to collaborate' in French ?", ["Collaborer", "Coopérer", "Travailler ensemble"], "Collaborer"),
("What is the translation of 'innovation' in French ?", ["Créativité", "Invention", "Innovation"], "Innovation"),
("How do you say 'to research' in French ?", ["Étudier", "Rechercher", "Explorer"], "Rechercher"),
("What is the French word for 'education' ?", ["Éducation", "Formation", "Apprentissage"], "Éducation"),
("How do you say 'to analyze data' in French ?", ["Analyser des données", "Interpréter des données", "Étudier des données"], "Analyser des données"),
("What is the translation of 'strategy' in French ?", ["Tactique", "Stratégie", "Planification"], "Stratégie"),
("How do you say 'to evaluate' in French ?", ["Évaluer", "Analyser", "Examiner"], "Évaluer"),
("What is the French word for 'industry' ?", ["Industrie", "Entreprise", "Commerce"], "Industrie"),
("How do you say 'to innovate solutions' in French ?", ["Trouver des solutions innovantes", "Innover des solutions", "Créer des solutions"], "Innover des solutions"),
("What is the translation of 'management' in French ?", ["Gestion", "Administration", "Direction"], "Gestion"),
("How do you say 'to implement a plan' in French ?", ["Mettre en place un plan", "Exécuter un plan", "Planifier un plan"], "Mettre en place un plan")],
'C1': [("What is the French word for 'philosophy' ?", ["Philosophique", "Philosophe", "Philosophie"], "Philosophie"),
("How do you say 'to analyze critically' in French ?", ["Analyser de manière critique", "Critiquer", "Étudier profondément"], "Analyser de manière critique"),
("What is the translation of 'literature' in French ?", ["Littérature", "Livre", "Écriture"], "Littérature"),
("How do you say 'to debate' in French ?", ["Débattre", "Discuter", "Déclarer"], "Débattre"),
("What is the French word for 'research' ?", ["Recherché", "Recherche", "Chercher"], "Recherche"),
("How do you say 'to analyze in depth' in French ?", ["Analyser en profondeur", "Étudier en détail", "Scruter"], "Analyser en profondeur"),
("What is the translation of 'knowledge' in French ?", ["Savoir", "Connaissance", "Intelligence"], "Connaissance"),
("How do you say 'to express one's ideas' in French ?", ["Exprimer ses idées", "Déclarer ses idées", "Dire ses idées"], "Exprimer ses idées"),
("What is the French word for 'culture' ?", ["Nature", "Civilisation", "Culture"], "Culture"),
("How do you say 'to formulate hypotheses' in French ?", ["Formuler des hypothèses", "Élaborer des hypothèses", "Créer des hypothèses"], "Formuler des hypothèses"),
("What is the translation of 'philosopher' in French ?", ["Philosophe", "Philosophique", "Philosophie"], "Philosophe"),
("How do you say 'to discuss ideas' in French ?", ["Discuter des idées", "Parler des idées", "Échanger des idées"], "Discuter des idées"),
("What is the French word for 'analysis' ?", ["Analyse", "Étude", "Examen"], "Analyse"),
("How do you say 'to interpret data' in French ?", ["Interpréter des données", "Analyser des données", "Comprendre des données"], "Interpréter des données"),
("What is the translation of 'debate' in French ?", ["Débat", "Discussion", "Conversation"], "Débat"),
("How do you say 'to analyze critically' in French ?", ["Analyser de manière critique", "Critiquer", "Scruter"], "Analyser de manière critique"),
("What is the French word for 'reflection' ?", ["Pensée", "Réflexion", "Idée"], "Réflexion"),
("How do you say 'to examine closely' in French ?", ["Examiner de près", "Étudier de près", "Scruter"], "Examiner de près"),
("What is the translation of 'literary analysis' in French ?", ["Analyse littéraire", "Étude littéraire", "Critique littéraire"], "Analyse littéraire"),
("How do you say 'to articulate ideas' in French ?", ["Articuler des idées", "Formuler des idées", "Exprimer des idées"], "Articuler des idées")],
'C2': [("What is the French word for 'sophisticated' ?", ["Sophistiqué", "Élégant", "Raffiné"], "Sophistiqué"),
("How do you say 'to synthesize information' in French ?", ["Synthétiser des informations", "Résumer des informations", "Condenser des informations"], "Synthétiser des informations"),
("What is the translation of 'researcher' in French ?", ["Chercheur", "Investigateur", "Scientifique"], "Chercheur"),
("How do you say 'to analyze in depth' in French ?", ["Analyser en profondeur", "Étudier en détail", "Examiner minutieusement"], "Analyser en profondeur"),
("What is the French word for 'intellectual' ?", ["Intellectuel", "Mental", "Pensif"], "Intellectuel"),
("How do you say 'to examine thoroughly' in French ?", ["Examiner minutieusement", "Étudier en profondeur", "Scruter attentivement"], "Examiner minutieusement"),
("What is the translation of 'knowledge' in French ?", ["Savoir", "Connaissance", "Intelligence"], "Connaissance"),
("How do you say 'to express complex ideas' in French ?", ["Exprimer des idées complexes", "Communiquer des idées compliquées", "Articuler des concepts élaborés"], "Exprimer des idées complexes"),
("What is the French word for 'proficiency' ?", ["Compétence", "Maîtrise", "Expertise"], "Maîtrise"),
("How do you say 'to formulate hypotheses' in French ?", ["Formuler des hypothèses", "Élaborer des hypothèses", "Créer des hypothèses"], "Formuler des hypothèses"),
("What is the translation of 'philosopher' in French ?", ["Philosophe", "Philosophique", "Philosophie"], "Philosophe"),
("How do you say 'to engage in critical discourse' in French ?", ["S'engager dans un discours critique", "Participer à une discussion critique", "Débattre de manière critique"], "S'engager dans un discours critique"),
("What is the French word for 'reflection' ?", ["Pensée", "Réflexion", "Idée"], "Réflexion"),
("How do you say 'to analyze complex data' in French ?", ["Analyser des données complexes", "Étudier des données compliquées", "Examiner des données sophistiquées"], "Analyser des données complexes"),
("What is the translation of 'debate' in French ?", ["Débat", "Discussion", "Conversation"], "Débat"),
("How do you say 'to critically evaluate' in French ?", ["Évaluer de manière critique", "Analyser de manière critique", "Étudier de manière critique"], "Évaluer de manière critique"),
("What is the French word for 'scholarship' ?", ["Bourse d'études", "Savoir", "Érudition"], "Bourse d'études"),
("How do you say 'to examine rigorously' in French ?", ["Examiner rigoureusement", "Analyser rigoureusement", "Étudier de manière stricte"], "Examiner rigoureusement"),
("What is the translation of 'academic' in French ?", ["Universitaire", "Scolaire", "Éducatif"], "Universitaire"),
("How do you say 'to articulate complex concepts' in French ?", ["Articuler des concepts complexes", "Exprimer des idées sophistiquées", "Formuler des idées élaborées"], "Articuler des concepts complexes")]
    }
    questions_for_level = questions_dict.get(level, [])
    if len(questions_for_level) > num_questions:
        return random.sample(questions_for_level, num_questions)
    else:
        return questions_for_level



# Créer l'interface utilisateur principale avec un style personnalisé
st.markdown("""
    <style>
        .big-font {
            font-size:30px !important;
            font-weight: bold;
        }
        .tab-font {
            font-size:20px !important;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">Jaeger - Votre Assistant d\'Apprentissage de Langue</p>', unsafe_allow_html=True)

# Convertir l'image de fond de la barre latérale en base64
sidebar_background = get_img_as_base64("/Users/hugopierazzi/Downloads/Sidebarstreamlit.png")

# CSS pour appliquer l'image de fond à la barre latérale
# sidebar_css = f"""
# <style>
# section[data-testid="stSidebar"] {{
    # background-image: url("data:image/png;base64,{sidebar_background}");
    # background-size: cover;
    # background-position: center; 
# # }}
# </style>
# """

# Appliquer le CSS à l'application
# st.markdown(sidebar_css, unsafe_allow_html=True)




# Initialiser la variable de session pour la première page
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'Accueil'

# Barre latérale avec des boutons
sidebar = st.sidebar
sidebar.markdown("## Menu")

# Bouton pour la page d'accueil
if sidebar.button("Accueil"):
    st.session_state['current_page'] = 'Accueil'

# Bouton pour la page "Forme toi en ligne"
if sidebar.button("Forme toi en ligne"):
    st.session_state['current_page'] = 'Forme toi en ligne'

if st.session_state['current_page'] == 'Accueil':
    # Appliquer le CSS pour le fond d'écran uniquement sur la page d'accueil
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url("data:image/png;base64,{background_image}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# Utiliser des onglets pour organiser les fonctionnalités principales
    tab1, tab2, tab3 = st.tabs(["Évaluation de Difficulté", "Recommandation de Textes", "Analyse Détaillée de Textes"])
    with tab1:
        st.header("Évaluation de Difficulté de Texte")
        user_input = st.text_area("Entrez une phrase en français :", '')
        if st.button('Évaluer'):
            if user_input:
                predicted_level = predict(user_input)  # Remplacez par votre fonction de prédiction réelle
                st.write(f"Niveau prédit : {predicted_level}")
            else:
                st.write("Veuillez entrer du texte.")
        st.markdown("Détermine ton niveau puis viens te former en Ligne avec nous !")
        if st.button("Forme toi en ligne", key="btn_forme_toi_1"):
            go_to_forme_toi_en_ligne()


    with tab2:
            st.header("Recommandation de Textes")
            user_input = st.text_area("Entrez une phrase pour déterminer votre niveau :", '', key="txt_reco")
            if st.button('Obtenir des Recommandations', key="btn_reco"):
                if user_input:
                    user_level = predict(user_input)
                    st.write(f"Votre niveau prédit est : {user_level}")

                    recommended_links = get_recommended_texts(user_level)
                    if recommended_links:
                        st.write("Liens recommandés pour votre niveau :")
                        for link in recommended_links:
                            st.markdown(f"[Textes recommandés]({link})", unsafe_allow_html=True)
                    else:
                        st.write("Aucun lien trouvé pour ce niveau.")
            st.markdown("Détermine ton niveau puis viens te former en Ligne avec nous !")
            if st.button("Forme toi en ligne", key="btn_forme_toi_2"):
                go_to_forme_toi_en_ligne()

    with tab3:
        st.header("Analyse Détaillée de Textes")
        user_input = st.text_area("Entrez un texte en français pour l'analyse :", '', key="txt_analysis")
        if st.button('Analyser le Texte', key="btn_analysis"):
            if user_input:
                analyzed_words = analyze_text(user_input)
                for word, level in analyzed_words:
                    st.markdown(f"**{word}**: Niveau {level}")
            else:
                st.write("Veuillez entrer du texte pour l'analyse.")
        st.markdown("Détermine ton niveau puis viens te former en Ligne avec nous !")
        if st.button("Forme toi en ligne", key="btn_forme_toi_3"):
            go_to_forme_toi_en_ligne()




elif st.session_state['current_page'] == 'Forme toi en ligne':
    st.header("Forme toi en ligne")
    tab_voc, tab_audio = st.tabs(["Apprend Ton Voc", "Exercice Audio"])

    with tab_voc:
        level = st.selectbox("Choisissez votre niveau:", ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'])
        quiz_questions = generate_quiz_questions(level)
        user_responses = {}

        for i, (question, options, answer) in enumerate(quiz_questions, 1):
            user_responses[question] = st.radio(f"Question {i}: {question}", options, key=f"question_{i}")

        if st.button('Vérifier les réponses'):
            correct_answers = 0
            for question, (_, _, answer) in zip(user_responses, quiz_questions):
                if user_responses[question] == answer:
                    correct_answers += 1
                    st.success(f"Bonne réponse pour: '{question}'!")
                else:
                    st.error(f"Mauvaise réponse pour: '{question}'. La bonne réponse est: '{answer}'")

            st.write(f"Vous avez {correct_answers} sur {len(quiz_questions)} réponses correctes.")

    with tab_audio:
        st.header("Exercices Audio")
        level_audio = st.selectbox("Choisissez votre niveau pour les exercices audio:", ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'])
        audio_links = get_audio_exercises(level_audio)
        st.write("Liens pour les exercices audio :")
        for link in audio_links:
            st.markdown(f"[Exercice Audio]({link})", unsafe_allow_html=True)


        # ... Vos imports et fonctions existants ...



