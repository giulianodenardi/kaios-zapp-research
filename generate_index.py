import os
import re

# Detecta se está na raiz do repositório ou dentro de docs/
DOCS_DIR = "docs" if os.path.exists("docs") else "."

def parse_front_matter(file_path):
    """ Extrai title, document_type e id do Front Matter YAML """
    meta = {
        "title": None,
        "document_type": None,
        "id": None
    }
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Procura o bloco entre --- e --- no inicio do arquivo
        match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if match:
            yaml_block = match.group(1)
            
            # Extrai o title
            title_match = re.search(r'title:\s*["\']?(.*?)["\']?\s*$', yaml_block, re.MULTILINE)
            if title_match:
                meta["title"] = title_match.group(1).strip()
                
            # Extrai document_type
            type_match = re.search(r'document_type:\s*["\']?(.*?)["\']?\s*$', yaml_block, re.MULTILINE)
            if type_match:
                meta["document_type"] = type_match.group(1).strip()
                
            # Extrai id
            id_match = re.search(r'id:\s*["\']?(.*?)["\']?\s*$', yaml_block, re.MULTILINE)
            if id_match:
                meta["id"] = id_match.group(1).strip()

        # Fallback: Se não achou título no Front Matter, tenta pegar o H1 (# Título)
        if not meta["title"]:
            h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            if h1_match:
                meta["title"] = h1_match.group(1).strip()
            else:
                meta["title"] = os.path.splitext(os.path.basename(file_path))[0]

    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")
        meta["title"] = os.path.basename(file_path)

    return meta

def generate_index():
    artigos = []
    manual = []
    outros = []

    # Varre todos os arquivos .md dentro da pasta docs e subpastas
    for root, _, files in os.walk(DOCS_DIR):
        for file in sorted(files):
            if file.endswith(".md") and not file.startswith("index"):
                full_path = os.path.join(root, file)
                meta = parse_front_matter(full_path)
                
                # Gera caminho relativo para uso no HTML/MD
                rel_path = os.path.relpath(full_path, DOCS_DIR).replace("\\", "/")

                item = {
                    "title": meta["title"],
                    "path": rel_path,
                    "id": meta["id"]
                }

                doc_type = (meta["document_type"] or "").lower()
                doc_id = (meta["id"] or "").lower()
                path_lower = rel_path.lower()

                # Categorização baseada nos metadados do Front Matter
                if doc_type == "article" or "art-" in doc_id or "artigo" in path_lower:
                    artigos.append(item)
                elif doc_type == "manual" or "fase" in path_lower or "manual" in path_lower:
                    manual.append(item)
                else:
                    outros.append(item)

    # Função aux para renderizar no Markdown
    def render_md_list(items):
        if not items:
            return "_Nenhum documento encontrado._"
        return "\n".join([f"- [{item['title']}]({item['path']})" for item in items])

    # Função aux para renderizar no HTML
    def render_html_list(items):
        if not items:
            return "        <li><em>Nenhum documento encontrado.</em></li>"
        return "\n".join([f'        <li><a href="{item["path"]}">{item["title"]}</a></li>' for item in items])

    # Monta index.md
    md_content = f"""# Acervo e Documentação KaiOS / WhatsApp Research

## 📚 Acervo de Artigos
{render_md_list(artigos)}

## 📖 Fases do Manual
{render_md_list(manual)}
"""
    if outros:
        md_content += f"\n## 📄 Outros Documentos\n{render_md_list(outros)}\n"

    # Monta index.html
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
{render_html_list(artigos)}
    </ul>

    <h2>📖 Fases do Manual</h2>
    <ul>
{render_html_list(manual)}
    </ul>
"""
    if outros:
        html_content += f"""
    <h2>📄 Outros Documentos</h2>
    <ul>
{render_html_list(outros)}
    </ul>"""

    html_content += "\n</body>\n</html>"

    # Salva os dois arquivos
    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(md_content)

    with open(os.path.join(DOCS_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Processamento concluído!")
    print(f"   - Artigos: {len(artigos)}")
    print(f"   - Manual: {len(manual)}")
    print(f"   - Outros: {len(outros)}")

if __name__ == "__main__":
    generate_index()