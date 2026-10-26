# Portfólio — Talita Michelini

Site estático em um único arquivo: `index.html` (HTML, CSS e JavaScript, com as imagens e o recorte da foto embutidos). Não precisa de backend nem de instalação.

## Navegação
As cinco páginas (Início, Sobre mim, Projetos, Ferramentas e Contato) ficam lado a lado e rolam na horizontal: roda do mouse, deslizar no celular, setas do teclado, menu, pontinhos e setas laterais. O endereço muda a cada página (`#inicio`, `#sobre`, `#projetos`, `#ferramentas`, `#contato`).

## O que editar
Tudo fica no começo do bloco `<script>` do `index.html`:

- `CONFIG`: seus links (GitHub, LinkedIn, e-mail e WhatsApp). Campo vazio fica desativado na página.
- `PROJECTS`: título, descrição, tecnologias e imagens de cada card.
- `TOOLS`: as categorias da página Ferramentas (a faixa em movimento usa a mesma lista).

## Publicar
Qualquer hospedagem de site estático serve (Vercel, GitHub Pages, Netlify). Basta o `index.html` na raiz do repositório. Se for reaproveitar o repositório do site antigo, apague `vercel.json`, `main.py` e os demais arquivos antigos antes do `git push`.
