<div align="center">
  <h1>🎨 UI Maker for 3ds Max</h1>
  <p><strong>A Next-Gen, Visual UI Builder and Rigging Tool for Autodesk 3ds Max</strong></p>


[![Donate ❤️](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/donate/?hosted_button_id=LAMNRY6DDWDC4)
<img src="https://img.shields.io/badge/Autodesk-3ds%20Max-0696D7?style=flat-square&logo=autodesk" alt="3ds Max">
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-green.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)
</div>

---

## 📖 Overview
**UI Maker** is a powerful Python/PySide6 tool designed for 3ds Max Technical Directors (TDs) and 3D Artists. It allows you to visually build custom user interfaces (Panels, Sliders, Dropdowns, etc.) and wire them directly to 3ds Max scene properties **without writing a single line of code**.

Whether you are rigging a complex character, creating a control panel for a `tyFlow` simulation, or managing scene states, UI Maker handles the complex data wiring in the background.

![UI Maker Screenshot](link_to_your_screenshot_here.png) *(Replace this with a cool screenshot or GIF of your tool in action!)*

---

## ✨ Key Features

* 🛠️ **Visual Drag & Drop Interface:** Build your UI using Tabs, Groups, Sliders, Spinners, Checkboxes, Radio Buttons, Dropdowns, and Color Pickers.
* 🔍 **Smart Deep Scanner:** Easily navigate through complex nested properties. UI Maker penetrates deep into objects, modifiers, materials, and even **tyFlow Events & Operators**.
* 🔀 **Multiplexer Logic:** Use Dropdowns and Radio Groups as "State Managers". Select one item from a list to enable a specific modifier while automatically disabling the rest.
* 🧠 **Max-Native UX:** Custom `MaxSpinner` with drag-to-change functionality, Shift/Alt acceleration, and seamless `undo` block integration.
* 💾 **Embedded Scene Data:** Save your custom UI layouts directly into the `.max` file (Base64 encoded) or export them as sidecar `.mui` JSON files.

---

## 🚀 Installation & Usage

### Prerequisites
- Autodesk 3ds Max (Versions supporting Python 3 and PySide6).
- `pymxs` (Built-in with modern 3ds Max).

### How to Run
1. Clone or download this repository.
2. In 3ds Max, go to **Scripting -> Run Script...**
3. Select the `launcher.py` file from the downloaded folder.
4. The UI Maker dockable panel will appear!

### Basic Workflow
1. **Edit Mode (🛠️):** Toggle to Edit Mode. Drag elements from the left Toolbox into the Canvas.
2. **Wire Parameters (⚙️):** Click the Settings gear on any element. Select a property from the Max Tree on the left, and click **🎯 Pick**.
3. **User Mode (🔒):** Toggle back to User Mode to lock the UI and start controlling your scene!
4. **Save (💾):** Click "Save to Max File" to embed the UI into your current scene.

---

## 🧰 Supported UI Elements

| Element | Description | Features |
| :--- | :--- | :--- |
| **Slider & Spinner** | Numeric controls | Custom Min/Max/Default ranges, Drag-to-change (Spinner). |
| **Checkbox** | Boolean control | Perfect for toggling visibility or modifier states. |
| **Dropdown & Radio** | List controls | Dynamic multi-linking (Multiplexer logic). |
| **Color Picker** | Color control | Native 3ds Max Color translation. |
| **Tabs & Groups** | Layout containers | Organize massive UIs cleanly. Supports nested drops. |

---

## 🔬 Advanced: The Deep Scanner & tyFlow
Standard 3ds Max parameter exposure often hides complex plugin data. UI Maker features a recursive `Deep Scan` engine that navigates through `SubAnims` and `Nested Properties`. This allows you to effortlessly rig internal parameters of **tyFlow** (e.g., specific operator values inside `Event_001`).

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ☕ Support
If this tool saves you hours of rigging time, consider supporting the development!

<a href="https://paypal.me/YOUR_PAYPAL_LINK" target="_blank"><img src="https://img.shields.io/badge/Donate-PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="Donate via PayPal"></a>

---
*Developed with ❤️ by [Iman Shirani (Espadan)] for the 3ds Max Community.*
