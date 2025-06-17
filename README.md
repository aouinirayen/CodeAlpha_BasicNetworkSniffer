# 🛡️ Basic Network Sniffer – HTTP Packet Analyzer

Ce projet est un sniffer réseau simple en Python utilisant la bibliothèque `scapy`. Il permet de capturer le trafic réseau TCP, d’analyser les paquets HTTP, de détecter la présence de mots sensibles (comme `password`, `login`, `admin`, etc.), d'afficher les résultats en console de manière claire et de sauvegarder les données analysées dans un fichier CSV.

---

## 📦 Fonctionnalités principales

- 📡 **Sniffing du trafic HTTP** sur le réseau.
- 🧾 **Analyse du contenu des paquets TCP**, y compris le payload.
- 🚨 **Détection automatique** de mots sensibles dans les paquets.
- 🛑 Affichage clair dans le terminal : source, destination, contenu, alerte si suspect.
- 📝 **Sauvegarde automatique dans un fichier `log_paquets.csv`** avec :
  - Heure
  - IP source
  - IP destination
  - Protocole
  - Contenu (payload)
  - Alerte contenu suspect (OUI/NON)
  - Entêtes HTTP détectées

---

## 🛠️ Prérequis

- Python **3.8+**
- Bibliothèques Python :
  - `scapy` (`pip install scapy`)

---

## 🚀 Installation

1. **Cloner le projet :**
   ```bash
   git clone https://github.com/aouinirayen/CodeAlpha_BasicNetworkSniffer.git
   cd CodeAlpha_BasicNetworkSniffer
Créer un environnement virtuel (optionnel mais recommandé) :

bash
Copier
Modifier
python -m venv .venv
.venv\Scripts\activate  # Sur Windows
source .venv/bin/activate  # Sur Linux/macOS
Installer les dépendances :

bash
Copier
Modifier
pip install scapy
▶️ Lancer le sniffer
bash
Copier
Modifier
python sniffer.py
🧪 Exemple d'affichage dans le terminal
yaml
Copier
Modifier
📦 Paquet HTTP détecté :
🕒 Heure : 2025-06-17 20:56:34
🔹 De 192.168.1.144 vers 34.206.58.73
🔸 Protocole : TCP
🧾 Contenu : GET /get?password=1234 HTTP/1.1...
⚠️ Contenu suspect : OUI
------------------------------------------------------------
📁 Exemple du fichier log_paquets.csv
Heure	IP Source	IP Destination	Protocole	Payload	Contenu suspect	Entêtes HTTP
2025-06-17 20:56:34	192.168.1.144	34.206.58.73	TCP	GET /get?password=1234 HTTP/1.1	OUI	User-Agent: Mozilla...; Host: httpbin.org; ...

🔒 Mots sensibles détectés
Liste configurable dans le script (mots_sensibles) :

python
Copier
Modifier
["password", "login", "admin", "secret", "token"]
✅ Étapes suivantes (non incluses mais prévues) :
🔔 Ajout d'une alerte sonore si paquet suspect.

🖥️ Intégration d'une interface graphique Tkinter.

📊 Ajout de filtres (ex : ne sniffer que HTTP, ignorer les images, etc.)

👨‍💻 Auteur
Rayen Aouini – GitHub

📜 Licence
Projet éducatif sous licence MIT.

yaml
Copier
Modifier

---

Souhaites-tu que je crée aussi un logo simple en ASCII ou un schéma pour ce `README.md` ?








