---
assignee: Optic Dust & David
start: 2026-12-18
due: 2027-01-01
status: In Progress
tags: [city, build, villagers, optic-dust]
---

# Trading Hall Dome (Optic Dust / User)

**Description:**
Finish the massive villager trading hall dome behind the iPhone.


WARNING!! NEW INFO!! we have to make sure ONLY ONE VILLAGER ZOMBIE AT A TIME!!! fuckkk the original redstone didnt account for htis!! fuck~I ahem..~ I just realized that ACTUALLY we can just break their lecturns after locking them in place then cure them and re link them 1 at a time


we have 22 book spots
---

### 📚 In the Library Already (Locked & Safe)

- **Aqua Affinity I** (✔️ 6/1)
    
- **Bane of Arthropods V** (✔️ paired with Fortune III)
    
- **Channeling I** (✔️ paired with Power V) - one under casino for only 10 emeralds
    
- **Density V** (✔️ 21/1)
    
- **Feather Falling IV** (✔️ 55/30)
    
- **Flame** (✔️ paired with Density V)
    
- **Fortune III** (✔️ paired with Bane of Arthropods V)
    
- **Frost Walker I** (✔️ paired with Lunge III)
    
- **Impaling V** (✔️)
    
- **Looting III** (✔️ paired with Silk Touch I)
    
- **Lunge III** (✔️ paired with Frost Walker I)
    
- **Mending I** (✔️ standalone & paired with Riptide/Thorns)
    
- **Power V** (✔️ paired with Channeling I)
    
- **Protection IV** (✔️ ~22 emeralds)
    
- **Respiration III** (✔️)
    
- **Riptide III** (✔️ paired with Thorns/Mending)
    
- **Sharpness V** (✔️ 44)
    
- **Silk Touch I** (✔️ standalone & paired with Looting III)
    
- **Thorns** (✔️ paired with Riptide/Mending)
    
- **Unbreaking III** (✔️ 30/5)
    

### 🧟 Owned, but Not in the Library Yet (In Notepad, No Checkmark)

- **Depth Strider III** - might have died actually?
    
- **Efficiency V**
    
- **Fire Aspect II**
  

### 💀 Dead or Missing (The Ones We Actually Care About)

- **Infinity I** _(Marked missing)_
    
- **Loyalty III** _(Marked missing)_
    

### 🤷 Ones we might not care about, but I think we're missing (The PvP & Fishing Maybes)

- **Luck of the Sea III** _(confirmed owned under casino
    
- **Lure III** _confirmed owned on a sharpness V guy not in the library currently.. maybe i should replace the hsarpness guy... also a mending guy has oit
    
- **Multishot I** _(Low key for PvP)_
    
- **Piercing IV** _(You were unsure on this one)_
    
- **Quick Charge III** _(Low key for PvP)_


so far the crossed out ones are deisnated in zones where the zombie architecture works.. the rest we w ill need to make more room for i think by raising the second floor higher

### 🏛️ Layout & Architecture
- **Center:** Park area with an elevator entrance coming up from below.
- **Town Hall:** Middle building featuring a large clock tower.
- **Blacksmith:** Left side. Built with spruce, dark oak, deepslate tiles, or blackstone bricks with metal accents. Houses armor and tools (consider splitting armor/tools into two separate buildings). 
- **Library:** Right side. 2-story building, likely birch wood. Houses all librarians.
- **Additional:** 1-story restaurant (left) and 1-story miscellaneous building (right).

### 📖 Lore & Atmosphere
- **Theme:** A segregated, oppressive society where Iron Golems are treated as second-class citizens to Villagers (Jim Crow style).
- **Podiums:** - A grand, high podium on the left for the Villager King (and Wei).
  - A smaller, lower podium on the right for the Iron Golem "politician".

### ⚙️ Technical Notes & Redstone
  - This stops the bugged 1.21.11 Zombie Horses from spawning AND instantly gives us the 2-block vertical clearance needed for the delivery pipes underneath.
- **Apple & Potion Delivery Pipe (Hybrid System):**
  - **Inner Base (Water Streams):** Run water streams on the lower stone slab layer. To avoid needing a full ice floor, place exactly **one block of Packed Ice every 8 blocks** (where the water resets) to maintain item momentum.
  - **Outer Edge (Minecart Handoff):** The water streams will drop the items onto a Hopper Minecart track on the outer perimeter.
  - **Performance & Bug Prevention:** - Map the chunk borders! The minecart track MUST sit entirely within a **single chunk** to prevent Bedrock's asynchronous chunk-unloading bugs from breaking the cart.
    - Hook the minecart to a detector rail so it only runs when an item is actually dispensed. This is vastly more lag-efficient than using 20-30 hoppers.

![[Pasted image 20260302162814.png]]