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

## 📊 Trading Hall Library Layout
**Total Villagers:** 16 Active | 4 Missing/Dead | 20 Total Slots Mapped

### 🛡️ DOWNSTAIRS: Armor & Universals (8 Active, 1 Dead)
*No expansion needed. Fits the 11-slot layout perfectly.*

**🛡️ Universal Core Armor (Front Left Wall - 4 Slots)**
- ✔️ **Villager 1:** Mending I (**12**) + Mending I (**12**)
- ✔️ **Villager 2:** Unbreaking III (**30**/5) + Smite II
- ✔️ **Villager 3:** Protection IV (**~22**) + Flame (**10**)
- [EMPTY] *(Room for PvP specialized armor later)*

**🪖 Helmet Section (Front Right Wall - 4 Slots)**
- ✔️ **Villager 4:** Respiration III (**23**)
- ✔️ **Villager 5:** Aqua Affinity I (**6**/1)
- [EMPTY]
- [EMPTY]

**🥾 Boot Section (Back Left & Middle Wall - 3 Slots)**
- ✔️ **Villager 6:** Feather Falling IV (**55**/30)
- ✔️ **Villager 7:** Frost Walker I + Lunge III 
- 💀 **Villager 8:** [EMPTY] Reserved for **Depth Strider III** *(Dead - Need to replace)*

---

### ⛏️ UPSTAIRS: Tools & Weapons (8 Active, 3 Dead/Missing)
*Swords are locked to the Front Right. Pickaxes are grouped on the Front Left.*

**⛏️ Pickaxe & Tools Section (Front Left Wall - 5 Slots)**
- ✔️ **Villager 9:** Efficiency V (**23**) + Flame (**19**)
- ✔️ **Villager 10:** Bane of Arthropods V (**26**) + Fortune III (**46**) 
- ✔️ **Villager 11:** Silk Touch I (**8**) + Unbreaking II (**18**)
- [EMPTY]
- [EMPTY]

**⚔️ Swords & Mace Section (Front Right Wall - 4 Slots max)**
*(This wall is completely full)*
- ✔️ **Villager 12:** Sharpness V (**34**) + Lure III (**36**) *(Casino replacement)*
- ✔️ **Villager 13:** Looting III (**15**) *(Casino replacement)*
- ✔️ **Villager 14:** Density V (**21**/1) + Flame (**10**) *(Mace)*
- 💀 **Villager 15:** [EMPTY] Reserved for **Fire Aspect II** *(Dead - Need to replace)*

**🏹 Bow Section (Back Left Wall - 1 Slot max)**
- ✔️ **Villager 16:** Power V (**11**) + Channeling I (**45**)

**🔱 Trident & Bow Overflow Section (Back Right Wall - 4 Slots)**
- 💀 **Villager 17:** [EMPTY] Reserved for **Infinity I** *(Missing - Bow)*
- ✔️ **Villager 18:** Riptide III (**33**/28) + Thorns (**40**/35) + Mending I (**10**/5)
- ✔️ **Villager 19:** Impaling V
- 💀 **Villager 20:** [EMPTY] Reserved for **Loyalty III** *(Missing)*

---

### 🗑️ THE BANISHED / ARCHIVE
*Obsolete villagers removed from the main Library to save space/emeralds. Move to AoT City.*
- **Old Sword:** Sharpness V (**44**) *(Replaced by 34 guy)*
- **Old Tools:** Looting III (**27**) + Silk Touch I (**13**) *(Replaced by 15 Looting / 8 Silk Touch guys)*
- **Under Casino Spares:** Luck of the Sea III (**10**), Channeling I (**10**), Lure III (**15**), Lure III (**17**) + Mending I (**16**).


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