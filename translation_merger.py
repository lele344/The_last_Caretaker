#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translation Editor Pro v2.0 - Modern UI Edition
================================================
Editor professionale con interfaccia moderna e pulsanti arrotondati
"""

import csv
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from typing import Dict, List
from datetime import datetime
from collections import defaultdict
import copy


# ==================== TRANSLATIONS ====================
TRANSLATIONS = {
    'en': {
        'title': 'Translation Editor Pro',
        'menu_file': 'File', 'menu_load_base': 'Load Base File', 'menu_add_trans': 'Add Translation File',
        'menu_save': 'Save Final Output', 'menu_exit': 'Exit', 'menu_view': 'View',
        'menu_theme': 'Toggle Theme', 'menu_lang': 'Language', 'menu_help': 'Help', 'menu_about': 'About',
        'base_file': '📄 Base File', 'no_file': 'No file loaded', 'load_base_btn': '📂 Load Base File',
        'merge_stages': '📚 Merge Stages', 'add_trans_btn': '➕ Add Translation',
        'execute_merge': '🔄 Execute Merge', 'undo_last': '↩️ Undo', 'clear_stages': '🗑️ Clear',
        'save_output': '💾 SAVE OUTPUT', 'search': '🔍 Search:', 'filter_added': '🟢 Added',
        'filter_removed': '🔴 Removed', 'filter_modified': '🟡 Modified', 'filter_all': '⚪ All',
        'col_status': 'Status', 'col_key': 'Key', 'col_source': 'Source (EN)', 'col_translation': 'Translation',
        'ready': 'Ready', 'loaded_rows': 'Loaded: {0} rows', 'added_stage': 'Added: {0}',
        'merge_success': 'Merged {0} file(s)!', 'saved_success': 'File saved!\n{0}',
        'no_data': 'No data to save!', 'load_base_first': 'Load base file first!',
        'add_one_file': 'Add at least one translation file!', 'no_history': 'No history to undo!',
        'undo_success': 'Undo successful', 'stages_cleared': 'Stages cleared',
        'duplicates_found': 'Duplicates Found', 'duplicates_msg': 'Found {0} duplicates.\nReview them in the table.',
        'error': 'Error', 'warning': 'Warning', 'success': 'Success', 'info': 'Info',
        'about_text': 'Translation Editor Pro v2.0\n\nProfessional CSV translation manager\n\n• Modern UI\n• Interactive table\n• Multi-stage merge\n• Change tracking\n• Multi-language',
        'select_base': 'Select Base CSV', 'select_trans': 'Select Translation CSV', 'save_file': 'Save Output',
    },
    'it': {
        'title': 'Translation Editor Pro',
        'menu_file': 'File', 'menu_load_base': 'Carica File Base', 'menu_add_trans': 'Aggiungi Traduzione',
        'menu_save': 'Salva Output', 'menu_exit': 'Esci', 'menu_view': 'Vista',
        'menu_theme': 'Cambia Tema', 'menu_lang': 'Lingua', 'menu_help': 'Aiuto', 'menu_about': 'Info',
        'base_file': '📄 File Base', 'no_file': 'Nessun file', 'load_base_btn': '📂 Carica File Base',
        'merge_stages': '📚 Stage Merge', 'add_trans_btn': '➕ Aggiungi Traduzione',
        'execute_merge': '🔄 Esegui Merge', 'undo_last': '↩️ Annulla', 'clear_stages': '🗑️ Pulisci',
        'save_output': '💾 SALVA OUTPUT', 'search': '🔍 Cerca:', 'filter_added': '🟢 Aggiunte',
        'filter_removed': '🔴 Rimosse', 'filter_modified': '🟡 Modificate', 'filter_all': '⚪ Tutte',
        'col_status': 'Stato', 'col_key': 'Chiave', 'col_source': 'Sorgente (EN)', 'col_translation': 'Traduzione',
        'ready': 'Pronto', 'loaded_rows': 'Caricate: {0} righe', 'added_stage': 'Aggiunto: {0}',
        'merge_success': '{0} file uniti!', 'saved_success': 'File salvato!\n{0}',
        'no_data': 'Nessun dato!', 'load_base_first': 'Carica prima file base!',
        'add_one_file': 'Aggiungi almeno un file!', 'no_history': 'Nessuna cronologia!',
        'undo_success': 'Annullamento OK', 'stages_cleared': 'Stage puliti',
        'duplicates_found': 'Duplicati Trovati', 'duplicates_msg': 'Trovati {0} duplicati.\nControlla nella tabella.',
        'error': 'Errore', 'warning': 'Attenzione', 'success': 'Successo', 'info': 'Info',
        'about_text': 'Translation Editor Pro v2.0\n\nGestore professionale traduzioni CSV\n\n• UI Moderna\n• Tabella interattiva\n• Merge multi-stage\n• Tracciamento modifiche\n• Multi-lingua',
        'select_base': 'Seleziona CSV Base', 'select_trans': 'Seleziona CSV Traduzione', 'save_file': 'Salva Output',
    },
    'ru': {
        'title': 'Translation Editor Pro',
        'menu_file': 'Файл', 'menu_load_base': 'Загрузить базу', 'menu_add_trans': 'Добавить перевод',
        'menu_save': 'Сохранить', 'menu_exit': 'Выход', 'menu_view': 'Вид',
        'menu_theme': 'Сменить тему', 'menu_lang': 'Язык', 'menu_help': 'Помощь', 'menu_about': 'О программе',
        'base_file': '📄 Базовый файл', 'no_file': 'Нет файла', 'load_base_btn': '📂 Загрузить базу',
        'merge_stages': '📚 Этапы слияния', 'add_trans_btn': '➕ Добавить перевод',
        'execute_merge': '🔄 Объединить', 'undo_last': '↩️ Отменить', 'clear_stages': '🗑️ Очистить',
        'save_output': '💾 СОХРАНИТЬ', 'search': '🔍 Поиск:', 'filter_added': '🟢 Добавлено',
        'filter_removed': '🔴 Удалено', 'filter_modified': '🟡 Изменено', 'filter_all': '⚪ Все',
        'col_status': 'Статус', 'col_key': 'Ключ', 'col_source': 'Источник (EN)', 'col_translation': 'Перевод',
        'ready': 'Готово', 'loaded_rows': 'Загружено: {0} строк', 'added_stage': 'Добавлен: {0}',
        'merge_success': 'Объединено {0} файлов!', 'saved_success': 'Файл сохранен!\n{0}',
        'no_data': 'Нет данных!', 'load_base_first': 'Загрузите базу!',
        'add_one_file': 'Добавьте файл!', 'no_history': 'Нет истории!',
        'undo_success': 'Отмена OK', 'stages_cleared': 'Этапы очищены',
        'duplicates_found': 'Найдены дубликаты', 'duplicates_msg': 'Найдено {0} дубликатов.\nСмотрите в таблице.',
        'error': 'Ошибка', 'warning': 'Предупреждение', 'success': 'Успех', 'info': 'Информация',
        'about_text': 'Translation Editor Pro v2.0\n\nПрофессиональный менеджер CSV\n\n• Современный UI\n• Интерактивная таблица\n• Многоэтапное слияние\n• Отслеживание изменений\n• Мультиязычность',
        'select_base': 'Выбрать базовый CSV', 'select_trans': 'Выбрать CSV перевода', 'save_file': 'Сохранить результат',
    }
}


# ==================== DATA CLASSES ====================
class TranslationData:
    """Gestisce i dati delle traduzioni"""
    
    def __init__(self):
        self.rows: List[Dict[str, str]] = []
        self.changes: Dict[int, str] = {}
        self.duplicates: Dict[str, List[int]] = defaultdict(list)
        
    def load_from_csv(self, filepath: str):
        """Carica dati da CSV"""
        self.rows = []
        self.changes = {}
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.rows.append({
                    'key': row.get('key', ''),
                    'source': row.get('source', ''),
                    'Translation': row.get('Translation', '')
                })
        self._detect_duplicates()
    
    def _detect_duplicates(self):
        """Rileva duplicati KEY+SOURCE"""
        self.duplicates.clear()
        for idx, row in enumerate(self.rows):
            key_source = f"{row['key']}|||{row['source']}"
            self.duplicates[key_source].append(idx)
        self.duplicates = {k: v for k, v in self.duplicates.items() if len(v) > 1}
    
    def get_change_status(self, idx: int) -> str:
        return self.changes.get(idx, 'kept')


class MergeStage:
    """Stage di merge"""
    
    def __init__(self, name: str, filepath: str):
        self.name = name
        self.filepath = filepath
        self.timestamp = datetime.now()


# ==================== MODERN BUTTON ====================
class ModernButton(tk.Canvas):
    """Pulsante moderno con gradiente e bordi arrotondati"""
    
    def __init__(self, parent, text="", command=None, bg_color="#0078d4", fg_color="#ffffff", 
                 width=150, height=40, radius=10, **kwargs):
        super().__init__(parent, width=width, height=height, bg=parent['bg'], 
                        highlightthickness=0, **kwargs)
        
        self.command = command
        self.text = text
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.radius = radius
        self.width = width
        self.height = height
        self.is_hovered = False
        
        self.draw_button()
        
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    
    def draw_button(self):
        """Disegna pulsante con gradiente"""
        self.delete("all")
        
        # Colore base o hover
        if self.is_hovered:
            color = self.lighten_color(self.bg_color)
        else:
            color = self.bg_color
        
        # Bordi arrotondati
        self.create_rounded_rect(2, 2, self.width-2, self.height-2, 
                                self.radius, fill=color, outline="")
        
        # Shadow effect
        shadow_color = self.darken_color(self.bg_color)
        self.create_rounded_rect(3, 3, self.width-1, self.height-1, 
                                self.radius, fill="", outline=shadow_color, width=1)
        
        # Testo
        self.create_text(self.width/2, self.height/2, text=self.text, 
                        fill=self.fg_color, font=("Segoe UI", 10, "bold"))
    
    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        """Crea rettangolo con bordi arrotondati"""
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)
    
    def lighten_color(self, color):
        """Schiarisce colore per hover"""
        if color.startswith('#'):
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
            r = min(255, r + 30)
            g = min(255, g + 30)
            b = min(255, b + 30)
            return f"#{r:02x}{g:02x}{b:02x}"
        return color
    
    def darken_color(self, color):
        """Scurisce colore per shadow"""
        if color.startswith('#'):
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
            r = max(0, r - 40)
            g = max(0, g - 40)
            b = max(0, b - 40)
            return f"#{r:02x}{g:02x}{b:02x}"
        return color
    
    def on_click(self, event):
        if self.command:
            self.command()
    
    def on_enter(self, event):
        self.is_hovered = True
        self.draw_button()
        self.config(cursor="hand2")
    
    def on_leave(self, event):
        self.is_hovered = False
        self.draw_button()
        self.config(cursor="")
    
    def configure_text(self, text):
        """Aggiorna testo"""
        self.text = text
        self.draw_button()


# ==================== MAIN APPLICATION ====================
class TranslationEditorPro:
    """Editor professionale con UI moderna"""
    
    def __init__(self, root):
        self.root = root
        self.current_lang = 'it'
        self.root.title(self.t('title'))
        self.root.geometry("1600x950")
        
        # Dati
        self.base_data = TranslationData()
        self.current_data = TranslationData()
        self.merge_stages: List[MergeStage] = []
        self.history: List[TranslationData] = []
        
        # Tema
        self.theme = 'dark'
        self.colors = {
            'dark': {
                'bg': '#1a1a1a', 'fg': '#e0e0e0', 'bg2': '#252525', 'bg3': '#2d2d2d',
                'accent': '#0078d4', 'accent_hover': '#1e90ff',
                'success': '#10b981', 'warning': '#f59e0b', 'danger': '#ef4444',
                'added': '#4ade80', 'removed': '#f87171', 'modified': '#fbbf24', 'kept': '#9ca3af',
            },
            'light': {
                'bg': '#f5f5f5', 'fg': '#1a1a1a', 'bg2': '#ffffff', 'bg3': '#e5e5e5',
                'accent': '#0078d4', 'accent_hover': '#1e90ff',
                'success': '#059669', 'warning': '#d97706', 'danger': '#dc2626',
                'added': '#22c55e', 'removed': '#ef4444', 'modified': '#f59e0b', 'kept': '#6b7280',
            }
        }
        
        self.setup_ui()
    
    def t(self, key: str, *args) -> str:
        """Traduce chiave"""
        text = TRANSLATIONS.get(self.current_lang, TRANSLATIONS['en']).get(key, key)
        return text.format(*args) if args else text
    
    def change_language(self, lang: str):
        """Cambia lingua e aggiorna UI"""
        self.current_lang = lang
        self.root.title(self.t('title'))
        self.refresh_ui_texts()
    
    def refresh_ui_texts(self):
        """Aggiorna tutti i testi UI"""
        # Labels
        if not self.base_data.rows:
            self.base_file_label.config(text=self.t('no_file'))
        self.status_label.config(text=self.t('ready'))
        
        # Frames
        self.base_frame.config(text=self.t('base_file'))
        self.stages_frame.config(text=self.t('merge_stages'))
        
        # Buttons
        self.load_base_btn.configure_text(self.t('load_base_btn'))
        self.add_trans_btn.configure_text(self.t('add_trans_btn'))
        self.execute_merge_btn.configure_text(self.t('execute_merge'))
        self.undo_btn.configure_text(self.t('undo_last'))
        self.clear_btn.configure_text(self.t('clear_stages'))
        self.save_btn.configure_text(self.t('save_output'))
        
        # Toolbar
        self.search_label.config(text=self.t('search'))
        self.filter_added_btn.configure_text(self.t('filter_added'))
        self.filter_removed_btn.configure_text(self.t('filter_removed'))
        self.filter_modified_btn.configure_text(self.t('filter_modified'))
        self.filter_all_btn.configure_text(self.t('filter_all'))
        
        # Table headers
        self.tree.heading('status', text=self.t('col_status'))
        self.tree.heading('key', text=self.t('col_key'))
        self.tree.heading('source', text=self.t('col_source'))
        self.tree.heading('translation', text=self.t('col_translation'))
    
    def setup_ui(self):
        """Setup interfaccia moderna"""
        c = self.colors[self.theme]
        self.root.configure(bg=c['bg'])
        
        # Menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.t('menu_file'), menu=file_menu)
        file_menu.add_command(label=self.t('menu_load_base'), command=self.load_base_file)
        file_menu.add_command(label=self.t('menu_add_trans'), command=self.add_translation_file)
        file_menu.add_separator()
        file_menu.add_command(label=self.t('menu_save'), command=self.save_final_output)
        file_menu.add_separator()
        file_menu.add_command(label=self.t('menu_exit'), command=self.root.quit)
        
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.t('menu_view'), menu=view_menu)
        view_menu.add_command(label=self.t('menu_theme'), command=self.toggle_theme)
        
        lang_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.t('menu_lang'), menu=lang_menu)
        lang_menu.add_command(label="🇬🇧 English", command=lambda: self.change_language('en'))
        lang_menu.add_command(label="🇮🇹 Italiano", command=lambda: self.change_language('it'))
        lang_menu.add_command(label="🇷🇺 Русский", command=lambda: self.change_language('ru'))
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.t('menu_help'), menu=help_menu)
        help_menu.add_command(label=self.t('menu_about'), command=self.show_about)
        
        # Main container
        main_frame = tk.Frame(self.root, bg=c['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # LEFT PANEL
        left_panel = tk.Frame(main_frame, bg=c['bg'], width=340)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 15))
        left_panel.pack_propagate(False)
        
        # Base file section
        self.base_frame = tk.LabelFrame(left_panel, text=self.t('base_file'), 
                                       bg=c['bg2'], fg=c['fg'], font=("Segoe UI", 10, "bold"),
                                       padx=15, pady=15)
        self.base_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.base_file_label = tk.Label(self.base_frame, text=self.t('no_file'), 
                                        bg=c['bg2'], fg='gray', wraplength=280,
                                        font=("Segoe UI", 9), anchor='w', justify='left')
        self.base_file_label.pack(fill=tk.X, pady=(0, 12))
        
        self.load_base_btn = ModernButton(self.base_frame, text=self.t('load_base_btn'),
                                          command=self.load_base_file, bg_color=c['accent'],
                                          width=290, height=45, radius=12)
        self.load_base_btn.pack()
        
        # Stages section
        self.stages_frame = tk.LabelFrame(left_panel, text=self.t('merge_stages'),
                                         bg=c['bg2'], fg=c['fg'], font=("Segoe UI", 10, "bold"),
                                         padx=15, pady=15)
        self.stages_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        list_container = tk.Frame(self.stages_frame, bg=c['bg3'], relief=tk.FLAT, bd=0)
        list_container.pack(fill=tk.BOTH, expand=True, pady=(0, 12))
        
        scroll = tk.Scrollbar(list_container, bg=c['bg3'])
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.stages_listbox = tk.Listbox(list_container, yscrollcommand=scroll.set,
                                         bg=c['bg3'], fg=c['fg'], font=("Consolas", 9),
                                         selectbackground=c['accent'], selectforeground='white',
                                         relief=tk.FLAT, bd=0, highlightthickness=0)
        self.stages_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.config(command=self.stages_listbox.yview)
        
        # Buttons
        self.add_trans_btn = ModernButton(self.stages_frame, text=self.t('add_trans_btn'),
                                          command=self.add_translation_file, bg_color=c['success'],
                                          width=290, height=38, radius=10)
        self.add_trans_btn.pack(pady=3)
        
        self.execute_merge_btn = ModernButton(self.stages_frame, text=self.t('execute_merge'),
                                              command=self.execute_merge, bg_color=c['accent'],
                                              width=290, height=38, radius=10)
        self.execute_merge_btn.pack(pady=3)
        
        self.undo_btn = ModernButton(self.stages_frame, text=self.t('undo_last'),
                                     command=self.undo_last, bg_color=c['warning'],
                                     width=290, height=38, radius=10)
        self.undo_btn.pack(pady=3)
        
        self.clear_btn = ModernButton(self.stages_frame, text=self.t('clear_stages'),
                                      command=self.clear_stages, bg_color=c['danger'],
                                      width=290, height=38, radius=10)
        self.clear_btn.pack(pady=3)
        
        # SAVE BUTTON - GRANDE E PROMINENTE
        save_container = tk.Frame(left_panel, bg=c['bg'])
        save_container.pack(fill=tk.X)
        
        self.save_btn = ModernButton(save_container, text=self.t('save_output'),
                                     command=self.save_final_output, bg_color="#10b981",
                                     width=310, height=55, radius=15)
        self.save_btn.pack()
        
        # RIGHT PANEL
        right_panel = tk.Frame(main_frame, bg=c['bg'])
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Toolbar
        toolbar = tk.Frame(right_panel, bg=c['bg2'], relief=tk.FLAT, bd=0)
        toolbar.pack(fill=tk.X, pady=(0, 15), ipady=10, ipadx=10)
        
        self.search_label = tk.Label(toolbar, text=self.t('search'), bg=c['bg2'], fg=c['fg'],
                                     font=("Segoe UI", 10))
        self.search_label.pack(side=tk.LEFT, padx=(5, 8))
        
        search_entry_frame = tk.Frame(toolbar, bg='white', relief=tk.FLAT, bd=1)
        search_entry_frame.pack(side=tk.LEFT, padx=(0, 25))
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', lambda *args: self.on_search())
        search_entry = tk.Entry(search_entry_frame, textvariable=self.search_var, width=35,
                               font=("Segoe UI", 10), relief=tk.FLAT, bd=0)
        search_entry.pack(padx=8, pady=6)
        
        # Filter buttons
        self.filter_added_btn = ModernButton(toolbar, text=self.t('filter_added'),
                                            command=lambda: self.filter_by('added'),
                                            bg_color=c['added'], width=110, height=35, radius=8)
        self.filter_added_btn.pack(side=tk.LEFT, padx=3)
        
        self.filter_removed_btn = ModernButton(toolbar, text=self.t('filter_removed'),
                                              command=lambda: self.filter_by('removed'),
                                              bg_color=c['removed'], width=110, height=35, radius=8)
        self.filter_removed_btn.pack(side=tk.LEFT, padx=3)
        
        self.filter_modified_btn = ModernButton(toolbar, text=self.t('filter_modified'),
                                               command=lambda: self.filter_by('modified'),
                                               bg_color=c['modified'], width=110, height=35, radius=8)
        self.filter_modified_btn.pack(side=tk.LEFT, padx=3)
        
        self.filter_all_btn = ModernButton(toolbar, text=self.t('filter_all'),
                                          command=lambda: self.filter_by('all'),
                                          bg_color=c['kept'], width=90, height=35, radius=8)
        self.filter_all_btn.pack(side=tk.LEFT, padx=3)
        
        # Table
        table_container = tk.Frame(right_panel, bg=c['bg3'], relief=tk.FLAT, bd=0)
        table_container.pack(fill=tk.BOTH, expand=True)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background=c['bg2'], foreground=c['fg'],
                       fieldbackground=c['bg2'], borderwidth=0, font=("Consolas", 9))
        style.configure("Treeview.Heading", background=c['bg3'], foreground=c['fg'],
                       borderwidth=1, font=("Segoe UI", 10, "bold"))
        style.map("Treeview", background=[('selected', c['accent'])],
                 foreground=[('selected', 'white')])
        
        vsb = ttk.Scrollbar(table_container, orient="vertical")
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        
        hsb = ttk.Scrollbar(table_container, orient="horizontal")
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        
        columns = ('status', 'key', 'source', 'translation')
        self.tree = ttk.Treeview(table_container, columns=columns, show='headings',
                                yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.tree.heading('status', text=self.t('col_status'))
        self.tree.heading('key', text=self.t('col_key'))
        self.tree.heading('source', text=self.t('col_source'))
        self.tree.heading('translation', text=self.t('col_translation'))
        
        self.tree.column('status', width=120, minwidth=100, stretch=False)
        self.tree.column('key', width=280, minwidth=100)
        self.tree.column('source', width=480, minwidth=150)
        self.tree.column('translation', width=480, minwidth=150)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        # Status bar
        status_bar = tk.Frame(right_panel, bg=c['bg2'], relief=tk.FLAT, bd=0)
        status_bar.pack(fill=tk.X, pady=(15, 0), ipady=8, ipadx=10)
        
        self.status_label = tk.Label(status_bar, text=self.t('ready'), bg=c['bg2'], fg=c['fg'],
                                     font=("Segoe UI", 9), anchor='w')
        self.status_label.pack(side=tk.LEFT, padx=5)
        
        self.stats_label = tk.Label(status_bar, text="", bg=c['bg2'], fg=c['fg'],
                                    font=("Segoe UI", 9, "bold"), anchor='e')
        self.stats_label.pack(side=tk.RIGHT, padx=5)
    
    def load_base_file(self):
        """Carica file base"""
        filepath = filedialog.askopenfilename(
            title=self.t('select_base'),
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filepath:
            try:
                self.base_data = TranslationData()
                self.base_data.load_from_csv(filepath)
                self.current_data = copy.deepcopy(self.base_data)
                self.history = []
                
                c = self.colors[self.theme]
                self.base_file_label.config(text=Path(filepath).name, fg=c['success'])
                self.refresh_table()
                self.status_label.config(text=self.t('loaded_rows', len(self.base_data.rows)))
                
                if self.base_data.duplicates:
                    messagebox.showwarning(
                        self.t('duplicates_found'),
                        self.t('duplicates_msg', len(self.base_data.duplicates))
                    )
            except Exception as e:
                messagebox.showerror(self.t('error'), f"Failed to load:\n{str(e)}")
    
    def add_translation_file(self):
        """Aggiungi file traduzione"""
        filepath = filedialog.askopenfilename(
            title=self.t('select_trans'),
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filepath:
            name = f"Stage {len(self.merge_stages) + 1}: {Path(filepath).name}"
            stage = MergeStage(name, filepath)
            self.merge_stages.append(stage)
            self.stages_listbox.insert(tk.END, name)
            self.status_label.config(text=self.t('added_stage', Path(filepath).name))
    
    def execute_merge(self):
        """Esegui merge"""
        if not self.base_data.rows:
            messagebox.showwarning(self.t('warning'), self.t('load_base_first'))
            return
        
        if not self.merge_stages:
            messagebox.showwarning(self.t('warning'), self.t('add_one_file'))
            return
        
        self.history.append(copy.deepcopy(self.current_data))
        
        for stage in self.merge_stages:
            self.merge_translation_file(stage)
        
        self.refresh_table()
        self.update_statistics()
        messagebox.showinfo(self.t('success'), self.t('merge_success', len(self.merge_stages)))
    
    def merge_translation_file(self, stage: MergeStage):
        """Merge singolo file"""
        trans_data = TranslationData()
        trans_data.load_from_csv(stage.filepath)
        
        trans_lookup = {}
        for row in trans_data.rows:
            key_source = f"{row['key']}|||{row['source']}"
            trans_lookup[key_source] = row['Translation']
        
        for idx, row in enumerate(self.current_data.rows):
            key_source = f"{row['key']}|||{row['source']}"
            
            if key_source in trans_lookup:
                new_trans = trans_lookup[key_source]
                old_trans = row['Translation']
                
                if old_trans != new_trans:
                    if old_trans == '' and new_trans != '':
                        self.current_data.changes[idx] = 'added'
                    elif old_trans != '' and new_trans == '':
                        self.current_data.changes[idx] = 'removed'
                    else:
                        self.current_data.changes[idx] = 'modified'
                    
                    row['Translation'] = new_trans
    
    def refresh_table(self):
        """Aggiorna tabella"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        c = self.colors[self.theme]
        icons = {'added': '🟢', 'removed': '🔴', 'modified': '🟡', 'kept': '⚪'}
        
        for idx, row in enumerate(self.current_data.rows):
            status = self.current_data.get_change_status(idx)
            status_text = f"{icons.get(status, '⚪')} {status}"
            
            item = self.tree.insert('', tk.END, values=(
                status_text,
                row['key'][:50] + '...' if len(row['key']) > 50 else row['key'],
                row['source'][:100] + '...' if len(row['source']) > 100 else row['source'],
                row['Translation'][:100] + '...' if len(row['Translation']) > 100 else row['Translation']
            ))
            
            if status in c:
                self.tree.tag_configure(status, foreground=c[status])
                self.tree.item(item, tags=(status,))
    
    def update_statistics(self):
        """Aggiorna statistiche"""
        total = len(self.current_data.rows)
        added = sum(1 for s in self.current_data.changes.values() if s == 'added')
        removed = sum(1 for s in self.current_data.changes.values() if s == 'removed')
        modified = sum(1 for s in self.current_data.changes.values() if s == 'modified')
        
        self.stats_label.config(text=f"Total: {total} | 🟢 {added} | 🔴 {removed} | 🟡 {modified}")
    
    def save_final_output(self):
        """Salva output finale"""
        if not self.current_data.rows:
            messagebox.showwarning(self.t('warning'), self.t('no_data'))
            return
        
        filepath = filedialog.asksaveasfilename(
            title=self.t('save_file'),
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filepath:
            try:
                with open(filepath, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=['key', 'source', 'Translation'])
                    writer.writeheader()
                    writer.writerows(self.current_data.rows)
                
                messagebox.showinfo(self.t('success'), self.t('saved_success', filepath))
                self.status_label.config(text=f"Saved: {Path(filepath).name}")
            except Exception as e:
                messagebox.showerror(self.t('error'), f"Save failed:\n{str(e)}")
    
    def undo_last(self):
        """Annulla ultimo merge"""
        if self.history:
            self.current_data = self.history.pop()
            self.refresh_table()
            self.update_statistics()
            self.status_label.config(text=self.t('undo_success'))
        else:
            messagebox.showinfo(self.t('info'), self.t('no_history'))
    
    def clear_stages(self):
        """Pulisci stage"""
        self.merge_stages.clear()
        self.stages_listbox.delete(0, tk.END)
        self.status_label.config(text=self.t('stages_cleared'))
    
    def toggle_theme(self):
        """Cambia tema"""
        self.theme = 'light' if self.theme == 'dark' else 'dark'
        # Riavvia UI per applicare tema
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_ui()
        if self.current_data.rows:
            self.refresh_table()
    
    def on_search(self):
        """Cerca nella tabella"""
        search = self.search_var.get().lower()
        if not search:
            self.refresh_table()
            return
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        icons = {'added': '🟢', 'removed': '🔴', 'modified': '🟡', 'kept': '⚪'}
        
        for idx, row in enumerate(self.current_data.rows):
            if (search in row['key'].lower() or
                search in row['source'].lower() or
                search in row['Translation'].lower()):
                
                status = self.current_data.get_change_status(idx)
                self.tree.insert('', tk.END, values=(
                    f"{icons[status]} {status}",
                    row['key'][:50] + '...' if len(row['key']) > 50 else row['key'],
                    row['source'][:100] + '...' if len(row['source']) > 100 else row['source'],
                    row['Translation'][:100] + '...' if len(row['Translation']) > 100 else row['Translation']
                ))
    
    def filter_by(self, filter_status: str):
        """Filtra per stato"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        icons = {'added': '🟢', 'removed': '🔴', 'modified': '🟡', 'kept': '⚪'}
        
        for idx, row in enumerate(self.current_data.rows):
            status = self.current_data.get_change_status(idx)
            
            if filter_status == 'all' or status == filter_status:
                self.tree.insert('', tk.END, values=(
                    f"{icons[status]} {status}",
                    row['key'][:50] + '...' if len(row['key']) > 50 else row['key'],
                    row['source'][:100] + '...' if len(row['source']) > 100 else row['source'],
                    row['Translation'][:100] + '...' if len(row['Translation']) > 100 else row['Translation']
                ))
    
    def show_about(self):
        """Mostra info"""
        messagebox.showinfo(self.t('menu_about'), self.t('about_text'))


if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationEditorPro(root)
    root.mainloop()
