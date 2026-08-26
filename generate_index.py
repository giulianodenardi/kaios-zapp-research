import os
import re

# Caminho da pasta docs (ajuste para "." se o script rodar de dentro de /docs)
DOCS_DIR = "docs" if os.path.exists("docs") else "."

def get_file_title(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Tenta pegar do Front Matter YAML (title: "...")
    yaml_match = re.search(r"^---\n.*?title:\s*[\"']?(.*?)[\"']?\n.*?---", content, re.DOTALL | re.MULTILINE)
    if yaml_match:
        return yaml_match.group(1).strip()

    # 2. Tenta pegar do primeiro H1 (# Titulo)
    h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()

    # 3. Se não achar nada, usa o nome do arquivo
    return os.path.basename(file_path)

def find_dir_case_insensitive(parent, name):
    for entry in os.listdir(parent):
        if entry.lower() == name.lower() and os.path.isdir(os.path.join(parent, entry)):
            return os.path.join(parent, entry)
    return None

def build_links(directory):
    md_links = []
    html_links = []
    
    if directory and os.path.exists(directory):
        for file in sorted(os.listdir(directory)):
            if file.endswith(".md") and not file.startswith("index"):
                path = os.path.join(directory, file)
                title = get_file_title(path)
                
                # Relativo para o GitHub Pages / Links
                rel_path = os.path.relpath(path, DOCS_DIR).replace("\\", "/")
                
                md_links.append(f"- [{title}]({rel_path})")
                html_links.append(f'        <li><a href="{rel_path}">{title}</a></li>')
                
    return "\n".join(md_links), "\n".join(html_links)

def generate_index():
    articles_dir = find_dir_case_insensitive(DOCS_DIR, "artigos")
    manual_dir = find_dir_case_insensitive(DOCS_DIR, "manual")

    art_md, art_html = build_links(articles_dir)
    man_md, man_html = build_links(manual_dir)

    # 1. Gerar index.md (versao nativa GitHub)
    md_content = f"""# Acervo e Documentação KaiOS / WhatsApp Research

## 📚 Acervo de Artigos
{art_md if art_md else "_Nenhum artigo encontrado._"}

## 📖 Fases do Manual
{man_md if man_md else "_Nenhuma fase encontrada._"}
"""

    # 2. Gerar index.html (versao GitHub Pages)
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KaiOS Research - Índice</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; max-width: 850px; margin: 40px auto; padding: 0 20px; color: #24292e; }}
        h1 {{ border-bottom: 2px solid #eaecef; padding-bottom: 0.3em; }}
        h2 {{ margin-top: 32px; color: #0366d6; border-bottom: 1px solid #eee; padding-bottom: 6px; }}
        ul {{ padding-left: 24px; }}
        li {{ margin: 10px 0; }}
        a {{ color: #0366d6; text-decoration: none; font-weight: 500; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Acervo e Documentação KaiOS / WhatsApp Research</h1>
    
    <h2>📚 Acervo de Artigos</h2>
    <ul>
{art_html if art_html else "        <li><em>Nenhum artigo encontrado.</em></li>"}
    </ul>

    <h2>📖 Fases do Manual</h2>
    <ul>
{man_html if man_html else "        <li><em>Nenhuma fase encontrada.</em></li>"}
    </ul>
</body>
</html>"""

    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(md_content)

    with open(os.path.join(DOCS_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ index.md e index.html gerados com sucesso!")

if __name__ == "__main__":
    generate_index()