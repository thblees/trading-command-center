# Einmal-Patch: fuegt die RSI-Divergenz-Screener-Kachel als erste Kachel
# in beide "Eigene Tools & Dashboards"-Sektionen der index.html ein.
src = open("index.html", encoding="utf-8").read()

if "divergenz-screener" in src:
    print("Kachel schon vorhanden - nichts zu tun")
else:
    anchor = '<a href="http://www.meine-geldseite.de/momentum" target="_blank" class="card hl-green">'
    tile = '''<a href="https://thblees.github.io/divergenz-screener/" target="_blank" class="card hl-teal">
        <div class="card-top"><span class="card-icon">\U0001F4C8</span><span class="card-tag tag-live">Live Tool</span></div>
        <div class="card-title">RSI-Divergenz-Screener S&amp;P 500</div>
        <div class="card-desc">Scannt täglich nach US-Börsenschluss alle S&amp;P-500-Aktien auf bullische RSI-Divergenzen (regulär und versteckt, Tageschart). Frühsignale noch am selben Abend, Bestätigung am Folgetag.</div>
        <div class="card-footer"><span class="card-url">thblees.github.io/divergenz-screener</span><span class="card-arrow">→</span></div>
      </a>

      '''
    n = src.count(anchor)
    assert n == 2, f"Anker {n}x gefunden, erwartet 2"
    src = src.replace(anchor, tile + anchor)
    open("index.html", "w", encoding="utf-8").write(src)
    print("Kachel an 2 Stellen eingefuegt")
