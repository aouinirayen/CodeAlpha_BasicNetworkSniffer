from scapy.all import sniff, IP

def afficher_paquet(packet):
    if IP in packet:
        ip_source = packet[IP].src
        ip_dest = packet[IP].dst
        print(f"De {ip_source} vers {ip_dest}")

print("📡 En écoute du trafic réseau (Ctrl+C pour arrêter)...")
sniff(prn=afficher_paquet, count=10)
