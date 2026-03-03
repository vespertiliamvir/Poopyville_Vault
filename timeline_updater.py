import os
from datetime import datetime, timedelta

TICKETS_DIR = 'Tickets'

# 1. Create Lava Room ticket if it doesn't exist
lava_path = os.path.join(TICKETS_DIR, "Lava_Room.md")
if not os.path.exists(lava_path):
    with open(lava_path, "w") as f:
        f.write("---\nstatus: Todo\n---\n# Lava Room\nAssigned to Wei.\n")

# 2. Your core priority schedule
schedule_logic = [
    ("Face_Cards_-_Queens", 48),
    ("Face_Cards_-_Jacks", 48),
    ("Poker_Redstone_-_Shuffler", 42),
    ("Plinko_-_Hook_up_7-Segment", 7),
    ("Plinko_-_Payment", 7),
    ("Dropper_Game_-_Core", 42),
    ("Dropper_Game_-_7-Segment", 7),
    ("Slot_Machines_-_Group_1", 7),
    ("Slot_Machines_-_Group_2", 7),
    ("Casino_-_Redo_Lighting", 7),
    ("Casino_-_Detailing", 14),
    ("iPhone_-_Raise_up", 42),
    ("iPhone_-_Finalize", 14)
]

current_date = datetime(2026, 3, 1)
timeline_map = {}

for partial_name, days in schedule_logic:
    start_str = current_date.strftime("%Y-%m-%d")
    current_date += timedelta(days=days)
    due_str = current_date.strftime("%Y-%m-%d")
    timeline_map[partial_name] = (start_str, due_str)

backlog_start = current_date.strftime("%Y-%m-%d")

# 3. Update all files with Assignees and Dates
for filename in os.listdir(TICKETS_DIR):
    if not filename.endswith('.md'):
        continue
        
    filepath = os.path.join(TICKETS_DIR, filename)
    
    # Assign names based on the file title
    assignee = "David" # Default assignment
    if "Contractors" in filename:
        assignee = "Contractors"
    elif "Tao" in filename:
        assignee = "Tao"
    elif "Rama" in filename:
        assignee = "Rama"
    elif "Optic" in filename:
        assignee = "Optic Dust & David"
    elif "Lava" in filename:
        assignee = "Wei"
        
    # Assign dates
    start_date = backlog_start
    due_date = (datetime.strptime(backlog_start, "%Y-%m-%d") + timedelta(days=14)).strftime("%Y-%m-%d")
    
    for partial_name, (start, due) in timeline_map.items():
        if partial_name in filename:
            start_date = start
            due_date = due
            break
            
    # Hardcode Wei's Lava Room deadline to June 30th
    if "Lava" in filename:
        start_date = "2026-06-16"
        due_date = "2026-06-30"
        
    # Read and modify the file
    with open(filepath, 'r') as file:
        lines = file.readlines()
        
    if lines and lines[0].strip() == "---":
        new_lines = []
        has_assignee = False
        has_start = False
        has_due = False
        
        for line in lines:
            if line.startswith("start:"):
                new_lines.append(f"start: {start_date}\n")
                has_start = True
            elif line.startswith("due:"):
                new_lines.append(f"due: {due_date}\n")
                has_due = True
            elif line.startswith("assignee:"):
                new_lines.append(f"assignee: {assignee}\n")
                has_assignee = True
            else:
                new_lines.append(line)
                
        # Inject any missing properties
        if not has_assignee:
            new_lines.insert(1, f"assignee: {assignee}\n")
        if not has_start:
            new_lines.insert(2, f"start: {start_date}\n")
        if not has_due:
            new_lines.insert(3, f"due: {due_date}\n")
            
        with open(filepath, 'w') as file:
            file.writelines(new_lines)

print("\nSuccess! All tickets assigned and timed.")