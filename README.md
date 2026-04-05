# Star Wars Genesis 日本語化パッチ

[English](#english) | [日本語](#日本語)

---

## 日本語

### 概要

[Star Wars Genesis](https://genesismodlist.com/) (Starfield Wabbajack Modlist) の日本語化パッチです。

MODで追加されたアイテム、スキル、パーク、クエスト目標、ロケーション、NPC、フォースパワーなどのテキストを日本語に翻訳します。

### 対応バージョン

| 項目 | バージョン |
|------|-----------|
| Star Wars Genesis | v8.7.0 (2026/03/13) |
| Starfield | v1.15.222 |
| 必須DLC | Shattered Space |

> **注意:** Star Wars Genesisのメジャーアップデート後は、新しいテキストが追加されている可能性があります。`--scan` コマンドで未翻訳テキストを確認し、必要に応じて翻訳辞書を更新してください。

### 翻訳状況

| 項目 | 数値 |
|------|------|
| 翻訳辞書エントリ | 4,405 |

翻訳対象:
- フォースパワー・ライトセーバー関連
- スキル・パーク・背景
- 武器・防具・アイテム・武器MOD
- クエスト目標・ロケーション
- NPC・エイリアン・クリーチャー
- 食料・飲料・素材
- 船・乗り物・船システム
- マンダロリアン・ベスカー関連
- ステータス効果・ダメージ種別
- ワークベンチ・クラフト関連

### 対象プラグイン

| MODフォルダ | プラグインファイ�� |
|---|---|
| Ascension - Gameplay Overhaul | Ascension.esm |
| Star Wars Blasters and Melee | Star Wars Blasters.esm |
| Star Wars Aliens | SW Aliens.esm |
| Star Wars Resources - Blasters | SW Blasters.esm |
| Star Wars - Mandalorian Forge Ruins | MandalorianForge.esm |
| Basic Sith Lightning | Basic Sith Lightning.esm |
| Star Wars Genesis - Override Patch | StarWarsGenesisOverridePatch.esm |

### 必要条件

- [Star Wars Genesis](https://genesismodlist.com/) v8.7.0以降がインストール済み
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

### 未翻訳テキストの確認

翻訳されていないテキストを確認するには、スキャンモードを使用します：

```batch
python full_translator.py --scan
```

スキャン結果は `untranslated_strings.txt` に出力され、未翻訳テキストが出現回数順にリストされます。このファイルを参考に `translations_*.py` に翻訳を追加できます。

### アンインストール方法

`uninstall.bat` をダブルクリックするか、`plugin_backups` フォルダ内のオリジナルファイルを各MODフォルダにコピーして戻してください。

### 注意事項

- 翻訳を適用する前に、元のプラグインファイルのバックアップが `plugin_backups` フォルダに自動作成されます
- Star Wars Genesisのアップデート後は再度翻訳を適用する必要があります
- 一部のテキスト（内部ID、システム文字列など）は意図的に翻訳されていません

### 貢献方法

翻訳の修正・追加は大歓迎です！

1. このリポジトリをフォーク
2. `--scan` で未翻訳テキストを確認
3. `translations_*.py` ファイルに翻訳を追加
4. プルリクエストを送信

翻訳辞書の形式:
```python
"English text": "日本語テキスト",
```

翻訳ファイルの構成:
| ファイル | 内容 |
|---|---|
| `translations_force.py` | フォースパワー関連 |
| `translations_backgrounds.py` | 背景・経歴 |
| `translations_skills.py` | スキル・パーク |
| `translations_items.py` | アイテム・装備 |
| `translations_bonuses.py` | ボーナス・効果 |
| `translations_misc.py` | その他全般（食料、NPC、武器MOD等） |

### ライセンス

MIT License - 詳細は [LICENSE](LICENSE) を参照

---

## English

### Overview

Japanese localization patch for [Star Wars Genesis](https://genesismodlist.com/) (Starfield Wabbajack Modlist).

Translates mod-added items, skills, perks, quest objectives, locations, NPCs, Force powers, and more into Japanese.

### Compatibility

| Item | Version |
|------|---------|
| Star Wars Genesis | v8.7.0 (2026/03/13) |
| Starfield | v1.15.222 |
| Required DLC | Shattered Space |

> **Note:** After major Star Wars Genesis updates, new text may have been added. Use the `--scan` command to check for untranslated text and update the translation dictionaries as needed.

### Translation Status

| Item | Value |
|------|-------|
| Dictionary Entries | 4,405 |

Translated content:
- Force powers & Lightsabers
- Skills, Perks & Backgrounds
- Weapons, Armor, Items & Weapon Mods
- Quest Objectives & Locations
- NPCs, Aliens & Creatures
- Food, Drinks & Materials
- Ships, Vehicles & Ship Systems
- Mandalorian & Beskar content
- Status Effects & Damage Types
- Workbenches & Crafting

### Target Plugins

| Mod Folder | Plugin File |
|---|---|
| Ascension - Gameplay Overhaul | Ascension.esm |
| Star Wars Blasters and Melee | Star Wars Blasters.esm |
| Star Wars Aliens | SW Aliens.esm |
| Star Wars Resources - Blasters | SW Blasters.esm |
| Star Wars - Mandalorian Forge Ruins | MandalorianForge.esm |
| Basic Sith Lightning | Basic Sith Lightning.esm |
| Star Wars Genesis - Override Patch | StarWarsGenesisOverridePatch.esm |

### Requirements

- [Star Wars Genesis](https://genesismodlist.com/) v8.7.0 or later installed
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

### Scanning for Untranslated Text

To check for untranslated text in your plugin files:

```batch
python full_translator.py --scan
```

Results are saved to `untranslated_strings.txt`, listing untranslated text sorted by frequency. Use this file as a reference to add translations to `translations_*.py`.

### Uninstallation

Double-click `uninstall.bat`, or copy the original files from `plugin_backups` folder back to each mod folder.

### Notes

- Original plugin files are automatically backed up to `plugin_backups` folder before translation
- Re-apply translations after Star Wars Genesis updates
- Some texts (internal IDs, system strings) are intentionally left untranslated

### Contributing

Contributions are welcome!

1. Fork this repository
2. Run `--scan` to find untranslated text
3. Add translations to `translations_*.py` files
4. Submit a pull request

Translation dictionary format:
```python
"English text": "日本語テキスト",
```

Translation file structure:
| File | Content |
|---|---|
| `translations_force.py` | Force powers |
| `translations_backgrounds.py` | Backgrounds & origins |
| `translations_skills.py` | Skills & perks |
| `translations_items.py` | Items & equipment |
| `translations_bonuses.py` | Bonuses & effects |
| `translations_misc.py` | Miscellaneous (food, NPCs, weapon mods, etc.) |

### License

MIT License - See [LICENSE](LICENSE) for details

---

## Credits

- [Star Wars Genesis](https://genesismodlist.com/) modlist by DeityVengy
- Translation by the community
