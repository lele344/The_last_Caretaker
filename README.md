# 🌍 Translation Editor Pro v2.0

> **Editor professionale per gestire traduzioni CSV con interfaccia moderna e sistema di merge multi-stage**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## 📋 Indice

- [Caratteristiche](#-caratteristiche)
- [Screenshots](#-screenshots)
- [Installazione](#-installazione)
- [Utilizzo](#-utilizzo)
- [Workflow Tipico](#-workflow-tipico)
- [Funzionalità Avanzate](#-funzionalità-avanzate)
- [Struttura Progetto](#-struttura-progetto)
- [FAQ](#-faq)
- [Contribuire](#-contribuire)
- [Licenza](#-licenza)

## ✨ Caratteristiche

### 🎨 Interfaccia Moderna
- **Pulsanti arrotondati** con effetto hover e ombreggiature
- **Tema scuro/chiaro** switchable
- **Design responsive** con layout professionale
- **Colori vivaci** per stati delle traduzioni
- **Font moderni** (Segoe UI, Consolas)

### 🌍 Multi-lingua
- **3 lingue supportate**: 🇬🇧 Inglese | 🇮🇹 Italiano | 🇷🇺 Russo
- **Switch istantaneo** - cambia lingua senza riavviare
- Tutti i testi UI tradotti dinamicamente

### 📊 Visualizzazione Avanzata
- **Tabella interattiva** con colonne ridimensionabili
- **Codifica a colori**:
  - 🟢 **Verde**: Traduzioni aggiunte
  - 🔴 **Rosso**: Traduzioni rimosse
  - 🟡 **Giallo**: Traduzioni modificate
  - ⚪ **Grigio**: Traduzioni mantenute
- **Scrolling orizzontale/verticale** per grandi dataset
- **Truncamento intelligente** del testo lungo

### 🔄 Sistema di Merge Potente
- **Merge multi-stage**: aggiungi più file prima di salvare
- **Logica intelligente**:
  - `KEY + SOURCE` match → aggiorna traduzione
  - `KEY` match ma `SOURCE` diverso → svuota traduzione
  - `KEY` non presente → mantieni originale
- **Tracciamento modifiche** in tempo reale
- **Sistema Undo/Redo** per annullare operazioni

### 🔍 Ricerca e Filtri
- **Ricerca real-time** su key, source e translation
- **Filtri rapidi** per stato (aggiunte/rimosse/modificate/tutte)
- **Statistiche live** con conteggi aggiornati

### 🛡️ Sicurezza Dati
- **Rilevamento duplicati** automatico (KEY+SOURCE)
- **Validazione CSV** completa
- **Backup automatico** tramite history
- **Encoding UTF-8** per caratteri speciali

## 📸 Screenshots

### Interfaccia Principale (Dark Theme)
```
┌─────────────────────────────────────────────────────────────────────┐
│  📄 File Base          │  🔍 Search: [________]  🟢🔴🟡⚪              │
│  ✓ nuovo.csv           │  ┌──────────────────────────────────────┐  │
│  [📂 Carica File Base] │  │ Status│Key│Source│Translation         │  │
│                        │  ├──────────────────────────────────────┤  │
│  📚 Stage Merge        │  │ 🟢 added │key1│Hello│Ciao            │  │
│  ┌──────────────────┐  │  │ 🟡 modified│key2│World│Mondo       │  │
│  │Stage 1: trans.csv│  │  │ ⚪ kept │key3│Test│Test             │  │
│  └──────────────────┘  │  └──────────────────────────────────────┘  │
│  [➕ Aggiungi]         │  📊 Total: 3373 | 🟢 481 | 🔴 12 | 🟡 89   │
│  [🔄 Esegui Merge]     │                                             │
│  [↩️ Annulla]          │                                             │
│  [🗑️ Pulisci]          │                                             │
│                        │                                             │
│  [💾 SALVA OUTPUT]     │                                             │
└─────────────────────────────────────────────────────────────────────┘
```

## 🚀 Installazione

### Prerequisiti
- Python 3.8 o superiore
- tkinter (incluso in Python standard)

### Installazione Rapida

```bash
# Clona repository
git clone https://github.com/tuousername/translation-editor-pro.git
cd translation-editor-pro

# Nessuna dipendenza esterna necessaria!
# tkinter è incluso in Python
```

### Verifica Installazione

```bash
python -c "import tkinter; print('✓ tkinter OK')"
```

Se vedi `✓ tkinter OK`, sei pronto!

## 💡 Utilizzo

### Avvio Rapido

```bash
cd "estrazione dal tedesco"
python translation_editor_pro.py
```

### Workflow Tipico

#### 1️⃣ **Carica File Base**
```
File → Carica File Base → seleziona nuovo.csv
```
Il file base contiene tutte le chiavi di traduzione del gioco.

#### 2️⃣ **Aggiungi Traduzioni**
```
➕ Aggiungi Traduzione → seleziona Game_locres__MANCANTI.csv
```
Puoi aggiungere multipli file in stage separati.

#### 3️⃣ **Esegui Merge**
```
🔄 Esegui Merge
```
Vedi immediatamente i cambiamenti colorati nella tabella!

#### 4️⃣ **Salva Output**
```
💾 SALVA OUTPUT → scegli destinazione
```
Il file finale contiene tutte le traduzioni unite.

### Shortcut Utili

| Azione | Shortcut Menu |
|--------|---------------|
| Carica base | `File → Carica File Base` |
| Aggiungi traduzione | `File → Aggiungi Traduzione` |
| Salva | `File → Salva Output` |
| Cambia tema | `Vista → Cambia Tema` |
| Cambia lingua | `Lingua → 🇬🇧/🇮🇹/🇷🇺` |

## 🎯 Funzionalità Avanzate

### Sistema di Staging

Aggiungi **multipli file** prima di salvare:

```python
Stage 1: traduzioni_parziali.csv
Stage 2: correzioni.csv
Stage 3: nuove_voci.csv
```

Quando clicchi **🔄 Esegui Merge**, tutti vengono applicati in sequenza.

### Logica di Merge

```
Per ogni riga nel file base:
  
  SE (KEY + SOURCE) trovato nel file traduzione:
    → Aggiorna traduzione
    → Colora riga (verde/giallo/rosso)
  
  ALTRIMENTI:
    → Mantieni originale
    → Colora grigio
```

### Rilevamento Duplicati

Se il file contiene duplicati `KEY+SOURCE`, ricevi un warning:

```
⚠️ Duplicati Trovati
Trovati 5 duplicati.
Controlla nella tabella.
```

### Storia Modifiche

Ogni merge viene salvato in history:

```
↩️ Undo → torna allo stato precedente
```

Stack illimitato fino alla chiusura dell'app.

## 📁 Struttura Progetto

```
PakTest/
├── estrazione dal tedesco/
│   ├── translation_editor_pro.py    # ⭐ Editor principale
│   ├── Game.locres.csv               # File base originale
│   ├── nuovo.csv                     # File base pulito
│   └── Game_locres__MANCANTI.csv     # Traduzioni parziali
│
├── repak/                            # Tool per PAK files
│   └── repak.exe
│
├── repak_replace.py                  # Script inserimento in PAK
├── check_translations.py             # Analizzatore qualità
└── README.md                         # 📖 Questa guida
```

### File Chiave

| File | Descrizione |
|------|-------------|
| `translation_editor_pro.py` | Editor grafico principale |
| `repak_replace.py` | Inserisce locres nel PAK |
| `check_translations.py` | Verifica qualità traduzioni |
| `nuovo.csv` | File base con tutte le chiavi |

## 🔧 Integrazione con Altri Script

### 1. Verifica Qualità Traduzioni

```bash
python check_translations.py
```

Output:
```
📊 Analisi Traduzioni
━━━━━━━━━━━━━━━━━━━━━
✗ Traduzioni mancanti: 2492
✗ Errori tag: 4
✗ Problemi placeholder: 209
```

### 2. Inserisci nel PAK

```bash
python repak_replace.py
```

Workflow automatico:
1. Trova gioco via Steam
2. Estrae PAK originale
3. Sostituisce Game.locres
4. Ricrea PAK
5. Installa nel gioco

## ❓ FAQ

### Q: Che formato CSV supporta?
**A:** Standard CSV con header: `key,source,Translation`

### Q: Posso usarlo con altri giochi?
**A:** Sì! Funziona con qualsiasi CSV chiave-testo-traduzione.

### Q: Come gestisce i caratteri speciali?
**A:** UTF-8 encoding completo, supporta emoji, cirillico, caratteri accentati.

### Q: Posso annullare un merge?
**A:** Sì, usa il pulsante **↩️ Annulla** o ricarica il file base.

### Q: Perché il tema scuro?
**A:** Riduce affaticamento oculare. Usa `Vista → Cambia Tema` per tema chiaro.

### Q: Quante lingue posso aggiungere?
**A:** Modifica il dizionario `TRANSLATIONS` nel codice per aggiungere altre lingue.

## 🐛 Risoluzione Problemi

### Errore: "No module named 'tkinter'"

**Windows:**
```bash
# Reinstalla Python con opzione "tcl/tk"
```

**Linux:**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

### Errore: "Failed to load CSV"

Verifica che il CSV abbia:
- Header: `key,source,Translation`
- Encoding: UTF-8
- Formato valido (nessuna virgola non escaped)

### Performance lente con file grandi

Per file con >10,000 righe:
- Usa filtri per ridurre visualizzazione
- Cerca per testo specifico
- Considera di dividere in più file

## 🤝 Contribuire

Contributi benvenuti! 

### Come Contribuire

1. **Fork** il repository
2. **Crea branch** per la tua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** le modifiche (`git commit -m 'Add AmazingFeature'`)
4. **Push** al branch (`git push origin feature/AmazingFeature`)
5. Apri una **Pull Request**

### Idee per Contributi

- [ ] Export in formati aggiuntivi (JSON, XLSX)
- [ ] Modifica inline delle celle
- [ ] Grafici statistiche
- [ ] Plugin system
- [ ] API REST per integrazione
- [ ] Supporto Git per versioning

## 📝 Changelog

### v2.0.0 - 2025-11-10
- ✨ UI completamente rinnovata con pulsanti moderni
- ✨ Bordi arrotondati e effetti hover
- ✨ Multi-lingua completo (EN/IT/RU)
- ✨ Sistema di staging migliorato
- 🐛 Fix errore reload dopo merge

### v1.0.0 - 2025-11-09
- 🎉 Release iniziale
- ✅ Merge multi-stage
- ✅ Tracciamento modifiche
- ✅ Rilevamento duplicati

## 📄 Licenza

Distribuito sotto licenza MIT. Vedi `LICENSE` per maggiori informazioni.

## 👤 Autore

**Translation Editor Pro** - Sviluppato per gestire traduzioni mod di giochi Unreal Engine

---

## 🌟 Credits

- **tkinter** - GUI framework
- **Python CSV** - Parsing CSV
- **Unreal Engine** - Formato .locres

---

<div align="center">

**⭐ Se questo progetto ti è utile, lascia una stella! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/tuousername/translation-editor-pro?style=social)](https://github.com/tuousername/translation-editor-pro/stargazers)

</div>

---

## 🔗 Link Utili

- [Documentazione Completa](docs/)
- [Video Tutorial](https://youtube.com/...)
- [Report Bug](https://github.com/tuousername/translation-editor-pro/issues)
- [Richiedi Feature](https://github.com/tuousername/translation-editor-pro/issues/new?labels=enhancement)

---

**Versione:** 2.0.0 | **Ultimo aggiornamento:** 10 Novembre 2025
