---
modified: 2026-09-26T19:31
created: 2026-09-01T22:47
---
# Executive MBA Notes 

```dataview
LIST rows.file.link
FROM "002 MBA/010 Notes" 
where file.name != "index" and file.name != file.folder
FLATTEN regexreplace(file.folder, "^[^/]*/[^/]*/?", "") AS trimmed_folder
group by trimmed_folder as "Folder"
```
