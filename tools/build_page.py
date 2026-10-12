#!/usr/bin/env python3
"""Render contributions/NN/draft.md into a website-root essay page.

Handles only the markdown this project actually uses: h1/h2, paragraphs,
blockquotes, bullet lists, thematic breaks, and inline em/strong/code/links.
HTML comments in the draft are build notes and are dropped.
"""
import html, os, re, sys

src, dst, number, date = sys.argv[1:5]
canonical = f'https://impossible-task.de/{os.path.basename(dst)}'
text = open(src).read()
text = re.sub(r'<!--.*?-->', '', text, flags=re.S).strip()

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',
               lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    return t

lines = text.split('\n')
title = byline = None
out, i = [], 0

# Title and byline come first and are lifted into the page header block.
while i < len(lines):
    ln = lines[i].strip()
    if ln.startswith('# ') and title is None:
        title = ln[2:].strip(); i += 1; continue
    if ln.startswith('*by ') and byline is None:
        byline = ln.strip('*'); i += 1; continue
    if ln == '':
        i += 1; continue
    break

def flush(buf, tag='p', cls=''):
    if not buf: return
    c = f' class="{cls}"' if cls else ''
    out.append(f'<{tag}{c}>{inline(" ".join(buf))}</{tag}>')
    buf.clear()

buf, in_endnotes = [], False
while i < len(lines):
    raw = lines[i]; ln = raw.strip()
    if ln == '---':
        flush(buf); out.append('<hr>')
        out.append('<div class="endnotes">'); in_endnotes = True; i += 1; continue
    if ln.startswith('## '):
        flush(buf); out.append(f'<h2>{inline(ln[3:].strip())}</h2>'); i += 1; continue
    if ln.startswith('### '):
        flush(buf); out.append(f'<h3>{inline(ln[4:].strip())}</h3>'); i += 1; continue
    if ln.startswith('> '):
        flush(buf)
        q = []
        while i < len(lines) and lines[i].strip().startswith('>'):
            q.append(lines[i].strip().lstrip('>').strip()); i += 1
        paras, cur = [], []
        for seg in q:
            if seg == '':
                if cur: paras.append(' '.join(cur)); cur = []
            else:
                cur.append(seg)
        if cur: paras.append(' '.join(cur))
        inner = ''.join(f'<p>{inline(p)}</p>' for p in paras)
        out.append(f'<blockquote>{inner}</blockquote>')
        continue
    if ln.startswith('- '):
        flush(buf)
        items = []
        while i < len(lines) and lines[i].strip().startswith('- '):
            item = [lines[i].strip()[2:]]; i += 1
            while i < len(lines) and lines[i].startswith('  ') and lines[i].strip():
                item.append(lines[i].strip()); i += 1
            items.append(' '.join(item))
        out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ul>')
        continue
    if ln == '':
        flush(buf); i += 1; continue
    buf.append(ln); i += 1
flush(buf)
if in_endnotes: out.append('</div>')

body = '\n            '.join(out)
page = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)} &mdash; impossible task</title>
    <link rel="canonical" href="{html.escape(canonical, quote=True)}">
    <link rel="license" href="https://creativecommons.org/licenses/by/4.0/">
    <link rel="service-desc" type="application/json" href="/.well-known/libp2p-access.json">
    <link rel="stylesheet" href="site.css">
</head>
<body>

    <div class="container">

        <header>
            <div class="logo-text"><a href="/">[ impossible task ]</a></div>
            <div class="meta-line">{number} &middot; Published: {date}</div>
        </header>

        <main>

            <h1>{html.escape(title)}</h1>
            <div class="byline">{inline(byline)}</div>

            {body}

        </main>

        <footer>
            <a href="/privacy.html">Privacy Policy</a>
            &middot; Text licensed under <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>
            &middot; <a rel="service-desc" type="application/json" href="/.well-known/libp2p-access.json">libp2p access for agents</a>
        </footer>

    </div>

</body>
</html>
'''
open(dst, 'w').write(page)
print(f'wrote {dst}: {len(page)} bytes, title={title!r}')
