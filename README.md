# 📡 CodeAlpha - Basic Network Sniffer

Un sniffer réseau Python simple et efficace, développé par **Rayen Aouini** dans le cadre du programme **CodeAlpha**.  
👉 [Lien du dépôt GitHub](https://github.com/aouinirayen/CodeAlpha_BasicNetworkSniffer)

---

## 🚀 Fonctionnalités actuelles

✅ Capture de paquets en temps réel (TCP/IP)  
✅ Détection automatique de mots sensibles (`password`, `login`, `admin`, `token`, `secret`)  
✅ Affichage lisible en console (paquet, IPs, protocole, contenu)  
✅ Alerte visuelle (⚠️) si un paquet contient des données suspectes  
✅ Extraction des entêtes HTTP (User-Agent, Host, etc.)  
✅ Export des résultats dans un fichier CSV (`log_paquets.csv`) :

- Heure exacte de capture
- IP source et destination
- Protocole
- Payload (contenu)
- Contenu suspect : **OUI / NON**
- Entêtes HTTP (si présents)

---

## 🧪 Exemple d’exécution console

```text
📦 Paquet HTTP détecté :
🕒 Heure : 2025-06-17 20:56:34
🔹 De 192.168.1.144 vers 34.206.58.73
🔸 Protocole : TCP
🧾 Contenu : GET /get?password=1234 HTTP/1.1
User-Agent: Mozilla/5.0...
⚠️ Contenu suspect : OUI
------------------------------------------------------------
