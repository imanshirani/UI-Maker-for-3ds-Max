# ==========================================
# COLOR PALETTE 
# ==========================================
COLOR_ACCENT = "#00aaff"              
COLOR_ACCENT_HOVER = "#0088cc"        
COLOR_ITEM_HOVER = "#3d3d3d"          
COLOR_BG_DARK = "#1a1a1a"             
COLOR_BG_MED = "#2b2b2b"              
COLOR_GROUP_BG = "#252525"            
COLOR_TEXT = "#e0e0e0"                
COLOR_TEXT_LIGHT = "#ffffff"          
COLOR_BORDER = "#3f3f3f"              
COLOR_BORDER_LIGHT = "#555555"        
COLOR_BORDER_DARK = "#444444"         

# button
COLOR_BTN_BG = "#3a3a3a"              
COLOR_BTN_PRESSED = "#222222"         
COLOR_BTN_ACTION_BG = "#005a9e"       
COLOR_BTN_ACTION_BORDER = "#004a87"   
COLOR_BTN_ALT = "#333333"             

# paypal
COLOR_PAYPAL_BG = "#FFC439"
COLOR_PAYPAL_TEXT = "#00457C"
COLOR_PAYPAL_HOVER = "#FFD46A"

# ==========================================
# STYLESHEETS 
# ==========================================

MAIN_STYLE = f"""
QWidget {{
    background-color: {COLOR_BG_MED};
    color: {COLOR_TEXT};
    font-family: 'Segoe UI', sans-serif;
    font-size: 12px;
}}

QListWidget {{
    background-color: {COLOR_BG_DARK};
    border: 1px solid {COLOR_BORDER};
    border-radius: 4px;
    outline: none;
}}
QListWidget::item:hover {{
    background-color: {COLOR_ITEM_HOVER};
}}
QListWidget::item:selected {{
    background-color: {COLOR_ITEM_HOVER};
    border: 1px solid {COLOR_ACCENT}; 
    color: {COLOR_TEXT_LIGHT};
}}

QPushButton {{
    background-color: {COLOR_BTN_BG};
    border: 1px solid {COLOR_BORDER_LIGHT};
    border-radius: 3px;
    color: {COLOR_TEXT};
    padding: 4px;
}}
QPushButton:hover {{
    background-color: {COLOR_ITEM_HOVER};
    border: 1px solid {COLOR_ACCENT}; 
}}
QPushButton:pressed {{
    background-color: {COLOR_BTN_PRESSED};
}}

QLineEdit {{
    background-color: {COLOR_BG_DARK};
    border: 1px solid {COLOR_BORDER_DARK};
    border-radius: 4px;
    padding: 5px;
    color: {COLOR_TEXT}; 
}}
QLineEdit:focus {{
    border: 1px solid {COLOR_ACCENT}; 
}}

QScrollBar:vertical {{
    border: none;
    background: {COLOR_BG_MED};
    width: 8px;
}}
QScrollBar::handle:vertical {{
    background: {COLOR_BORDER_LIGHT};
    min-height: 20px;
    border-radius: 4px;
}}
QScrollBar::handle:vertical:hover {{
    background: {COLOR_ACCENT};
}}
"""

DARK_THEME = MAIN_STYLE

#inster 
BTN_ACTION = f"""
QPushButton {{
    background-color: {COLOR_BTN_ACTION_BG};
    font-weight: bold;
    color: {COLOR_TEXT_LIGHT};
    border: 1px solid {COLOR_BTN_ACTION_BORDER};
}}
QPushButton:hover {{
    background-color: {COLOR_ACCENT};
    color: {COLOR_TEXT_LIGHT};
}}
"""

GROUP_BOX_HEADER = f"""
QGroupBox {{
    font-weight: bold;
    border: 1px solid {COLOR_BORDER};
    border-radius: 5px;
    margin-top: 10px;
    padding-top: 10px;
    background-color: {COLOR_GROUP_BG};
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 10px;
    padding: 0 3px;
    color: {COLOR_ACCENT};
}}
"""

#SpinBox
SPIN_BOX_STYLE = f"""
QDoubleSpinBox {{
    background-color: {COLOR_BG_DARK};
    color: {COLOR_TEXT_LIGHT};
    border: 1px solid {COLOR_BORDER_DARK};
    border-radius: 3px;
    padding: 2px;
    selection-background-color: {COLOR_ACCENT};
}}
QDoubleSpinBox:focus {{
    border: 1px solid {COLOR_ACCENT};
}}
"""

PROGRESS_BAR_STYLE = f"""
    QProgressBar {{
        border: 1px solid {COLOR_BORDER_DARK}; 
        border-radius: 2px; 
        height: 12px; 
        text-align: center; 
        font-size: 9px;
        color: {COLOR_TEXT_LIGHT};
        background-color: {COLOR_BG_DARK};
    }}
    QProgressBar::chunk {{ 
        background-color: {COLOR_ACCENT}; 
        border-radius: 1px;
    }}
"""

