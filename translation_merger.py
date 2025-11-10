#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translation Merger Tool
-----------------------
Strumento per unire traduzioni esistenti con nuovi file CSV di localizzazione.
Confronta KEY e SOURCE per identificare traduzioni esistenti da mantenere
e righe modificate o non tradotte.
"""

import csv
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from typing import Dict, List, Tuple
import threading


# ==================== LOCALIZATIONS ====================
TRANSLATIONS = {
    'en': {
        'title': 'Translation Merger Tool',
        'description': 'Select the source CSV file (English) and one or more files with translations.\nThe script will compare KEY and SOURCE to merge existing translations.',
        'source_file': 'Source File (EN):',
        'no_file': 'No file selected',
        'select_file': 'Select File',
        'translation_files': 'Translation Files:',
        'add_file': 'Add File',
        'remove_selected': 'Remove Selected',
        'remove_all': 'Remove All',
        'output_file': 'Output File:',
        'auto_generated': 'Will be generated automatically',
        'choose_output': 'Choose Output',
        'execute_merge': 'EXECUTE MERGE',
        'results': 'Results:',
        'error': 'Error',
        'select_source_error': 'Select the source file!',
        'select_translation_error': 'Add at least one translation file!',
        'success': 'Success',
        'merge_completed': 'Merge completed!',
        'translated': 'Translated',
        'file_saved': 'File saved',
        'select_source_title': 'Select Source File (EN)',
        'select_translation_title': 'Select Translation File',
        'select_output_title': 'Select Output File',
        'loading_source': 'Loading source file...',
        'loading_translations': 'Loading translations',
        'processing': 'Processing',
        'completed': 'Completed!',
        'merge_completed_header': 'MERGE COMPLETED!',
        'output_file_label': 'Output File:',
        'statistics': 'STATISTICS:',
        'total_rows': 'Total rows:',
        'translated_check': 'Translated (✓):',
        'not_translated': 'Not translated (✗):',
        'source_modified': 'Source modified (⚠):',
        'legend': 'LEGEND:',
        'legend_translated': 'Existing translation applied (KEY and SOURCE match)',
        'legend_not_translated': 'No translation found (needs translation)',
        'legend_modified': 'SOURCE modified compared to existing translation\n      (requires manual verification/update)',
        'file_saved_success': 'The file has been saved successfully!\n   You can open it to verify and complete missing translations.',
        'language': 'Language:',
    },
    'it': {
        'title': 'Translation Merger Tool',
        'description': 'Seleziona il file CSV sorgente (inglese) e uno o più file con traduzioni.\nLo script confronterà KEY e SOURCE per unire le traduzioni esistenti.',
        'source_file': 'File Sorgente (EN):',
        'no_file': 'Nessun file selezionato',
        'select_file': 'Seleziona File',
        'translation_files': 'File Traduzioni:',
        'add_file': 'Aggiungi File',
        'remove_selected': 'Rimuovi Selezionato',
        'remove_all': 'Rimuovi Tutti',
        'output_file': 'File Output:',
        'auto_generated': 'Verrà generato automaticamente',
        'choose_output': 'Scegli Output',
        'execute_merge': 'ESEGUI MERGE',
        'results': 'Risultati:',
        'error': 'Errore',
        'select_source_error': 'Seleziona il file sorgente!',
        'select_translation_error': 'Aggiungi almeno un file di traduzione!',
        'success': 'Successo',
        'merge_completed': 'Merge completato!',
        'translated': 'Tradotte',
        'file_saved': 'File salvato',
        'select_source_title': 'Seleziona File Sorgente (EN)',
        'select_translation_title': 'Seleziona File Traduzione',
        'select_output_title': 'Seleziona File Output',
        'loading_source': 'Caricamento file sorgente...',
        'loading_translations': 'Caricamento traduzioni',
        'processing': 'Processamento',
        'completed': 'Completato!',
        'merge_completed_header': 'MERGE COMPLETATO!',
        'output_file_label': 'File Output:',
        'statistics': 'STATISTICHE:',
        'total_rows': 'Totale righe:',
        'translated_check': 'Tradotte (✓):',
        'not_translated': 'Non tradotte (✗):',
        'source_modified': 'Source modificato (⚠):',
        'legend': 'LEGENDA:',
        'legend_translated': 'Traduzione esistente applicata (KEY e SOURCE corrispondono)',
        'legend_not_translated': 'Nessuna traduzione trovata (riga da tradurre)',
        'legend_modified': 'SOURCE modificato rispetto alla traduzione esistente\n      (richiede verifica/aggiornamento manuale)',
        'file_saved_success': 'Il file è stato salvato con successo!\n   Puoi aprirlo per verificare e completare le traduzioni mancanti.',
        'language': 'Lingua:',
    },
    'ru': {
        'title': 'Инструмент слияния переводов',
        'description': 'Выберите исходный CSV-файл (английский) и один или несколько файлов с переводами.\nСкрипт сравнит KEY и SOURCE для объединения существующих переводов.',
        'source_file': 'Исходный файл (EN):',
        'no_file': 'Файл не выбран',
        'select_file': 'Выбрать файл',
        'translation_files': 'Файлы переводов:',
        'add_file': 'Добавить файл',
        'remove_selected': 'Удалить выбранное',
        'remove_all': 'Удалить все',
        'output_file': 'Выходной файл:',
        'auto_generated': 'Будет создан автоматически',
        'choose_output': 'Выбрать выход',
        'execute_merge': 'ВЫПОЛНИТЬ СЛИЯНИЕ',
        'results': 'Результаты:',
        'error': 'Ошибка',
        'select_source_error': 'Выберите исходный файл!',
        'select_translation_error': 'Добавьте хотя бы один файл перевода!',
        'success': 'Успех',
        'merge_completed': 'Слияние завершено!',
        'translated': 'Переведено',
        'file_saved': 'Файл сохранён',
        'select_source_title': 'Выберите исходный файл (EN)',
        'select_translation_title': 'Выберите файл перевода',
        'select_output_title': 'Выберите выходной файл',
        'loading_source': 'Загрузка исходного файла...',
        'loading_translations': 'Загрузка переводов',
        'processing': 'Обработка',
        'completed': 'Завершено!',
        'merge_completed_header': 'СЛИЯНИЕ ЗАВЕРШЕНО!',
        'output_file_label': 'Выходной файл:',
        'statistics': 'СТАТИСТИКА:',
        'total_rows': 'Всего строк:',
        'translated_check': 'Переведено (✓):',
        'not_translated': 'Не переведено (✗):',
        'source_modified': 'Источник изменён (⚠):',
        'legend': 'ЛЕГЕНДА:',
        'legend_translated': 'Применён существующий перевод (KEY и SOURCE совпадают)',
        'legend_not_translated': 'Перевод не найден (требуется перевод)',
        'legend_modified': 'SOURCE изменён по сравнению с существующим переводом\n      (требуется ручная проверка/обновление)',
        'file_saved_success': 'Файл успешно сохранён!\n   Вы можете открыть его для проверки и завершения недостающих переводов.',
        'language': 'Язык:',
    }
}


class TranslationMerger:
    """Gestisce la logica di merge delle traduzioni"""
    
    def __init__(self):
        self.source_data: Dict[str, Tuple[str, str]] = {}  # key -> (source, translation)
        self.translation_data: Dict[str, Tuple[str, str]] = {}  # key -> (source, translation)
        
    def load_csv_file(self, filepath: str) -> Dict[str, Tuple[str, str]]:
        """Carica un file CSV e restituisce un dizionario key -> (source, translation)"""
        data = {}
        try:
            with open(filepath, 'r', encoding='utf-8', newline='') as f:
                # Prova diverse configurazioni di CSV
                sample = f.read(4096)
                f.seek(0)
                
                # Determina il delimitatore
                sniffer = csv.Sniffer()
                try:
                    dialect = sniffer.sniff(sample)
                    delimiter = dialect.delimiter
                except:
                    delimiter = ','
                
                reader = csv.DictReader(f, delimiter=delimiter)
                
                for row in reader:
                    # Gestisce diverse varianti di nomi colonna
                    key = row.get('key') or row.get('Key') or row.get('KEY')
                    source = row.get('source') or row.get('Source') or row.get('SOURCE')
                    translation = row.get('Translation') or row.get('translation') or row.get('TRANSLATION') or ''
                    
                    if key and source is not None:
                        data[key] = (source, translation)
                        
        except Exception as e:
            raise Exception(f"Errore caricamento file {Path(filepath).name}: {str(e)}")
            
        return data
    
    def merge_translations(self, source_file: str, translation_files: List[str], 
                          progress_callback=None) -> List[Dict[str, str]]:
        """
        Merge delle traduzioni.
        
        Args:
            source_file: File CSV sorgente (inglese)
            translation_files: Lista di file CSV con traduzioni (italiano)
            progress_callback: Callback per aggiornare la progress bar
            
        Returns:
            Lista di dizionari con le righe del CSV risultante
        """
        # Carica il file sorgente
        if progress_callback:
            progress_callback(10, "Caricamento file sorgente...")
        
        source_data = self.load_csv_file(source_file)
        total_keys = len(source_data)
        
        # Carica tutti i file di traduzione
        translation_data = {}
        progress_step = 40 / len(translation_files) if translation_files else 0
        
        for idx, trans_file in enumerate(translation_files):
            if progress_callback:
                progress_callback(10 + (idx + 1) * progress_step, 
                                f"Caricamento traduzioni {idx + 1}/{len(translation_files)}...")
            
            trans_data = self.load_csv_file(trans_file)
            
            # Unisce le traduzioni (l'ultimo file vince in caso di duplicati)
            for key, (source, translation) in trans_data.items():
                if key not in translation_data:
                    translation_data[key] = {}
                translation_data[key][source] = translation
        
        # Processa i merge
        result = []
        processed = 0
        
        for key, (source, _) in source_data.items():
            processed += 1
            
            if progress_callback and processed % 100 == 0:
                progress_callback(50 + (processed / total_keys * 50), 
                                f"Processamento: {processed}/{total_keys}")
            
            translation = ''
            status = 'NON_TRADOTTA'
            
            # Cerca traduzione esistente
            if key in translation_data:
                trans_dict = translation_data[key]
                
                # Cerca traduzione con stesso source
                if source in trans_dict:
                    translation = trans_dict[source]
                    status = 'TRADOTTA'
                else:
                    # Source modificato - prende la prima traduzione disponibile come riferimento
                    if trans_dict:
                        translation = list(trans_dict.values())[0]
                        status = 'SOURCE_MODIFICATO'
            
            result.append({
                'key': key,
                'source': source,
                'Translation': translation,
                'status': status
            })
        
        if progress_callback:
            progress_callback(100, "Completato!")
        
        return result
    
    def save_csv(self, data: List[Dict[str, str]], output_file: str):
        """Salva i risultati in un file CSV"""
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['key', 'source', 'Translation']
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            
            writer.writeheader()
            writer.writerows(data)
    
    def get_statistics(self, data: List[Dict[str, str]]) -> Dict[str, int]:
        """Calcola statistiche sui risultati"""
        stats = {
            'totale': len(data),
            'tradotte': 0,
            'non_tradotte': 0,
            'source_modificato': 0
        }
        
        for row in data:
            status = row.get('status', 'NON_TRADOTTA')
            if status == 'TRADOTTA':
                stats['tradotte'] += 1
            elif status == 'SOURCE_MODIFICATO':
                stats['source_modificato'] += 1
            else:
                stats['non_tradotte'] += 1
        
        return stats


class TranslationMergerGUI:
    """Interfaccia grafica per il Translation Merger"""
    
    def __init__(self, root):
        self.root = root
        self.merger = TranslationMerger()
        self.source_file = None
        self.translation_files = []
        self.output_file = None
        self.current_language = 'it'  # Default language
        
        self.root.title(self.t('title'))
        self.root.geometry("800x650")
        self.root.resizable(True, True)
        
        self.setup_ui()
    
    def t(self, key):
        """Get translation for current language"""
        return TRANSLATIONS.get(self.current_language, TRANSLATIONS['en']).get(key, key)
    
    def change_language(self, lang_code):
        """Change interface language"""
        self.current_language = lang_code
        # Ricostruisce l'interfaccia con la nuova lingua
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_ui()
        
    def setup_ui(self):
        """Configura l'interfaccia utente"""
        # Frame principale
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Language selector
        lang_frame = ttk.Frame(main_frame)
        lang_frame.grid(row=0, column=0, columnspan=3, sticky=tk.E, pady=5)
        
        ttk.Label(lang_frame, text=self.t('language')).pack(side=tk.LEFT, padx=5)
        
        lang_var = tk.StringVar(value=self.current_language)
        lang_combo = ttk.Combobox(lang_frame, textvariable=lang_var, 
                                  values=['en', 'it', 'ru'], 
                                  state='readonly', width=10)
        lang_combo.pack(side=tk.LEFT)
        lang_combo.bind('<<ComboboxSelected>>', 
                       lambda e: self.change_language(lang_var.get()))
        
        # Titolo
        title_label = ttk.Label(main_frame, text=self.t('title'), 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=1, column=0, columnspan=3, pady=10)
        
        # Descrizione
        desc_label = ttk.Label(main_frame, text=self.t('description'), 
                              justify=tk.LEFT, wraplength=750)
        desc_label.grid(row=2, column=0, columnspan=3, pady=10, sticky=tk.W)
        
        # Separatore
        ttk.Separator(main_frame, orient=tk.HORIZONTAL).grid(row=3, column=0, columnspan=3, 
                                                              sticky=(tk.W, tk.E), pady=10)
        
        # File sorgente
        row = 4
        ttk.Label(main_frame, text=self.t('source_file'), font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        
        self.source_label = ttk.Label(main_frame, text=self.t('no_file'), 
                                     foreground='gray')
        self.source_label.grid(row=row, column=1, sticky=tk.W, padx=5)
        
        ttk.Button(main_frame, text=self.t('select_file'), 
                  command=self.select_source_file).grid(row=row, column=2, padx=5)
        
        # File traduzioni
        row += 1
        ttk.Label(main_frame, text=self.t('translation_files'), font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        
        # Lista file traduzioni
        row += 1
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        self.translation_listbox = tk.Listbox(list_frame, height=6)
        self.translation_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, 
                                 command=self.translation_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.translation_listbox.config(yscrollcommand=scrollbar.set)
        
        # Pulsanti per gestire le traduzioni
        row += 1
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=row, column=0, columnspan=3, pady=5)
        
        ttk.Button(button_frame, text=self.t('add_file'), 
                  command=self.add_translation_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text=self.t('remove_selected'), 
                  command=self.remove_translation_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text=self.t('remove_all'), 
                  command=self.clear_translation_files).pack(side=tk.LEFT, padx=5)
        
        # Separatore
        row += 1
        ttk.Separator(main_frame, orient=tk.HORIZONTAL).grid(row=row, column=0, columnspan=3, 
                                                              sticky=(tk.W, tk.E), pady=10)
        
        # File di output
        row += 1
        ttk.Label(main_frame, text=self.t('output_file'), font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        
        self.output_label = ttk.Label(main_frame, text=self.t('auto_generated'), 
                                     foreground='gray')
        self.output_label.grid(row=row, column=1, sticky=tk.W, padx=5)
        
        ttk.Button(main_frame, text=self.t('choose_output'), 
                  command=self.select_output_file).grid(row=row, column=2, padx=5)
        
        # Progress bar
        row += 1
        self.progress = ttk.Progressbar(main_frame, mode='determinate', length=750)
        self.progress.grid(row=row, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))
        
        self.progress_label = ttk.Label(main_frame, text="")
        row += 1
        self.progress_label.grid(row=row, column=0, columnspan=3)
        
        # Pulsante esegui
        row += 1
        self.execute_button = ttk.Button(main_frame, text=self.t('execute_merge'), 
                                        command=self.execute_merge, 
                                        style='Accent.TButton')
        self.execute_button.grid(row=row, column=0, columnspan=3, pady=20)
        
        # Area risultati
        row += 1
        ttk.Label(main_frame, text=self.t('results'), font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5)
        
        row += 1
        self.result_text = tk.Text(main_frame, height=8, width=90, state='disabled')
        self.result_text.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E))
        
        result_scroll = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, 
                                     command=self.result_text.yview)
        result_scroll.grid(row=row, column=3, sticky=(tk.N, tk.S))
        self.result_text.config(yscrollcommand=result_scroll.set)
        
        # Configura peso delle righe per resize
        main_frame.rowconfigure(6, weight=1)
        main_frame.rowconfigure(row, weight=1)
        
    def select_source_file(self):
        """Seleziona il file sorgente"""
        filename = filedialog.askopenfilename(
            title=self.t('select_source_title'),
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filename:
            self.source_file = filename
            self.source_label.config(text=Path(filename).name, foreground='black')
            
    def add_translation_file(self):
        """Aggiunge un file di traduzione"""
        filenames = filedialog.askopenfilenames(
            title=self.t('select_translation_title'),
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        for filename in filenames:
            if filename not in self.translation_files:
                self.translation_files.append(filename)
                self.translation_listbox.insert(tk.END, Path(filename).name)
                
    def remove_translation_file(self):
        """Rimuove il file di traduzione selezionato"""
        selection = self.translation_listbox.curselection()
        if selection:
            index = selection[0]
            self.translation_listbox.delete(index)
            self.translation_files.pop(index)
            
    def clear_translation_files(self):
        """Rimuove tutti i file di traduzione"""
        self.translation_listbox.delete(0, tk.END)
        self.translation_files.clear()
        
    def select_output_file(self):
        """Seleziona il file di output"""
        filename = filedialog.asksaveasfilename(
            title=self.t('select_output_title'),
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filename:
            self.output_file = filename
            self.output_label.config(text=Path(filename).name, foreground='black')
            
    def update_progress(self, value, message):
        """Aggiorna la progress bar"""
        self.progress['value'] = value
        self.progress_label.config(text=message)
        self.root.update_idletasks()
        
    def execute_merge(self):
        """Esegue il merge delle traduzioni"""
        # Validazione
        if not self.source_file:
            messagebox.showerror(self.t('error'), self.t('select_source_error'))
            return
            
        if not self.translation_files:
            messagebox.showerror(self.t('error'), self.t('select_translation_error'))
            return
        
        # Genera nome output se non specificato
        if not self.output_file:
            source_path = Path(self.source_file)
            self.output_file = str(source_path.parent / f"{source_path.stem}_merged.csv")
            self.output_label.config(text=Path(self.output_file).name, foreground='black')
        
        # Disabilita il pulsante durante l'esecuzione
        self.execute_button.config(state='disabled')
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state='disabled')
        
        # Esegue in un thread separato per non bloccare la UI
        thread = threading.Thread(target=self._execute_merge_thread)
        thread.daemon = True
        thread.start()
        
    def _execute_merge_thread(self):
        """Thread worker per il merge"""
        try:
            # Esegue il merge
            result_data = self.merger.merge_translations(
                self.source_file,
                self.translation_files,
                self.update_progress
            )
            
            # Salva il risultato
            self.merger.save_csv(result_data, self.output_file)
            
            # Calcola statistiche
            stats = self.merger.get_statistics(result_data)
            
            # Mostra risultati
            self.root.after(0, self._show_results, stats, self.output_file)
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Errore", str(e)))
        finally:
            self.root.after(0, lambda: self.execute_button.config(state='normal'))
            
    def _show_results(self, stats, output_file):
        """Mostra i risultati nell'interfaccia"""
        result_text = f"""
╔══════════════════════════════════════════════════════════════╗
║           {self.t('merge_completed_header').center(54)}           ║
╚══════════════════════════════════════════════════════════════╝

📄 {self.t('output_file_label')} {Path(output_file).name}

📊 {self.t('statistics')}
   • {self.t('total_rows')}              {stats['totale']:>6}
   • {self.t('translated_check')}              {stats['tradotte']:>6}  ({stats['tradotte']/stats['totale']*100:.1f}%)
   • {self.t('not_translated')}          {stats['non_tradotte']:>6}  ({stats['non_tradotte']/stats['totale']*100:.1f}%)
   • {self.t('source_modified')}     {stats['source_modificato']:>6}  ({stats['source_modificato']/stats['totale']*100:.1f}%)

💡 {self.t('legend')}
   ✓  {self.t('legend_translated')}
   ✗  {self.t('legend_not_translated')}
   ⚠  {self.t('legend_modified')}

✅ {self.t('file_saved_success')}
"""
        
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, result_text)
        self.result_text.config(state='disabled')
        
        messagebox.showinfo(self.t('success'), 
                           f"{self.t('merge_completed')}\n\n"
                           f"{self.t('translated')}: {stats['tradotte']}/{stats['totale']}\n"
                           f"{self.t('file_saved')}: {Path(output_file).name}")


def main():
    """Entry point dell'applicazione"""
    root = tk.Tk()
    TranslationMergerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
