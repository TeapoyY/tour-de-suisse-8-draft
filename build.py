#!/usr/bin/env python3
"""
build.py — Tour de Suisse 8-0 from Vuelta 21-0 template
X-0 Sports Draft #13: Tour de Suisse 8 stages (shortest X-0)
Stage race: 8 stages (1 prologue/ITT + 1 sprint + 2 hills + 3 mountain + 1 ITT)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VUELTA = ROOT / 'source/index.html'
DRIVERS_JS = ROOT / 'source/DRIVERS.js'
OUT = ROOT / 'output.html'

with open(VUELTA, 'r') as f:
    html = f.read()

with open(DRIVERS_JS, 'r') as f:
    dataset = f.read()

# === 1) DRIVERS array replacement (regex, not split, per 9/7 lesson) ===
old_drv_pattern = re.compile(r'const DRIVERS = \[([\s\S]*?)\];', re.MULTILINE)
m = old_drv_pattern.search(html)
if not m:
    print("ERROR: cannot find DRIVERS array in template")
    sys.exit(1)

DRIVERS_RE = re.compile(r'const DRIVERS = \[([\s\S]*?)\];', re.MULTILINE)
SCHEDULE_RE = re.compile(r'const SCHEDULE = \[([\s\S]*?)\];', re.MULTILINE)

dataset_drv = DRIVERS_RE.search(dataset)
if not dataset_drv:
    print("ERROR: cannot find DRIVERS array in dataset")
    sys.exit(1)
new_drivers = f"const DRIVERS = [\n{dataset_drv.group(1).strip()}\n];"
html = old_drv_pattern.sub(new_drivers, html)
print(f"  DRIVERS replaced ({m.end() - m.start()} bytes)")

# === 2) SCHEDULE array replacement ===
old_sched_pattern = re.compile(r'const SCHEDULE = \[([\s\S]*?)\];', re.MULTILINE)
m = old_sched_pattern.search(html)
if not m:
    print("ERROR: cannot find SCHEDULE array in template")
    sys.exit(1)

dataset_sched = SCHEDULE_RE.search(dataset)
if not dataset_sched:
    print("ERROR: cannot find SCHEDULE array in dataset")
    sys.exit(1)
new_sched = f"const SCHEDULE = [\n{dataset_sched.group(1).strip()}\n];"
html = old_sched_pattern.sub(new_sched, html)
print(f"  SCHEDULE replaced ({m.end() - m.start()} bytes)")

# === 3) ERA_NAMES (full form) replacement ===
old_era = """const ERA_NAMES = {
    1: "1960s-70s",
    2: "1980s",
    3: "1990s",
    4: "2000s",
    5: "2010s",
    6: "2020s"
};"""
new_era = """const ERA_NAMES = {
    1: "1930s-60s",
    2: "1970s-80s",
    3: "1990s",
    4: "2000s",
    5: "2010s",
    6: "2020s"
};"""
if old_era in html:
    html = html.replace(old_era, new_era)
    print("  ERA_NAMES (full form) replaced")
else:
    print("  WARNING: ERA_NAMES (full form) pattern not found")

# === 4) ERA_LABELS (shorthand) replacement - 9/5 lesson: must do BOTH ===
old_labels = """const ERA_LABELS = {
    1: "60-70s",
    2: "80s",
    3: "90s",
    4: "00s",
    5: "10s",
    6: "20s"
};"""
new_labels = """const ERA_LABELS = {
    1: "33-69",
    2: "70-89",
    3: "90-99",
    4: "00-09",
    5: "10-19",
    6: "20-now"
};"""
if old_labels in html:
    html = html.replace(old_labels, new_labels)
    print("  ERA_LABELS (shorthand) replaced")
else:
    print("  WARNING: ERA_LABELS (shorthand) pattern not found")

# === 5) STAGE_BONUSES - Vuelta template uses inline `bonuses` in winProb, not separate var ===
# No replacement needed; our SCHEDULE types match Vuelta's existing bonuses dict exactly
print("  STAGE_BONUSES: not needed (template uses inline `bonuses` in winProb)")

# === 6) Title and header text ===
# CRITICAL: Replace "Vuelta a España" as a UNIT first (before any "Vuelta" → "Tour de Suisse" replacement, which would create "Tour de Suisse a España")
html = html.replace('Vuelta a España', 'Tour de Suisse')
html = html.replace('Vuelta a España', 'Tour de Suisse')  # belt-and-suspenders
# 21-0 → 8-0 (the title and h1 use "21-0: Tour de Suisse" format with a colon)
html = html.replace('21-0:', '8-0:')
html = html.replace('21-0 ', '8-0 ')
html = html.replace('21-0<', '8-0<')  # for h1 line end
# Title block has "Can You Win the Maillot Rojo?" — replace to "Can You Win the Swiss Champion?"
html = html.replace('Can You Win the Swiss Champion?', 'Can You Win the Swiss Champion?')  # already done above
# Description meta
html = html.replace('Draft legendary Tour de Suisse cyclists', 'Draft legendary Tour de Suisse cyclists')
# 21-stage → 8-stage (must run BEFORE article fix to catch "21-stage")
html = html.replace('21-stage', '8-stage')
html = html.replace('try to win every stage in a 8-stage', 'try to win every stage in an 8-stage')
html = html.replace(' 8 stages. 1 goal: 21-0', ' 8 stages. 1 goal: 8-0')
html = html.replace('1 goal: 21-0', '1 goal: 8-0')
# Title bar replacement
html = html.replace('<em>Maillot Rojo</em>', '<em>Swiss Champion</em>')
# 21 stages → 8 stages (5 places typical)
html = html.replace('21 stages', '8 stages')
html = html.replace('21 STAGES', '8 STAGES')
# Race counter (HTML)
html = html.replace('STAGE <span id="race-counter">1</span> OF 21', 'STAGE <span id="race-counter">1</span> OF 8')
# Stat box
html = html.replace('<div class="v">21</div><div class="l">Stages</div>', '<div class="v">8</div><div class="l">Stages</div>')

# === 7) Tagline ===
html = html.replace('Draft legends. Race 21 stages. Win all. Wear the <em>Maillot Rojo</em>.',
                    'Draft legends. Race 8 stages. Win all. Conquer Swiss roads.')

# === 8) Share text and hashtags ===
html = html.replace('#Vuelta21Zero #MaillotRojo #LaVuelta', '#TourdeSuisse8Zero #SwissCycling #TdS')
html = html.replace('#Vuelta21Zero', '#TourdeSuisse8Zero')
html = html.replace('Vuelta21', 'TourdeSuisse8')
html = html.replace('VueltaZero', 'TdS8Zero')
# Cross-link
html = html.replace('21-0 🔴 (Vuelta)', '8-0 🇨🇭 (Tour de Suisse)')

# === 9) Color theme (Maillot Rojo red → Swiss red+white) ===
# Keep red but lighter
html = html.replace('--accent: #dc2626; /* Maillot Rojo red */', '--accent: #ef4444; /* Swiss red */')
html = html.replace('--accent: #7f1d1d;', '--accent: #b91c1c;')
html = html.replace('/* Maillot Rojo red */', '/* Swiss red */')

# === 10) Era-specific replacements: 60-70s → 33-69, 80s → 70-89, etc ===
# (Vuelta template may have these in comments)
html = html.replace('60-70s', '33-69')
html = html.replace('"80s"', '"70-89"')
html = html.replace('"90s"', '"90-99"')
html = html.replace('"00s"', '"00-09"')
html = html.replace('"10s"', '"10-19"')
html = html.replace('"20s"', '"20-now"')

# === 11) Final / finale display ===
html = html.replace("'${wins} stage wins'", "'${wins} stage wins'")
# Finale record (the "21-0" reference)
# If template uses "${wins}-${losses}" it stays correct
# Update finale title "Strong" / "Polka dot" to TdS labels
# Vuelta had: "STRONG", "POLKA DOT BID" — change to climbing/ITT themed
html = html.replace('🚴 STRONG — ${wins} stage wins', '🇨🇭 CONQUEROR — ${wins} stage wins')
html = html.replace('🚴 POLKA DOT BID — ${wins} stage wins', '🏔 ALPINE — ${wins} stage wins')

# === 11b) Header emoji (Vuelta used 🔴, TdS uses 🇨🇭) ===
# Apply only to specific title/subtitle positions, not the cross-link footer
# Title: "🔴 8-0:" → "🇨🇭 8-0:" (only the very first emoji on the page)
html = html.replace('<title>🇨🇭 8-0:', '<title>🇨🇭 8-0:')  # already
html = html.replace('<h1>🇨🇭 8-0:', '<h1>🇨🇭 8-0:')  # already
# Direct: title has 🔴 8-0: pattern
html = html.replace('🔴 8-0: Tour de Suisse', '🇨🇭 8-0: Tour de Suisse')
# Replace the "Made for 🔴 Tour de Suisse" line
html = html.replace('Made for 🔴 Tour de Suisse', 'Made for 🇨🇭 Tour de Suisse')
html = html.replace('for 🔴 Tour de Suisse', 'for 🇨🇭 Tour de Suisse')
# Finale labels: STRONG/SPRINT/Polka Dot → Swiss-themed
# These are inside template literal: `🔴 STRONG — ${wins} stage wins`
html = html.replace('`🔴 STRONG — ${wins} stage wins`', '`🇨🇭 CONQUEROR — ${wins} stage wins`')
html = html.replace('`🔴 SPRINT BID — ${wins} stage wins`', '`🏔 ALPINE — ${wins} stage wins`')

# === 12) n !== 6 bug (defensive fix per 8/28 + 9/5 lessons) ===
html = html.replace("disabled = n !== 6;", "disabled = n !== 5;")

# === 13) n !== 5 (TdS uses 5 picks) ===
# (this is just defensive)

# === 14) Belt-and-suspenders: any Vuelta leakage cleanup ===
# Replace all remaining "Vuelta" with "Tour de Suisse"
# but keep DRIVERS dataset and dataset references intact
# (DRIVERS are rider names, not "Vuelta")
# Strategy: only replace Vuelta in non-dataset context
# Use a precise set of strings that should be cleaned

# Belt-suspenders for Vuelta leakage cleanup - REPLACE COMPOUNDS FIRST
compound_belt = [
    # Compound names (must replace before individual words)
    ("Vuelta a España", "Tour de Suisse"),
    ("La Vuelta", "Tour de Suisse"),
    ("Maillot Rojo", "Swiss Champion"),
    ("maillot rojo", "swiss champion"),
    ("La Roja", "Swiss Champion"),
    # Stage names
    ("Lisbon", "Küsnacht"),
    ("Madrid", "Andermatt"),
    ("Iberian", "Swiss"),
    ("Spanish", "Swiss"),
    # Hashtags
    ("#Vuelta21Zero", "#TourdeSuisse8Zero"),
    ("#LaVuelta", "#TdS"),
    ("#MaillotRojo", "#SwissCycling"),
    # Vuelta (now any individual "Vuelta" leftover)
    ("Vuelta", "Tour de Suisse"),
    ("vuelta", "tour de suisse"),
]

# Apply in order (compounds first to avoid word-fragment issues)
for old, new in compound_belt:
    if old in html and old != new:
        before = html.count(old)
        if before > 0:
            html = html.replace(old, new)
            if before > 0:
                print(f"  belt-suspenders: {old!r} → {new!r}  ({before} occurrences)")

# === 14b) Share text — AFTER Vuelta→Tour de Suisse replacement ===
html = html.replace('`🔴 My Tour de Suisse', '`🇨🇭 My Tour de Suisse')
html = html.replace('const text = `🔴 My Tour de Suisse', 'const text = `🇨🇭 My Tour de Suisse')
# Other share text variants
html = html.replace('`🔴 My Tour de Suisse 8-0', '`🇨🇭 My Tour de Suisse 8-0')

# === 15) Update title bar / app title to "Tour de Suisse" ===
# Title bar (top of page)
html = html.replace('>Vuelta<', '>TdS<')
html = html.replace('>Vuelta a España<', '>Tour de Suisse<')

# === 16) AI field strength (per 9/5 lesson: short season needs stronger AI) ===
# Vuelta AI was OVR 80-90 range. Tour de Suisse has 8 stages only,
# so even with same AI strength OVR 99 will hit ~70%+ perfect (per 8/22 IndyCar pattern)
# Solution: make AI field 84-94 range (slightly stronger than Vuelta's 80-90)
# Pattern: find existing AI OVR generation in template
# Vuelta template uses: `aiOVR = 80 + Math.floor(rng() * 11)` typically
# Need to find and replace

# Use belt-and-suspenders since exact pattern varies
ai_patterns = [
    ("80 + Math.floor(rng() * 11)", "84 + Math.floor(rng() * 11)"),
    ("80 + Math.floor(rng()*11)", "84 + Math.floor(rng()*11)"),
    ("80 + Math.floor(rng() * 10)", "84 + Math.floor(rng() * 11)"),
    ("78 + Math.floor(rng() * 12)", "84 + Math.floor(rng() * 11)"),
    ("ovr: 80 + Math.floor", "ovr: 84 + Math.floor"),
]
for old, new in ai_patterns:
    if old in html:
        html = html.replace(old, new)
        print(f"  AI strength: {old!r} → {new!r}")
        break

# === 17) Save ===
html = html.replace('\ufe0f', '')
with open(OUT, 'w') as f:
    f.write(html)
(ROOT / 'index.html').write_text(html)
print(f"\n  Output: {OUT} ({len(html)} bytes)")

# === 18) Verify checks ===
checks = [
    ('const DRIVERS', 'DRIVERS array'),
    ('const SCHEDULE', 'SCHEDULE array'),
    ('const ERA_NAMES', 'ERA_NAMES'),
    ('const ERA_LABELS', 'ERA_LABELS'),
    ('const STAGE_BONUSES', 'STAGE_BONUSES'),
    ('Tour de Suisse', 'Tour de Suisse brand'),
    ('8-0', 'X-0 number'),
    ('Küsnacht', 'TdS stage name'),
    ('Andermatt', 'TdS stage name'),
    ('Pogačar', 'Modern legend (Pogačar)'),
    ('Vingegaard', 'Modern legend (Vingegaard)'),
    ('van der Poel', 'Modern legend (MvDP)'),
    ('Cancellara', 'Swiss icon'),
]
print("\n  Verification:")
for s, desc in checks:
    n = html.count(s)
    marker = '✅' if n >= 1 else '❌'
    print(f"    {marker} {desc:35s} count={n}")

# Check for Vuelta leakage
leakage = [
    'Vuelta', 'Maillot', 'Lisbon', 'Madrid', 'Iberian', 'Spanish',
    'Vuelta21', 'Vingegaard', 'Heras', 'Contador', 'Iberian'
]
print("\n  Vuelta leakage check:")
for s in leakage:
    n = html.count(s)
    if n > 0:
        # Vingegaard/Contador are TdS dataset riders too, allowed
        if s in ('Vingegaard', 'Contador'):
            print(f"    ✅ {s} count={n} (TdS dataset, allowed)")
        else:
            print(f"    ⚠  {s} count={n} (leakage!)")
    else:
        print(f"    ✅ {s} count=0 (clean)")
