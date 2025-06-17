from scapy.all import sniff, IP, TCP
import csv
from datetime import datetime
import os

# Mots sensibles à détecter
mots_sensibles = ["password", "login", "admin", "secret", "token"]

# Initialiser le fichier CSV si inexistant
csv_filename = "log_paquets.csv"
if not os.path.exists(csv_filename):
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Heure", "IP Source", "IP Destination", "Protocole", "Payload", "Contenu suspect", "Entêtes HTTP"])

def analyse_paquet(packet):
    if IP in packet and TCP in packet:
        ip_source = packet[IP].src
        ip_dest = packet[IP].dst
        protocole = "TCP"

        try:
            contenu = bytes(packet[TCP].payload)
            contenu_text = contenu[:512].decode('utf-8', errors='replace')
        except:
            contenu_text = "[illisible]"

        # Vérifier si c’est HTTP
        if any(m in contenu_text for m in ["HTTP", "GET", "POST", "Host:", "User-Agent"]):
            # Détection contenu suspect
            est_suspect = "NON"
            for mot in mots_sensibles:
                if mot.lower() in contenu_text.lower():
                    est_suspect = "OUI"
                    break

            # Extraction entêtes HTTP simples
            headers = ""
            for ligne in contenu_text.split("\r\n"):
                if ":" in ligne:
                    headers += ligne + "; "

            # Affichage terminal
            print("📦 Paquet HTTP détecté :")
            print(f"🕒 Heure : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"🔹 De {ip_source} vers {ip_dest}")
            print(f"🔸 Protocole : {protocole}")
            print(f"🧾 Contenu : {contenu_text[:80]}...")
            print(f"⚠️ Contenu suspect : {est_suspect}")
            print("-" * 60)

            # Enregistrement CSV
            with open(csv_filename, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    ip_source,
                    ip_dest,
                    protocole,
                    contenu_text[:80],
                    est_suspect,
                    headers
                ])

# Lancer le sniffing
print("📡 Sniffing des paquets HTTP en cours... (Ctrl + C pour arrêter)")
sniff(filter="tcp", prn=analyse_paquet, store=0)
