import pandas as pd

# Importez les données à partir d'un fichier CSV
df_merged = pd.read_csv('bibliography.csv')  

# Créez une fonction pour générer les références BibTeX
def generate_bibtex(row):
    authors = row['Author'][2:-2].split("', '")  # Pour extraire la liste des auteurs
    first_author = authors[0].split()[0] 
    year = str(row['Year'])[2:]  # Extrait les deux derniers chiffres de l'année

    # Créez la référence BibTeX
    bibtex = f"@article{{{first_author}{year},\n"
    bibtex += f"  title = {{{row['Title']}}},\n"
    bibtex += f"  author = {{{', '.join(authors)}}},\n"
    bibtex += f"  year = {row['Year']},\n"
    bibtex += f"  journal = {{{row['Journal']}}},\n"
    bibtex += f"  volume = {row['Volume']},\n"
    bibtex += f"  number = {row['Issue']},\n"
    bibtex += f"  url = {{{row['Link']}}}\n"
    bibtex += "}"

    return bibtex

# Appliquez la fonction pour générer les références BibTeX et stockez-les dans une nouvelle colonne
df_merged['BibTeX'] = df_merged.apply(generate_bibtex, axis=1)

# Enregistrez les références BibTeX dans un fichier spécifié
with open('references.bib', 'w') as file:
    for bibtex in df_merged['BibTeX']:
        file.write(bibtex + '\n')
