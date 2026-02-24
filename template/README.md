# 📊 Trading Command Center – Template

Ein persönliches Trading Dashboard als einzelne HTML-Datei. Kostenlos auf GitHub Pages hostbar, keine Server nötig.

## ✨ Features

- **Morning Briefing** mit Uhrzeit, Datum und Wochentag-Hinweisen
- **Live Markt-Status** (NYSE offen / Pre-Market / After-Hours / geschlossen)
- **Hell/Dunkel-Modus** mit automatischer Speicherung
- **Persönliche Watchlist** – Symbole hinzufügen, Klick öffnet TradingView Chart
- **Tagesnotizen** – werden automatisch im Browser gespeichert
- **Manus KI-Skills** – 8 vorkonfigurierte KI-Analyse-Buttons
- **Responsive Design** – funktioniert auf Desktop und Tablet

## 🚀 In 5 Minuten zum eigenen Dashboard

### Schritt 1: Template herunterladen
Lade die Datei `index.html` herunter.

### Schritt 2: Anpassen
Öffne die Datei in einem Texteditor (z.B. Notepad, VS Code) und ersetze:

| Suchen | Ersetzen durch |
|---|---|
| `DEIN_NAME` | Deinen Namen oder Handle |
| `DEINE_URL` | Deine eigenen Links |

### Schritt 3: Auf GitHub Pages hosten (kostenlos)

1. Gehe zu [github.com](https://github.com) und erstelle ein kostenloses Konto
2. Erstelle ein neues Repository: `trading-dashboard`
3. Lade die `index.html` hoch
4. Gehe zu **Settings → Pages → Source: main branch**
5. Dein Dashboard ist live unter: `https://DEIN_GITHUB_NAME.github.io/trading-dashboard/`

### Alternativ: Lokal öffnen
Doppelklick auf die `index.html` – fertig. Kein Server nötig.

## 🎨 Kacheln anpassen

### Neue Kachel hinzufügen
Kopiere diesen Block und passe ihn an:

```html
<a href="DEINE_URL" target="_blank" class="card hl-blue">
  <div class="card-top">
    <span class="card-icon">📊</span>
    <span class="card-tag tag-tool">Tool</span>
  </div>
  <div class="card-title">Name des Tools</div>
  <div class="card-desc">Kurze Beschreibung was dieses Tool macht.</div>
  <div class="card-footer">
    <span class="card-url">url.com</span>
    <span class="card-arrow">→</span>
  </div>
</a>
```

### Farben für Kacheln (`class="card hl-XXX"`)

| Klasse | Farbe | Verwendung |
|---|---|---|
| `hl-blue` | Blau | Allgemeine Tools |
| `hl-green` | Grün | Eigene Tools, Live-Daten |
| `hl-orange` | Orange | Wichtige Tools, DWHI |
| `hl-purple` | Lila | Manus Skills, Premium |
| `hl-red` | Rot | Warnsignale, Risiko |
| `hl-teal` | Türkis | Makro, Futures |
| `hl-yellow` | Gelb | News, Research |

### Tags für Kacheln (`class="card-tag tag-XXX"`)

| Klasse | Label | Farbe |
|---|---|---|
| `tag-tool` | Tool | Blau |
| `tag-news` | News | Grün |
| `tag-premium` | Premium | Gelb |
| `tag-live` | Live Tool | Grün |
| `tag-manus` | Manus Skill | Lila |

## 🤖 Manus Skills nutzen

Die vorkonfigurierten Skill-Buttons öffnen [manus.im](https://manus.im) direkt mit dem passenden Prompt. Du brauchst ein Manus-Konto.

Verfügbare Skills:
- COT Analyse
- Investment Thesen Finder
- ETF Momentum Analyse
- Makro Zyklusanalyse
- Optionsexperte
- Sektor Rotation Detector
- Risikomanager
- Investment Entscheider

## 📝 Neue Sektion hinzufügen

```html
<section id="meine-sektion" class="section">
  <div class="section-header">
    <span class="section-icon">🔍</span>
    <span class="section-title">Mein Bereich</span>
    <span class="section-badge">Beschreibung</span>
  </div>
  <div class="card-grid">
    <!-- Kacheln hier einfügen -->
  </div>
</section>
```

Und den Nav-Link ergänzen:
```html
<a href="#meine-sektion">🔍 Mein Bereich</a>
```

## 💡 Tipps

- **Bookmarks**: Speichere die URL als Startseite in deinem Browser
- **Watchlist**: Symbole werden dauerhaft im Browser gespeichert
- **Notizen**: Werden täglich gespeichert – der Vortag bleibt erhalten
- **Dark Mode**: Einstellung wird gespeichert und beim nächsten Öffnen beibehalten

## 🙏 Credits

Template erstellt von [thblees / meine-geldseite.de](https://www.meine-geldseite.de)  
Manus KI Skills: [manus.im](https://manus.im)
