# core/phishing_analyzer_core.py
import requests
from urllib.parse import urlparse
import ipaddress
import csv
from datetime import datetime

mots_suspects = ["password", "login", "admin", "token", "secret"]

CSV_PATH = "logs/phishing_logs.csv"

def est_adresse_ip(hostname):
    try:
        ipaddress.ip_address(hostname)
        return True
    except ValueError:
        return False

def analyser_url(url):
    resultats = []
    anomalies = []

    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resultats.append(f"🔍 Analyse de l'URL : {url}")

    if url.startswith("https"):
        connexion = "HTTPS"
        resultats.append("✅ Connexion sécurisée (HTTPS)")
    else:
        connexion = "HTTP"
        anomalies.append(("Connexion non sécurisée", "Les connexions HTTP peuvent être interceptées facilement (Man-in-the-middle)"))
        resultats.append("⚠️ Connexion non sécurisée (HTTP)")

    mot_suspect_trouve = "NON"
    for mot in mots_suspects:
        if mot in url.lower():
            mot_suspect_trouve = "OUI"
            anomalies.append((f"Mot suspect : {mot}", "Mot utilisé souvent dans les attaques de phishing."))
            resultats.append(f"⚠️ Lien contient un mot suspect : '{mot}'")

    domaine_ip = "Non détecté"
    try:
        domaine = urlparse(url).hostname
        if domaine:
            if est_adresse_ip(domaine):
                domaine_ip = domaine
                anomalies.append(("Adresse IP directe", "Les sites légitimes utilisent un nom de domaine, pas une IP brute."))
                resultats.append(f"⚠️ Adresse IP directe : {domaine}")
            else:
                domaine_ip = domaine
                resultats.append(f"🌐 Domaine : {domaine}")
    except:
        resultats.append("❌ Impossible d'extraire le domaine")

    code_http = "N/A"
    redirection = "NON"
    try:
        reponse = requests.get(url, timeout=5, allow_redirects=True)
        code_http = reponse.status_code
        resultats.append(f"📶 Statut HTTP : {reponse.status_code}")
        if len(reponse.history) > 0:
            redirection = "OUI"
            anomalies.append(("Redirection", f"Redirection détectée vers : {reponse.url}"))
            resultats.append(f"⚠️ Redirection détectée vers : {reponse.url}")
        else:
            resultats.append("✅ Pas de redirection")
    except requests.exceptions.SSLError:
        anomalies.append(("Erreur SSL", "Certificat SSL invalide ou absent : attention au spoofing."))
        resultats.append("❌ Erreur SSL : certificat invalide ou absent")
    except requests.exceptions.RequestException as e:
        anomalies.append(("Erreur de requête", str(e)))
        resultats.append(f"❌ Erreur requête : {e}")

    if anomalies:
        resultats.append("\n📛 Risques détectés :")
        for a, exp in anomalies:
            resultats.append(f"- {a} ➜ {exp}")
    else:
        resultats.append("✅ Aucun comportement suspect détecté.")

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for a, exp in anomalies:
            writer.writerow([horodatage, url, connexion, domaine_ip, code_http, redirection, a, exp])
        if not anomalies:
            writer.writerow([horodatage, url, connexion, domaine_ip, code_http, redirection, "Aucun", "RAS"])

    return "\n".join(resultats)