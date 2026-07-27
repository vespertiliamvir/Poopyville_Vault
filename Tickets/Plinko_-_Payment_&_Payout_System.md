---
assignee: David
start: 2026-07-24
due: 2026-07-31
status: In Progress
tags: [casino, plinko, redstone, 3-points, priority-3]
---

# Plinko - Payment & Payout System

**Description:**
Hook up the item intake payment and the automated payout dispensing.

**Technical Notes:**
Ensure proper ratios so the house maintains an edge.
SECURITY: Build a bedrock pipe for hopper intakes to prevent theft from 12-year-olds. Include a temporary-permanent acoustic alarm sealed in duplicated bedrock. The noteblock sound radius must intersect with the casino floor strictly within a 2x2 area to keep it subtle and unobtrusive.

### Plinko Probabilities & Expected Value (EV)
* **Standard Payouts (Option 1):** `[36, 9, 1, 9, 36]`
* **Peg Anomaly:** The peg dividing the center and the mid-right slot is broken and always forces the block left into the center slot.

**True Landing Probabilities:**
- Far Left (36 payout): 1/16 (6.25%)
- Mid Left (9 payout): 4/16 (25.0%)
- Center (1 payout): 9/16 (56.25%)
- Mid Right (9 payout): 1/16 (6.25%)
- Far Right (36 payout): 1/16 (6.25%)

**Expected Value (EV):** 7.875 diamonds per play.
* **Verdict:** If the price is **9 diamonds to play**, the house makes an average profit of ~1.13 diamonds per play. This guarantees profits while letting the user "break even" 31% of the time. The 9-diamond entry allows redstone to be incredibly compact by utilizing an AutoCrafter.

## Current Implementation Status (July 27)
- **Increment Line Routing:** Designed and verified. The 9-diamond AutoCrafter spits out an Increment pulse that routes to: (1) Internal Super Counter (lifetime tokens), (2) Internal Source of Truth (available plays), and (3) External View Model (7-segment display). 
- **Decrement Line:** Button press sends a signal to the Bedrock vault. Vault validates `plays > 0`, drops the concrete powder, and sends actual decrement pulse to the View Model.
- **Physical Security integration underway:** Building the bedrock cell, placing the Euclidean-geometry Calibrated Sculk Sensors (Freq 12 for blocks destroyed, Freq 13 for blocks placed), and routing the 7-tick secure alarm wire.
