# 🌍 Translation Editor Pro v2.0

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](#)

> 🇮🇹 **[Italiano](#-italiano)** | 🇬🇧 **[English](#-english)** | 🇷🇺 **[Русский](#-русский)**

---

## 🇮🇹 Italiano

### 📖 Descrizione

**Translation Editor Pro** è un editor grafico professionale per gestire file CSV di traduzioni con interfaccia moderna, pulsanti arrotondati e sistema di merge multi-stage.

### ✨ Caratteristiche Principali

- 🎨 **UI Moderna**: Pulsanti arrotondati con effetto hover, gradienti e ombreggiature
- 🌍 **Multi-lingua**: Supporto completo per Inglese, Italiano e Russo
- 📊 **Visualizzazione a Colori**: 🟢 Aggiunte | 🔴 Rimosse | 🟡 Modificate | ⚪ Mantenute
- 🔄 **Merge Multi-Stage**: Aggiungi più file prima di salvare
- 🔍 **Ricerca e Filtri**: Trova rapidamente le traduzioni
- ↩️ **Undo/Redo**: Annulla operazioni con history illimitato
- 🌓 **Tema Scuro/Chiaro**: Proteggi i tuoi occhi

### 🚀 Avvio Rapido

```bash
python translation_merger.py
```

### 📋 Workflow

1. **Carica File Base** (`File → Carica File Base`)
   - Seleziona il CSV con tutte le chiavi (es. `nuovo.csv`)

2. **Aggiungi Traduzioni** (`➕ Aggiungi Traduzione`)
   - Aggiungi uno o più file con traduzioni parziali
   - Ogni file diventa uno "stage"

3. **Esegui Merge** (`🔄 Esegui Merge`)
   - Unisce tutti gli stage in sequenza
   - Vedi i cambiamenti colorati in tempo reale

4. **Salva Output** (`💾 SALVA OUTPUT`)
   - Salva il risultato finale

### 🎯 Logica di Merge

```
Per ogni riga del file base:
  
  SE esiste KEY + SOURCE nel file traduzione:
    → Aggiorna Translation
    → Colora: 🟢 se aggiunta, 🟡 se modificata, 🔴 se rimossa
  
  ALTRIMENTI:
    → Mantieni Translation originale
    → Colora: ⚪ mantenuta
```

### 📁 Formato CSV

Il file CSV deve avere questa struttura:

```csv
key,source,Translation
MENU_START,Start Game,Inizia Partita
MENU_EXIT,Exit,Esci
```

### 🔧 Requisiti

- **Python**: 3.8 o superiore
- **tkinter**: Incluso in Python (nessuna installazione necessaria)

### 🌓 Cambio Tema

`Vista → Cambia Tema` per passare da scuro a chiaro.

### 🌍 Cambio Lingua

`Lingua → 🇬🇧 English / 🇮🇹 Italiano / 🇷🇺 Русский`

Tutti i testi dell'interfaccia cambiano istantaneamente!

### ❓ FAQ

**Q: Posso usarlo per altri giochi?**  
A: Sì! Funziona con qualsiasi CSV key-source-translation.

**Q: Come annullo un merge?**  
A: Usa il pulsante `↩️ Annulla` o ricarica il file base.

**Q: Supporta caratteri speciali?**  
A: Sì, encoding UTF-8 completo (emoji, cirillico, accentate).

**Q: Quanti file posso unire?**  
A: Illimitati! Aggiungi tutti gli stage che vuoi.

### 🐛 Problemi Comuni

**Errore: "No module named 'tkinter'"**

```bash
# Windows: Reinstalla Python con "tcl/tk"
# Linux: sudo apt-get install python3-tk
# macOS: brew install python-tk
```

**Errore: "Failed to load CSV"**

Verifica:
- Header: `key,source,Translation`
- Encoding: UTF-8
- Nessuna virgola non escaped

### 📜 Licenza

MIT License - Usa, modifica e distribuisci liberamente!

---

---

## 🇬🇧 English

### 📖 Description

**Translation Editor Pro** is a professional graphical editor for managing CSV translation files with modern interface, rounded buttons, and multi-stage merge system.

### ✨ Key Features

- 🎨 **Modern UI**: Rounded buttons with hover effects, gradients, and shadows
- 🌍 **Multi-language**: Full support for English, Italian, and Russian
- 📊 **Color-coded View**: 🟢 Added | 🔴 Removed | 🟡 Modified | ⚪ Kept
- 🔄 **Multi-Stage Merge**: Add multiple files before saving
- 🔍 **Search & Filters**: Quickly find translations
- ↩️ **Undo/Redo**: Revert operations with unlimited history
- 🌓 **Dark/Light Theme**: Protect your eyes

### 🚀 Quick Start

```bash
python translation_merger.py
```

### 📋 Workflow

1. **Load Base File** (`File → Load Base File`)
   - Select the CSV with all keys (e.g., `nuovo.csv`)

2. **Add Translations** (`➕ Add Translation`)
   - Add one or more files with partial translations
   - Each file becomes a "stage"

3. **Execute Merge** (`🔄 Execute Merge`)
   - Merges all stages in sequence
   - See color-coded changes in real-time

4. **Save Output** (`💾 SAVE OUTPUT`)
   - Save the final result

### � Merge Logic

```
For each row in base file:
  
  IF KEY + SOURCE exists in translation file:
    → Update Translation
    → Color: 🟢 if added, 🟡 if modified, 🔴 if removed
  
  ELSE:
    → Keep original Translation
    → Color: ⚪ kept
```

### 📁 CSV Format

The CSV file must have this structure:

```csv
key,source,Translation
MENU_START,Start Game,Start Game
MENU_EXIT,Exit,Exit
```

### 🔧 Requirements

- **Python**: 3.8 or higher
- **tkinter**: Included in Python (no installation needed)

### 🌓 Theme Toggle

`View → Toggle Theme` to switch between dark and light.

### 🌍 Language Switch

`Language → 🇬🇧 English / 🇮🇹 Italiano / 🇷🇺 Русский`

All interface texts change instantly!

### ❓ FAQ

**Q: Can I use it for other games?**  
A: Yes! Works with any key-source-translation CSV.

**Q: How to undo a merge?**  
A: Use the `↩️ Undo` button or reload the base file.

**Q: Does it support special characters?**  
A: Yes, full UTF-8 encoding (emoji, Cyrillic, accented).

**Q: How many files can I merge?**  
A: Unlimited! Add as many stages as you want.

### 🐛 Common Issues

**Error: "No module named 'tkinter'"**

```bash
# Windows: Reinstall Python with "tcl/tk"
# Linux: sudo apt-get install python3-tk
# macOS: brew install python-tk
```

**Error: "Failed to load CSV"**

Check:
- Header: `key,source,Translation`
- Encoding: UTF-8
- No unescaped commas

### 📜 License

MIT License - Use, modify, and distribute freely!

---
---

## 🇺 Русский

### � Описание

**Translation Editor Pro** — профессиональный графический редактор для управления CSV-файлами переводов с современным интерфейсом, закругленными кнопками и системой многоэтапного слияния.

### ✨ Основные возможности

- 🎨 **Современный UI**: Закругленные кнопки с эффектами наведения, градиентами и тенями
- 🌍 **Мультиязычность**: Полная поддержка английского, итальянского и русского
- 📊 **Цветовая кодировка**: 🟢 Добавлено | 🔴 Удалено | 🟡 Изменено | ⚪ Сохранено
- 🔄 **Многоэтапное слияние**: Добавляйте несколько файлов перед сохранением
- 🔍 **Поиск и фильтры**: Быстро находите переводы
- ↩️ **Отмена/Повтор**: Отменяйте операции с неограниченной историей
- 🌓 **Темная/Светлая тема**: Берегите глаза

### � Быстрый старт

```bash
python translation_merger.py
```

### 📋 Рабочий процесс

1. **Загрузить базовый файл** (`Файл → Загрузить базу`)
   - Выберите CSV со всеми ключами (например, `nuovo.csv`)

2. **Добавить переводы** (`➕ Добавить перевод`)
   - Добавьте один или несколько файлов с частичными переводами
   - Каждый файл становится "этапом"

3. **Выполнить слияние** (`🔄 Объединить`)
   - Объединяет все этапы последовательно
   - Видите изменения с цветовой кодировкой в реальном времени

4. **Сохранить результат** (`💾 СОХРАНИТЬ`)
   - Сохраните финальный результат

### 🎯 Логика слияния

```
Для каждой строки в базовом файле:
  
  ЕСЛИ KEY + SOURCE существует в файле перевода:
    → Обновить Translation
    → Цвет: 🟢 если добавлено, 🟡 если изменено, 🔴 если удалено
  
  ИНАЧЕ:
    → Сохранить оригинальный Translation
    → Цвет: ⚪ сохранено
```

### 📁 Формат CSV

CSV-файл должен иметь такую структуру:

```csv
key,source,Translation
MENU_START,Start Game,Начать игру
MENU_EXIT,Exit,Выход
```

### 🔧 Требования

- **Python**: 3.8 или выше
- **tkinter**: Включен в Python (установка не требуется)

### 🌓 Смена темы

`Вид → Сменить тему` для переключения между темной и светлой.

### 🌍 Смена языка

`Язык → 🇬🇧 English / 🇮🇹 Italiano / 🇷🇺 Русский`

Все тексты интерфейса меняются мгновенно!

### ❓ Часто задаваемые вопросы

**В: Можно ли использовать для других игр?**  
О: Да! Работает с любым CSV формата key-source-translation.

**В: Как отменить слияние?**  
О: Используйте кнопку `↩️ Отменить` или перезагрузите базовый файл.

**В: Поддерживаются ли специальные символы?**  
О: Да, полная поддержка UTF-8 (эмодзи, кириллица, акценты).

**В: Сколько файлов можно объединить?**  
О: Неограниченно! Добавляйте столько этапов, сколько нужно.

### 🐛 Распространенные проблемы

**Ошибка: "No module named 'tkinter'"**

```bash
# Windows: Переустановите Python с опцией "tcl/tk"
# Linux: sudo apt-get install python3-tk
# macOS: brew install python-tk
```

**Ошибка: "Failed to load CSV"**

Проверьте:
- Заголовок: `key,source,Translation`
- Кодировка: UTF-8
- Нет неэкранированных запятых

### 📜 Лицензия

Лицензия MIT — используйте, изменяйте и распространяйте свободно!

---

<div align="center">

**Made with ❤️ for translators and modders**

**Версия / Version / Versione:** 2.0.0 | **Дата / Date / Data:** 10 ноября / November / novembre 2025

</div>

