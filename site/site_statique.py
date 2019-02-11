# coding=utf-8

# J'importe les packages dont j'ai besoin.
import markdown2
import argparse
import os

# Réalisation d'une interface en ligne de commande.
parser = argparse.ArgumentParser(usage="")
parser.add_argument("-i", "--input-directory", action="store", type=str, required=True, help="Répertoire d'entrée contenant les fichiers markdown.")
parser.add_argument("-o", "--output-directory", action="store", type=str, required=True, help="Répertoire de sortie, contenant les fichiers markdown en html.")
# help_def = parser.add_argument("-h", "--help", action="store", type=str, required=True, help="Aide")
args = parser.parse_args()

# Je nomme ma fonction qui convertie les fichiers.md en fichiers.html.
def md_to_html():
    # Je regarde l'interieur du dossier fichiers_md
    dossier_md = os.listdir(args.input_directory)
    # Je parcours l'ensemble des fichiers de dossier_md.
    for fichier in dossier_md:
        # J'ouvre et je lis le dossier_md.
        with open(args.input_directory + '/' + fichier, 'r+', encoding = 'utf-8') as fichiers_md:
                # Je convertie l'interierur des fichiers en .md en .html.
                HTML = markdown2.markdown(fichiers_md.read())
                # Je remplace l'extension des fichiers en .md par .html. 
                htmls = open(args.output_directory + '/' + fichier.replace(".md", ".html"), "w+", encoding="utf-8")
                # J'écris le tout.
                htmls.write(HTML)

# J'appelle ma fonction md_to_html.
md_to_html()