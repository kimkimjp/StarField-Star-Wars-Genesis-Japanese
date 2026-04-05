#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Star Wars Genesis - Full Text Translator
Imports all translation modules and applies them to plugin files
"""

import os
import struct
import shutil
import zlib

# Import all translation modules
from translations_force import FORCE_TRANSLATIONS
from translations_backgrounds import BACKGROUND_TRANSLATIONS
from translations_skills import SKILL_TRANSLATIONS
from translations_items import ITEM_TRANSLATIONS
from translations_bonuses import BONUS_TRANSLATIONS
from translations_misc import MISC_TRANSLATIONS

# Merge all translations into one dictionary
FULL_TRANSLATIONS = {}
FULL_TRANSLATIONS.update(FORCE_TRANSLATIONS)
FULL_TRANSLATIONS.update(BACKGROUND_TRANSLATIONS)
FULL_TRANSLATIONS.update(SKILL_TRANSLATIONS)
FULL_TRANSLATIONS.update(ITEM_TRANSLATIONS)
FULL_TRANSLATIONS.update(BONUS_TRANSLATIONS)
FULL_TRANSLATIONS.update(MISC_TRANSLATIONS)

# Additional translations not in modules
ADDITIONAL_TRANSLATIONS = {
    # === Challenge descriptions ===
    "Kill <repetitions> enemies with a rifle.":
        "ライフルで<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies with pistols.":
        "ピストルで<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies with a pistol.":
        "ピストルで<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies with a shotgun.":
        "ショットガンで<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies with a heavy weapon.":
        "ヘビーウェポンで<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies with a laser weapon.":
        "レーザー武器で<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies with explosives.":
        "爆発物で<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies with explosives":
        "爆発物で<repetitions>体の敵を倒す",
    "Kill <repetitions> enemies with an energy weapon.":
        "エネルギー武器で<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies with a ballistic weapon":
        "バリスティック武器で<repetitions>体の敵を倒す",
    "Kill <repetitions> enemies using a scoped weapon.":
        "スコープ付き武器で<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies in Zero G environments.":
        "無重力環境で<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies in Zero-G environments.":
        "無重力環境で<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies with a non-automatic weapon":
        "非自動武器で<repetitions>体の敵を倒す",
    "Kill <repetitions> enemies with non-automatic weapons.":
        "非自動武器で<repetitions>体の敵を倒す。",
    "Kill <repetitions> enemies while not in command of a follower.":
        "フォロワーを連れていない状態で<repetitions>体の敵を倒す。",
    "Heal <repetitions> damage.":
        "<repetitions>のダメージを回復。",
    "Take <repetitions> fall damage.":
        "<repetitions>の落下ダメージを受ける。",
    "Take <repetitions> points of energy damage.":
        "<repetitions>ポイントのエネルギーダメージを受ける。",
    "Take <repetitions> points of physical damage.":
        "<repetitions>ポイントの物理ダメージを受ける。",
    "Perform <repetitions> sneak attacks.":
        "<repetitions>回のスニークアタックを行う。",
    "Successfully pickpocket <repetitions> times.":
        "<repetitions>回のスリに成功する。",
    "Successfully Manipulate <repetitions> different people.":
        "<repetitions>人の異なる人物の操作に成功する。",
    "Boost jump <repetitions> times while in combat.":
        "戦闘中に<repetitions>回ブーストジャンプする。",
    "Destroy or board <repetitions> ships with a crew of 2 or more.":
        "クルー2人以上の船を<repetitions>隻破壊または乗り込む。",
    "Destroy or board <repetitions> ships with a crew of 5 or more.":
        "クルー5人以上の船を<repetitions>隻破壊または乗り込む。",
    "Destroy or board <repetitions> ships with a crew of 4 or more.":
        "クルー4人以上の船を<repetitions>隻破壊または乗り込む。",
    "Destroy <repetitions> enemy ships while in targeting mode.":
        "ターゲティングモードで<repetitions>隻の敵船を破壊。",
    "Deal <repetitions> damage to enemy ships with EM weapons.":
        "EM武器で敵船に<repetitions>ダメージを与える。",
    "Deal <repetitions> damage to enemy ships with Energy weapons.":
        "エネルギー武器で敵船に<repetitions>ダメージを与える。",
    "Deal <repetitions> damage to enemy ships with missile weapons.":
        "ミサイル武器で敵船に<repetitions>ダメージを与える。",
    "Deal <repetitions> damage to enemy ships with ballistic weapons. ":
        "バリスティック武器で敵船に<repetitions>ダメージを与える。",
    "Deal <repetitions> damage to enemy ships with particle beam weapons.":
        "パーティクルビーム武器で敵船に<repetitions>ダメージを与える。",
    "Deal <repetitions> damage to enemy ships with automated turret weapons.":
        "自動タレット武器で敵船に<repetitions>ダメージを与える。",
    "Deal <repetitions> damage to enemy ships with automated turret weapons. ":
        "自動タレット武器で敵船に<repetitions>ダメージを与える。",

    # === Crew/Companion ===
    "You can have up to ten active crew members.":
        "最大10人のアクティブなクルーメンバーを持てる。",
    "You can have up to seven active crew members.":
        "最大7人のアクティブなクルーメンバーを持てる。",
    "You can have up to twelve active crew members.":
        "最大12人のアクティブなクルーメンバーを持てる。",
    "You can have up to fifteen active crew members.":
        "最大15人のアクティブなクルーメンバーを持てる。",
    "Companions gain affinity 25% faster.":
        "コンパニオンの好感度が25%早く上昇。",
    "Companions have 50 more health and 50kg more carrying capacity.":
        "コンパニオンの体力+50、積載量+50kg。",
    "Companions will occasionally heal you when you get low health. ":
        "コンパニオンが体力が低い時に時々回復してくれる。",
    "Doubles the bonuses of Combat and Physical Crew Skills on Companions. Companions have a chance to pick themselves up from a downed state.":
        "コンパニオンの戦闘とフィジカルクルースキルのボーナスを2倍にする。コンパニオンがダウン状態から自力で起き上がる可能性がある。",
    "Crew: Follower gains a Chameleon-like effect when motionless and sneaking":
        "クルー：フォロワーが静止してスニーキング中にカメレオンのような効果を得る",
    "Crew: Companion is 25% harder to detect when sneaking":
        "クルー：コンパニオンがスニーキング中に25%発見されにくくなる",
    "Crew: Followers no longer set off enemy mines.":
        "クルー：フォロワーが敵の地雷を作動させなくなる。",

    # === Manipulation/Control ===
    "Manipulated targets now obey commands for a substantial amount of time.":
        "操作されたターゲットがかなりの時間命令に従う。",
    "You can force a target NPC at or below your level to obey commands for a limited time.":
        "自分のレベル以下のNPCを限られた時間命令に従わせることができる。",
    "You can force a target NPC up to 10 levels higher than you to obey commands for a limited time.":
        "自分より最大10レベル高いNPCを限られた時間命令に従わせることができる。",
    "You can force a target NPC up to 20 levels higher than you to obey commands for a limited time.":
        "自分より最大20レベル高いNPCを限られた時間命令に従わせることができる。",
    "You can force a target NPC at or below your level to stop fighting for a while.":
        "自分のレベル以下のNPCを一時的に戦闘を止めさせることができる。",
    "You can force a target NPC up to 10 levels higher than you to stop fighting for a while.":
        "自分より最大10レベル高いNPCを一時的に戦闘を止めさせることができる。",
    "You can force a target NPC up to 20 levels higher than you to stop fighting for a while.":
        "自分より最大20レベル高いNPCを一時的に戦闘を止めさせることができる。",
    "You can force a target NPC at or below your level to flee for a limited time.":
        "自分のレベル以下のNPCを限られた時間逃走させることができる。",
    "You can force a target NPC up to 10 levels higher than you to flee for a limited time.":
        "自分より最大10レベル高いNPCを限られた時間逃走させることができる。",
    "You can force a target NPC up to 20 levels higher than you to flee for a limited time.":
        "自分より最大20レベル高いNPCを限られた時間逃走させることができる。",
    "You can force a target NPC at or below your level to attack their allies for a limited time.":
        "自分のレベル以下のNPCを限られた時間味方を攻撃させることができる。",
    "You can force a target NPC up to 10 levels higher than you to attack their allies for a limited time.":
        "自分より最大10レベル高いNPCを限られた時間味方を攻撃させることができる。",
    "You can force a target NPC up to 20 levels higher than you to attack their allies for a limited time.":
        "自分より最大20レベル高いNPCを限られた時間味方を攻撃させることができる。",
    "You can force target NPCs to permanently stop fighting (unless they're attacked again).":
        "ターゲットNPCを恒久的に戦闘を止めさせることができる（再度攻撃されない限り）。",
    "Enemies affected by Instigation will attack their allies until they are dead.":
        "扇動の影響を受けた敵は死ぬまで味方を攻撃する。",
    "Intimidated targets now flee for substantial amount of time.":
        "威嚇されたターゲットがかなりの時間逃走する。",

    # === Creature control ===
    "You can force a target alien creature up to 10 levels higher than you to attack their allies for a limited time.":
        "自分より最大10レベル高いエイリアンクリーチャーを限られた時間味方を攻撃させることができる。",
    "You can force a target alien creature up to 10 levels higher than you to stop fighting for a limited time.":
        "自分より最大10レベル高いエイリアンクリーチャーを限られた時間戦闘を止めさせることができる。",
    "You can force a target alien creature up to 10 levels higher than you to flee for a limited time.":
        "自分より最大10レベル高いエイリアンクリーチャーを限られた時間逃走させることができる。",
    "You can force a target creature up to 10 levels higher than you to obey commands for a limited time.":
        "自分より最大10レベル高いクリーチャーを限られた時間命令に従わせることができる。",

    # === Robot control ===
    "You deal 30% more damage to Robots and Turrets. You can force a target robot up to 10 levels higher than you to attack their allies for a limited time.":
        "ロボットとタレットへのダメージが30%増加。自分より最大10レベル高いロボットを限られた時間味方を攻撃させることができる。",
    "You deal 10% more damage to Robots and Turrets. You can force a target robot up to 10 levels higher than you to stop fighting for a limited time.":
        "ロボットとタレットへのダメージが10%増加。自分より最大10レベル高いロボットを限られた時間戦闘を止めさせることができる。",
    "You can force a target robot up to 10 levels higher than you to obey commands for a limited time.":
        "自分より最大10レベル高いロボットを限られた時間命令に従わせることができる。",

    # === Research/Craft ===
    "You can create improved chems.":
        "改良型ケミカルを作成可能。",
    "You can create superior chems.":
        "上級ケミカルを作成可能。",
    "You can create cutting-edge chems.":
        "最先端ケミカルを作成可能。",
    "You can craft gourmet food and drinks.":
        "グルメフードと飲料を作成可能。",
    "You can craft specialty food and drinks.":
        "特製フードと飲料を作成可能。",
    "You can craft food and drink delicacies.":
        "高級フードと飲料を作成可能。",
    "Crafting food and drinks occasionally doesn't use up resources. You can craft exotic recipes.":
        "食べ物と飲み物の作成時に時々資源を消費しない。エキゾチックなレシピを作成可能。",
    "Crafting chems occasionally triples the amount created.":
        "ケミカル作成時に時々作成量が3倍になる。",
    "You can research basic magazine and ammo upgrades.":
        "基本的なマガジンと弾薬アップグレードを研究可能。",
    "You can research master magazine and ammo upgrades.":
        "マスターマガジンと弾薬アップグレードを研究可能。",
    "You can research improved magazine and ammo upgrades.":
        "改良型マガジンと弾薬アップグレードを研究可能。",
    "You can research experimental projects at a Research Lab.":
        "研究ラボで実験プロジェクトを研究可能。",
    "You can research and construct superior outpost modules.":
        "上級アウトポストモジュールを研究・建設可能。",
    "You can research and construct cutting-edge outpost modules.":
        "最先端アウトポストモジュールを研究・建設可能。",
    "You can construct improved outpost modules, and research additional modules at a Research Lab.":
        "改良型アウトポストモジュールを建設可能。研究ラボで追加モジュールを研究可能。",
    "You can craft improved weapon mods at a Weapon Workbench, and research additional weapon mods at a Research Lab.":
        "武器ワークベンチで改良型武器モッドを作成可能。研究ラボで追加武器モッドを研究可能。",
    "You can craft improved spacesuit, helmet, and pack mods, and research additional mods at a Research Lab.":
        "改良型宇宙服、ヘルメット、パックモッドを作成可能。研究ラボで追加モッドを研究可能。",
    "You can research and craft superior weapon mods.":
        "上級武器モッドを研究・作成可能。",
    "You can research and craft cutting-edge weapon mods.":
        "最先端武器モッドを研究・作成可能。",
    "You can research and craft master-level weapon mods.":
        "マスターレベル武器モッドを研究・作成可能。",
    "You can research and craft superior spacesuit, helmet, and pack mods.":
        "上級宇宙服、ヘルメット、パックモッドを研究・作成可能。",
    "You can research and craft cutting-edge spacesuit, helmet, and pack mods.":
        "最先端宇宙服、ヘルメット、パックモッドを研究・作成可能。",
    "Construction of spacesuit, helmet, and pack mods occasionally doesn't cost resources.":
        "宇宙服、ヘルメット、パックモッドの建設時に時々資源を消費しない。",
    "You can craft rare manufactured components at an Industrial Workbench.":
        "産業ワークベンチで希少な製造コンポーネントを作成可能。",
    "You can craft exotic manufactured components at an Industrial Workbench.":
        "産業ワークベンチでエキゾチックな製造コンポーネントを作成可能。",
    "You can craft unique manufactured components at an Industrial Workbench. Outpost extractors have a chance to produce additional resources.":
        "産業ワークベンチでユニークな製造コンポーネントを作成可能。アウトポストの抽出機が追加資源を生産する可能性がある。",
    "Sudden developments during research are twice as common. Resources required to craft items and complete research projects is reduced by 60%.":
        "研究中の突発的な進展が2倍の頻度で発生。アイテム作成と研究プロジェクト完了に必要な資源が60%減少。",
    "Resources required to craft items and complete research projects is reduced by 10%.":
        "アイテム作成と研究プロジェクト完了に必要な資源が10%減少。",
    "Resources required to craft items and complete research projects is reduced by 20%.":
        "アイテム作成と研究プロジェクト完了に必要な資源が20%減少。",
    "Resources required to craft items and complete research projects is reduced by 40%.":
        "アイテム作成と研究プロジェクト完了に必要な資源が40%減少。",

    # === Pickpocket ===
    "10% greater chance to successfully pickpocket.":
        "スリの成功率が10%上昇。",
    "20% greater chance to successfully pickpocket.":
        "スリの成功率が20%上昇。",
    "30% greater chance to successfully pickpocket.":
        "スリの成功率が30%上昇。",
    "50% greater chance to successfully pickpocket. Can now pickpocket holstered weapons.":
        "スリの成功率が50%上昇。収納中の武器もスリ可能。",

    # === Commerce ===
    "Buy for 5% less and sell for 2% more.":
        "購入価格5%減、売却価格2%増。",
    "Buy for 10% less and sell for 4% more.":
        "購入価格10%減、売却価格4%増。",
    "Buy for 15% less and sell for 6% more.":
        "購入価格15%減、売却価格6%増。",
    "Buy for 20% less and sell for 10% more.":
        "購入価格20%減、売却価格10%増。",

    # === Persuasion ===
    "10% increased chance of success when persuading someone.":
        "説得の成功確率が10%上昇。",
    "20% increased chance of success when persuading someone.":
        "説得の成功確率が20%上昇。",
    "30% increased chance of success when persuading someone.":
        "説得の成功確率が30%上昇。",
    "50% increased chance of success when persuading someone.":
        "説得の成功確率が50%上昇。",
    "You now have access to Bribery in speech challenges.":
        "会話チャレンジで賄賂オプションが使用可能に。",
    "Occasionally, bribery won't cost any money.":
        "時々、賄賂がお金を消費しない。",

    # === Hacking ===
    "You can attempt to hack Advanced locks, and 2 auto attempts can be banked.":
        "高度なロックのハッキングが可能。自動試行を2回まで蓄積可能。",
    "You can attempt to hack Expert locks, and 3 auto attempts can be banked. Rings now turn blue when the pick can be slotted.":
        "エキスパートロックのハッキングが可能。自動試行を3回まで蓄積可能。ピックを差し込めるときリングが青く変わる。",
    "You can attempt to hack Master-level locks, and 4 auto attempts can be banked.":
        "マスターレベルロックのハッキングが可能。自動試行を4回まで蓄積可能。",
    "Expend a digipick to eliminate keys that aren't required to solve the puzzle. 5 auto attempts can be banked.":
        "デジピックを消費してパズルの解決に不要なキーを除去。自動試行を5回まで蓄積可能。",

    # === Piloting ===
    "Unlock the ability to pilot Class B ships.":
        "クラスB船の操縦能力をアンロック。",
    "Unlock the ability to pilot Class C ships.":
        "クラスC船の操縦能力をアンロック。",
    "You can now utilize ship thrusters. ":
        "宇宙船スラスターの使用が可能に。",
    "Allows the installation of improved ship modules.":
        "改良型宇宙船モジュールのインストールが可能。",
    "Allows the installation of superior ship modules.":
        "上級宇宙船モジュールのインストールが可能。",
    "Allows the installation of cutting-edge ship modules.":
        "最先端宇宙船モジュールのインストールが可能。",
    "Allows the installation of experimental ship modules.":
        "実験的宇宙船モジュールのインストールが可能。",

    # === Piracy ===
    "Ships 10% stronger will automatically surrender to piracy demands. Enemy contraband scans are 10% less effective.":
        "10%強い船が自動的に海賊要求に降伏する。敵の禁制品スキャンの効果が10%減少。",
    "Ships 20% stronger will automatically surrender to piracy demands. Enemy contraband scans are 20% less effective.":
        "20%強い船が自動的に海賊要求に降伏する。敵の禁制品スキャンの効果が20%減少。",
    "Ships 30% stronger will automatically surrender to piracy demands. Enemy contraband scans are 30% less effective.":
        "30%強い船が自動的に海賊要求に降伏する。敵の禁制品スキャンの効果が30%減少。",
    "Ships 50% stronger will automatically surrender to piracy demands. Enemy contraband scans are 50% less effective.":
        "50%強い船が自動的に海賊要求に降伏する。敵の禁制品スキャンの効果が50%減少。",

    # === Scanning ===
    "You can scan the moons of your current planet. You have a 10% chance to discover a trait when scanning.":
        "現在の惑星の衛星をスキャン可能。スキャン時に10%の確率でトレイトを発見。",
    "You can scan any planet or moon in this system. You have a 20% chance to discover a trait when scanning.":
        "このシステム内の全ての惑星と衛星をスキャン可能。スキャン時に20%の確率でトレイトを発見。",
    "You can scan any planet or moon within 16 Light Years. You have a 30% chance to discover a trait when scanning.":
        "16光年以内の全ての惑星と衛星をスキャン可能。スキャン時に30%の確率でトレイトを発見。",
    "You can scan any planet or moon within 30 Light Years. You have a 50% chance to discover a trait when scanning.":
        "30光年以内の全ての惑星と衛星をスキャン可能。スキャン時に50%の確率でトレイトを発見。",
    "You can detect uncommon inorganic resources on planet and moon surfaces, and more information about ships in space.":
        "惑星と衛星の表面でアンコモン無機資源を検出可能。宇宙の船についてのより多くの情報を取得。",
    "You can detect rare inorganic resources on planet and moon surfaces, and more specific information about ships in space.":
        "惑星と衛星の表面でレア無機資源を検出可能。宇宙の船についてのより具体的な情報を取得。",
    "You can detect exotic inorganic resources on planet and moon surfaces, and gain better combat information on ships in space.":
        "惑星と衛星の表面でエキゾチック無機資源を検出可能。宇宙の船についてのより良い戦闘情報を取得。",
    "You can detect unique inorganic resources on planet and moon surfaces, and gain a complete list of cargo on ships in space.":
        "惑星と衛星の表面でユニーク無機資源を検出可能。宇宙の船の貨物の完全なリストを取得。",
    "Adds an optional zoom to the hand scanner, and scan distance is increased to 20 meters.":
        "ハンドスキャナーにオプションのズームを追加。スキャン距離が20メートルに増加。",
    "Adds another level of zoom to the hand scanner, and scan distance is increased to 30 meters.":
        "ハンドスキャナーに別のズームレベルを追加。スキャン距離が30メートルに増加。",
    "Adds another level of zoom to the hand scanner, and scan distance is increased to 40 meters.":
        "ハンドスキャナーに別のズームレベルを追加。スキャン距離が40メートルに増加。",
    "Adds another level of zoom to the hand scanner, and scan distance is increased to 50 meters.":
        "ハンドスキャナーに別のズームレベルを追加。スキャン距離が50メートルに増加。",
    "Tracked resources will get highlighted when using the hand scanner.":
        "ハンドスキャナー使用時に追跡中の資源がハイライト表示される。",

    # === Zoology/Botany ===
    "Get more common organic resources from creatures and harvest from them without harming them, learn additional info about them from the scanner, and allows you to produce animal resources at your outposts.":
        "クリーチャーからより多くのコモン有機資源を取得し、傷つけずに収穫できる。スキャナーから追加情報を得られ、アウトポストで動物資源を生産可能。",
    "Get more uncommon organic resources from creatures, and learn information about them more quickly using the scanner.":
        "クリーチャーからより多くのアンコモン有機資源を取得。スキャナーを使ってより早く情報を得る。",
    "Get more rare organic resources from creatures, and learn information about them more quickly using the scanner.":
        "クリーチャーからより多くのレア有機資源を取得。スキャナーを使ってより早く情報を得る。",
    "Occasionally harvest additional rarer resources from creatures, and learn information about them more quickly using the scanner.":
        "クリーチャーから時々追加のレア資源を収穫。スキャナーを使ってより早く情報を得る。",
    "Get more common and uncommon organic resources from plants, learn additional info about them from the scanner, and allows some plants to be cultivated at your outposts.":
        "植物からより多くのコモンとアンコモン有機資源を取得。スキャナーから追加情報を得られ、アウトポストで一部の植物を栽培可能。",
    "Get more rare organic resources from plants, and learn information about them more quickly using the scanner.":
        "植物からより多くのレア有機資源を取得。スキャナーを使ってより早く情報を得る。",
    "Get more exotic organic resources from plants, and learn information about them more quickly using the scanner.":
        "植物からより多くのエキゾチック有機資源を取得。スキャナーを使ってより早く情報を得る。",
    "Occasionally harvest additional rarer resources from plants, and learn information about them more quickly using the scanner.":
        "植物から時々追加のレア資源を収穫。スキャナーを使ってより早く情報を得る。",
    "Get more common and uncommon inorganic resources from surface objects.":
        "表面オブジェクトからより多くのコモンとアンコモン無機資源を取得。",
    "Get more rare inorganic resources from surface objects.":
        "表面オブジェクトからより多くのレア無機資源を取得。",
    "Get more exotic inorganic resources from surface objects.":
        "表面オブジェクトからより多くのエキゾチック無機資源を取得。",
    "Occasionally harvest additional rarer resources from surface objects.":
        "表面オブジェクトから時々追加のレア資源を収穫。",

    # === Outpost building ===
    "You can build outposts on planets with extreme temperatures (Deep Freeze and Inferno). Increase the maximum number of Outposts you can build by 4.":
        "極端な温度の惑星（ディープフリーズとインフェルノ）にアウトポストを建設可能。建設可能なアウトポストの最大数が4増加。",
    "You can build outposts on planets with extreme gravity. Increase the maximum number of Outposts you can build by 16.":
        "極端な重力の惑星にアウトポストを建設可能。建設可能なアウトポストの最大数が16増加。",
    "You can build outposts on planets with extreme pressure. Increase the maximum number of Outposts you can build by 8.":
        "極端な気圧の惑星にアウトポストを建設可能。建設可能なアウトポストの最大数が8増加。",
    "You can build outposts on planets with toxic or corrosive atmospheres. Increase the maximum number of Outposts you can build by 12.":
        "有毒または腐食性の大気を持つ惑星にアウトポストを建設可能。建設可能なアウトポストの最大数が12増加。",
    "Outpost modules now cost 50% fewer resources to build. ":
        "アウトポストモジュールの建設に必要な資源が50%減少。",
    "Outposts permanently produce resouces 5% faster.":
        "アウトポストの資源生産が恒久的に5%高速化。",
    "Increases the production rate of inorganic resources by 10%.":
        "無機資源の生産率が10%増加。",
    "Increases the production rate of organic resources by 10%.":
        "有機資源の生産率が10%増加。",

    # === Targeting mode ===
    "Time to lock onto enemy ships is reduced by 15%. ":
        "敵船へのロックオン時間が15%短縮。",
    "Time to lock onto enemy ships is reduced by 60%. Deal 20% increased system damage in targeting mode.":
        "敵船へのロックオン時間が60%短縮。ターゲティングモードでシステムダメージが20%増加。",
    "Time to lock onto enemy ships is reduced by 30%. You have a 10% increased chance of critically hitting a target-locked ship.":
        "敵船へのロックオン時間が30%短縮。ロックオンした敵船へのクリティカル率が10%上昇。",

    # === Lone Wolf bonuses ===
    "Gain 30 Damage Resistance for each Spacesuit and Helmet equipped when you don't have a companion or any crew.":
        "コンパニオンやクルーがいない時、装備した宇宙服とヘルメットごとにダメージ耐性30を獲得。",
    "Gain 60 Damage Resistance for each Spacesuit and Helmet equipped when you don't have a companion or any crew.":
        "コンパニオンやクルーがいない時、装備した宇宙服とヘルメットごとにダメージ耐性60を獲得。",
    "Gain 90 Damage Resistance for each Spacesuit and Helmet equipped when you don't have a companion or any crew.":
        "コンパニオンやクルーがいない時、装備した宇宙服とヘルメットごとにダメージ耐性90を獲得。",
    "Gain 120 Damage Resistance for each Spacesuit and Helmet equipped when you don't have a companion or any crew.":
        "コンパニオンやクルーがいない時、装備した宇宙服とヘルメットごとにダメージ耐性120を獲得。",

    # === Infection/Injury recovery ===
    "Slightly increased chance to recover from injuries naturally.":
        "負傷から自然に回復する確率がわずかに上昇。",
    "Moderately increased chance to recover from injuries naturally.":
        "負傷から自然に回復する確率が適度に上昇。",
    "Noticeably increased chance to recover from injuries naturally.":
        "負傷から自然に回復する確率が顕著に上昇。",
    "Slightly increased chance to recover from infections naturally.":
        "感染から自然に回復する確率がわずかに上昇。",
    "Moderately increased chance to recover from infections naturally.":
        "感染から自然に回復する確率が適度に上昇。",
    "Noticeably increased chance to recover from infections naturally.":
        "感染から自然に回復する確率が顕著に上昇。",
    "Greatly increased chance to recover from infections naturally. 20% chance of not gaining an infection when you otherwise would.":
        "感染から自然に回復する確率が大幅に上昇。感染するはずだった時に20%の確率で感染しない。",
    "20% chance of not gaining an injury when you otherwise would.":
        "負傷するはずだった時に20%の確率で負傷しない。",
    "Reduced chance to gain afflictions from environmental damage sources.":
        "環境ダメージ源からの苦痛を得る確率が減少。",
    "Gain 10 resistance to Airborne environmental damage.":
        "空気感染環境ダメージへの耐性10を獲得。",
    "Gain 10 resistance to Thermal environmental damage.":
        "熱環境ダメージへの耐性10を獲得。",
    "Gain 10 resistance to Corrosive and Radiation environmental damage.":
        "腐食と放射線環境ダメージへの耐性10を獲得。",

    # === Aiming accuracy ===
    "All weapons have increased aim down sights accuracy by 25%":
        "全ての武器の照準精度が25%増加。",
    "All weapons have increased aim down sights accuracy by 50%":
        "全ての武器の照準精度が50%増加。",
    "All weapons have increased aim down sights accuracy by 75%":
        "全ての武器の照準精度が75%増加。",
    "All weapons have increased aim down sights accuracy by 99% and 30% increased range.":
        "全ての武器の照準精度が99%増加し、射程が30%増加。",

    # === Misc food bonuses ===
    "Food and drink are 10% more effective.":
        "食べ物と飲み物の効果が10%向上。",
    "Food and drink are now 20% more effective.":
        "食べ物と飲み物の効果が20%向上。",
    "Food and drink are now 30% more effective.":
        "食べ物と飲み物の効果が30%向上。",
    "Food and drink are now 50% more effective.":
        "食べ物と飲み物の効果が50%向上。",
    "Healing items are permanently 5% more effective.":
        "回復アイテムの効果が恒久的に5%向上。",

    # === Misc loot bonuses ===
    "There's a chance you'll find extra aid items, like Med Packs or chems, when searching containers.":
        "コンテナを探索する時、メドパックやケミカルなどの追加回復アイテムを見つける可能性がある。",
    "There's a chance you'll find extra credits when searching containers.":
        "コンテナを探索する時、追加クレジットを見つける可能性がある。",
    "There's a chance you'll find extra ammo when searching containers.":
        "コンテナを探索する時、追加弾薬を見つける可能性がある。",

    # === Human enemy bonuses ===
    "Human enemies have a 30% increased chance to enter a downed state after taking enough damage.":
        "人間の敵が十分なダメージを受けた後にダウン状態になる確率が30%上昇。",
    "Humanoid enemies have a 50% increased chance to not naturally recover from a downed state.":
        "ヒューマノイドの敵がダウン状態から自然に回復しない確率が50%上昇。",
    "Human enemies now can enter a downed state earlier.":
        "人間の敵がより早くダウン状態になる。",
    "Previous ranks now apply to all enemy types. You now do 100% more damage to downed enemies.":
        "前のランクが全ての敵タイプに適用されるようになる。ダウンした敵へのダメージが100%増加。",

    # === Ship repair ===
    "Occasionally, repairing one block of a system will repair the entire system.":
        "時々、システムの1ブロックを修理すると、システム全体が修理される。",
    "Used to repair spaceship hull damage.":
        "宇宙船の船体ダメージを修理するために使用。",

    # === Weapon magazine perks ===
    "Slightly increases magazine size and weapon bash critical chance for all BlasTech blasters.":
        "全てのブラステック製ブラスターのマガジンサイズと武器バッシュクリティカル率がわずかに増加。",
    "Further increases magazine size and weapon bash critical chance for all BlasTech blasters.":
        "全てのブラステック製ブラスターのマガジンサイズと武器バッシュクリティカル率がさらに増加。",
    "Permanently increases blaster damage by 5%.":
        "ブラスターダメージが恒久的に5%増加。",
    "Permanently increases energy damage by 5%.":
        "エネルギーダメージが恒久的に5%増加。",
    "Permanently increases stun damage by 5%.":
        "スタンダメージが恒久的に5%増加。",
    "Permanently do 5% more damage to droids.":
        "ドロイドへのダメージが恒久的に5%増加。",

    # === Time-related ===
    "Pain hurts - but only if you're not strong enough to take it.":
        "痛みは辛い——だが、それに耐えられるだけの強さがあれば別だ。",
    "Time itself is yours to manipulate, as you slow the world... and all those in it.":
        "時間そのものがあなたの意のままになる。世界を…そしてその中のすべてを遅くする。",
    "Phase through the normal flow of time and slow down the universe for a duration.":
        "通常の時間の流れを超越し、一定時間宇宙の時を遅くする。",
    "Phase through the normal flow of time and slow down the universe for a duration. ":
        "通常の時間の流れを超越し、一定時間宇宙の時を遅くする。",
    "A refined sense of focus that enhances accuracy, making every shot land with deadly precision.":
        "精度を高める洗練された集中力。すべての射撃が致命的な精度で命中する。",
    "While there have been significant advancements in ship-borne weaponry, sometimes the simplest tool is the most effective.":
        "宇宙船兵器の技術は大きく進歩したが、時に最もシンプルな道具こそが最も効果的である。",
    "In the chaos of combat, the seconds needed to reload your weapon could be the difference between life and death.":
        "戦闘の混乱の中で、武器をリロードするのに必要な秒数が生死を分けることがある。",
    "There are those who can find just about anything, and their success is usually dependent on knowing how, and where, to look.":
        "ほぼ何でも見つけられる者がいて、その成功は通常、どこで、どうやって探すかを知っていることにかかっている。",
    "A blaster at your side is great and all, but sometimes the best weapon is simply an old adage: \"Knowledge is Power.\"":
        "腰のブラスターは素晴らしいが、時に最高の武器は単に古い格言だ：「知識は力なり」。",
}

FULL_TRANSLATIONS.update(ADDITIONAL_TRANSLATIONS)


def translate_text(text):
    if text in FULL_TRANSLATIONS:
        return FULL_TRANSLATIONS[text]
    text_stripped = text.rstrip()
    if text_stripped in FULL_TRANSLATIONS:
        return FULL_TRANSLATIONS[text_stripped]
    return text


class FullPluginWriter:
    def __init__(self):
        self.translations = 0
        self.compressed_translations = 0

    def process_subrecords(self, data):
        result = bytearray()
        offset = 0
        modified = False

        while offset < len(data) - 6:
            if offset + 6 > len(data):
                result.extend(data[offset:])
                break

            subrecord_type = bytes(data[offset:offset+4])
            subrecord_size = struct.unpack('<H', data[offset+4:offset+6])[0]

            if offset + 6 + subrecord_size > len(data):
                result.extend(data[offset:])
                break

            subrecord_data = data[offset+6:offset+6+subrecord_size]

            if subrecord_type in [b'FULL', b'DESC', b'DNAM', b'NNAM', b'TNAM', b'CNAM']:
                null_pos = subrecord_data.find(b'\x00')
                if null_pos > 0:
                    try:
                        original = bytes(subrecord_data[:null_pos]).decode('utf-8')
                    except (UnicodeDecodeError, ValueError, struct.error):
                        try:
                            original = bytes(subrecord_data[:null_pos]).decode('cp1252')
                        except (UnicodeDecodeError, ValueError, struct.error):
                            result.extend(subrecord_type)
                            result.extend(struct.pack('<H', subrecord_size))
                            result.extend(subrecord_data)
                            offset += 6 + subrecord_size
                            continue

                    translated = translate_text(original)

                    if translated != original:
                        new_data = translated.encode('utf-8') + b'\x00'
                        result.extend(subrecord_type)
                        result.extend(struct.pack('<H', len(new_data)))
                        result.extend(new_data)
                        self.translations += 1
                        modified = True
                        offset += 6 + subrecord_size
                        continue

            result.extend(subrecord_type)
            result.extend(struct.pack('<H', subrecord_size))
            result.extend(subrecord_data)
            offset += 6 + subrecord_size

        return bytes(result), modified

    def process_compressed_record(self, header, compressed_data):
        if len(compressed_data) < 4:
            return None
        original_decompressed_size = struct.unpack('<I', compressed_data[:4])[0]
        try:
            decompressed = zlib.decompress(compressed_data[4:])
        except zlib.error:
            return None
        old_translations = self.translations
        translated_data, modified = self.process_subrecords(decompressed)
        if not modified:
            return None
        compressed_count = self.translations - old_translations
        self.compressed_translations += compressed_count
        try:
            recompressed = zlib.compress(translated_data, 6)
        except zlib.error:
            return None
        new_record_data = struct.pack('<I', len(translated_data)) + recompressed
        new_header = bytearray(header)
        struct.pack_into('<I', new_header, 4, len(new_record_data))
        return bytes(new_header) + new_record_data

    def process_record(self, data, offset):
        record_type = bytes(data[offset:offset+4])
        if record_type == b'GRUP':
            grup_size = struct.unpack('<I', data[offset+4:offset+8])[0]
            grup_header = bytearray(data[offset:offset+24])
            inner_offset = offset + 24
            inner_end = offset + grup_size
            inner_data = bytearray()
            while inner_offset < inner_end:
                rec_data, consumed = self.process_record(data, inner_offset)
                inner_data.extend(rec_data)
                inner_offset += consumed
            new_grup_size = 24 + len(inner_data)
            struct.pack_into('<I', grup_header, 4, new_grup_size)
            return bytes(grup_header) + bytes(inner_data), grup_size
        else:
            if offset + 24 > len(data):
                return bytes(data[offset:]), len(data) - offset
            record_size = struct.unpack('<I', data[offset+4:offset+8])[0]
            record_flags = struct.unpack('<I', data[offset+8:offset+12])[0]
            header = data[offset:offset+24]
            subrecord_data = data[offset+24:offset+24+record_size]
            is_compressed = bool(record_flags & 0x00040000)
            if is_compressed:
                result = self.process_compressed_record(header, subrecord_data)
                if result:
                    return result, 24 + record_size
                else:
                    return bytes(data[offset:offset+24+record_size]), 24 + record_size
            new_subrecords, modified = self.process_subrecords(subrecord_data)
            if modified:
                new_header = bytearray(header)
                struct.pack_into('<I', new_header, 4, len(new_subrecords))
                return bytes(new_header) + new_subrecords, 24 + record_size
            else:
                return bytes(data[offset:offset+24+record_size]), 24 + record_size

    def translate_plugin(self, input_path, output_path=None):
        if output_path is None:
            output_path = input_path
        plugin_name = os.path.basename(input_path)
        print(f"\n  Processing: {plugin_name}")
        with open(input_path, 'rb') as f:
            data = f.read()
        if data[:4] != b'TES4':
            print(f"    Invalid plugin")
            return 0
        self.translations = 0
        self.compressed_translations = 0
        new_data = bytearray()
        offset = 0
        while offset < len(data):
            rec_data, consumed = self.process_record(data, offset)
            new_data.extend(rec_data)
            offset += consumed
        if self.translations > 0:
            with open(output_path, 'wb') as f:
                f.write(new_data)
            print(f"    Total translations: {self.translations}")
            print(f"    (From compressed: {self.compressed_translations})")
        else:
            print(f"    No translations needed")
        return self.translations


def main():
    import sys
    mods_path = r"C:\Star Wars Genesis\Game\mods"
    backup_dir = os.path.join(mods_path, "Star Wars Genesis Japanese", "plugin_backups")

    target_plugins = [
        ("Ascension - Gameplay Overhaul", "Ascension.esm"),
        ("Star Wars Blasters and Melee", "Star Wars Blasters.esm"),
        ("Star Wars Aliens", "SW Aliens.esm"),
        ("Star Wars Resources - Blasters", "SW Blasters.esm"),
        ("Star Wars - Mandalorian Forge Ruins", "MandalorianForge.esm"),
        ("Basic Sith Lightning", "Basic Sith Lightning.esm"),
        ("Star Wars Genesis - Override Patch", "StarWarsGenesisOverridePatch.esm"),
    ]

    print("=" * 60)
    print("Full Text Translator")
    print(f"Dictionary entries: {len(FULL_TRANSLATIONS)}")
    print("=" * 60)

    if not os.path.isdir(mods_path):
        print(f"エラー: MODディレクトリが見つかりません: {mods_path}")
        print("Star Wars Genesisのインストールパスを確認してください。")
        sys.exit(1)

    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        # Create backup directory
        os.makedirs(backup_dir, exist_ok=True)

        total = 0
        total_compressed = 0
        for folder, plugin in target_plugins:
            plugin_path = os.path.join(mods_path, folder, plugin)
            backup_path = os.path.join(backup_dir, plugin)
            if not os.path.exists(plugin_path):
                print(f"\n  {plugin}: Not found")
                continue
            if not os.path.exists(backup_path):
                if os.path.exists(plugin_path):
                    shutil.copy2(plugin_path, backup_path)
                    print(f"  バックアップ作成: {backup_path}")
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, plugin_path)
            writer = FullPluginWriter()
            count = writer.translate_plugin(plugin_path)
            total += count
            total_compressed += writer.compressed_translations
        print("\n" + "=" * 60)
        print(f"Total: {total} translations applied")
        print(f"From compressed records: {total_compressed}")
        print("=" * 60)
    else:
        print("\nUsage: python full_translator.py --apply")


if __name__ == "__main__":
    main()
