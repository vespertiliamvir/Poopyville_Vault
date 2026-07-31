---
status: Documentation
tags: [casino, plinko, redstone, timing, semaphore, knowledge-graph]
---

# Plinko - Token Synchronization, Decrement Logic & Semaphore Locking

This document captures the timing logic, edge-case handling, and semaphore locking mechanisms designed to prevent collisions between token increments (AutoCrafter deposits) and decrements (game play / button presses) on the 7-segment display and internal counters.

## 1. The Collision Problem & Semaphore Lock
Because the 7-segment display uses a fast piston feed tape, decrementing by 1 on a modulo-10 counter requires cycling **9 forward increments**. This takes time (~9 clock cycles). 
If a user dumps a bulk load of diamonds while actively playing, an incoming increment signal during a decrement cycle would crash or desynchronize the display.

### Solution: Decrement-Initiated Lock
- When a valid **Decrement Signal** (Play button pressed + True Count > 0) goes through, it immediately triggers a lock on the **Increment Intake (AutoCrafter hopper feed)**.
- Any incoming diamond increments are physically buffered in the hopper pipe.
- The lock holds until the 9-cycle decrement on the view model finishes and the machine is ready for the next play.

## 2. Decrement Architecture (The 9-Counter & 10-Counter)
- **10-Counter (Tens Place Control):** Tracks total increments/decrements. When it reaches 10, it resets to 0 and increments the Tens Place digits. When decrementing while sitting at 0, it unlocks the tens place decrement line so both digits step back together (e.g., 10 -> 09). Otherwise, it isolates decrements to the Ones Place only.
- **9-Counter (Decrement Loop):** Powered by a NOR latch running a slow redstone clock into a two-dropper counter. It fires exactly 9 times to rotate the display back by 1, then a comparator detects emptiness, resets the NOR latch, and halts the clock.

## 3. Edge Case Validation (The Zero-Balance Double-Tap Underflow)
- **Scenario:** A player with 0 tokens holds down the play button right as a single token is credited (0 -> 1), causing a rapid double-pulse input before the sticky piston lockout fully depresses.
- **Resolution:** Completely safe by physical design. Even if a double decrement signal erroneously reaches the counter when dropping from 1 back to 0, the dropper counters hit 0 on the first pulse. A subsequent pulse attempts to decrement a zeroed dropper, resulting in zero item movement (underflow impossible). The NOR latch is already tripped/reset, preventing extra display cycles or negative balance state creation.

## 4. Master Cooldown, NOR Latch & Elevator Feedback Loop
- **Deprecating Brittle Timers:** The unreliable Etho Hopper Clock has been completely removed in favor of a state-based **NOR Latch**.
- **Elevator Feedback Loop:** Upon game start, the NOR latch trips, locking both play button decrements and increment hopper intake. This latch is **only** reset and unlocked when an active confirmation pulse arrives from the very last piston of the Concrete Powder Elevator (signifying a new block is physically delivered and ready at the top of the board).
- **Single-Chunk Observer Routing & Debouncing:**
  - To eliminate chunk-unloading desynchronization, the feedback pulse routes straight down the expanded back wall inside a single chunk boundary via a **15 to 20 Observer chain**.
  - The signal is conditioned with a **pulse extender** and a **monostable circuit** (rising-edge detector / one-shot) to debounce the final piston movement.
- **Bedrock Timing Calibration:**
  - In Bedrock Edition, 1 Observer = 2 game ticks = 1 redstone tick = 0.1s.
  - A chain of 20 Observers + 5 repeaters = 25 redstone ticks = **~2.0–2.5 human seconds**.
  - This ~2.5s transit delay serves as an intentional mechanical buffer, allowing the concrete powder block to settle perfectly before the game unlocks for the next play.
