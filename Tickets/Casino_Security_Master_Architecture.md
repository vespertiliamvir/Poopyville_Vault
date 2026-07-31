---
status: Documentation
tags: [casino, security, redstone, reference, knowledge-graph]
---

# Casino Security Master Architecture

This document serves as the master source of truth for the physical and logic-based security of the Poopyville Casino. It details the required redstone protocols, Euclidean formulas, timing equations, and synchronization logic to prevent 12-year-olds from spoofing payouts, tampering with item filters, or breaking into the machines.

## 1. Calibrated Sculk Sensor Mechanics & Frequency Filtering
All physical security relies on **Calibrated Sculk Sensors** tuned with Amethyst Shards and a Lectern (or comparator) to actively filter out ambient casino floor activity.
- **Frequency 9 & 10 (Excluded / Ignored):** Opening (10) or closing (9) containers such as Shulker Boxes emits vibration frequencies 9 and 10. By calibrating sensors strictly above this range, players can freely access their Shulker boxes without triggering false alarms.
- **Frequency 12 (Signal Strength 12):** Listens ONLY for Blocks Destroyed (e.g., breaking glass, mining hoppers, snipping redstone).
- **Frequency 13 (Signal Strength 13):** Listens ONLY for Blocks Placed (e.g., placing redstone torches, repeaters, levers, concrete powder, or pistons).
- **Euclidean Geometry & 13-Block Offset Rationale:** Sensors operate on a true spherical Euclidean radius of 16 blocks (`sqrt(x^2 + y^2 + z^2) = distance`). By positioning a sensor exactly 13 blocks horizontally behind the Plinko machine, it leaves ~9.3 blocks of vertical reach (`sqrt(16^2 - 13^2) = 9.3` or `sqrt(13^2 + 9^2) = 15.8`). This precise positioning allows the spherical detection field to cleanly slice the front Plinko glass while leaving the public casino floor completely out of range!

## 2. Plinko Machine Security Protocol
Because the Plinko game is exposed to the public floor, it requires specialized three-dimensional coverage.
* **The Glass Case:** Sensors tuned to **Frequency 12 (Blocks Destroyed)** cover the entire physical encasement. *Reason: Prevents an intruder from breaking glass to drop their own concrete powder in, or mining open access ports.*
* **The Internal Airspace & Redstone:** Sensors tuned to **Frequency 13 (Blocks Placed)** cover the interior airspace and the entirety of the Jackpot redstone wire. *Reason: Even if an intruder enters through the roof without breaking blocks, they are physically forced to place concrete powder to drop it, or place a redstone torch to spoof the wire. Freq 13 catches both instantly.*
* **The Bedrock Cell (Admin Vault):** A massive Bedrock chamber beneath the machine that hosts the Plinko logic, the centralized password box, and the Audit Ledgers.

## 3. Slot Machine Security Protocol
Each slot machine (Diamond, Enchanted Apple, etc.) has three critical failure points requiring independent sensor coverage:
* **The Input (Compost Bins/Hoppers):** Fully encased in solid blocks/glass. Sensors tuned to **Frequency 12 (Blocks Destroyed)**. *Reason: Prevents players from mining the hoppers to swap out item filters to accept dirt as tokens.*
* **The Internal Redstone (Jackpot Lines):** Insulated heavily with Wool to block outside floor noise. Sensors tuned to **Frequency 13 (Blocks Placed)**. *Reason: Prevents an intruder from mining into the machine and placing a redstone torch next to the output dispenser.*
* **The Jackpot Box (Payout Reserve):** Sensors tuned to **Frequency 12 (Blocks Destroyed)**. *Reason: Stops brute-force robbery where a player mines straight into the machine to smash the reserve barrel.*

## 4. The Transmission Network, Chunk Unloading & The 7-Tick Rule
* **Bedrock Tubes:** All sensors and critical alarm transmission wires are sheathed inside Bedrock Tubes.
* **The 7-Tick Deadline & Chunk Unloading Rationale:** When an alarm trips, the signal MUST reach the central secure alarm chunk within **7 game ticks**. This requirement ensures the alarm triggers before an escaping intruder can fly away and unload adjacent chunks.
* **The Observer Diode & Bedrock Timing:** Once the signal crosses into the central alarm chunk, it hits an Observer Line. Observers act as one-way diodes—once an Observer fires, the pulse is self-replicating and unstoppable even if the intruder snips the trailing wire. 
  - *Bedrock Math:* `1 observer = 2 game ticks = 1 redstone tick = 0.1 human seconds`.

## 5. Audit Ledgers & Brute-Force Password Math
To manage accidental trips (e.g., a child placing a Shulker box too close to an unshielded edge):
* **Combination Lock Security:** The main Alarm Box is 100% encased in Bedrock and controlled by a lever combination array. 
  - `12 levers = 4,096 combinations` (~1+ hour to brute force).
  - `16 levers = 65,536 combinations` (mathematically impossible for players to guess). **16 levers is the standard for total vault immunity.**
* **Audit Ledgers:** Inside the Plinko Bedrock Cell, physical Lecterns track **Super Counters**: Lifetime Tokens generated, Total Plays, and Total Prize Pots/Jackpots. If an alarm rings unexpectedly, Admins audit the ledgers against physical reserves; if counts balance and zero reserves are missing, the alarm is reset without penalty.

## 6. Increment Line Routing (4-Way Distribution)
The Increment Line (generated by the AutoCrafter parsing 9 diamonds) routes to exactly **four destinations**:
1. **The Internal All-Time Super Counter** (Lifetime tokens generated, secured inside bedrock).
2. **The Internal Source of Truth Counter** (Currently available playable tokens).
3. **The External Super Counter** (Lifetime display visible to public).
4. **The External View Model** (Updates the casino floor 7-segment display).
When a game is played, the Internal Source of Truth validates `balance > 0`, drops the concrete powder, and sends the Actual Decrement pulse across the network.

## 7. Synchronization & Mechanical Safeguards (Cross-References)
- **Increment Semaphore Lock:** During a display decrement (which requires cycling 9 forward steps on the modulo-10 display), an automatic lock closes the Increment Intake hopper feed, forcing incoming diamonds to buffer safely in the pipe until rotation completes. (See: `Plinko_-_Token_Synchronization_&_Locking.md`).
- **NOR Latch Elevator Feedback Loop:** Deprecates brittle Etho Hopper clocks. A NOR Latch locks gameplay until a confirmation pulse returns from the very last piston of the Concrete Powder Elevator via a 15–20 Observer chain (~2.0–2.5s natural debounce buffer).
- **Zero-Balance Underflow Immunity:** Dropping from 1 to 0 with rapid double-pulsing is rendered harmless by physical hardware: dropper counters at 0 are physically empty, preventing item underflow or negative counts.
- **Concrete Powder Replenishment Silo:** An automated detection circuit monitors the magazine and gravity-injects new blocks from a standby reserve if powder runs empty or is destroyed. (See: `Plinko_-_Concrete_Powder_Replenishment.md`).
