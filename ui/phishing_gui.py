import tkinter as tk
from tkinter import messagebox, scrolledtext
from core.phishing_analyzer_core import analyser_url
from playsound import playsound
import os
import webbrowser
from .lang import texts  # Assurez-vous que lang.py est dans le même dossier ou accessible

# Langue par défaut
current_lang = "en"
def tr(key): return texts[current_lang][key]

# === Analyse de l’URL ===
def start_analysis():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", tr("empty_field"))
        return

    results = analyser_url(url)
    result_area.delete(1.0, tk.END)
    result_area.insert(tk.END, results)

    if "Risques détectés" in results or "Risk" in results:
        alarm_path = os.path.join(os.path.dirname(__file__), "sounds", "alarm.wav")
        if os.path.exists(alarm_path):
            playsound(alarm_path)

# === Infos phishing ===
def show_info():
    info = {
        "en": """🔍 What is a phishing link?
A phishing link is a fake URL designed to:
- steal your passwords,
- steal your credit card info,
- infect your device.

💡 How to recognize it?
- Spelling mistakes
- Urgency ("your account will be blocked!")
- Weird sender email (like paypal-support@gmail.com)
- Strange URLs (e.g. www.go0gle-security.com)""",
        "fr": """🔍 Qu’est-ce qu’un lien de phishing ?
Un lien de phishing est une fausse URL visant à :
- voler vos mots de passe,
- voler votre carte bancaire,
- infecter votre appareil.

💡 Comment les reconnaître ?
- Fautes d’orthographe
- Menace ou urgence ("votre compte sera bloqué !")
- Adresse email bizarre (ex : paypal-support@gmail.com)
- URL étrange (ex : www.go0gle-security.com)"""
    }
    win = tk.Toplevel()
    win.title(tr("what_is"))
    win.geometry("600x300")
    tk.Label(win, text=info[current_lang], justify="left", font=("Arial", 10)).pack(padx=20, pady=20)

# === Conseils ===
def show_tips():
    tips = {
        "en": """✅ How to protect yourself from phishing:

1. Check the sender's email
2. Don't click strange links
3. Use 2FA
4. Update antivirus
5. Never download unknown files
6. Check URLs before login
7. Use password manager
8. Don’t send private data by email""",
        "fr": """✅ Comment se protéger du phishing :

1. Vérifiez l'adresse de l’expéditeur
2. Ne cliquez pas sur les liens suspects
3. Activez la double authentification
4. Mettez à jour votre antivirus
5. Ne téléchargez jamais de pièces inconnues
6. Vérifiez les URL avant de vous connecter
7. Utilisez un gestionnaire de mots de passe
8. Ne communiquez jamais vos infos par email"""
    }
    win = tk.Toplevel()
    win.title(tr("tips"))
    win.geometry("600x300")
    tk.Label(win, text=tips[current_lang], justify="left", font=("Arial", 10)).pack(padx=20, pady=20)

# === Quiz ===
def start_quiz():
    q_en = [
        {"question": "Is this link safe? http://paypal-account-verification.com", "answer": "No"},
        {"question": "Should you click a link from SMS without checking?", "answer": "No"},
        {"question": "Do secure bank websites start with https?", "answer": "Yes"}
    ]
    q_fr = [
        {"question": "Ce lien est-il sûr ? http://paypal-account-verification.com", "answer": "Non"},
        {"question": "Faut-il cliquer sur un lien reçu par SMS sans vérifier ?", "answer": "Non"},
        {"question": "Les sites bancaires commencent-ils par https ?", "answer": "Oui"}
    ]
    questions = q_en if current_lang == "en" else q_fr

    quiz = tk.Toplevel()
    quiz.title(tr("quiz"))
    quiz.geometry("600x300")
    index = 0

    def show_question():
        question_label.config(text=questions[index]["question"])

    def answer(val):
        nonlocal index
        correct = questions[index]["answer"]
        if val == correct:
            messagebox.showinfo("Correct", tr("correct"))
        else:
            messagebox.showerror("Wrong", f"{tr('wrong')} ({correct})")
        index += 1
        if index < len(questions):
            show_question()
        else:
            messagebox.showinfo("Done", tr("done"))
            quiz.destroy()

    question_label = tk.Label(quiz, text="", font=("Arial", 12), wraplength=500)
    question_label.pack(pady=20)
    btn_yes = tk.Button(quiz, text="✅ Yes" if current_lang == "en" else "✅ Oui", command=lambda: answer("Yes" if current_lang == "en" else "Oui"))
    btn_no = tk.Button(quiz, text="❌ No" if current_lang == "en" else "❌ Non", command=lambda: answer("No" if current_lang == "en" else "Non"))
    btn_yes.pack(pady=5)
    btn_no.pack(pady=5)
    show_question()

