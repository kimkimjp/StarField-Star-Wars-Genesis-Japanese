# Star Wars Genesis 日本語化パッチ

[English](#english) | [日本語](#日本語)

---

## 日本語

### 概要

[Star Wars Genesis](https://www.nexusmods.com/starfield/mods/7257) (Starfield Wabbajack Modlist) の日本語化パッチです。

MODで追加されたアイテム、スキル、パーク、クエスト目標、ロケーション、NPC、フォースパワーなどのテキストを日本語に翻訳します。

### 翻訳状況

| 項目 | 数値 |
|------|------|
| 翻訳辞書エントリ | 4,252 |
| 適用された翻訳 | 9,705 |
| 翻訳率 | 約48% |

翻訳対象:
- フォースパワー・ライトセーバー関連
- スキル・パーク・背景
- 武器・防具・アイテム
- クエスト目標・ロケーション
- NPC・エイリアン・クリーチャー
- 食料・飲料・素材
- 船・乗り物

### 必要条件

- [Star Wars Genesis](https://www.nexusmods.com/starfield/mods/7257) がインストール済み
- Python 3.10以上

### インストール方法

#### 方法1: 自動インストール (推奨)

1. このリポジトリをダウンロードまたはクローン
2. `install.bat` をダブルクリックして実行
3. 翻訳が自動的に適用されます

#### 方法2: 手動インストール

1. このリポジトリを `[Star Wars Genesis]\Game\mods\Star Wars Genesis Japanese` に配置
2. コマンドプロンプトを開き、以下を実行:

```batch
cd "[Star Wars Genesis]\Game\mods\Star Wars Genesis Japanese"
python full_translator.py --apply
```

### アンインストール方法

`plugin_backups` フォルダ内のオリジナルファイルを各MODフォルダにコピーして戻してください。

### 注意事項

- 翻訳を適用する前に、元のプラグインファイルのバックアップが `plugin_backups` フォルダに自動作成されます
- Star Wars Genesisのアップデート後は再度翻訳を適用する必要があります
- 一部のテキスト（内部ID、システム文字列など）は意図的に翻訳されていません

### 貢献方法

翻訳の修正・追加は大歓迎です！

1. このリポジトリをフォーク
2. `translations_*.py` ファイルに翻訳を追加
3. プルリクエストを送信

翻訳辞書の形式:
```python
"English text": "日本語テキスト",
```

### ライセンス

MIT License - 詳細は [LICENSE](LICENSE) を参照

---

## English

### Overview

Japanese localization patch for [Star Wars Genesis](https://www.nexusmods.com/starfield/mods/7257) (Starfield Wabbajack Modlist).

Translates mod-added items, skills, perks, quest objectives, locations, NPCs, Force powers, and more into Japanese.

### Translation Status

| Item | Value |
|------|-------|
| Dictionary Entries | 4,252 |
| Applied Translations | 9,705 |
| Translation Rate | ~48% |

Translated content:
- Force powers & Lightsabers
- Skills, Perks & Backgrounds
- Weapons, Armor & Items
- Quest Objectives & Locations
- NPCs, Aliens & Creatures
- Food, Drinks & Materials
- Ships & Vehicles

### Requirements

- [Star Wars Genesis](https://www.nexusmods.com/starfield/mods/7257) installed
- Python 3.10+

### Installation

#### Method 1: Automatic Install (Recommended)

1. Download or clone this repository
2. Double-click `install.bat` to run
3. Translations will be applied automatically

#### Method 2: Manual Install

1. Place this repository at `[Star Wars Genesis]\Game\mods\Star Wars Genesis Japanese`
2. Open Command Prompt and run:

```batch
cd "[Star Wars Genesis]\Game\mods\Star Wars Genesis Japanese"
python full_translator.py --apply
```

### Uninstallation

Copy the original files from `plugin_backups` folder back to each mod folder.

### Notes

- Original plugin files are automatically backed up to `plugin_backups` folder before translation
- Re-apply translations after Star Wars Genesis updates
- Some texts (internal IDs, system strings) are intentionally left untranslated

### Contributing

Contributions are welcome!

1. Fork this repository
2. Add translations to `translations_*.py` files
3. Submit a pull request

Translation dictionary format:
```python
"English text": "日本語テキスト",
```

### License

MIT License - See [LICENSE](LICENSE) for details

---

## Credits

- Star Wars Genesis Modlist creators
- Translation by the community
