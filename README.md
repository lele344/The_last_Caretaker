# Translation Merger Tool 🌍

[English](#english) | [Italiano](#italiano) | [Русский](#русский)

---

## English

### Description
**Translation Merger Tool** is a Python application with a graphical interface designed to merge existing translations with new CSV localization files from games.

### Features
- ✅ **Multi-file support**: Combine multiple partial translation files
- 🔍 **Smart comparison**: Compares KEY and SOURCE to identify existing translations
- 📊 **Detailed statistics**: Shows translated, untranslated, and modified entries
- 🌍 **Multilingual interface**: English, Italian, and Russian
- 🎯 **Change detection**: Identifies when source text has been modified

### How to Use

1. **Launch the script**:
   ```bash
   python translation_merger.py
   ```

2. **Select language**: Choose your preferred interface language (EN/IT/RU) from the dropdown menu

3. **Select source file**: Click "Select File" and choose the English CSV file (e.g., `Game.locres.csv`)

4. **Add translation files**: Click "Add File" and select one or more translation CSV files (e.g., `Game.locres_italiano.csv`)

5. **Choose output** (optional): By default, the output file will be named `[source_file]_merged.csv`

6. **Execute merge**: Click "EXECUTE MERGE" and wait for completion

### Result Interpretation

The tool identifies three types of entries:

- **✓ Translated**: KEY exists and SOURCE matches → translation applied
- **✗ Not translated**: KEY not found → needs translation
- **⚠ Source modified**: KEY exists but SOURCE changed → requires manual review

### Requirements
- Python 3.7+
- tkinter (usually included with Python)

---

## Italiano

### Descrizione
**Translation Merger Tool** è un'applicazione Python con interfaccia grafica progettata per unire traduzioni esistenti con nuovi file CSV di localizzazione da giochi.

### Caratteristiche
- ✅ **Supporto multi-file**: Combina più file di traduzione parziali
- 🔍 **Confronto intelligente**: Compara KEY e SOURCE per identificare traduzioni esistenti
- 📊 **Statistiche dettagliate**: Mostra voci tradotte, non tradotte e modificate
- 🌍 **Interfaccia multilingua**: Inglese, Italiano e Russo
- 🎯 **Rilevamento modifiche**: Identifica quando il testo sorgente è stato modificato

### Come Usarlo

1. **Avvia lo script**:
   ```bash
   python translation_merger.py
   ```

2. **Seleziona lingua**: Scegli la lingua dell'interfaccia (EN/IT/RU) dal menu a tendina

3. **Seleziona file sorgente**: Clicca "Seleziona File" e scegli il file CSV inglese (es. `Game.locres.csv`)

4. **Aggiungi file traduzioni**: Clicca "Aggiungi File" e seleziona uno o più file CSV di traduzione (es. `Game.locres_italiano.csv`)

5. **Scegli output** (opzionale): Di default, il file di output sarà chiamato `[file_sorgente]_merged.csv`

6. **Esegui merge**: Clicca "ESEGUI MERGE" e attendi il completamento

### Interpretazione Risultati

Lo strumento identifica tre tipi di voci:

- **✓ Tradotta**: KEY esiste e SOURCE corrisponde → traduzione applicata
- **✗ Non tradotta**: KEY non trovata → richiede traduzione
- **⚠ Source modificato**: KEY esiste ma SOURCE cambiato → richiede revisione manuale

### Requisiti
- Python 3.7+
- tkinter (solitamente incluso con Python)

---

## Русский

### Описание
**Translation Merger Tool** — это приложение Python с графическим интерфейсом, предназначенное для объединения существующих переводов с новыми CSV-файлами локализации из игр.

### Возможности
- ✅ **Поддержка нескольких файлов**: Объединяет несколько частичных файлов переводов
- 🔍 **Интеллектуальное сравнение**: Сравнивает KEY и SOURCE для определения существующих переводов
- 📊 **Подробная статистика**: Показывает переведённые, непереведённые и изменённые записи
- 🌍 **Многоязычный интерфейс**: Английский, Итальянский и Русский
- 🎯 **Обнаружение изменений**: Определяет, когда исходный текст был изменён

### Как Использовать

1. **Запустите скрипт**:
   ```bash
   python translation_merger.py
   ```

2. **Выберите язык**: Выберите предпочитаемый язык интерфейса (EN/IT/RU) из выпадающего меню

3. **Выберите исходный файл**: Нажмите "Выбрать файл" и выберите английский CSV-файл (напр. `Game.locres.csv`)

4. **Добавьте файлы переводов**: Нажмите "Добавить файл" и выберите один или несколько CSV-файлов переводов (напр. `Game.locres_italiano.csv`)

5. **Выберите выход** (необязательно): По умолчанию выходной файл будет называться `[исходный_файл]_merged.csv`

6. **Выполните слияние**: Нажмите "ВЫПОЛНИТЬ СЛИЯНИЕ" и дождитесь завершения

### Интерпретация Результатов

Инструмент определяет три типа записей:

- **✓ Переведено**: KEY существует и SOURCE совпадает → перевод применён
- **✗ Не переведено**: KEY не найден → требуется перевод
- **⚠ Источник изменён**: KEY существует, но SOURCE изменён → требуется ручная проверка

### Требования
- Python 3.7+
- tkinter (обычно включён в Python)

---

## License / Licenza / Лицензия

MIT License - Free to use and modify

---

## Support / Supporto / Поддержка

For issues or questions, please create an issue in the repository.

Per problemi o domande, crea un issue nel repository.

Для вопросов или проблем создайте issue в репозитории.
