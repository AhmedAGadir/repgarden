# RepGarden colours

Decided by Ahmed on 28 October 2026 from proposal 1. Four Tailwind v4 scales and nothing custom. `colours.css` holds the tokens for both modes, `colours.json` the same as data, and `colours-sheet.png` the proposal sheet with the roles table and the screens it was judged on.

| Scale | Tailwind | Job |
|---|---|---|
| Stone | `stone` | The neutrals: page, cards, lines, text. Warm, like soil, so the garden art can sit on them in any style |
| Leaf | `green` | The one primary: buttons, links, active states, growth. Success reuses it: in a garden, growing is the success state |
| Carrot | `orange` | Accent for the moments that grow something, the pot, highlights. Never carries white text; used on dark text or on tints |
| Harvest gold | `amber` | Accent for seeds, harvests and the potato |

Danger is `red`, info is `sky`, warning is `amber` on its 100 tint.

**Light mode:** page stone-50, cards white, lines stone-200, text stone-800, muted stone-500, primary button green-700 with white text (4.95:1), links green-700, tint green-100 with green-800 text, carrot orange-500, gold amber-400 with stone-950 text.

**Dark mode is its own palette, not an inversion:** page stone-950 (never black), cards stone-900 with a stone-800 line, text stone-100, muted stone-400, primary button green-500 with stone-950 text (8.9:1), links green-400, tint green-950 with green-300 text, carrot orange-400, gold amber-400. Nothing is pure white or pure black.

Every text pair meets 4.5:1 in both modes, measured with WCAG 2 relative luminance. A custom leaf hue can replace `green` with the art direction later without changing any role.
