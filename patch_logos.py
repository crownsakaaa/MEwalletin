#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('MEwalletin.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = (
    'function drawB(){var h="",c=BC[S.c],p=c&&c.p[S.p];\n'
    ' if(S.st==="cat"){h=bh("Bayar tagihan","x")+\'<div class="bl2">\'+BC.map(function(x,i){return \'<button class="brw" data-b="cat" data-v="\'+i+\'"><span class="ic">\'+x.k[0]+\'</span><span class="nm">\'+x.k+\'<small>\'+x.d+\'</small></span><span>\'+ik("r")+\'</span></button>\'}).join("")+\'</div>\'}\n'
    ' else if(S.st==="prov"){h=bh(c.k,"bk")+\'<div class="bl2">\'+c.p.map(function(x,i){return \'<button class="brw" data-b="prov" data-v="\'+i+\'"><span class="ic">\'+esc(x[0][0])+\'</span><span class="nm">\'+esc(x[0])+\'</span><span>\'+ik("r")+\'</span></button>\'}).join("")+\'</div>\'}'
)

new_block = (
    'var CATLOGO={\n'
    ' "Internet":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#0a4fa8"/><path d="M18 8a10 10 0 100 20A10 10 0 0018 8zm0 2c.9 0 2.2 1.6 3 4.5H15c.8-2.9 2.1-4.5 3-4.5zm-5 .8A12 12 0 0011 14H8.5a8.1 8.1 0 014.5-3.2zm10 0A8.1 8.1 0 0127.5 14H25a12 12 0 00-2-3.2zM8.5 16H12c-.1.65-.1 1.3-.1 2s0 1.35.1 2H8.5A8 8 0 018 18a8 8 0 01.5-2zm5.5 0h8c.1.65.1 1.3.1 2s-.1 1.35-.1 2H14c-.1-.65-.1-1.3-.1-2s0-1.35.1-2zm9 0h3.5c.3.64.5 1.3.5 2a8 8 0 01-.5 2H23c.1-.65.1-1.3.1-2s0-1.35-.1-2zM11 22h2.5c.5 1.2 1.2 2.3 2 3.2A8.1 8.1 0 0111 22zm6.5 0h1c-.8 2.9-2.1 4.5-3 4.5s-2.2-1.6-3-4.5h1zm1 0h2.5A8.1 8.1 0 0125 25.2 12 12 0 0122.5 22z" fill="#fff" opacity=".9"/></svg>\',\n'
    ' "Listrik":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#003087"/><path d="M20 9l-8 12h7l-2 8 9-13h-7z" fill="#FFD100"/></svg>\',\n'
    ' "Layanan berbayar":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#1a1a2e"/><path d="M13 11h4l4 7-4 7h-4l4-7z" fill="#a855f7"/><path d="M18 11h5l-5 14h-1l4-7-3-7z" fill="#7c3aed"/></svg>\',\n'
    ' "Pulsa":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#e8002d"/><path d="M18 10a8 8 0 100 16A8 8 0 0018 10zm0 2a6 6 0 110 12 6 6 0 010-12zm0 2.5a3.5 3.5 0 100 7 3.5 3.5 0 000-7z" fill="#fff"/></svg>\'\n'
    '};\n'
    'var PROVLOGO={\n'
    ' "IndiHome":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#e3000f"/><text x="18" y="23" text-anchor="middle" fill="#fff" font-size="6" font-weight="700" font-family="Arial,sans-serif">IndiHome</text></svg>\',\n'
    ' "Biznet":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#003399"/><text x="18" y="24" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700" font-family="Arial,sans-serif">Biznet</text></svg>\',\n'
    ' "MyRepublic":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#ff6600"/><text x="18" y="22" text-anchor="middle" fill="#fff" font-size="5.5" font-weight="700" font-family="Arial,sans-serif">MyRepublic</text></svg>\',\n'
    ' "First Media":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#00539b"/><text x="18" y="23" text-anchor="middle" fill="#fff" font-size="6" font-weight="700" font-family="Arial,sans-serif">First Media</text></svg>\',\n'
    ' "Token PLN":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#003087"/><path d="M20 9l-8 12h7l-2 8 9-13h-7z" fill="#FFD100"/></svg>\',\n'
    ' "Tagihan PLN":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#003087"/><path d="M20 9l-8 12h7l-2 8 9-13h-7z" fill="#FFD100"/></svg>\',\n'
    ' "Netflix":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#141414"/><path d="M12 9h3.5l3 9.5V9H22v18l-3.5-.5-3-9.5V27H12z" fill="#e50914"/></svg>\',\n'
    ' "HBO":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#1c1c1e"/><text x="18" y="25" text-anchor="middle" fill="#fff" font-size="12" font-weight="900" font-family="Arial,sans-serif">HBO</text></svg>\',\n'
    ' "Disney+":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#113ccf"/><text x="18" y="20" text-anchor="middle" fill="#fff" font-size="7.5" font-weight="800" font-family="Arial,sans-serif">Disney</text><text x="23" y="30" text-anchor="middle" fill="#48c9f8" font-size="12" font-weight="900" font-family="Arial,sans-serif">+</text></svg>\',\n'
    ' "Spotify":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#1db954"/><path d="M12 15c3.8-1.2 8-1 11 .8" stroke="#fff" stroke-width="2" stroke-linecap="round"/><path d="M13 19c3.2-1 6.8-.8 9.5.6" stroke="#fff" stroke-width="2" stroke-linecap="round"/><path d="M14 23c2.6-.8 5.6-.6 7.5.4" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>\',\n'
    ' "YouTube Premium":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#ff0000"/><rect x="9" y="12" width="18" height="12" rx="3" fill="#fff"/><path d="M15.5 15.5l7 2.5-7 2.5z" fill="#ff0000"/></svg>\',\n'
    ' "Vidio":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#00aaff"/><text x="18" y="24" text-anchor="middle" fill="#fff" font-size="10" font-weight="700" font-family="Arial,sans-serif">Vidio</text></svg>\',\n'
    ' "Telkomsel":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#e4002b"/><text x="18" y="22" text-anchor="middle" fill="#fff" font-size="5.5" font-weight="700" font-family="Arial,sans-serif">Telkomsel</text></svg>\',\n'
    ' "Indosat":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#ffd700"/><text x="18" y="22" text-anchor="middle" fill="#1a1a1a" font-size="6.5" font-weight="700" font-family="Arial,sans-serif">Indosat</text></svg>\',\n'
    ' "XL":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#0032a0"/><text x="18" y="26" text-anchor="middle" fill="#fff" font-size="15" font-weight="900" font-family="Arial,sans-serif">XL</text></svg>\',\n'
    ' "Tri":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#111"/><text x="18" y="27" text-anchor="middle" fill="#fff" font-size="18" font-weight="900" font-family="Arial,sans-serif">3</text></svg>\',\n'
    ' "Smartfren":\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="#003087"/><text x="18" y="22" text-anchor="middle" fill="#fff" font-size="5.5" font-weight="700" font-family="Arial,sans-serif">Smartfren</text></svg>\'\n'
    '};\n'
    'function _logo(map,key){return map[key]||(\'<svg viewBox="0 0 36 36" width="36" height="36"><rect width="36" height="36" rx="10" fill="var(--panel2)"/><text x="18" y="23" text-anchor="middle" fill="var(--lime)" font-size="14" font-weight="700" font-family="sans-serif">\'+esc(key[0])+\'</text></svg>\')}\n'
    'function drawB(){var h="",c=BC[S.c],p=c&&c.p[S.p];\n'
    ' if(S.st==="cat"){h=bh("Bayar tagihan","x")+\'<div class="bl2">\'+BC.map(function(x,i){return \'<button class="brw" data-b="cat" data-v="\'+i+\'"><span class="ic" style="background:none;padding:0;overflow:hidden;border-radius:10px;width:36px;height:36px">\'+_logo(CATLOGO,x.k)+\'</span><span class="nm">\'+x.k+\'<small>\'+x.d+\'</small></span><span>\'+ik("r")+\'</span></button>\'}).join("")+\'</div>\'}\n'
    ' else if(S.st==="prov"){h=bh(c.k,"bk")+\'<div class="bl2">\'+c.p.map(function(x,i){return \'<button class="brw" data-b="prov" data-v="\'+i+\'"><span class="ic" style="background:none;padding:0;overflow:hidden;border-radius:10px;width:36px;height:36px">\'+_logo(PROVLOGO,x[0])+\'</span><span class="nm">\'+esc(x[0])+\'</span><span>\'+ik("r")+\'</span></button>\'}).join("")+\'</div>\'}'
)

content = content.replace(old_block, new_block)

with open('MEwalletin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Verifying...")
with open('MEwalletin.html', 'r', encoding='utf-8') as f:
    c2 = f.read()
print("CATLOGO present:", 'var CATLOGO' in c2)
print("PROVLOGO present:", 'var PROVLOGO' in c2)
print("_logo present:", 'function _logo' in c2)
