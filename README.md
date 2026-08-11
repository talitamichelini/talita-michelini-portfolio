# Talita Michelini — Landing Page de Portfólio

Landing page pessoal para apresentar meu trabalho com automação de
atendimento (WhatsApp e Instagram) e agentes de IA.

🔗 **Site no ar:** _(adicione aqui o link da Vercel depois do deploy)_

## Stack

**Front-end**
- HTML, CSS e JavaScript puro (sem framework) — foco em performance e simplicidade
- Design dark mode com efeito glassmorphism

**Backend**
- Python + FastAPI
- Envio de e-mail via SMTP (Gmail) para o formulário de contato
- Deploy como função serverless na Vercel

## Estrutura do projeto

```
.
├── index.html          # Site completo (front-end)
├── main.py             # API do formulário de contato (backend)
├── requirements.txt    # Dependências Python
├── .env.example        # Modelo de variáveis de ambiente
└── .gitignore
```

## Rodando localmente

```bash
# 1. instalar dependências do backend
pip install -r requirements.txt

# 2. criar o .env a partir do exemplo e preencher com dados reais
cp .env.example .env

# 3. rodar o backend
uvicorn main:app --reload

# 4. abrir o index.html no navegador (ou usar a extensão Live Server do VSCode)
```

## Deploy

O projeto é publicado na [Vercel](https://vercel.com), que hospeda o
`index.html` como site estático e o `main.py` como função serverless,
ambos no mesmo domínio — por isso o front-end chama a API pelo caminho
relativo `/api/contact`, sem precisar de configuração de CORS.

Variáveis de ambiente necessárias no painel da Vercel:
- `EMAIL_ADDRESS`
- `EMAIL_APP_PASSWORD`
- `TO_EMAIL`

---

Feito por [Talita Michelini](https://instagram.com/talitamichelini).
