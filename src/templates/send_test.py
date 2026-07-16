import smtplib
import sys
from pathlib import Path
from email.message import EmailMessage

if len(sys.argv) < 2:
    print('Verwendung: python3 send_test.py "Pfad/zur/Vorlage.html"')
    raise SystemExit(1)

html_path = Path(sys.argv[1])

if not html_path.is_file():
    print(f"HTML-Datei nicht gefunden: {html_path}")
    raise SystemExit(1)

html = html_path.read_text(encoding="utf-8")

message = EmailMessage()
message["From"] = "accounting@akademikerhilfe.at"
message["To"] = "test@example.com"
message["Subject"] = f"TEST – {html_path.stem}"

message.set_content("Testnachricht mit HTML-Inhalt.")
message.add_alternative(html, subtype="html")

with smtplib.SMTP("localhost", 1025) as smtp:
    smtp.send_message(message)

print(f"Testmail versendet: {html_path.name}")
print("Mailpit über Port 8025 öffnen.")