# === Lien vers vidéo ===
def open_video():
    webbrowser.open("https://www.youtube.com/watch?v=3GBmpqhQI8s")

# === Changer de langue ===
def set_language(lang):
    global current_lang
    current_lang = lang
    update_texts()

def update_texts():
    window.title(tr("title"))
    label_instruction.config(text=tr("enter_url"))
    btn_analyze.config(text=tr("analyze"))
    btn_info.config(text=tr("what_is"))
    btn_tips.config(text=tr("tips"))
    btn_quiz.config(text=tr("quiz"))
    btn_video.config(text=tr("video"))

# === Interface ===
window = tk.Tk()
window.geometry("750x620")
window.resizable(False, False)
window.configure(bg="#f4f4f4")

# Menu de langue
menu = tk.Menu(window)
lang_menu = tk.Menu(menu, tearoff=0)
lang_menu.add_command(label="English", command=lambda: set_language("en"))
lang_menu.add_command(label="Français", command=lambda: set_language("fr"))
menu.add_cascade(label="🌐 Language", menu=lang_menu)
window.config(menu=menu)

# Header
tk.Label(window, text="Phishing Link Analyzer", font=("Arial", 16, "bold"), bg="#f4f4f4", fg="#333").pack(pady=10)

# Entrée URL
label_instruction = tk.Label(window, text=tr("enter_url"), font=("Arial", 11), bg="#f4f4f4")
label_instruction.pack(pady=5)
url_entry = tk.Entry(window, width=85)
url_entry.pack(pady=5)

# Bouton analyse
btn_analyze = tk.Button(window, text=tr("analyze"), command=start_analysis, bg="#007acc", fg="white", font=("Arial", 10, "bold"), width=20)
btn_analyze.pack(pady=10)

# Zone résultats
result_area = scrolledtext.ScrolledText(window, width=90, height=15, wrap=tk.WORD)
result_area.pack(padx=10, pady=10)

# Boutons pédagogiques
frame_buttons = tk.Frame(window, bg="#f4f4f4")
frame_buttons.pack(pady=10)
btn_info = tk.Button(frame_buttons, text=tr("what_is"), command=show_info, bg="#ffcc00", font=("Arial", 10, "bold"), width=22)
btn_tips = tk.Button(frame_buttons, text=tr("tips"), command=show_tips, bg="#33cc33", font=("Arial", 10, "bold"), width=22)
btn_quiz = tk.Button(frame_buttons, text=tr("quiz"), command=start_quiz, bg="#cc3300", fg="white", font=("Arial", 10, "bold"), width=22)
btn_video = tk.Button(frame_buttons, text=tr("video"), command=open_video, bg="#6a5acd", fg="white", font=("Arial", 10, "bold"), width=22)

btn_info.grid(row=0, column=0, padx=5, pady=5)
btn_tips.grid(row=0, column=1, padx=5, pady=5)
btn_quiz.grid(row=1, column=0, padx=5, pady=5)
btn_video.grid(row=1, column=1, padx=5, pady=5)

update_texts()
window.mainloop()
