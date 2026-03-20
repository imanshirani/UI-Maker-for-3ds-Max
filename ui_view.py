
from PySide6 import QtWidgets, QtCore, QtGui
import style
import importlib         
importlib.reload(style)  
import pymxs
rt = pymxs.runtime

# ==========================================
# Settings Dialog
# ==========================================
class SettingsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.setWindowTitle("Settings & About")
        self.resize(350, 250)
        self.setStyleSheet(style.MAIN_STYLE) 
        self.setup_ui()

    def setup_ui(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        tabs = QtWidgets.QTabWidget()
        tabs.setStyleSheet(f"QTabWidget::pane {{ border: 1px solid {style.COLOR_BORDER}; }}")
        
        tab_settings = QtWidgets.QWidget()
        lay_settings = QtWidgets.QVBoxLayout(tab_settings)
        lay_settings.setSpacing(10)
        chk_auto_sync = QtWidgets.QCheckBox("Auto-sync UI with Max Scene")
        chk_auto_sync.setChecked(True)
        chk_tooltips = QtWidgets.QCheckBox("Show Tooltips in User Mode")
        chk_tooltips.setChecked(True)
        lay_settings.addWidget(chk_auto_sync)
        lay_settings.addWidget(chk_tooltips)
        lay_settings.addStretch()
        
        tab_about = QtWidgets.QWidget()
        lay_about = QtWidgets.QVBoxLayout(tab_about)
        lay_about.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        lay_about.setSpacing(15)
        
        lbl_title = QtWidgets.QLabel("UI Maker")
        lbl_title.setStyleSheet(f"font-size: 18px; font-weight: bold; color: {style.COLOR_ACCENT};")
        lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        lbl_info = QtWidgets.QLabel("Version 0.003 Beta\nCreated for Custom 3ds Max User Interface\nDeveloped by Iman Shirani")
        lbl_info.setStyleSheet(style.APP_INFO_LABEL)
        lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        
        btn_github = QtWidgets.QPushButton(" 🌟 View on GitHub")
        btn_github.setStyleSheet(style.BTN_GITHUB)
        btn_github.setCursor(QtCore.Qt.PointingHandCursor)
        btn_paypal = QtWidgets.QPushButton(" ☕ Support via PayPal")
        btn_paypal.setStyleSheet(style.BTN_PAYPAL)
        btn_paypal.setCursor(QtCore.Qt.PointingHandCursor)
        
        btn_github.clicked.connect(lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/imanshirani/UI-Maker-for-3ds-Max")))
        btn_paypal.clicked.connect(lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://www.paypal.com/donate/?hosted_button_id=LAMNRY6DDWDC4")))
        
        lay_about.addWidget(lbl_title)
        lay_about.addWidget(lbl_info)
        lay_about.addWidget(btn_github)
        lay_about.addWidget(btn_paypal)
        
        tabs.addTab(tab_settings, "⚙️ Settings")
        tabs.addTab(tab_about, "ℹ️ About")
        main_layout.addWidget(tabs)

# ==========================================
# UI
# ==========================================
class UIMakerWindow(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        super().__init__() 
        self.setWindowTitle("UI Maker")
        if parent:
            self.setParent(parent)
            
        self.setObjectName("UIMakerDockWidget")
        self.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)

        self.main_container = QtWidgets.QWidget()
        self.setWidget(self.main_container)
        self.main_container.setStyleSheet(style.MAIN_STYLE)
        
        self.is_edit_mode = False 
        self.nodes_list = []
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self.main_container)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)

        self.create_header()
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.main_layout.addWidget(self.splitter)

        self.create_left_panel()
        self.create_right_panel()

        self.left_panel.hide()
        self.splitter.setSizes([300, 700]) 

    def create_header(self):
        self.header_layout = QtWidgets.QHBoxLayout()
        self.title_label = QtWidgets.QLabel("UI Maker")
        self.title_label.setStyleSheet(f"font-size: 16px; font-weight: bold; color: {style.COLOR_ACCENT};")
        
        
        self.btn_save_scene = QtWidgets.QPushButton("💾 Save to Max File")
        self.btn_save_scene.setStyleSheet(style.BTN_ACTION)
        self.btn_save_scene.clicked.connect(self.save_to_scene)
        self.btn_save_scene.hide() 

        self.btn_load = QtWidgets.QPushButton("📂 Load .mui")
        self.btn_load.setStyleSheet(style.BTN_GITHUB)
        self.btn_load.clicked.connect(self.load_from_file)
        self.btn_load.hide()

        self.btn_save = QtWidgets.QPushButton("💾 Save .mui")
        self.btn_save.setStyleSheet(style.BTN_GITHUB)
        self.btn_save.clicked.connect(self.save_to_file)
        self.btn_save.hide()
        
        self.mode_btn = QtWidgets.QPushButton("🔒 User Mode")
        self.mode_btn.setCheckable(True)
        self.mode_btn.setFixedSize(120, 30)
        self.mode_btn.setStyleSheet(style.BTN_ACTION)
        self.mode_btn.clicked.connect(self.toggle_mode)

        self.header_layout.addWidget(self.title_label)
        self.header_layout.addStretch()
        
        self.header_layout.addWidget(self.btn_save_scene)
        self.header_layout.addWidget(self.btn_load)
        self.header_layout.addWidget(self.btn_save)
        self.header_layout.addWidget(self.mode_btn)
        
        self.main_layout.addLayout(self.header_layout)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setStyleSheet(f"color: {style.COLOR_BORDER};")
        self.main_layout.addWidget(line)

    def create_left_panel(self):
        self.left_panel = QtWidgets.QWidget()
        self.left_layout = QtWidgets.QVBoxLayout(self.left_panel)
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.setSpacing(10)

        self.create_toolbar()

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setStyleSheet(f"color: {style.COLOR_BORDER_DARK};")
        self.left_layout.addWidget(line)

        # --- 3ds Max parameters ---
        tree_header_lay = QtWidgets.QHBoxLayout()
        lbl = QtWidgets.QLabel("3ds Max Parameters")
        lbl.setStyleSheet(f"font-weight: bold; color: {style.COLOR_TEXT};")
        
        btn_refresh_tree = QtWidgets.QPushButton("🔄 Refresh")
        btn_refresh_tree.setStyleSheet(style.BTN_GITHUB)
        btn_refresh_tree.setCursor(QtCore.Qt.PointingHandCursor)
        btn_refresh_tree.clicked.connect(self.populate_max_tree)
        
        tree_header_lay.addWidget(lbl)
        tree_header_lay.addStretch()
        tree_header_lay.addWidget(btn_refresh_tree)
        self.left_layout.addLayout(tree_header_lay)

        # --- Serach Box ---
        self.search_box = QtWidgets.QLineEdit()
        self.search_box.setPlaceholderText("🔍 Search parameters...")
        self.search_box.setStyleSheet(style.SEARCH_BOX_STYLE)
        self.search_box.textChanged.connect(self.filter_tree_items)
        self.left_layout.addWidget(self.search_box)

        # --- Tree Parameters ---
        self.tree_widget = QtWidgets.QTreeWidget()
        self.tree_widget.setHeaderHidden(True)
        self.left_layout.addWidget(self.tree_widget)
        
        self.populate_max_tree()
        self.splitter.addWidget(self.left_panel)

    def filter_tree_items(self, text):
        
        search_text = text.lower()
        
        
        def search_node(item):
            match = search_text in item.text(0).lower()
            child_match = False
            for i in range(item.childCount()):
                if search_node(item.child(i)):
                    child_match = True
            
            
            should_show = match or child_match
            item.setHidden(not should_show)
            
            
            if search_text and should_show:
                item.setExpanded(True)
            elif not search_text:
                item.setExpanded(False) 
                
            return should_show

        for i in range(self.tree_widget.topLevelItemCount()):
            search_node(self.tree_widget.topLevelItem(i))
    

    def create_toolbar(self):
        header_lay = QtWidgets.QHBoxLayout()
        lbl_tools = QtWidgets.QLabel("UI Toolbox")
        lbl_tools.setStyleSheet(f"font-weight: bold; color: {style.COLOR_TEXT};")
        
        btn_settings = QtWidgets.QPushButton("⚙️")
        btn_settings.setFixedSize(28, 28)
        btn_settings.setStyleSheet(style.BTN_SETTING) 
        btn_settings.setToolTip("Settings & About")
        btn_settings.setCursor(QtCore.Qt.PointingHandCursor)
        btn_settings.clicked.connect(self.open_settings)
        
        header_lay.addWidget(lbl_tools)
        header_lay.addStretch()
        header_lay.addWidget(btn_settings)
        self.left_layout.addLayout(header_lay)

        self.tools_layout = QtWidgets.QGridLayout()
        self.tools_layout.setSpacing(5)

        tools = [
            ("📑 Tab", "Create New Tab"),
            ("📦 Group", "Create Group"),            
            ("➖ Separator", "Horizontal Line Divider"),
            ("🎚️ Slider", "Numerical Slider"),
            ("🔢 Spinner", "Spinner (Exact Number)"),
            ("🔤 Label", "Plain Text"),
            ("✅ Check", "Checkbox"),
            ("🔘 Radio", "Radio Button (Single Select)"),
            ("📋 Dropdown", "Dropdown Menu (List)"),
            ("🎨 Color", "Color Picker")
        ]


        row, col = 0, 0
        for text, tooltip in tools:
            btn = QtWidgets.QPushButton(text)
            btn.setToolTip(tooltip)
            btn.setStyleSheet(style.BTN_GITHUB)
            btn.setCursor(QtCore.Qt.PointingHandCursor)
            
            
            btn.clicked.connect(lambda checked=False, t=text: self.add_element_to_canvas(t))
            
            self.tools_layout.addWidget(btn, row, col)
            col += 1
            if col > 1: 
                col = 0
                row += 1

        self.left_layout.addLayout(self.tools_layout)

    def create_right_panel(self):
        self.right_panel = QtWidgets.QWidget()
        self.right_layout = QtWidgets.QVBoxLayout(self.right_panel)
        self.right_layout.setContentsMargins(0, 0, 0, 0)
        
        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        
        self.canvas_widget = QtWidgets.QWidget()
        self.canvas_widget.setStyleSheet(f"background-color: {style.COLOR_BG_DARK}; border: 1px solid {style.COLOR_BORDER}; border-radius: 5px;")
        
        self.canvas_layout = QtWidgets.QVBoxLayout(self.canvas_widget)
        self.canvas_layout.setAlignment(QtCore.Qt.AlignTop)
        
        self.empty_label = QtWidgets.QLabel("Canvas is Empty.\nClick tools in Edit Mode to add elements.")
        self.empty_label.setAlignment(QtCore.Qt.AlignCenter)
        self.empty_label.setStyleSheet(f"color: {style.COLOR_BORDER_LIGHT}; font-style: italic;")
        self.canvas_layout.addWidget(self.empty_label)

        
        self.scroll_area.setWidget(self.canvas_widget)
        self.right_layout.addWidget(self.scroll_area)
        self.splitter.addWidget(self.right_panel)


    def populate_max_tree(self):
        
        self.tree_widget.clear()
        selected_nodes = rt.selection
        
        if len(selected_nodes) == 0:
            item = QtWidgets.QTreeWidgetItem(["No Object Selected"])
            item.setForeground(0, QtGui.QColor("#888888"))
            self.tree_widget.addTopLevelItem(item)
            return

        def deep_scan_properties(max_target, parent_item, path_prefix="", depth=0, max_depth=5):
            if depth > max_depth: return
            try:
                
                prop_names = rt.getPropNames(max_target)
                if not prop_names: return

                folders = []
                parameters = []

                # 1. Folders and Properties
                for p in prop_names:
                    prop_name = str(p)
                    norm = prop_name.lower().replace("_", "")
                    
                    
                    if norm in ["deleted", "modifiedobject", "material"]: continue

                    try:
                        
                        prop_val = rt.getProperty(max_target, prop_name)
                        sub_props = rt.getPropNames(prop_val)
                    except:
                        sub_props = None

                    full_path = f"{path_prefix}.{prop_name}" if path_prefix else prop_name

                    
                    if sub_props and len(sub_props) > 0:
                        folders.append((prop_name, prop_val, full_path))
                    else:
                        parameters.append((prop_name, full_path))

                # 2. Folders First
                for prop_name, prop_val, full_path in folders:
                    child_item = QtWidgets.QTreeWidgetItem([f"📁 {prop_name}"])
                    child_item.setForeground(0, QtGui.QColor(style.COLOR_ACCENT)) 
                    parent_item.addChild(child_item)
                    
                    deep_scan_properties(prop_val, child_item, full_path, depth + 1, max_depth)

                # 3 . properties
                for prop_name, full_path in parameters:
                    child_item = QtWidgets.QTreeWidgetItem([prop_name])
                    child_item.setForeground(0, QtGui.QColor("#FFFFFF")) 
                    child_item.setData(0, QtCore.Qt.UserRole, full_path)
                    parent_item.addChild(child_item)
                    
            except Exception as e:
                pass

        for node in selected_nodes:
            # 1. root
            root_item = QtWidgets.QTreeWidgetItem([node.name])
            root_item.setForeground(0, QtGui.QColor(style.COLOR_ACCENT))
            root_item.setData(0, QtCore.Qt.UserRole, node.handle)
            self.tree_widget.addTopLevelItem(root_item)

            # 2. principal properties
            deep_scan_properties(node, root_item, "")

            # 3. modifiers
            if node.modifiers.count > 0:
                mod_category = QtWidgets.QTreeWidgetItem(["📦 Modifiers"])
                mod_category.setForeground(0, QtGui.QColor("#888888"))
                root_item.addChild(mod_category)
                for i in range(node.modifiers.count):
                    mod = node.modifiers[i]
                    mod_item = QtWidgets.QTreeWidgetItem([mod.name])
                    mod_item.setForeground(0, QtGui.QColor(style.COLOR_ACCENT))
                    mod_category.addChild(mod_item)
                    deep_scan_properties(mod, mod_item, f"modifiers[{i}]")

            # 4. material
            if node.material:
                mat_category = QtWidgets.QTreeWidgetItem(["🎨 Material"])
                mat_category.setForeground(0, QtGui.QColor("#888888"))
                root_item.addChild(mat_category)
                mat_item = QtWidgets.QTreeWidgetItem([node.material.name])
                mat_item.setForeground(0, QtGui.QColor(style.COLOR_ACCENT))
                mat_category.addChild(mat_item)
                deep_scan_properties(node.material, mat_item, "material")

        if not self.search_box.text():
            self.tree_widget.expandToDepth(0)
        else:
            self.filter_tree_items(self.search_box.text())
    
    def add_element_to_canvas(self, elem_type):
        
        if self.empty_label.isVisible():
            self.empty_label.hide()

        if "Tab" in elem_type:
            new_node = UITabNode(parent_canvas=self)
        elif "Group" in elem_type:
            new_node = UIGroupNode("New Group", parent_canvas=self)
        else:
            new_node = UIElementNode(elem_type, elem_type, parent_canvas=self)

        
        new_node.set_edit_mode(self.is_edit_mode)

        self.canvas_layout.addWidget(new_node)
        self.nodes_list.append(new_node)

    def check_empty_state(self):
        
        self.nodes_list = [node for node in self.nodes_list if node is not None]
        
        
        root_nodes = [n for n in self.nodes_list if n.parentWidget() == self.canvas_widget]
        
        if len(root_nodes) == 0:
            self.empty_label.show()
        else:
            self.empty_label.hide()

    def toggle_mode(self):
        self.is_edit_mode = self.mode_btn.isChecked()
        if self.is_edit_mode:
            self.mode_btn.setText("🛠 Edit Mode")
            self.mode_btn.setStyleSheet(style.BTN_EDIT_MODE) 
            self.left_panel.show()
            self.btn_save.show() 
            self.btn_load.show()
            self.btn_save_scene.show()
            
            self.canvas_widget.setStyleSheet(style.CANVAS_EDIT_STYLE) 
            
            for node in self.nodes_list:
                node.set_edit_mode(True)
        else:
            self.mode_btn.setText("🔒 User Mode")
            self.mode_btn.setStyleSheet(style.BTN_ACTION)
            self.left_panel.hide()
            self.btn_save.hide() 
            self.btn_load.hide() 
            self.btn_save_scene.hide()
            
            self.canvas_widget.setStyleSheet(style.CANVAS_USER_STYLE) 
            
            for node in self.nodes_list:
                node.set_edit_mode(False)

    def open_settings(self):
        dialog = SettingsDialog(self)
        dialog.exec_()
    # ==========================================
    # Save & Load
    # ==========================================
    def get_ui_data(self):
        ui_data = {
            "ui_name": "UI Maker",
            "version": "0.001",
            "elements": []
        }
        
        def serialize_node(node):
            
            title = ""
            if hasattr(node, 'title_edit'): title = node.title_edit.text()
            elif hasattr(node, 'tab_name_edit'): title = node.tab_name_edit.text()
            
            data = {
                "type": getattr(node, 'elem_type', node.__class__.__name__),
                "title": title,
                "expression": node.expr_edit.text() if hasattr(node, 'expr_edit') else "x",
                "linked_handle": getattr(node, 'linked_handle', None),
                "linked_prop": getattr(node, 'linked_prop', None),
                "options": getattr(node, 'options_edit').text() if hasattr(node, 'options_edit') else None, 
                "multi_links": getattr(node, 'multi_links', {}), 
                "children": []
            }
            
            
            if hasattr(node, 'drop_container'):
                container = node.drop_container
                for i in range(container.main_layout.count()):
                    w = container.main_layout.itemAt(i).widget()
                    
                    if w and (hasattr(w, 'elem_type') or w.__class__.__name__ in ['UIGroupNode', 'UITabNode']):
                        data["children"].append(serialize_node(w))
                        
            
            elif hasattr(node, 'tab_widget'):
                data["tabs"] = []
                for i in range(node.tab_widget.count()):
                    tab_container = node.tab_widget.widget(i)
                    tab_data = {"name": node.tab_widget.tabText(i), "children": []}
                    for j in range(tab_container.main_layout.count()):
                        w = tab_container.main_layout.itemAt(j).widget()
                        if w and (hasattr(w, 'elem_type') or w.__class__.__name__ in ['UIGroupNode', 'UITabNode']):
                            tab_data["children"].append(serialize_node(w))
                    data["tabs"].append(tab_data)
                    
            return data

        
        for node in self.nodes_list:
            if node.parentWidget() == self.canvas_widget:
                ui_data["elements"].append(serialize_node(node))
                
        return ui_data

    def load_from_dict(self, data):
        
        
        for node in self.nodes_list:
            node.setParent(None)
            node.deleteLater()
        self.nodes_list.clear()
        
        def build_node(item_data, parent_drop_container=None):
            
            elem_type = item_data.get("type", "")
            
            # add element to canvas
            if elem_type == "UITabNode": elem_type = "Tab"
            elif elem_type == "UIGroupNode": elem_type = "Group"
            
            # 1. UI Element
            if "Tab" in elem_type: 
                new_node = UITabNode(parent_canvas=self)
            elif "Group" in elem_type: 
                new_node = UIGroupNode("New Group", parent_canvas=self)
            else: 
                new_node = UIElementNode(elem_type, item_data.get("title", elem_type), parent_canvas=self)
            
            
            self.nodes_list.append(new_node)
            
            # 2. Wiring
            new_node.linked_handle = item_data.get("linked_handle")
            new_node.linked_prop = item_data.get("linked_prop")
            
            if new_node.linked_handle and new_node.linked_prop and hasattr(new_node, 'param_edit'):
                try:
                    obj = rt.maxOps.getNodeByHandle(new_node.linked_handle)
                    obj_name = obj.name if obj else "Unknown/Deleted"
                    new_node.param_edit.setText(f"{obj_name}.{new_node.linked_prop}")
                except:
                    new_node.param_edit.setText("Error Loading Link")

            # 3. 
            new_node.multi_links = item_data.get("multi_links", {})
            
            
            if hasattr(new_node, 'options_edit') and item_data.get("options"):
                new_node.options_edit.setText(item_data.get("options"))

            # Expression
            if hasattr(new_node, 'expr_edit') and item_data.get("expression"):
                new_node.expr_edit.setText(item_data.get("expression"))
                
            # 4. Min/Max/Default
            if hasattr(new_node, 'spn_min'):
                new_node.spn_min.setValue(item_data.get("min", 0.0))
                new_node.spn_max.setValue(item_data.get("max", 100.0))
                new_node.spn_def.setValue(item_data.get("default", 50.0))
                
                if new_node.ui_widget:
                    new_node.ui_widget.setValue(item_data.get("default", 50.0))

            # 5. 
            if parent_drop_container:
                parent_drop_container.main_layout.addWidget(new_node)
                if hasattr(parent_drop_container, 'empty_lbl'):
                    parent_drop_container.empty_lbl.hide()
            else:
                self.canvas_layout.addWidget(new_node)
                self.empty_label.hide()
                
            # 6. Recursive
            if "children" in item_data and hasattr(new_node, 'drop_container'):
                for child_data in item_data["children"]:
                    build_node(child_data, new_node.drop_container)
                    
            # 7. Tabs
            if "tabs" in item_data and hasattr(new_node, 'tab_widget'):                
                while new_node.tab_widget.count() > 0:
                    new_node.tab_widget.removeTab(0)
                    
                new_node.tab_count = 0
                for tab_data in item_data["tabs"]:
                    new_node.tab_count += 1
                    tab_container = DropContainer(new_node)
                    new_node.tab_widget.addTab(tab_container, tab_data.get("name", f"Tab {new_node.tab_count}"))
                    
                   
                    for child_data in tab_data.get("children", []):
                        build_node(child_data, tab_container)
            
            # 8. Edit/User
            new_node.set_edit_mode(self.is_edit_mode)
            return new_node

        
        for item in data.get("elements", []):
            build_node(item)
            
        self.check_empty_state()
        
        
        self.mode_btn.setChecked(False)
        self.toggle_mode()

    def save_to_scene(self):
        
        import json
        import base64
        import os
        
        data = self.get_ui_data()
        json_str = json.dumps(data, ensure_ascii=False)
        
        
        b64_bytes = base64.b64encode(json_str.encode('utf-8'))
        b64_str = b64_bytes.decode('ascii') 
        
        rt.setUserProp(rt.rootNode, "UIMakerData", b64_str)
        
        max_path = rt.maxFilePath
        max_name = rt.maxFileName
        
        if max_path and max_name:
            full_path = os.path.join(max_path, max_name)
            rt.saveMaxFile(full_path, clearNeedSaveFlag=True, useNewFile=False, quiet=True)
            print(f"[UI Maker] UI Data saved and Max file updated: {full_path}")            
            QtWidgets.QMessageBox.information(self, "Save Successful", "UI information successfully saved to max file!")
        
        else:
            rt.setSaveRequired(True)
            print("[UI Maker] Data injected! Please SAVE your Max scene now (Ctrl+S).")            
            QtWidgets.QMessageBox.warning(self, "Action Required", "Information injected into Max.\nPlease save the Max file now (Ctrl+S).")
    def load_from_scene(self):
        
        import json
        import base64
        import os
        
        # Embedded
        val = rt.getUserProp(rt.rootNode, "UIMakerData")
        # 
        if val != rt.undefined and val is not None and str(val).strip() != "":
            try:
                clean_str = str(val).strip()
                json_str = base64.b64decode(clean_str.encode('ascii')).decode('utf-8')
                data = json.loads(json_str)
                self.load_from_dict(data)
                print("[UI Maker] UI Data loaded automatically from Embedded Scene Data!")
                return True
            except Exception as e:
                print(f"[UI Maker] Failed to decode embedded data: {e}")
                pass
                
        # Sidecar
        try:
            max_path = rt.maxFilePath
            max_name = rt.maxFileName
            if max_path and max_name:
                base_name = os.path.splitext(max_name)[0]
                mui_file_path = os.path.join(max_path, base_name + ".mui")
                
                if os.path.exists(mui_file_path):
                    with open(mui_file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    self.load_from_dict(data)
                    print(f"[UI Maker] UI Data loaded automatically from sidecar file: {mui_file_path}")
                    return True
        except Exception as e:
            print(f"[UI Maker] Failed to load sidecar .mui file: {e}")
            pass
            
        return False

    def save_to_file(self):
        import json
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save UI", "", "Max UI Files (*.mui);;JSON Files (*.json)")
        if file_path:
            data = self.get_ui_data()
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self):
        import json
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load UI", "", "Max UI Files (*.mui);;JSON Files (*.json)")
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.load_from_dict(data)

    

# ==========================================
# Drag & Drop
# ==========================================
class DragHandle(QtWidgets.QLabel):
    
    def __init__(self, parent_node):
        super(DragHandle, self).__init__(" ⣿ ")
        self.parent_node = parent_node
        self.setStyleSheet("color: #888; font-size: 14px; padding: 2px;")
        self.setCursor(QtCore.Qt.OpenHandCursor)
        self.setToolTip("Drag to Move")
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_pos = event.pos()
            
    def mouseMoveEvent(self, event):
        if not (event.buttons() & QtCore.Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_pos).manhattanLength() < QtWidgets.QApplication.startDragDistance():
            return
            
        drag = QtGui.QDrag(self.parent_node)
        mime_data = QtCore.QMimeData()
        mime_data.setText(str(id(self.parent_node))) 
        drag.setMimeData(mime_data)
        
        
        pixmap = self.parent_node.grab()
        drag.setPixmap(pixmap.scaledToWidth(250))
        drag.setHotSpot(event.pos())
        
        drag.exec_(QtCore.Qt.MoveAction)


class DropContainer(QtWidgets.QWidget):
    
    def __init__(self, parent_node):
        super(DropContainer, self).__init__()
        self.parent_node = parent_node
        self.setAcceptDrops(True)
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        
        self.empty_lbl = QtWidgets.QLabel("Drop Elements Here")
        self.empty_lbl.setStyleSheet(f"color: {style.COLOR_BORDER_LIGHT}; font-style: italic;")
        self.empty_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.empty_lbl)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
            self.setStyleSheet(f"background-color: {style.COLOR_ITEM_HOVER}; border: 1px dashed {style.COLOR_ACCENT}; border-radius: 4px;")

    def dragLeaveEvent(self, event):
        self.setStyleSheet("background-color: transparent; border: none;")

    def dropEvent(self, event):
        self.setStyleSheet("background-color: transparent; border: none;")
        widget_id = event.mimeData().text()
        
        canvas = self.parent_node.parent_canvas
        dropped_node = None
        
        for node in canvas.nodes_list:
            if str(id(node)) == widget_id and node != self.parent_node:
                dropped_node = node
                break
        
        if dropped_node:
            self.empty_lbl.hide()
            dropped_node.setParent(None) 
            self.main_layout.addWidget(dropped_node) 
            event.acceptProposedAction()

