# 🇨🇭 8-0: Tour de Suisse Draft

Draft legends. Race 8 stages. Win all. Conquer Swiss roads.

**Live**: https://teapoyy.github.io/tour-de-suisse-8-draft/

## What's this?

X-0 Sports Draft #13. Fork of [Vuelta 21-0](https://github.com/TeapoyY/vuelta-21-draft) with:
- 84 Tour de Suisse legends (1930s-2020s)
- 8 stages (Küsnacht Prologue → Basel Sprint → Emmental Hills → Nufenen Pass → Andermatt Summit → Gstaad Hills → Andeer ITT → Andermatt Mountain)
- Modern era focus: Pogačar / Vingegaard / Evenepoel / van der Poel / Cancellara / Hinault / Merckx

## How to play

1. Pick 5 legends from 6 eras (era tabs: 33-69, 70-89, 90-99, 00-09, 10-19, 20-now)
2. Same-era synergy bonus (+1.5 OVR per additional rider)
3. Race 8 stages: 1 ITT, 1 flat, 2 hills, 3 mountain, 1 final ITT
4. Goal: 8-0 perfect season

## Stats

- Monte Carlo OVR 99: 4.34/8 wins, 0% perfect 8-0 ✅
- OVR 95: 1.27/8 wins (struggle for perfect)
- OVR 90: 0.01/8 wins (very hard)
- OVR 80 and below: 0 wins
- Target: OVR 99 perfect 8-0 is rare (0%) — gives aspirational goal

## Color theme

Swiss red + white — uses `var(--accent)` Maillot Jaune-style palette. Subtle cross to "Maillot Rojo" Vuelta red (cross-link visible in footer).

## X-0 Sports Draft Matrix

| # | Variant | Status | Live |
|---|---------|--------|------|
| 1 | NFL 38-0 | ✅ | [link](https://github.com/TeapoyY/squad-draft-football) |
| 2 | NASCAR Cup 36-0 | ✅ | [link](https://github.com/TeapoyY/nascar-36-draft) |
| 3 | Tour de France 21-0 | ✅ | [link](https://github.com/TeapoyY/tour-de-france-21-draft) |
| 4 | IndyCar 17-0 | ✅ | [link](https://github.com/TeapoyY/indycar-17-draft) |
| 5 | Formula E 17-0 | ✅ | [link](https://github.com/TeapoyY/formulae-17-draft) |
| 6 | MotoGP 20-0 | ✅ | [link](https://github.com/TeapoyY/motogp-20-draft) |
| 7 | Endurance 24-0 | ✅ | [link](https://github.com/TeapoyY/endurance-24-draft) |
| 8 | WRC 13-0 | ✅ | [link](https://github.com/TeapoyY/wrc-13-draft) |
| 9 | Giro d'Italia 23-0 | ✅ | [link](https://github.com/TeapoyY/giro-23-draft) |
| 10 | Vuelta a España 21-0 | ✅ | [link](https://github.com/TeapoyY/vuelta-21-draft) |
| **11** | **Tour de Suisse 8-0** | **✅** | **[this repo]** |

## Why Tour de Suisse?

- **Blue ocean**: 6/15 cycling week queries return 0 cycling-specific apps (verified 9/9)
- **Race legend**: 1933-present (93 years), "Race of the Helvetia"
- **Tour de France warm-up**: 8-stage format = quick gameplay loop
- **Swiss culture**: time trial specialists + climbers (Cancellara, Hinault, Merckx have all won)
- **Famous moments**: Hinault 1981 comeback, Cancellara 2008 prologue, Froome 2013 TT masterclass

## Tech

- Single HTML file (~38KB), zero dependencies
- LocalStorage for best score persistence
- Pure vanilla JS, no build step
- Mobile-first responsive
