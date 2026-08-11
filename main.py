"""
Backend do formulário de contato — Talita Michelini
-----------------------------------------------------
O que esse arquivo faz:
1. Sobe uma API com um único endpoint: POST /api/contact
2. Recebe os dados do formulário do site (nome, contato, tipo, mensagem)
3. Envia um e-mail pra você (via Gmail) com esses dados

Como rodar local:
    1. python -m venv venv
    2. source venv/bin/activate   (no Windows: venv\\Scripts\\activate)
    3. pip install -r requirements.txt
    4. copie .env.example para .env e preencha com seus dados reais
    5. uvicorn main:app --reload
    6. a API vai estar em http://localhost:8000
       (documentação automática em http://localhost:8000/docs)

Veja o README.md para instruções completas, incluindo como gerar a
"senha de app" do Gmail e como publicar isso no Render.
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")        # e-mail que ENVIA (ex: talitamichelini.prog@gmail.com)
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")  # senha de app do Gmail (não é sua senha normal!)
TO_EMAIL = os.getenv("TO_EMAIL", EMAIL_ADDRESS)    # e-mail que RECEBE (pode ser o mesmo)

app = FastAPI(title="Talita Michelini - Contact API")

# CORS: permite que o navegador (rodando no seu site) chame essa API.
# Em produção, troque "*" pela URL real do seu site para maior segurança,
# ex: allow_origins=["https://talitamichelini.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)


class ContactForm(BaseModel):
    nome: str = Field(..., min_length=1, max_length=120)
    contato: str = Field(..., min_length=1, max_length=120)
    tipo: str = Field(..., min_length=1, max_length=120)
    mensagem: str = Field(..., min_length=1, max_length=2000)


@app.get("/")
def health_check():
    """Endpoint simples pra confirmar que a API está no ar."""
    return {"status": "ok", "service": "talita-michelini-contact-api"}


@app.post("/api/contact")
def send_contact_email(form: ContactForm):
    if not EMAIL_ADDRESS or not EMAIL_APP_PASSWORD:
        # Isso normalmente significa que o .env não foi configurado ainda.
        raise HTTPException(
            status_code=500,
            detail="Servidor de e-mail não configurado. Verifique o arquivo .env.",
        )

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL
    msg["Subject"] = f"Novo contato pelo site — {form.nome}"

    corpo = f"""Você recebeu uma nova mensagem pelo formulário do site:

Nome: {form.nome}
WhatsApp/Instagram: {form.contato}
Tipo de automação desejada: {form.tipo}

Mensagem:
{form.mensagem}
"""
    msg.attach(MIMEText(corpo, "plain", "utf-8"))

    try:
        # Gmail exige conexão segura (SSL) na porta 465
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
            server.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        raise HTTPException(
            status_code=500,
            detail="Falha ao autenticar no Gmail. Confira EMAIL_ADDRESS e EMAIL_APP_PASSWORD no .env.",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar e-mail: {e}")

    return {"status": "sent"}
