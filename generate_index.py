import os
import re

DOCS_DIR = "docs" if os.path.exists("docs") else "."

def parse_front_matter(file_path):
    meta = {
        "title": None,
        "document_type": None,
        "id": None,
        "order": None
    }
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if match:
            yaml_block = match.group(1)
            
            title_match = re.search(r'title:\s*["\']?(.*?)["\']?\s*$', yaml_block, re.MULTILINE)
            if title_match:
                meta["title"] = title_match.group(1).strip()
                
            type_match = re.search(r'document_type:\s*["\']?(.*?)["\']?\s*$', yaml_block, re.MULTILINE)
            if type_match:
                meta["document_type"] = type_match.group(1).strip()
                
            id_match = re.search(r'id:\s*["\']?(.*?)["\']?\s*$', yaml_block, re.MULTILINE)
            if id_match:
                meta["id"] = id_match.group(1).strip()

        if not meta["title"]:
            h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            if h1_match:
                meta["title"] = h1_match.group(1).strip()
            else:
                meta["title"] = os.path.splitext(os.path.basename(file_path))[0]

    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")
        meta["title"] = os.path.basename(file_path)

    # Extrai o número para ordenação natural (ex: FASE-01 -> 1, FASE-02 -> 2, ART-001 -> 1)
    filename = os.path.basename(file_path)
    nums = re.findall(r'\d+', filename)
    if not nums and meta["id"]:
        nums = re.findall(r'\d+', meta["id"])
    meta["order"] = int(nums[0]) if nums else 999

    return meta

def scan_markdown_files():
    artigos = []
    manual = []
    outros = []

    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            # Ignora index.md e index.html para não listar a si mesmos
            if file.endswith(".md") and not file.startswith("index"):
                full_path = os.path.join(root, file)
                meta = parse_front_matter(full_path)
                
                # Gera o caminho relativo EXATO a partir de docs/
                rel_path = os.path.relpath(full_path, DOCS_DIR).replace("\\", "/")

                item = {
                    "title": meta["title"],
                    "path": rel_path,
                    "id": meta["id"],
                    "order": meta["order"]
                }

                doc_type = (meta["document_type"] or "").lower()
                doc_id = (meta["id"] or "").lower()
                path_lower = rel_path.lower()

                if doc_type == "article" or "art-" in doc_id or "artigo" in path_lower or "article" in path_lower:
                    artigos.append(item)
                elif doc_type == "manual" or "fase" in path_lower or "manual" in path_lower:
                    manual.append(item)
                else:
                    outros.append(item)

    # Ordenação numérico-crescente (1, 2, 3... em vez de 1, 10, 2)
    artigos.sort(key=lambda x: (x["order"], x["title"]))
    manual.sort(key=lambda x: (x["order"], x["title"]))
    outros.sort(key=lambda x: (x["order"], x["title"]))

    return artigos, manual, outros

def generate_index():
    artigos, manual, outros = scan_markdown_files()

    def render_md_list(items):
        if not items:
            return "_Nenhum documento encontrado._"
        return "\n".join([f"- [{item['title']}]({item['path']})" for item in items])

    def render_html_list(items):
        if not items:
            return "        <li><em>Nenhum documento encontrado.</em></li>"
        return "\n".join([f'        <li><a href="{item["path"]}">{item["title"]}</a></li>' for item in items])

    md_content = f"""# Acervo e Documentação KaiOS / WhatsApp Research

## 📚 Acervo de Artigos
{render_md_list(artigos)}

## 📖 Fases do Manual
{render_md_list(manual)}
"""
    if outros:
        md_content += f"\n## 📄 Outros Documentos\n{render_md_list(outros)}\n"

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

    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(md_content)

    with open(os.path.join(DOCS_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Sucesso!")
    print(f"   - Artigos encontrados: {len(artigos)}")
    print(f"   - Fases do Manual encontradas (ordenadas): {len(manual)}")

if __name__ == "__main__":
    generate_index()