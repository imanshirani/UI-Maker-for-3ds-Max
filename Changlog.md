Changlog

03-20-2026

# 🚀 UI Maker v0.004 (Open Beta)

Version 0.004 introduces highly requested quality-of-life improvements, powerful new multi-select UI elements, and essential bug fixes to ensure your saved data loads flawlessly.

### ✨ New Features
* **TextBlock Tool (`📝 TextBlock`):** Added a new tool specifically for multi-line descriptions and instructions. It features a larger text area in the settings and automatic word-wrap, making it perfect for adding detailed notes or documentation directly inside your custom UIs.
* **Checklist Tool (`☑️ Checklist`):** Introduced a multi-item checklist element. Similar to a Radio Group, you can define multiple items (Item 1, Item 2, etc.), but users can check multiple boxes independently. Each item can be wired to a different parameter in 3ds Max.
* **Multi-Target Checkboxes:** The standard single Checkbox (`✅ CheckBox`) now fully supports the "Multi-Links" system! You can now wire a single checkbox to multiple 3ds Max properties simultaneously (e.g., toggling the visibility of 5 different lights with one click).

### 💅 UI/UX Improvements
* **Extended Title Fields:** Addressed user feedback regarding text getting cut off. The maximum width for UI Element title fields has been significantly increased, allowing for much longer descriptions without truncating mid-sentence.
* **Refined Checkbox & Radio Styles:** Added custom, high-contrast CSS styling for Checkboxes and Radio Buttons. They now feature custom indicators and accent colors, ensuring they stand out clearly against the dark theme instead of blending into the background.

### 🛠️ Bug Fixes
* **Group Name Loading:** Fixed a critical bug where custom Group names would correctly save to the `.mui` file but would revert back to "New Group" upon loading.
* **Parameter Range Saving:** Fixed an issue where the `Min`, `Max`, and `Default` values for Sliders and Spinners were successfully applying in real-time but failing to serialize and save into the scene or `.mui` file.
* **Tool Name Conflict (Substring Bug):** Resolved an underlying logical bug where the "Checklist" tool was being mistakenly identified and rendered as a single "CheckBox" due to naming overlaps.

---
*Developed by Iman Shirani. Thank you for the continued feedback and bug reports!*

03-20-2026
# 🚀 UI Maker v0.003 (Open Beta)

We are constantly refining UI Maker to be as stable, intuitive, and professional as possible. Version 0.003 brings a highly requested visual organization tool, critical crash preventions, and a much cleaner codebase architecture.

### ✨ New Features
* **Separator Tool (`➖ Separator`):** Added a new horizontal divider to the UI Toolbox. You can now visually separate and categorize your custom UI layouts, making complex rigs much easier to read and navigate.

### 🛠️ Critical Bug Fixes & Stability
* **Instant Default Value Sync:** Fixed a bug where `Min`, `Max`, and `Default` values for Spinners and Sliders were not immediately applied upon creation. UI widgets now accurately snap to their defined Default values the moment they are generated.
* **Resolved Function Conflicts:** Cleaned up duplicate functions (e.g., overlapping `toggle_mode` methods) that were blocking UI styling updates from properly executing.

### 💅 UI/UX & Architecture Polish
* **Refined Edit Mode Interface:** Thinned down the main canvas dashed border from 2px to 1px for a cleaner, more modern workspace aesthetic that takes up less visual weight.
* **Total Stylesheet Centralization (Code Refactoring):** Migrated all hard-coded visual properties (Group/Tab borders, Separator lines, and Edit Mode buttons) entirely out of the logic file (`ui_view.py`) and into a centralized `style.py` file. This ensures cleaner code and makes future theme updates effortless.

---
*Thank you to everyone testing the Beta! Please report any bugs or feature requests in the Issues tab.*

---
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
