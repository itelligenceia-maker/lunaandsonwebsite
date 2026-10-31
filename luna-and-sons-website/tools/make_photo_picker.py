#!/usr/bin/env python3
"""
Builds tools/photo-picker.html — a contact sheet of every photo in the project with its
file name, so you can choose which one goes in each Process step / Services card.
Open it by double-clicking tools/photo-picker.html. Click a tile to copy its path.
INTERNAL TOOL: don't upload this file to the live site.
Run: python3 tools/make_photo_picker.py
"""
import html
import os
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXT = {".jpg", ".jpeg", ".png", ".webp"}
SKIP_DIRS = {"logo", "process", "_backup-before-process-update", "tools", ".git", ".vscode"}

groups = {}
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
    rel_dir = os.path.relpath(dirpath, ROOT)
    for fn in sorted(filenames):
        if os.path.splitext(fn)[1].lower() in EXT and not fn.startswith("."):
            groups.setdefault(rel_dir, []).append(fn)

sections = []
for d in sorted(groups):
    tiles = []
    for fn in groups[d]:
        rel = fn if d == "." else f"{d}/{fn}"
        size_kb = os.path.getsize(os.path.join(ROOT, rel)) // 1024
        tiles.append(
            f'<button class="t" data-path="{html.escape(rel)}" title="Click to copy path">'
            f'<img loading="lazy" src="../{quote(rel)}" alt="">'
            f'<span>{html.escape(fn)}</span><small>{size_kb} KB</small></button>')
    sections.append(f'<h2>{html.escape(d)}/ <small>{len(tiles)} photos</small></h2><div class="g">{"".join(tiles)}</div>')

page = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Photo picker (internal)</title>
<meta name="robots" content="noindex">
<style>
body{{font-family:system-ui,sans-serif;margin:24px;background:#f6f4f8;color:#222}}
h1{{margin:0 0 4px}} p{{margin:0 0 20px;color:#555}}
h2{{margin:32px 0 12px;font-size:1.1rem;color:#4B1D63}} h2 small{{color:#888;font-weight:400}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}}
.t{{border:1px solid #ddd;background:#fff;border-radius:10px;padding:0;cursor:pointer;text-align:left;overflow:hidden}}
.t:hover{{border-color:#4B1D63}} .t.copied{{outline:3px solid #4B1D63}}
.t img{{display:block;width:100%;height:150px;object-fit:cover;background:#eee}}
.t span{{display:block;padding:8px 10px 0;font-size:12px;word-break:break-all}} .t small{{display:block;padding:0 10px 8px;color:#888;font-size:11px}}
</style></head><body>
<h1>Photo picker</h1><p>Every photo in the project. Click a tile to copy its path, then tell me (or Claude Code) which step/service it belongs to. Internal tool: don't publish.</p>
{"".join(sections)}
<script>document.querySelectorAll('.t').forEach(b=>b.addEventListener('click',()=>{{navigator.clipboard&&navigator.clipboard.writeText(b.dataset.path);b.classList.add('copied');setTimeout(()=>b.classList.remove('copied'),900)}}))</script>
</body></html>"""
with open(os.path.join(ROOT, "tools", "photo-picker.html"), "w", encoding="utf-8") as f:
    f.write(page)
print("wrote tools/photo-picker.html —", sum(len(v) for v in groups.values()), "photos in", len(groups), "folders")
