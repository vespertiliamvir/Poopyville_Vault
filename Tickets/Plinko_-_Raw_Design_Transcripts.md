# Plinko & Casino Security - Raw Design Transcripts & Architecture Ramblings

This document compiles the unedited and raw architectural stream-of-consciousness design sessions from David regarding the Poopyville Casino, Plinko Machine, Slot Machines, Redstone Synchronization, and Physical Security Protocols. This file is intended for AI subagents and deep analysis to ensure zero technical requirements or nuance are missed in the formal Knowledge Graph documentation.

## Session 1: Initial Plinko I/O & Security Conundrums
- **Input/Output Routing:** 9-diamond AutoCrafter spits out an Increment Line. Increment line goes to: Internal Super Counter (lifetime tokens), Internal Source of Truth (current playable tokens), External Super Counter (lifetime displays), and External View Model (7-segment display).
- **Decrement Routing:** Play button sends signal into Bedrock cell. Bedrock cell verifies true count > 0, fires Actual Decrement out to view model, lifetime counter, and triggers the concrete powder piston feed tape.
- **Security Conundrum (Spoofing Payouts):** Concrete powder falls through Plinko board to hit observers at bottom. If observers/payout wiring are outside bedrock, a player can break the wall and manually update the jackpot observer to steal 36 diamonds.
- **Replenishment Tank Note:** Concrete powder magazine ran out/lost a piece. Need a detection circuit and storage silo to automatically inject new concrete powder blocks when empty.

## Session 2: Slot Machine Hardening & Sculk Sensor Calibration
- **Slot Machine Flaw:** Players could break into slot machine redstone and trigger fake Enchanted Apple / Diamond jackpot wins. 
- **Calibrated Sculk Sensors (Vibration Frequencies):** 
  - Opening/closing Shulker boxes = Frequencies 10 & 9 (MUST NOT TRIGGER ALARM so friends aren't annoyed).
  - Block Destroyed (Mining glass, hoppers, walls) = Frequency 12 (Signal Strength 12).
  - Block Placed (Placing redstone torches, levers, concrete powder, pistons) = Frequency 13 (Signal Strength 13).
- **Brute-Force Password Math:** Alarm boxes sealed in Bedrock using lever combination locks. 12 levers = 4,096 combinations (1+ hour to guess). 16 levers = 65,536 combinations (mathematically impossible for kids).
- **Chunk Loading Rule:** Alarm wires must reach a centralized secure alarm chunk within ~6 to 7 game ticks before an escaping player unloads the chunks.

## Session 3: Euclidean Geometry & Audit Ledgers
- **Sensor Geometry:** Sculk sensors operate on True Spherical Euclidean Geometry (hypotenuse calculation), NOT Manhattan distance. With a 16-block detection radius, a sensor placed 13 blocks back horizontally still has ~9 blocks of vertical reach (`sqrt(13^2 + 9^2) = 15.8`), perfectly slicing the front Plinko glass while ignoring the casino floor.
- **Audit Ledgers (Lecterns):** Housed in the Plinko Bedrock Cell. Tracks Super Counters (Lifetime Tokens, Total Plays, Prize Pots). If an alarm sounds unexpectedly (e.g., child mining near unshielded zone), Admins compare ledgers against physical reserves. If math checks out, password box is reset with zero consequences.
- **The Unstoppable Observer Worm:** Once an alarm wire reaches the main chunk boundary, it connects to an Observer chain. Observers act as one-way diodes: once triggered, the pulse is self-replicating and unstoppable even if the intruder snips the trailing wire.
- **Slot Machine 3-Point Cover:** 
  1. Input (Compost Bins/Hoppers): Encased in blocks, covered by Freq 12 (Block Destroy) to prevent swapping filter items for dirt.
  2. Internal Redstone (Jackpot Lines): Heavily wool-insulated, covered by Freq 13 (Block Place) to stop spoofing via redstone torches.
  3. Jackpot Reserves: Covered by Freq 12 (Block Destroy) to prevent smash-and-grab brute force robberies.

## Session 4: Token Synchronization, Semaphore Locking & Underflow Safety
- **The Collision Problem:** 7-segment display uses a fast piston feed tape. Decrementing by 1 on modulo-10 takes 9 forward cycles (~9 clock pulses). If a player dumps diamonds while actively playing, incoming increments clash with decrements on the view model.
- **The Increment Semaphore Lock:** When a valid Decrement signal fires, it immediately triggers a lock on the Increment Intake hopper feed. Incoming diamonds buffer in the pipe until the 9-cycle display decrement finishes.
- **Decrement Architecture:** 10-Counter manages tens-place rollover and combined decrements (10 -> 09). 9-Counter runs a slow redstone clock into a two-dropper counter powered by a NOR latch to step the display back exactly 9 times.
- **Zero-Balance Double-Tap Edge Case:** If a player with 0 tokens holds down the play button as 1 token arrives, causing a rapid double-pulse before the sticky piston lockout depresses, hardware limits protect the system. Dropper counters at 0 are physically empty—attempting to decrement an empty dropper results in zero item movement (underflow impossible) and the NOR latch remains reset.

## Session 5: replacing Brute Hopper Clocks with NOR Latch Elevator Feedback Loops
- **Removing Brittle Timers:** Instead of using an Etho Hopper Clock in the basement to guess when a gameplay session is finished, replace it with a robust **NOR Latch**.
- **Elevator Feedback Loop:** When play starts, the NOR latch trips, locking both further decrements (button presses) and increment intake processing. The latch ONLY unlocks when a confirmation feedback pulse arrives from the very last piston of the Concrete Powder Elevator (signifying a new piece of powder has officially arrived at the top and the board is physically reloaded and ready).
- **Single-Chunk Routing & Observer Chain Delay:** To keep the feedback wire stable without crossing tricky chunk borders, run the elevator confirmation pulse down through the expanded back casino wall using an Observer worm (15 to 20 observers) plus a pulse extender with a monostable circuit (rising edge detector/one-shot) to debounce the signal.
- **Timing Calculation:** In Bedrock, 1 observer = 2 game ticks = 1 redstone tick = 0.1 human seconds. A chain of 20 observers + 5 repeaters = 25 redstone ticks = 2.5 human seconds. This tiny 2.0-2.5 second natural transit delay serves as an ideal mechanical buffer right as the concrete powder drops into place!
