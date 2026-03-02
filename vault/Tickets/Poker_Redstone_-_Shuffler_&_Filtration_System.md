---
status: Todo
tags: [casino, poker, redstone, 5-points, priority-2]
---

# Poker Redstone - Shuffler & Filtration System

**Description:**
Hook up the complex shuffler, dealer, and muck filtration logic.

**Technical Notes:**
LOGIC: Dispensers/droppers shoot into each other -> hoppers -> autocrafters (count exactly 2 cards) -> barrels. Dealer button deals via vertical pipeline. Muck filter: sucked in, counted for full deck, trash items filtered out. Pre-load next deck in autocrafters while previous deck gets filtered.