class MaxSpinner(QtWidgets.QDoubleSpinBox):
    
    def __init__(self, parent=None):
        super(MaxSpinner, self).__init__(parent)
        self.setAccelerated(True)
        self.setKeyboardTracking(False)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.setCursor(QtCore.Qt.SizeVerCursor) 
        self.setStyleSheet(style.SPIN_BOX_STYLE)
        self.last_y = 0
        self.is_dragging = False

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.last_y = event.pos().y()
            self.is_dragging = True
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            delta = self.last_y - event.pos().y()
            if delta != 0:
                step = self.singleStep()
                modifiers = QtWidgets.QApplication.keyboardModifiers()
                
                
                if modifiers == QtCore.Qt.ShiftModifier: step *= 10.0
                elif modifiers == QtCore.Qt.AltModifier: step *= 0.1
                
                self.setValue(self.value() + (delta * step))
                self.last_y = event.pos().y()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.is_dragging = False
        super().mouseReleaseEvent(event)

class MaxColorPicker(QtWidgets.QPushButton):
    
    colorChanged = QtCore.Signal(object) 

    def __init__(self, parent=None):
        super(MaxColorPicker, self).__init__("🎨 Choose Color", parent)
        self.current_color = QtGui.QColor(128, 128, 128)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.update_style()
        self.clicked.connect(self.pick_color)

    def update_style(self):
        
        text_color = "black" if self.current_color.lightness() > 128 else "white"
        self.setStyleSheet(f"background-color: {self.current_color.name()}; color: {text_color}; font-weight: bold; border: 1px solid {style.COLOR_BORDER}; border-radius: 3px; padding: 4px;")

    def pick_color(self):
        color = QtWidgets.QColorDialog.getColor(self.current_color, self, "Select Color")
        if color.isValid():
            self.current_color = color
            self.update_style()
            
            max_color = rt.Color(color.red(), color.green(), color.blue())
            self.colorChanged.emit(max_color)
            
    def set_color_from_data(self, hex_str):
        self.current_color = QtGui.QColor(hex_str)
        self.update_style()
class MaxRadioGroup(QtWidgets.QWidget):
    
    valueChanged = QtCore.Signal(int)

    def __init__(self, items=["Item 1", "Item 2"], parent=None):
        super(MaxRadioGroup, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.idClicked.connect(self._on_clicked)
        self.update_items(items)

    def update_items(self, items):
        
        for btn in self.button_group.buttons():
            self.button_group.removeButton(btn)
            self.layout.removeWidget(btn)
            btn.deleteLater()
        
        
        for i, text in enumerate(items):
            rb = QtWidgets.QRadioButton(text)
            self.button_group.addButton(rb, i + 1) 
            self.layout.addWidget(rb)
        
        if self.button_group.buttons():
            self.button_group.buttons()[0].setChecked(True)

    def _on_clicked(self, btn_id):
        self.valueChanged.emit(btn_id)
# ==========================================
#            Element Node
# ==========================================

class UIElementNode(QtWidgets.QWidget):
    def __init__(self, elem_type, title, parent_canvas=None):
        super(UIElementNode, self).__init__()
        self.elem_type = elem_type
        self.parent_canvas = parent_canvas
        self.setObjectName("UIElementNode")
        
        
        self.linked_handle = None
        self.linked_prop = None
        
        
        self.multi_links = {} 
        self.multi_link_edits = {} 
        
        self.wrapper_layout = QtWidgets.QVBoxLayout(self)
        self.wrapper_layout.setContentsMargins(0, 0, 0, 0)
        self.wrapper_layout.setSpacing(0)
        
        self.top_row_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QHBoxLayout(self.top_row_widget)
        self.main_layout.setContentsMargins(10, 5, 10, 5)
        
        self.title_edit = QtWidgets.QLineEdit(title)
        self.title_edit.setMinimumWidth(80)
        self.title_edit.setMaximumWidth(150)
        
        self.content_layout = QtWidgets.QHBoxLayout()
        self.content_layout.addWidget(self.title_edit) 
        self.build_content() 
        self.main_layout.addLayout(self.content_layout)
        
        self.edit_panel = QtWidgets.QWidget()
        self.edit_layout = QtWidgets.QHBoxLayout(self.edit_panel)
        self.edit_layout.setContentsMargins(0, 0, 0, 0)
        
        self.drag_handle = DragHandle(self)
        self.btn_up = QtWidgets.QPushButton("▲")
        self.btn_up.setFixedSize(24, 24)
        self.btn_up.setStyleSheet("background: transparent; border: none;")
        self.btn_up.clicked.connect(self.move_up)
        
        self.btn_down = QtWidgets.QPushButton("▼")
        self.btn_down.setFixedSize(24, 24)
        self.btn_down.setStyleSheet("background: transparent; border: none;")
        self.btn_down.clicked.connect(self.move_down)
        
        self.btn_settings = QtWidgets.QPushButton("⚙️")
        self.btn_settings.setFixedSize(24, 24)
        self.btn_settings.setStyleSheet("background: transparent; border: none;")
        self.btn_settings.clicked.connect(self.toggle_settings_drawer)
        
        self.btn_delete = QtWidgets.QPushButton("❌")
        self.btn_delete.setFixedSize(24, 24)
        self.btn_delete.setStyleSheet("background: transparent; color: #ff4444; border: none;")
        self.btn_delete.clicked.connect(self.delete_self)
        
        self.edit_layout.addWidget(self.drag_handle)
        self.edit_layout.addWidget(self.btn_up)
        self.edit_layout.addWidget(self.btn_down)
        self.edit_layout.addWidget(self.btn_settings)
        self.edit_layout.addWidget(self.btn_delete)
        self.main_layout.addWidget(self.edit_panel)
        self.wrapper_layout.addWidget(self.top_row_widget)
        
        self.build_settings_drawer()
        self.set_edit_mode(True)

    def build_content(self):
        if "Slider" in self.elem_type:
            self.ui_widget = QtWidgets.QSlider(QtCore.Qt.Horizontal)
            self.content_layout.addWidget(self.ui_widget)
        elif "Check" in self.elem_type:
            self.ui_widget = QtWidgets.QCheckBox() 
            self.content_layout.addWidget(self.ui_widget)
            self.content_layout.addStretch()
        elif "Radio" in self.elem_type:
            self.ui_widget = MaxRadioGroup(["Item 1", "Item 2"]) 
            self.content_layout.addWidget(self.ui_widget)
            self.content_layout.addStretch()
        elif "Spinner" in self.elem_type:
            self.ui_widget = MaxSpinner()
            self.ui_widget.setMinimumWidth(30)
            self.content_layout.addWidget(self.ui_widget)
            self.content_layout.addStretch()
        elif "Dropdown" in self.elem_type:
            self.ui_widget = QtWidgets.QComboBox()
            self.ui_widget.setStyleSheet(f"background-color: {style.COLOR_BG_DARK}; border: 1px solid {style.COLOR_BORDER}; color: {style.COLOR_TEXT}; padding: 2px;")
            self.ui_widget.addItems(["Item 1", "Item 2"])
            self.content_layout.addWidget(self.ui_widget)
        elif "Color" in self.elem_type:
            self.ui_widget = MaxColorPicker()
            self.content_layout.addWidget(self.ui_widget)
            self.content_layout.addStretch()
        elif "Label" in self.elem_type:
            self.title_edit.setMaximumWidth(9999)
            self.title_edit.setAlignment(QtCore.Qt.AlignCenter)
            self.ui_widget = None
        elif "Separator" in self.elem_type:
            self.title_edit.hide()            
            self.ui_widget = QtWidgets.QWidget()
            self.ui_widget.setFixedHeight(2)
            self.ui_widget.setMinimumWidth(100)
            self.ui_widget.setStyleSheet(style.SEPARATOR_STYLE)            
            self.content_layout.addWidget(self.ui_widget)
            
        self.connect_ui_signals()

    def build_settings_drawer(self):
        self.settings_drawer = QtWidgets.QWidget()
        self.settings_drawer.setStyleSheet(style.DRAWER_STYLE)
        
        
        main_drawer_lay = QtWidgets.QVBoxLayout(self.settings_drawer)
        main_drawer_lay.setContentsMargins(10, 10, 10, 10)
        
        # options
        top_grid = QtWidgets.QGridLayout()
        main_drawer_lay.addLayout(top_grid)

        # spinner slider
        if "Slider" in self.elem_type or "Spinner" in self.elem_type:
            self.spn_min = MaxSpinner(); self.spn_min.setMinimumWidth(30); self.spn_min.setRange(-999999, 999999); self.spn_min.setValue(0.0)
            self.spn_max = MaxSpinner(); self.spn_max.setMinimumWidth(30); self.spn_max.setRange(-999999, 999999); self.spn_max.setValue(100.0)
            self.spn_def = MaxSpinner(); self.spn_def.setMinimumWidth(30); self.spn_def.setRange(-999999, 999999); self.spn_def.setValue(50.0)
            
            top_grid.addWidget(QtWidgets.QLabel("Min:"), 0, 0)
            top_grid.addWidget(self.spn_min, 0, 1)
            top_grid.addWidget(QtWidgets.QLabel("Max:"), 0, 2)
            top_grid.addWidget(self.spn_max, 0, 3)
            top_grid.addWidget(QtWidgets.QLabel("Default:"), 0, 4)
            top_grid.addWidget(self.spn_def, 0, 5)

            self.spn_min.valueChanged.connect(lambda v: self.update_widget_range())
            self.spn_max.valueChanged.connect(lambda v: self.update_widget_range())
            self.spn_def.valueChanged.connect(lambda v: self.apply_default_value())
            
            
            self.update_widget_range()
            self.apply_default_value()

        if any(x in self.elem_type for x in ["Slider", "Spinner", "Dropdown", "Radio"]):
            
            if not hasattr(self, 'options_edit'):
                self.options_edit = QtWidgets.QLineEdit("Target 1, Target 2")
                self.options_edit.setStyleSheet(style.PARAM_EDIT_STYLE)
                self.options_edit.textChanged.connect(self.update_list_items)
                
               
                lbl_opt = QtWidgets.QLabel("Targets (Names):")
                top_grid.addWidget(lbl_opt, 1, 0)
                top_grid.addWidget(self.options_edit, 1, 1, 1, 5)
            
            #Pick
            self.multi_links_widget = QtWidgets.QWidget()
            self.multi_links_layout = QtWidgets.QVBoxLayout(self.multi_links_widget)
            self.multi_links_layout.setContentsMargins(0, 10, 0, 0)
            main_drawer_lay.addWidget(self.multi_links_widget)
            
            #
            initial_items = [i.strip() for i in self.options_edit.text().split(',') if i.strip()]
            self.build_multi_links_ui(initial_items)
            
        # radio button
        elif "Dropdown" in self.elem_type or "Radio" in self.elem_type:
            self.options_edit = QtWidgets.QLineEdit("Item 1, Item 2")
            self.options_edit.setStyleSheet(style.PARAM_EDIT_STYLE)
            self.options_edit.textChanged.connect(self.update_list_items)
            
            top_grid.addWidget(QtWidgets.QLabel("Options:"), 0, 0, 1, 1)
            top_grid.addWidget(self.options_edit, 0, 1, 1, 5)
            
           
            self.multi_links_widget = QtWidgets.QWidget()
            self.multi_links_layout = QtWidgets.QVBoxLayout(self.multi_links_widget)
            self.multi_links_layout.setContentsMargins(0, 10, 0, 0)
            main_drawer_lay.addWidget(self.multi_links_widget)
            
            self.build_multi_links_ui(["Item 1", "Item 2"])

        
        if "Label" not in self.elem_type and "Separator" not in self.elem_type:
            # Link
            row_link = top_grid.rowCount()
            self.param_edit = QtWidgets.QLineEdit()
            self.param_edit.setPlaceholderText("Select from tree and Pick ->")
            self.param_edit.setReadOnly(True)
            self.param_edit.setStyleSheet(style.PARAM_EDIT_STYLE)
            
            self.btn_pick = QtWidgets.QPushButton("🎯 Pick")
            self.btn_pick.setStyleSheet(style.BTN_ACTION)
            self.btn_pick.clicked.connect(self.pick_parameter_from_tree)

            # ---Disconnect ---
            self.btn_clear_link = QtWidgets.QPushButton("🔗X")
            self.btn_clear_link.setFixedSize(38, 28)
            self.btn_clear_link.setToolTip("Disconnect Link")
            self.btn_clear_link.setStyleSheet(style.BTN_DELETE)
            self.btn_clear_link.clicked.connect(self.clear_main_link)
            
            top_grid.addWidget(QtWidgets.QLabel("Link:"), row_link, 0)
            top_grid.addWidget(self.param_edit, row_link, 1, 1, 3)
            top_grid.addWidget(self.btn_pick, row_link, 4)
            top_grid.addWidget(self.btn_clear_link, row_link, 5) 

            # ---Expression ---
            self.expr_edit = QtWidgets.QLineEdit("") 
            self.expr_edit.setPlaceholderText("Use 'x' as input (e.g., x*10 or sin(x))")
            self.expr_edit.setStyleSheet(style.PARAM_EDIT_STYLE)
            
            top_grid.addWidget(QtWidgets.QLabel("Expression:"), row_link + 1, 0)
            top_grid.addWidget(self.expr_edit, row_link + 1, 1, 1, 5)

        self.wrapper_layout.addWidget(self.settings_drawer)
        self.settings_drawer.hide()

    def build_multi_links_ui(self, items):
        
        if not hasattr(self, 'multi_links_layout'): return

        
        for i in reversed(range(self.multi_links_layout.count())):
            widget = self.multi_links_layout.itemAt(i).widget()
            if widget: widget.deleteLater()
        self.multi_link_edits.clear()

        
        for item in items:
            row_w = QtWidgets.QWidget()
            row_lay = QtWidgets.QHBoxLayout(row_w)
            row_lay.setContentsMargins(0, 2, 0, 2)

            lbl = QtWidgets.QLabel(f"Link for '{item}':")
            lbl.setMinimumWidth(100)
            lbl.setStyleSheet("color: #00aaff;")

            edit = QtWidgets.QLineEdit()
            edit.setReadOnly(True)
            edit.setStyleSheet(style.PARAM_EDIT_STYLE)

            
            if item in self.multi_links:
                edit.setText(self.multi_links[item].get("path_str", ""))

            self.multi_link_edits[item] = edit

            btn = QtWidgets.QPushButton("🎯 Pick")
            btn.setStyleSheet(style.BTN_ACTION)
            btn.setFixedSize(60, 24) 
            btn.clicked.connect(lambda checked=False, i_name=item: self.pick_multi_parameter(i_name))

            
            btn_del = QtWidgets.QPushButton("🔗X")
            btn_del.setFixedSize(38, 28)
            btn_del.setStyleSheet(style.BTN_DELETE)
            btn_del.clicked.connect(lambda checked=False, i_name=item: self.remove_single_link(i_name))

            row_lay.addWidget(lbl)
            row_lay.addWidget(edit)
            row_lay.addWidget(btn)
            row_lay.addWidget(btn_del) 
            self.multi_links_layout.addWidget(row_w)

    def update_list_items(self, text):
        items = [i.strip() for i in text.split(',') if i.strip()]
        if not items: return
        
        if hasattr(self, 'ui_widget'):
            if isinstance(self.ui_widget, QtWidgets.QComboBox):
                self.ui_widget.blockSignals(True)
                self.ui_widget.clear()
                self.ui_widget.addItems(items)
                self.ui_widget.blockSignals(False)
            elif isinstance(self.ui_widget, MaxRadioGroup):
                self.ui_widget.blockSignals(True)
                self.ui_widget.update_items(items)
                self.ui_widget.blockSignals(False)
                
        
        self.build_multi_links_ui(items)

    def toggle_settings_drawer(self):
        if hasattr(self, 'settings_drawer'):
            is_visible = self.settings_drawer.isVisible()
            self.settings_drawer.setVisible(not is_visible)
            self.btn_settings.setStyleSheet("background: rgba(255, 255, 255, 0.1);" if not is_visible else "background: transparent;")

    def pick_parameter_from_tree(self):
        
        if not self.parent_canvas or not hasattr(self.parent_canvas, 'tree_widget'): return
        selected_items = self.parent_canvas.tree_widget.selectedItems()
        if not selected_items: return
            
        item = selected_items[0]
        if item.parent() is None or item.parent().text(0) in ["📦 Modifiers", "🎨 Material"]: return

        self.linked_prop = item.data(0, QtCore.Qt.UserRole)
        root_item = item
        while root_item.parent() is not None: root_item = root_item.parent()
        self.linked_handle = root_item.data(0, QtCore.Qt.UserRole)
        self.param_edit.setText(f"{root_item.text(0)} -> {self.linked_prop}")

    def pick_multi_parameter(self, item_name):
        
        if not self.parent_canvas or not hasattr(self.parent_canvas, 'tree_widget'): return
        selected_items = self.parent_canvas.tree_widget.selectedItems()
        if not selected_items: return

        item = selected_items[0]
        if item.parent() is None or item.parent().text(0) in ["📦 Modifiers", "🎨 Material"]: return

        prop = item.data(0, QtCore.Qt.UserRole)
        root_item = item
        while root_item.parent() is not None: root_item = root_item.parent()

        handle = root_item.data(0, QtCore.Qt.UserRole)
        path_str = f"{root_item.text(0)} -> {prop}"

        
        self.multi_links[item_name] = {
            "handle": handle,
            "prop": prop,
            "path_str": path_str
        }

        
        if item_name in self.multi_link_edits:
            self.multi_link_edits[item_name].setText(path_str)

    def set_edit_mode(self, is_edit):
        self.edit_panel.setVisible(is_edit)
        if is_edit:
            self.top_row_widget.setStyleSheet(style.EDIT_MODE_WIDGET)
            self.title_edit.setReadOnly(False)
            self.title_edit.setStyleSheet(style.EDIT_MODE_TITLE)
        else:
            self.top_row_widget.setStyleSheet(style.USER_MODE_WIDGET)
            self.title_edit.setReadOnly(True)
            self.title_edit.setStyleSheet(style.USER_MODE_TITLE)
            if hasattr(self, 'settings_drawer'):
                self.settings_drawer.hide()
                self.btn_settings.setStyleSheet("background: transparent;")

    def move_up(self):
        layout = self.parentWidget().layout()
        idx = layout.indexOf(self)
        if idx > 0 and not isinstance(layout.itemAt(idx - 1).widget(), QtWidgets.QLabel):
            layout.insertWidget(idx - 1, self)

    def move_down(self):
        layout = self.parentWidget().layout()
        if layout.indexOf(self) < layout.count() - 1:
            layout.insertWidget(layout.indexOf(self) + 1, self)

    def delete_self(self):
        if self.parent_canvas and self in self.parent_canvas.nodes_list:
            self.parent_canvas.nodes_list.remove(self)
        self.setParent(None)
        self.deleteLater()
        if self.parent_canvas: self.parent_canvas.check_empty_state()

    def connect_ui_signals(self):
        if not self.ui_widget: return
        
        if isinstance(self.ui_widget, QtWidgets.QSlider) or isinstance(self.ui_widget, MaxSpinner):
            self.ui_widget.valueChanged.connect(self.update_max_parameter)
        elif isinstance(self.ui_widget, QtWidgets.QCheckBox):
            self.ui_widget.stateChanged.connect(lambda v: self.update_max_parameter(v == 2))
        elif isinstance(self.ui_widget, MaxRadioGroup): 
            self.ui_widget.valueChanged.connect(self.update_max_parameter)
        elif isinstance(self.ui_widget, QtWidgets.QComboBox):
            self.ui_widget.currentIndexChanged.connect(lambda v: self.update_max_parameter(v + 1)) 
        elif isinstance(self.ui_widget, MaxColorPicker): 
            self.ui_widget.colorChanged.connect(self.update_max_parameter)

        if hasattr(self, 'spn_min'):
            self.spn_min.valueChanged.connect(lambda v: self.update_widget_range())
            self.spn_max.valueChanged.connect(lambda v: self.update_widget_range())

    def update_widget_range(self):
        mini, maxi = self.spn_min.value(), self.spn_max.value()
        if isinstance(self.ui_widget, QtWidgets.QSlider):
            self.ui_widget.setRange(int(mini), int(maxi))
        elif isinstance(self.ui_widget, MaxSpinner):
            self.ui_widget.setRange(mini, maxi)

    def apply_default_value(self):
        if not self.ui_widget: return
        val = self.spn_def.value()
        
        
        if isinstance(self.ui_widget, QtWidgets.QSlider):
            self.ui_widget.setValue(int(val))
        elif isinstance(self.ui_widget, MaxSpinner):
            self.ui_widget.setValue(val)

    def _calculate_expression(self, x):
        
        expr = self.expr_edit.text().strip() if hasattr(self, 'expr_edit') else "x"
        if expr == "x" or not expr:
            return x
        
        try:
            import math
            
            safe_dict = {
                "x": x,
                "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "pow": math.pow, "sqrt": math.sqrt, "pi": math.pi,
                "abs": abs, "min": min, "max": max, "log": math.log
            }
            
            return eval(expr, {"__builtins__": None}, safe_dict)
        except Exception as e:
            
            return x
        
    def update_max_parameter(self, value):
        try:
            
            final_value = self._calculate_expression(value)
            
            with pymxs.undo(False):
                #Multi-Link
                if self.multi_links:
                    
                    if "Dropdown" in self.elem_type or "Radio" in self.elem_type:
                        items = list(self.multi_link_edits.keys())
                        selected_idx = value - 1 
                        for i, item_name in enumerate(items):
                            link = self.multi_links.get(item_name)
                            if link:
                                
                                self._apply_to_max(link["handle"], link["prop"], (i == selected_idx))
                    
                    
                    else:
                        for link in self.multi_links.values():
                            self._apply_to_max(link["handle"], link["prop"], final_value)
                
                
                elif self.linked_handle and self.linked_prop:
                    self._apply_to_max(self.linked_handle, self.linked_prop, final_value)
                        
            rt.redrawViews()
        except Exception as e:
            print(f"[UI Maker] Sync Error: {e}")

    def _apply_to_max(self, handle, prop_path, val):
        
        obj = rt.maxOps.getNodeByHandle(int(handle))
        if not obj: return
        parts = prop_path.split('.')
        target = obj
        for part in parts[:-1]:
            if '[' in part:
                attr, idx_str = part.split('[')
                idx = int(idx_str.replace(']', ''))
                target = getattr(target, attr)[idx]
            else:
                target = getattr(target, part)
        
        last_part = parts[-1]
        if '[' in last_part:
            attr, idx_str = last_part.split('[')
            idx = int(idx_str.replace(']', ''))
            getattr(target, attr)[idx] = val
        else:
            setattr(target, last_part, val)

    def clear_main_link(self):
        
        self.linked_handle = None
        self.linked_prop = None
        if hasattr(self, 'param_edit'):
            self.param_edit.setText("")
            self.param_edit.setPlaceholderText("Link Disconnected")

    def remove_single_link(self, item_name):
        
        if item_name in self.multi_links:
            del self.multi_links[item_name] 
        
        if item_name in self.multi_link_edits:
            self.multi_link_edits[item_name].setText("")

# ==========================================
#            UIGroupNode
# ==========================================
class UIGroupNode(QtWidgets.QWidget):
    def __init__(self, title, parent_canvas=None):
        super(UIGroupNode, self).__init__()
        self.parent_canvas = parent_canvas
        self.setObjectName("UIGroupNode")
        
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        
        self.edit_panel = QtWidgets.QWidget()
        self.edit_layout = QtWidgets.QHBoxLayout(self.edit_panel)
        self.edit_layout.setContentsMargins(0, 0, 0, 0)
        
        self.drag_handle = DragHandle(self)
        self.title_edit = QtWidgets.QLineEdit(title)
        self.title_edit.setMaximumWidth(200)
        
        self.btn_up = QtWidgets.QPushButton("▲")
        self.btn_up.setFixedSize(24, 24)
        self.btn_up.setStyleSheet(f"background: transparent; color: {style.COLOR_TEXT}; border: none;")
        self.btn_up.clicked.connect(self.move_up)
        
        self.btn_down = QtWidgets.QPushButton("▼")
        self.btn_down.setFixedSize(24, 24)
        self.btn_down.setStyleSheet(f"background: transparent; color: {style.COLOR_TEXT}; border: none;")
        self.btn_down.clicked.connect(self.move_down)
        
        self.btn_delete = QtWidgets.QPushButton("❌")
        self.btn_delete.setFixedSize(24, 24)
        self.btn_delete.setStyleSheet("background: transparent; color: #ff4444; border: none; font-weight: bold;")
        self.btn_delete.clicked.connect(self.delete_self)
        
        self.edit_layout.addWidget(self.drag_handle)
        self.edit_layout.addWidget(self.title_edit)
        self.edit_layout.addWidget(self.btn_up)
        self.edit_layout.addWidget(self.btn_down)
        self.edit_layout.addStretch()
        self.edit_layout.addWidget(self.btn_delete)
        self.main_layout.addWidget(self.edit_panel)
        
        self.group_box = QtWidgets.QGroupBox(title)
        self.group_box.setStyleSheet(style.GROUP_BOX_HEADER) 
        self.group_layout = QtWidgets.QVBoxLayout(self.group_box)
        self.group_layout.setContentsMargins(10, 10, 10, 10) 
        
        self.drop_container = DropContainer(self)
        self.group_layout.addWidget(self.drop_container)
        
        self.main_layout.addWidget(self.group_box)
        self.title_edit.textChanged.connect(self.group_box.setTitle)
        self.set_edit_mode(True)

    def move_up(self):
        layout = self.parentWidget().layout()
        if not layout: return
        idx = layout.indexOf(self)
        if idx > 0:
            if isinstance(layout.itemAt(idx - 1).widget(), QtWidgets.QLabel): return
            layout.removeWidget(self)
            layout.insertWidget(idx - 1, self)

    def move_down(self):
        layout = self.parentWidget().layout()
        if not layout: return
        idx = layout.indexOf(self)
        if idx < layout.count() - 1:
            layout.removeWidget(self)
            layout.insertWidget(idx + 1, self)

    def set_edit_mode(self, is_edit):
        self.edit_panel.setVisible(is_edit)
        if is_edit:
            self.setStyleSheet(f"QWidget#UIGroupNode {{ {style.CONTAINER_EDIT_STYLE} }}")
            self.title_edit.setStyleSheet(f"background-color: {style.COLOR_BG_DARK}; border: 1px solid {style.COLOR_BORDER}; color: {style.COLOR_TEXT}; border-radius: 2px;")
        else:
            self.setStyleSheet(f"QWidget#UIGroupNode {{ {style.CONTAINER_USER_STYLE} }}")

    def delete_self(self):
        if self.parent_canvas and self in self.parent_canvas.nodes_list:
            self.parent_canvas.nodes_list.remove(self)
        self.setParent(None)
        self.deleteLater()
        if self.parent_canvas:
            self.parent_canvas.check_empty_state()

# ==========================================
# Tab Widget 
# ==========================================
class UITabNode(QtWidgets.QWidget):
    def __init__(self, parent_canvas=None):
        super(UITabNode, self).__init__()
        self.parent_canvas = parent_canvas
        self.setObjectName("UITabNode")
        
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        
        self.edit_panel = QtWidgets.QWidget()
        self.edit_layout = QtWidgets.QHBoxLayout(self.edit_panel)
        self.edit_layout.setContentsMargins(0, 0, 0, 0)
        
        self.drag_handle = DragHandle(self)
        
        self.tab_name_edit = QtWidgets.QLineEdit()
        self.tab_name_edit.setMaximumWidth(120)
        self.tab_name_edit.textChanged.connect(self.rename_current_tab)
        
        self.btn_up = QtWidgets.QPushButton("▲")
        self.btn_up.setFixedSize(24, 24)
        self.btn_up.setStyleSheet(f"background: transparent; color: {style.COLOR_TEXT}; border: none;")
        self.btn_up.clicked.connect(self.move_up)
        
        self.btn_down = QtWidgets.QPushButton("▼")
        self.btn_down.setFixedSize(24, 24)
        self.btn_down.setStyleSheet(f"background: transparent; color: {style.COLOR_TEXT}; border: none;")
        self.btn_down.clicked.connect(self.move_down)
        
        self.btn_add_tab = QtWidgets.QPushButton("➕ Tab")
        self.btn_add_tab.setStyleSheet(style.BTN_GITHUB)
        self.btn_add_tab.clicked.connect(self.add_new_tab)
        
        self.btn_remove_tab = QtWidgets.QPushButton("➖ Tab")
        self.btn_remove_tab.setStyleSheet(style.BTN_GITHUB)
        self.btn_remove_tab.clicked.connect(self.remove_current_tab)
        
        self.btn_delete = QtWidgets.QPushButton("❌")
        self.btn_delete.setFixedSize(24, 24)
        self.btn_delete.setStyleSheet("background: transparent; color: #ff4444; border: none; font-weight: bold;")
        self.btn_delete.clicked.connect(self.delete_self)
        
        self.edit_layout.addWidget(self.drag_handle)
        self.edit_layout.addWidget(self.tab_name_edit) 
        self.edit_layout.addWidget(self.btn_up)
        self.edit_layout.addWidget(self.btn_down)
        self.edit_layout.addWidget(self.btn_add_tab)
        self.edit_layout.addWidget(self.btn_remove_tab)
        self.edit_layout.addStretch()
        self.edit_layout.addWidget(self.btn_delete)
        self.main_layout.addWidget(self.edit_panel)
        
        self.tab_widget = QtWidgets.QTabWidget()
        self.tab_widget.setStyleSheet(f"QTabWidget::pane {{ border: 1px solid {style.COLOR_BORDER}; background: {style.COLOR_BG_DARK}; }} QTabBar::tab {{ background: {style.COLOR_BG_MED}; color: {style.COLOR_TEXT}; padding: 6px 15px; border: 1px solid {style.COLOR_BORDER}; margin-right: 2px; border-top-left-radius: 4px; border-top-right-radius: 4px; }} QTabBar::tab:selected {{ background: {style.COLOR_BTN_ACTION_BG}; color: white; border: 1px solid {style.COLOR_BTN_ACTION_BORDER}; }}")
        
        self.tab_widget.currentChanged.connect(self.sync_tab_name) 
        self.main_layout.addWidget(self.tab_widget)
        
        self.tab_count = 0
        self.add_new_tab() 
        self.set_edit_mode(True)

    def move_up(self):
        layout = self.parentWidget().layout()
        if not layout: return
        idx = layout.indexOf(self)
        if idx > 0:
            if isinstance(layout.itemAt(idx - 1).widget(), QtWidgets.QLabel): return
            layout.removeWidget(self)
            layout.insertWidget(idx - 1, self)

    def move_down(self):
        layout = self.parentWidget().layout()
        if not layout: return
        idx = layout.indexOf(self)
        if idx < layout.count() - 1:
            layout.removeWidget(self)
            layout.insertWidget(idx + 1, self)

    def add_new_tab(self):
        self.tab_count += 1
        new_tab = DropContainer(self) 
        self.tab_widget.addTab(new_tab, f"Tab {self.tab_count}")
        self.tab_widget.setCurrentIndex(self.tab_widget.count() - 1)
        
    def remove_current_tab(self):
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(self.tab_widget.currentIndex())

    def rename_current_tab(self, new_name):
        idx = self.tab_widget.currentIndex()
        if idx >= 0 and new_name.strip() != "":
            self.tab_widget.setTabText(idx, new_name)

    def sync_tab_name(self, index):
        if index >= 0:
            self.tab_name_edit.blockSignals(True) 
            self.tab_name_edit.setText(self.tab_widget.tabText(index))
            self.tab_name_edit.blockSignals(False)

    def set_edit_mode(self, is_edit):
        self.edit_panel.setVisible(is_edit)
        if is_edit:
            self.setStyleSheet(f"QWidget#UITabNode {{ {style.CONTAINER_EDIT_STYLE} }}")
            self.tab_name_edit.setStyleSheet(f"background-color: {style.COLOR_BG_DARK}; border: 1px solid {style.COLOR_BORDER}; color: {style.COLOR_TEXT}; border-radius: 2px;")
        else:
            self.setStyleSheet(f"QWidget#UITabNode {{ {style.CONTAINER_USER_STYLE} }}")

    def delete_self(self):
        if self.parent_canvas and self in self.parent_canvas.nodes_list:
            self.parent_canvas.nodes_list.remove(self)
        self.setParent(None)
        self.deleteLater()
        if self.parent_canvas:
            self.parent_canvas.check_empty_state()