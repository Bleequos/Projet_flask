from flask import render_template, url_for, request
from . import app, models
@app.route('/')
@app.route("/accueil")
def accueil():
    liste_produits = models.vue_cours_ressources.query.all()
    return render_template('accueil.html', title='Tous les produits', liste_produits=liste_produits)

@app.route('/produits')
def catalogue_de_produits():  #Le nom de la fonction est libre
    return '<h2>Nos produits</h2>'

@app.route('/tous_produits')
def tous_produits():
    liste_produits = models.vue_cours_ressources.query.all()
    return render_template('tous_produits.html',title='Tous les produits',liste_produits=liste_produits)

@app.route('/voir_video')
def voir_video():
    id_cours = request.args.get('id_cours')
    liste_produits = models.vue_cours_ressources.query.filter_by(cours_id=id_cours)
    return render_template('voir_video.html',title='Voir video',liste_produits=liste_produits)

