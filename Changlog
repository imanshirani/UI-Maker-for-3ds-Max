Changlog 
03-20-2026
# 🚀 UI Maker v0.002 (Open Beta)

We are excited to release **v0.002 Beta**, bringing massive upgrades to how you wire and control your 3ds Max scenes. This update transforms UI Maker from a simple UI builder into a powerful, Houdini-style system controller.

### ✨ New Features
* **Expression Engine (Math-Driven Logic):** You can now use mathematical formulas to drive your parameters! Instead of direct 1:1 linking, use the new Expression field to write formulas like `sin(x) * 10` for wave motions, or `1 - x` to invert a checkbox.
* **Multi-Parameter Linking (Batch Control):** Sliders and Spinners now support controlling multiple targets simultaneously. Simply type multiple target names separated by commas (e.g., `Sphere001, Sphere002, tyFlow_Event`) to drive them all with a single UI element.
* **Link Management System:** Added dedicated disconnect buttons to make rig management easier and safer. 
  * Use the **`🔗×`** button to safely clear a main parameter link without deleting the UI element.
  * Use the **`✕`** button on multi-link lists to remove a specific target from a batch group.

### 🛠 UI & Core Improvements
* **Stylesheet Optimization:** Cleaned up the UI logic by moving custom button styles (like the new delete/disconnect buttons) into a centralized `BTN_DELETE` class in `style.py`.
* **Enhanced Placeholders:** Added helpful placeholder text to the Expression and Link fields to guide new users on proper syntax and usage.
* **Robust Save/Load Integration:** The new Expression strings and Multi-link data structures are now fully integrated into the `.mui` file saving system and the Base64 embedded scene data.

---
*Thank you to everyone testing the Beta! Please report any bugs or feature requests in the Issues tab.*
