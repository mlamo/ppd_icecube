import glob
import healpy as hp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


sqrt = np.sqrt


def cos(angle):
    return np.cos(np.deg2rad(angle))

def sin(angle):
    return np.sin(np.deg2rad(angle))

def tan(angle):
    return np.tan(np.deg2rad(angle))

def arccos(angle):
    return np.rad2deg(np.arccos(angle))

def arcsin(angle):
    return np.rad2deg(np.arcsin(angle))

def arctan(angle):
    return np.rad2deg(np.arctan(angle))

def lire_donnees(dossier="inputs/icecube_10year_ps/events"):
    # accéder à la liste des fichiers présents dans le dossier
    liste_de_fichiers = sorted(glob.glob(dossier + "/*.csv"))
    dfs = []
    # pour chaque fichier, faire les actions suivantes
    for fichier in liste_de_fichiers:
        # 1/ ouvrir le fichier
        df = pd.read_csv(fichier, sep="\s+")
        # 2/ renommer correctement les colonnes
        colnames = list(df.columns)[1:]
        df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
        df.columns = colnames
        # 3/ stocker la liste d'événements
        dfs.append(df)
    # on rassemble toutes les listes en une seule
    dfs = pd.concat(dfs)
    # on réinitialise l'index donné à chaque événement
    dfs.reset_index(inplace=True)
    dfs.drop(dfs.columns[0], axis=1, inplace=True)
    return dfs

def liste_sources(groupe, fichier="inputs/sources.csv", ):
    df = pd.read_csv(fichier)
    df = df[["Name", "Ra", "Dec"]]
    df = df.rename(columns={"Name": "Nom", "Ra": "RA(source)", "Dec":"Dec(source)"})
    if groupe == "A":
        df = df.iloc[[5, 8, 9, 12, 39, 42, 63, 69, 94]]
    elif groupe == "B":
        df = df.iloc[[1, 2, 4, 33, 81, 88, 91, 98, 108]]
    elif groupe == "A+B":
        df = df.iloc[[5, 8, 9, 12, 39, 42, 63, 69, 94]+[1, 2, 4, 33, 81, 88, 91, 98, 108]]
    elif groupe == "Toutes":
        df = df
    else:
        raise RuntimeError("Nom de groupe inconnu !")  
    return df.to_dict(orient="records")

def dessiner_histogramme(fichier_de_sortie, variable, nom, couleur="blue", nbBins=20, ax_min=None, ax_max=None):
    range = [ax_min if ax_min is not None else np.min(variable), ax_max if ax_max is not None else np.max(variable)]
    plt.hist(variable, color=couleur, histtype="bar", bins=nbBins, range=range)
    plt.xlabel(nom, fontsize=15)
    plt.ylabel("Nombre d'événements par bin", fontsize=15)
    plt.tight_layout()
    plt.savefig(f"figures/{fichier_de_sortie}.png", dpi=300)
    
def dessiner_histogramme_2d(fichier_de_sortie, variable1, variable2, nom1, nom2, echelle_couleur="Blues", nbBins1=20, nbBins2=20):
    plt.hist2d(variable1, variable2, bins=(nbBins1, nbBins2), cmap=echelle_couleur)
    plt.xlabel(nom1, fontsize=15)
    plt.ylabel(nom2, fontsize=15)
    plt.tight_layout()
    plt.savefig(f"figures/{fichier_de_sortie}.png", dpi=300)
    
def dessiner_carte(fichier_de_sortie, ra, dec, couleur="blue", titre=None):
    if titre is None:
        titre = "Carte en coordonnées équatoriales"
    hp.mollview(rot=180, title=titre)
    hp.projscatter(ra, dec, lonlat=True, color=couleur, s=1, marker="x")
    hp.graticule()
    plt.savefig(f"figures/{fichier_de_sortie}.png", dpi=300)
    
def dessiner_carte_histogramme(fichier_de_sortie, ra, dec, echelle_couleur="Blues", titre=None, resolution=7):
    if titre is None:
        titre = "Carte en coordonnées équatoriales"
    h = np.zeros(hp.nside2npix(2**resolution))
    pixs = hp.ang2pix(2**resolution, ra, dec, lonlat=True)
    for pix in pixs:
        h[pix] += 1
    hp.mollview(h, rot=180, title=titre, cmap=echelle_couleur)
    hp.graticule()
    plt.savefig(f"figures/{fichier_de_sortie}.png", dpi=300)
    
def preparer_cercle(centre_ra, centre_dec, rayon, num_points=10000):
    # Generate angles evenly spaced along the circle's circumference
    circle_angles = np.linspace(0, 2 * np.pi, num_points)

    # Generate points on the circle using spherical coordinates
    circle_ra, circle_dec = [], []
    for angle in circle_angles:
        theta = centre_dec + rayon * np.cos(angle)
        phi = centre_ra + rayon * np.sin(angle)

        circle_ra.append(phi)
        circle_dec.append(theta)

    return circle_ra, circle_dec
    
def dessiner_carte_zoom(fichier_de_sortie, ra, dec, centre_ra, centre_dec, rayon, couleur="blue", titre=None):
    plt.scatter(ra, dec, color=couleur, marker="o")
    plt.scatter(centre_ra, centre_dec, color="k", marker="+", s=200)
    cercle_ra, cercle_dec = preparer_cercle(centre_ra, centre_dec, rayon)
    plt.plot(cercle_ra, cercle_dec, color="black", lw=2)
    plt.xlim((centre_ra-rayon, centre_ra+rayon))
    plt.ylim((centre_dec-rayon, centre_dec+rayon))
    plt.xlabel("RA[deg]")
    plt.ylabel("Dec[deg]")
    plt.savefig(f"figures/{fichier_de_sortie}.png", dpi=300)
    