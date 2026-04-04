@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ============================================================
echo   Star Wars Genesis 日本語化パッチ インストーラー
echo   Japanese Localization Patch Installer
echo ============================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [エラー] Pythonが見つかりません。Python 3.10以上をインストールしてください。
    echo [Error] Python not found. Please install Python 3.10 or higher.
    echo.
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Get script directory
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Check if translation files exist
if not exist "full_translator.py" (
    echo [エラー] full_translator.py が見つかりません。
    echo [Error] full_translator.py not found.
    pause
    exit /b 1
)

echo [OK] Translation files found
echo.

REM Check mod folders
set "MODS_DIR=%SCRIPT_DIR%.."
set "MISSING=0"

echo Checking mod folders...
echo.

if not exist "%MODS_DIR%\Ascension - Gameplay Overhaul\Ascension.esm" (
    echo [警告] Ascension.esm not found
    set "MISSING=1"
)

if not exist "%MODS_DIR%\Star Wars Blasters and Melee\Star Wars Blasters.esm" (
    echo [警告] Star Wars Blasters.esm not found
    set "MISSING=1"
)

if not exist "%MODS_DIR%\Star Wars Genesis - Override Patch\StarWarsGenesisOverridePatch.esm" (
    echo [警告] StarWarsGenesisOverridePatch.esm not found
    set "MISSING=1"
)

if "%MISSING%"=="1" (
    echo.
    echo [警告] 一部のプラグインファイルが見つかりません。
    echo [Warning] Some plugin files not found.
    echo Star Wars Genesisが正しくインストールされているか確認してください。
    echo Please verify Star Wars Genesis is properly installed.
    echo.
    set /p "CONTINUE=続行しますか？ Continue anyway? (y/n): "
    if /i not "!CONTINUE!"=="y" (
        exit /b 1
    )
)

echo.
echo ============================================================
echo   翻訳を適用しています... / Applying translations...
echo ============================================================
echo.

python full_translator.py --apply

if errorlevel 1 (
    echo.
    echo [エラー] 翻訳の適用に失敗しました。
    echo [Error] Failed to apply translations.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   インストール完了！ / Installation Complete!
echo ============================================================
echo.
echo ゲームを起動して翻訳を確認してください。
echo Please launch the game to verify the translations.
echo.
echo バックアップは plugin_backups フォルダに保存されています。
echo Backups are saved in the plugin_backups folder.
echo.
pause
