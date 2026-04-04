@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ============================================================
echo   Star Wars Genesis 日本語化パッチ アンインストーラー
echo   Japanese Localization Patch Uninstaller
echo ============================================================
echo.

set "SCRIPT_DIR=%~dp0"
set "BACKUP_DIR=%SCRIPT_DIR%plugin_backups"
set "MODS_DIR=%SCRIPT_DIR%.."

if not exist "%BACKUP_DIR%" (
    echo [エラー] バックアップフォルダが見つかりません。
    echo [Error] Backup folder not found.
    echo.
    echo plugin_backups フォルダが存在しない場合、手動で元のプラグインを
    echo 再インストールする必要があります。
    pause
    exit /b 1
)

echo バックアップから元のプラグインファイルを復元します。
echo Restoring original plugin files from backup.
echo.

set /p "CONFIRM=続行しますか？ Continue? (y/n): "
if /i not "%CONFIRM%"=="y" (
    echo キャンセルしました。
    exit /b 0
)

echo.

REM Restore each plugin
set "RESTORED=0"

if exist "%BACKUP_DIR%\Ascension.esm" (
    copy /y "%BACKUP_DIR%\Ascension.esm" "%MODS_DIR%\Ascension - Gameplay Overhaul\Ascension.esm" >nul
    echo [OK] Ascension.esm restored
    set /a "RESTORED+=1"
)

if exist "%BACKUP_DIR%\Star Wars Blasters.esm" (
    copy /y "%BACKUP_DIR%\Star Wars Blasters.esm" "%MODS_DIR%\Star Wars Blasters and Melee\Star Wars Blasters.esm" >nul
    echo [OK] Star Wars Blasters.esm restored
    set /a "RESTORED+=1"
)

if exist "%BACKUP_DIR%\SW Aliens.esm" (
    copy /y "%BACKUP_DIR%\SW Aliens.esm" "%MODS_DIR%\Star Wars Aliens\SW Aliens.esm" >nul
    echo [OK] SW Aliens.esm restored
    set /a "RESTORED+=1"
)

if exist "%BACKUP_DIR%\SW Blasters.esm" (
    copy /y "%BACKUP_DIR%\SW Blasters.esm" "%MODS_DIR%\Star Wars Resources - Blasters\SW Blasters.esm" >nul
    echo [OK] SW Blasters.esm restored
    set /a "RESTORED+=1"
)

if exist "%BACKUP_DIR%\MandalorianForge.esm" (
    copy /y "%BACKUP_DIR%\MandalorianForge.esm" "%MODS_DIR%\Star Wars - Mandalorian Forge Ruins\MandalorianForge.esm" >nul
    echo [OK] MandalorianForge.esm restored
    set /a "RESTORED+=1"
)

if exist "%BACKUP_DIR%\Basic Sith Lightning.esm" (
    copy /y "%BACKUP_DIR%\Basic Sith Lightning.esm" "%MODS_DIR%\Basic Sith Lightning\Basic Sith Lightning.esm" >nul
    echo [OK] Basic Sith Lightning.esm restored
    set /a "RESTORED+=1"
)

if exist "%BACKUP_DIR%\StarWarsGenesisOverridePatch.esm" (
    copy /y "%BACKUP_DIR%\StarWarsGenesisOverridePatch.esm" "%MODS_DIR%\Star Wars Genesis - Override Patch\StarWarsGenesisOverridePatch.esm" >nul
    echo [OK] StarWarsGenesisOverridePatch.esm restored
    set /a "RESTORED+=1"
)

echo.
echo ============================================================
echo   アンインストール完了！ / Uninstallation Complete!
echo   %RESTORED% ファイルを復元しました。 / %RESTORED% files restored.
echo ============================================================
echo.
pause
