# 📒 Mon carnet de bord

**Nom :LOUKOU

**Prénom :YAO EMMANUEL

**Adresse de mon site :** https://nuelmaah.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse : Le code est stocké sur GitHub, puis déployé sur PythonAnywhere où il est exécuté pour afficher le site web. Une copie existe aussi sur mon ordinateur pendant le développement. 

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse : Mon voisin peut voir mon site car il est hébergé sur les serveurs de PythonAnywhere. Son navigateur accède au site via Internet et reçoit les pages web sans qu'il soit nécessaire d'installer quoi que ce soit sur son ordinateur.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

> _Ma réponse :_ NOM DE DOMAINE : www.google.com
               _ CHEMIN : /maps

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ Le message Not Found signifie que la page ou la ressource demandée n'existe pas à l'adresse indiquée. Ce message est envoyé par le serveur, puis affiché par le navigateur.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Si deux fonctions portent le même nom dans flask_app.py, la seconde écrase la première. Flask détecte ce conflit et affiche une erreur dans l'Error Log, car deux routes ne peuvent pas utiliser la même fonction de vue.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie du code (HTML, CSS, JavaScript, images, etc.), tandis que le navigateur interprète ce code et affiche le résultat sous forme de page web lisible par l'utilisateur.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ <h1> : crée un titre principal.
                    <p> : crée un paragraphe de texte.
                    <ul> : crée une liste non ordonnée (avec des puces).
                    <li> : représente un élément de la liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ L'image s'affiche parce qu'elle est stockée sur un autre serveur accessible sur Internet. Le navigateur télécharge directement l'image depuis son adresse (URL) et l'affiche dans la page, même si elle n'est pas hébergée sur mon serveur PythonAnywhere.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ 
   
   Séparer le code Python du HTML permet de mieux organiser le projet. 
   Le développeur peut travailler sur la logique de l'application en Python, tandis que le graphiste ou web designer peut modifier l'apparence et la mise en page en HTML sans toucher au code Python.
   
   Cela facilite le travail en équipe, la maintenance et les évolutions du site.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Les {{ prenom }} sont remplacés par le serveur Flask avant que la page ne soit envoyée au navigateur.
   > Le navigateur ne reçoit pas {{ prenom }}, mais directement la valeur correspondante (par exemple « Emmanuel »).

Je l'ai vérifié en affichant le code source de la page dans le navigateur : on voit la valeur remplacée, et non {{ prenom }}.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML sert à structurer le contenu de la page,
   >  tandis que le CSS sert à définir l'apparence de ce contenu (couleurs, tailles, polices, espacements, disposition, etc.).

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Pour afficher la page /presentation, le navigateur doit télécharger plusieurs fichiers :
Le fichier HTML de la page.
Le fichier CSS (si la page utilise une feuille de style externe).
Les éventuelles images affichées sur la page.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Ctrl + F5 force le navigateur à recharger complètement la page et à télécharger à nouveau les fichiers, ce qui permet de voir immédiatement les modifications du CSS.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie HyperText Transfer Protocol. Le navigateur envoie la requête HTTP au serveur, et le serveur renvoie la réponse HTTP au navigateur.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ 

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ 

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ 

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ 

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ 

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ 

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ 

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ 

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ 

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ 

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ 

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ 

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ 

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ 

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ 

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ 

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ 

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ 

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ 
