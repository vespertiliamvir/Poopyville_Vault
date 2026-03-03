### 📋 Active Sprints
```dataview
TABLE start as "Start Date", due as "Deadline", assignee as "Assignee", status as "Status"
FROM "Tickets"
SORT due ASC
```


---

### 📊 Visual Timeline (Gantt Chart)
```dataviewjs
let pages = dv.pages('"Tickets"').where(p => p.start && p.due).sort(p => p.start);
let chart = "gantt\n    title Poopyville Server 1.0 Roadmap\n    dateFormat YYYY-MM-DD\n";

for (let p of pages) {
    let name = p.file.name.replace(/_/g, " ").replace(".md", "");
    chart += `    ${name} :${p.start}, ${p.due}\n`;
}

dv.paragraph("```mermaid\n" + chart + "\n```");
```