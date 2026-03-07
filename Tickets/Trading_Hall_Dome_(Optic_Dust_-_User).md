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


IF multiple villagers get turned into zombies, special measures will need to be taken to cure them 1 at a time after destroying the lecturns and securing them in place to not fuck up the linking


we have 22 book spots
---

## 📊 Trading Hall Library Layout
**Status:** In Dome for library reorganization/restructure. 
**Total Villagers:** 16 Active | 5 Missing/Dead/Future | 21 Total Slots Mapped

### 🛡️ DOWNSTAIRS: Armor & Universals (8 Active, 1 Dead, 1 Future)
*Highly subcategorized by armor piece. Universals isolated on the back wall.*

**🥾 Boots & 🪖 Helmets Section (Front Left Wall - 4 Slots)**
*Left side is Boots, Right side is Helmets*
- ✔️ **Villager 1 (Boots):** Feather Falling IV (**55**/30)
- 💀 **Villager 2 (Boots):** [EMPTY] Reserved for **Depth Strider III** *(Dead - Need to replace)*
- ✔️ **Villager 3 (Helmet):** Respiration III (**23**)
- ✔️ **Villager 4 (Helmet):** Aqua Affinity I (**6**/1)

**👕 Core Armor / Chestplate Section (Front Right Wall - 4 Slots)**
- ✔️ **Villager 5:** Protection IV (**~22**) + Flame (**10**)
- [EMPTY] *(Room for future specialized armor)*
- [EMPTY] *(Room for future specialized armor)*
- [EMPTY] *(Room for future specialized armor)*

**✨ Universal "God Book" Section (Back Middle Wall - 3 Slots)**
- ✔️ **Villager 6:** Mending I (**12**) + Mending I (**12**) *(Double Mending)*
- ✔️ **Villager 7:** Unbreaking III (**30**/5) + Smite II
- 💀 **Villager 8:** [EMPTY] Reserved for **Future Extra Unbreaking III**

---

### ⛏️ UPSTAIRS: Tools & Weapons (8 Active, 3 Dead/Missing)
*Subcategorized perfectly by weapon/tool type.*

**⛏️ Pickaxes & ⚔️ Core Swords (Front Left Wall - 5 Slots)**
- ✔️ **Villager 9 (Pickaxe):** Efficiency V (**23**) + Flame (**19**)
- ✔️ ~~**Villager 10 (Pickaxe):** Fortune III (**29**) + Thorns III (**36**) *(Casino replacement)~~* SWITCHED to fortune 3 for 26, with bane of arthropods V for 46 (and impaling Iv for 18)
- ✔️ **Villager 11 (Pickaxe):** Silk Touch I (**8**) + Unbreaking II (**18**)
- ✔️ **Villager 12 (Sword):** Sharpness V (**34**) + Lure III (**36**) *(Casino replacement)*
- ✔️ **Villager 13 (Sword):** Looting III (**15**) *(Casino replacement)*

**🔥 Fire, 🔨 Mace, & 🔱 Spear/Trident Section (Front Right Wall - 4 Slots)**
- 💀 **Villager 14 (Sword/Fire):** [EMPTY] Reserved for **Fire Aspect II** *(Dead - Need to replace)*
- ✔️ **Villager 15 (Mace):** Density V (**21**/1) + Flame (**10**) 
- ✔️ **Villager 16 (Mace/Boots):** Lunge III + Frost Walker I 
- ✔️ **Villager 17 (Trident):** Impaling V

**🏹 Bow Section (Back Middle Wall - 2 Slots)**
- ✔️ **Villager 18:** Power V (**11**) + Channeling I (**45**)
- 💀 **Villager 19:** [EMPTY] Reserved for **Infinity I** *(Missing - Bow)*

**🔱 Trident Overflow Section (Back Right Wall - 2 Slots)**
- ✔️ **Villager 20:** Riptide III (**33**/28) + Thorns (**40**/35) + Mending I (**10**/5)
- 💀 **Villager 21:** [EMPTY] Reserved for **Loyalty III** *(Missing - Trident)*

---

### 🗑️ THE BANISHED / ARCHIVE
*Obsolete villagers removed from the main Library to save space/emeralds. Move to AoT City.*
- **Old Tools:** Bane of Arthropods V (**26**) + Fortune III (**46**) *(Replaced by 29 Fort guy)*
- **Old Sword:** Sharpness V (**44**) *(Replaced by 34 guy)*
- **Old Tools:** Looting III (**27**) + Silk Touch I (**13**) *(Replaced by 15 Looting / 8 Silk Touch guys)*
- **Under Casino Spares:** Mending I (**16**) + Lure III (**17**), Luck of the Sea III (**10**), Channeling I (**10**), Lure III (**15**).

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