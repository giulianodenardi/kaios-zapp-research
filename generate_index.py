import os
import re

DOCS_DIR = "docs"

def get_file_title(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Tenta pegar título do Front Matter YAML (title: "...")
    yaml_match = re.search(r"^---\n.*?title:\s*[\"']?(.*?)[\"']?\n.*?---", content, re.DOTALL | re.MULTILINE)
    if yaml_match:
        return yaml_match.group(1).strip()

    # Se não tiver Front Matter, pega o primeiro heading H1 (# Título)
    h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()

    # Fallback se não achar nenhum dos dois
    return os.path.basename(file_path)

def generate_index():
    articles_dir = os.path.join(DOCS_DIR, "artigos")
    manual_dir = os.path.join(DOCS_DIR, "manual")

    def build_links(directory):
        items = []
        if os.path.exists(directory):
            for file in sorted(os.listdir(directory)):
                if file.endswith(".md"):
                    path = os.path.join(directory, file)
                    title = get_file_title(path)
                    # Link relativo amigável
                    rel_path = os.path.relpath(path, DOCS_DIR).replace("\\", "/")
                    items.append(f"- [{title}]({rel_path})")
        return "\n".join(items)

    artigos_links = build_links(articles_dir)
    manual_links = build_links(manual_dir)

    md_content = f"""# Acervo e Documentação KaiOS / WhatsApp Research

## 📚 Acervo de Artigos
{artigos_links}

## 📖 Fases do Manual
{manual_links}
"""

    # Atualiza o index.md original
    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(md_content)

    # Gera a versão HTML pura para leitura standalone/local
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>KaiOS Research - Índice</title>
    <style>
        body {{ font-family: system-ui, -apple-system, sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 0 20px; color: #24292e; }}
        h1 {{ border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }}
        h2 {{ margin-top: 24px; color: #0366d6; }}
        ul {{ padding-left: 20px; }}
        li {{ margin: 8px 0; }}
        a {{ color: #0366d6; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Acervo e Documentação KaiOS / WhatsApp Research</h1>
    <h2>📚 Acervo de Artigos</h2>
    {artigos_links.replace('- [', '<li><a href="').replace('](', '">').replace(')', '</a></li>')}
    <h2>📖 Fases do Manual</h2>
    {manual_links.replace('- [', '<li><a href="').replace('](', '">').replace(')', '</a></li>')}
</body>
</html>"""

    with open(os.path.join(DOCS_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

    print("index.md e index.html gerados com sucesso com os títulos reais!")

if __name__ == "__main__":
    generate_index()
