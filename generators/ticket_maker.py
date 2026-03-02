import json
import os

# The JSON file containing our recovered Jira tickets
JSON_FILE = 'tickets.json'
# The folder where the Obsidian Markdown files will be generated
# We are in /generators, so we go up one level and into /vault/Tickets
OUTPUT_DIR = os.path.join('..', 'vault', 'Tickets')

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

with open(JSON_FILE, 'r') as f:
    tickets = json.load(f)

for ticket in tickets:
    # Sanitize the filename for Obsidian
    filename = f"{ticket['title'].replace(' ', '_').replace('/', '-')}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Writing Obsidian-friendly Markdown with Frontmatter for the Kanban plugin
    with open(filepath, 'w') as md_file:
        md_file.write("---\n")
        md_file.write(f"status: {ticket['status']}\n")
        md_file.write(f"tags: {ticket['tags']}\n")
        md_file.write("---\n\n")
        md_file.write(f"# {ticket['title']}\n\n")
        md_file.write(f"**Description:**\n{ticket['description']}\n\n")
        md_file.write(f"**Technical Notes:**\n{ticket['notes']}\n")

print(f"Success! Generated {len(tickets)} Obsidian Markdown tickets for Poopyville.")
