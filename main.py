import sys
import os

# Ajoute le chemin racine du projet au sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Lancer l'interface graphique
from ui.phishing_gui import launch_gui

if __name__ == "__main__":
    print("Démarrage de l'application réseau...")
    launch_gui()
