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
## ✅ Task 2 - Phishing Awareness Training

An interactive GUI app that helps users learn about phishing:
- Real-time link analysis
- Sound alarm when threats detected
- Anti-phishing advice
- Educational explanation
- Interactive quiz
- Multilingual (English / French)

📁 Launch with:
