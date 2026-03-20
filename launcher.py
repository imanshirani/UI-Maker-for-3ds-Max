import sys
import os
import importlib

# --- Change PySide ---
try:
    from PySide6 import QtWidgets, QtCore
except ImportError:
    from PySide2 import QtWidgets, QtCore

import qtmax
import pymxs

rt = pymxs.runtime

current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir) 

import ui_view
importlib.reload(ui_view)

from ui_view import UIMakerWindow

def open_ui():
    global ui_maker_app
    
    max_main_window = qtmax.GetQMaxMainWindow()
    
    
    for child in max_main_window.findChildren(QtWidgets.QDockWidget, "UIMakerDockWidget"):
        max_main_window.removeDockWidget(child)
        child.deleteLater()

    
    ui_maker_app = UIMakerWindow(parent=max_main_window)
    max_main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, ui_maker_app)
    
    
    has_data = ui_maker_app.load_from_scene()
    ui_maker_app.setFloating(True)
    ui_maker_app.show()

def check_scene_and_open():
    
    import os
    
    
    has_embedded = rt.getUserProp(rt.rootNode, "UIMakerData")    
    
    has_sidecar = False
    max_path = rt.maxFilePath
    max_name = rt.maxFileName
    if max_path and max_name:
        base_name = os.path.splitext(max_name)[0]
        mui_file_path = os.path.join(max_path, base_name + ".mui")
        if os.path.exists(mui_file_path):
            has_sidecar = True
            
    
    if has_embedded or has_sidecar:
        open_ui()

def main():
    
    open_ui()
    
    
    current_dir_forward = current_dir.replace("\\", "/")
    
    
    callback_code = f"""
    callbacks.removeScripts id:#UIMakerAutoLoad
    callbacks.addScript #filePostOpen "python.Execute \\"import sys; sys.path.insert(0, r'{current_dir_forward}'); import launcher; launcher.check_scene_and_open()\\"" id:#UIMakerAutoLoad
    """
    rt.execute(callback_code)

if __name__ == "__main__":
    main()