ITEM_STYLE = f"""
    QWidget {{
        background-color: {COLOR_BG_MED};
        border-radius: 5px;
        border: 1px solid {COLOR_BORDER};
    }}
    QWidget:hover {{
        background-color: {COLOR_ITEM_HOVER};
        border: 1px solid {COLOR_ACCENT};
    }}
"""

#(PayPal/GitHub/Settings)
BTN_SETTING = f"""
QPushButton {{ 
    background-color: {COLOR_BG_DARK}; 
    color: {COLOR_TEXT_LIGHT}; 
    font-weight: bold; 
    padding: 6px; 
    border-radius: 4px; 
}} 
QPushButton:hover {{ 
    background-color: {COLOR_ITEM_HOVER}; 
    border: 1px solid {COLOR_ACCENT}; 
}}
"""

BTN_GITHUB = f"""
QPushButton {{ 
    background-color: {COLOR_BTN_ALT}; 
    color: {COLOR_TEXT_LIGHT}; 
    font-weight: bold; 
    padding: 6px; 
    border-radius: 4px; 
}} 
QPushButton:hover {{ 
    background-color: {COLOR_ITEM_HOVER}; 
    border: 1px solid {COLOR_ACCENT}; 
}}
"""

BTN_PAYPAL = f"""
QPushButton {{ 
    background-color: {COLOR_PAYPAL_BG}; 
    color: {COLOR_PAYPAL_TEXT}; 
    font-weight: bold; 
    padding: 6px; 
    border-radius: 4px; 
}} 
QPushButton:hover {{ 
    background-color: {COLOR_PAYPAL_HOVER}; 
}}
"""

APP_INFO_LABEL = f"font-size: 11px; color: {COLOR_TEXT};"

# ==========================================
# UI MAKER SPECIFIC STYLES
# ==========================================
TREE_NODE_OBJ = COLOR_ACCENT
TREE_NODE_PROP = "#FFFFFF"
TREE_NODE_CAT = "#888888"

SEARCH_BOX_STYLE = f"""
QLineEdit {{
    background-color: {COLOR_BG_DARK}; 
    border: 1px solid {COLOR_BORDER}; 
    color: {COLOR_TEXT}; 
    padding: 4px; 
    border-radius: 3px;
}}
"""

PARAM_EDIT_STYLE = f"""
QLineEdit {{
    background-color: {COLOR_BG_DARK}; 
    color: {COLOR_ACCENT}; 
    border: 1px solid {COLOR_BORDER}; 
    padding: 3px;
}}
"""

DRAWER_STYLE = f"""
QWidget {{
    background-color: {COLOR_BG_MED}; 
    border-top: 1px solid {COLOR_BORDER_DARK}; 
    border-bottom-left-radius: 4px; 
    border-bottom-right-radius: 4px;
}}
"""

EDIT_MODE_WIDGET = f"""
QWidget {{ 
    border: 1px dashed {COLOR_ACCENT}; 
    background-color: {COLOR_GROUP_BG}; 
    border-radius: 4px; 
    margin-top: 2px; 
}}
"""
BTN_DELETE = f"""
QPushButton {{
    color: #ff4444; 
    background-color: rgba(255, 0, 0, 0.1); 
    border: 1px solid #ff4444;
    font-weight: bold;
    border-radius: 3px;
}}
QPushButton:hover {{
    background-color: rgba(255, 0, 0, 0.2);
}}
"""

USER_MODE_WIDGET = "QWidget { border: none; background-color: transparent; }"
EDIT_MODE_TITLE = f"background-color: {COLOR_BG_DARK}; border: 1px solid {COLOR_BORDER}; color: {COLOR_TEXT}; border-radius: 2px;"
USER_MODE_TITLE = f"background-color: transparent; border: none; color: {COLOR_TEXT};"

# --- (Canvas) ---
CANVAS_EDIT_STYLE = f"background-color: {COLOR_BG_DARK}; border: 1px dashed #F57C00; border-radius: 5px;"
CANVAS_USER_STYLE = f"background-color: {COLOR_BG_DARK}; border: 1px solid {COLOR_BORDER}; border-radius: 5px;"

# --- (Group و Tab) ---
CONTAINER_EDIT_STYLE = f"border: 1px dashed {COLOR_ACCENT}; background-color: transparent; border-radius: 4px;"
CONTAINER_USER_STYLE = "border: none; background-color: transparent;"

BTN_EDIT_MODE = f"""
QPushButton {{
    background-color: #F57C00;
    color: {COLOR_TEXT_LIGHT};
    font-weight: bold;
    border: 1px solid #E65100;
    border-radius: 3px;
    padding: 4px;
}}
QPushButton:hover {{
    background-color: #FB8C00; 
}}
"""

# --- (Separator) ---
SEPARATOR_STYLE = f"""
QWidget {{
    background-color: {COLOR_BORDER_DARK}; 
    margin: 10px 5px; 
    border-radius: 1px;
}}
"""