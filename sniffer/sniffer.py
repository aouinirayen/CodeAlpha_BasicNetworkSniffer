from scapy.all import sniff, IP, TCP
import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import threading
import platform
import os

# === Configuration ===
mots_sensibles = ["password", "login", "admin", "secret", "token"]
fichier_csv = "log_paquets.csv"

# === Alerte sonore ===
def alerte_sonore():
    try:
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(1000, 300)
        else:
            from playsound import playsound
            playsound("beep.mp3")  # Assure-toi d’avoir ce fichier dans le dossier
    except Exception as e:
        print(f"Erreur alerte sonore : {e}")

# === Interface graphique ===
fenetre = tk.Tk()
fenetre.title("Sniffer HTTP - Vue en direct")
fenetre.geometry("900x400")

# === Tableau Tkinter ===
tableau = ttk.Treeview(fenetre, columns=("heure", "src", "dst", "proto", "suspect"), show="headings")
for col in ("heure", "src", "dst", "proto", "suspect"):
    tableau.heading(col, text=col.capitalize())
    tableau.column(col, width=150)
tableau.pack(fill=tk.BOTH, expand=True)

# === Création du fichier CSV si inexistant ===
if not os.path.exists(fichier_csv):
    with open(fichier_csv, "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["Heure", "IP Source", "IP Destination", "Protocole", "Payload", "Contenu suspect", "Entêtes HTTP"])

# === Analyse des paquets ===
def analyse_paquet(packet):
    if IP in packet and TCP in packet:
        ip_source = packet[IP].src
        ip_dest = packet[IP].dst
        protocole = "TCP"
        try:
            contenu = bytes(packet[IP].payload)
            contenu_text = contenu[:256].decode('utf-8', errors='replace')
        except:
            contenu_text = "[illisible]"

        if "HTTP" in contenu_text or "GET" in contenu_text or "POST" in contenu_text:
            est_suspect = "NON"
            for mot in mots_sensibles:
                if mot.lower() in contenu_text.lower():
                    est_suspect = "OUI"
                    alerte_sonore()
                    break

            headers = ""
            lignes = contenu_text.split("\r\n")
            for ligne in lignes:
                if ":" in ligne:
                    headers += ligne + "; "

            heure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("📦 Paquet HTTP détecté :")
            print(f"🕒 Heure : {heure}")
            print(f"🔹 De {ip_source} vers {ip_dest}")
            print(f"🔸 Protocole : {protocole}")
            print(f"🧾 Contenu : {contenu_text[:80]}...")
            print(f"⚠️ Contenu suspect : {est_suspect}")
            print("-" * 60)

            # Insertion interface
            tableau.insert("", "end", values=(heure, ip_source, ip_dest, protocole, est_suspect))

            # Sauvegarde CSV
            with open(fichier_csv, "a", newline="", encoding="utf-8") as fichier:
                writer = csv.writer(fichier)
                writer.writerow([heure, ip_source, ip_dest, protocole, contenu_text[:80], est_suspect, headers])

# === Thread sniffing ===
def lancer_sniffer():
    print("📡 Sniffing des paquets HTTP en cours... (Ctrl + C pour arrêter)")
    sniff(prn=analyse_paquet, store=0)

sniffer_thread = threading.Thread(target=lancer_sniffer)
sniffer_thread.daemon = True
sniffer_thread.start()

# === Lancer l’interface graphique ===
fenetre.mainloop()
