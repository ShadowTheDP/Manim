# Python 虛擬環境建立與管理指南 (Manim 專案專用)

這份文件詳細記錄了為此 Manim 專案建立 Python 3.12 虛擬環境的完整步驟與注意事項。

## 1. 為什麼選擇 Python 3.12？
經檢查專案快取 (`__pycache__`)，發現此專案之前的執行環境為 Python 3.12。為了確保 Manim 及其相依套件（如 `manim` 本身、`numpy` 等）的相容性，我們選擇使用 Python 3.12 重新建立虛擬環境。

## 2. 建立步驟詳解

### 步驟一：指定版本建立虛擬環境
如果你電腦中安裝了多個 Python 版本，可以使用 `py` 啟動器來指定版本：
```powershell
py -3.12 -m venv myenv
```
- **py -3.12**: 使用 Windows 的 Python 啟動器指定 3.12 版本。
- **-m venv**: 執行內建的虛擬環境模組。
- **myenv**: 虛擬環境的名稱。

### 步驟二：啟動虛擬環境 (Windows)
啟動後，系統才會使用該環境內的 Python 執行檔。
```powershell
.\myenv\Scripts\Activate.ps1
```
- **注意**：啟動後，終端機提示字元前方應出現 `(myenv)`。
- **疑難排解**：若出現「禁止執行指令碼」錯誤（UnauthorizedAccess），請參閱下方「常見問題解決」。

### 步驟三：更新 Pip 工具
建議在安裝任何套件前，先更新環境內的包管理工具：
```powershell
python -m pip install --upgrade pip
```

### 步驟四：安裝專案套件
針對 Manim 動畫專案，我們使用 `requirements.txt` 統一管理套件。請執行：
```powershell
pip install -r requirements.txt
```
**注意：** Manim 的安裝可能需要一些時間，因為它會下載多個科學計算庫（如 `scipy`, `pycairo` 等）。

### 步驟五：驗證環境
執行驗證腳本來確認 Manim 是否可載入：
```powershell
python test_env.py
```
*或是直接測試 manim 指令：* `manim --version`

## 3. 常見問題解決 (Troubleshooting)

### Q: 執行 Activate.ps1 時出現「禁止運行腳本」錯誤？
這是 Windows PowerShell 的安全性限制（Execution Policy）。
**解決方法：**
在 PowerShell 中輸入以下指令並按 Enter，然後輸入 `Y` 確認：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
這會允許執行你本地編寫的腳本（如虛擬環境的啟動腳本），同時維持系統安全性。

### Q: 執行 pip install 時出現 UnicodeDecodeError (GBK/cp936 錯誤)？
這是因為 `requirements.txt` 檔案中包含了中文註釋，而 Windows 的 pip 預設使用系統語系（GBK）讀取檔案。
**解決方法：**
1. 確保 `requirements.txt` 中只有英文與數字。
2. 我已經移除了檔案中的中文註釋，現在你可以直接重新執行安裝指令。

### Q: VS Code 總是自動執行 Anaconda 的 Python 而不是 myenv？
這是因為 VS Code 的 Python 擴充功能預設選擇了全域的 Anaconda 解釋器。
**解決方法：**
1. **手動選擇解釋器**：在 VS Code 中按下 `Ctrl + Shift + P`，輸入並選擇 `Python: Select Interpreter`，然後從清單中選擇路徑包含 `myenv` 的那一項。
2. **自動配置**：我已經為你建立了 `.vscode/settings.json`，強制 VS Code 使用專案目錄下的 `myenv`。
3. **重啟終端機**：關閉目前的終端機分頁並重新開啟一個新的，VS Code 應該會自動幫你執行 `activate.ps1`。

### Q: 執行 pip 指令出現「系統無法訪問此文件」或「Access is denied」？
這通常是因為 Windows 的權限限制或是 `pip.exe` 被防毒軟體暫時鎖定。
**解決方法：**
使用 Python 模組方式執行 pip，這能繞過直接呼叫 `.exe` 的權限問題：
```powershell
python -m pip install -r requirements.txt
```

## 4. 常見注意事項與維護

- **不要移動目錄**：虛擬環境內包含絕對路徑，若移動了專案資料夾，建議刪除 `myenv` 資料夾並重新建立。
- **Git 忽略**：在 `.gitignore` 中應加入 `myenv/`，不要將整個環境上傳到版本控制系統。
- **退出環境**：輸入 `deactivate` 即可回到全域環境。
- **版本衝突**：若 Manim 報錯，請檢查是否已啟動環境，並確認 `pip list` 中的套件版本是否正確。

---
*文件產生日期：2026-02-01*
