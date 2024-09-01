---
reviewed: "0"
tags:
  - periodic/daily
---

> [!my] review
>```dataview
>LIST
> WHERE (date(this.file.name) - date(file.day)).days = number(forgetting) AND file.folder != "Daily" AND file.folder != "Staff/Templates" AND contains(file, "day") 
>```

> [!my] review web pages
>```dataview
> TASK
> WHERE file.name = "learned" AND (date(this.file.name) - due).days = number(f)
> ```

>[!my] todo
>```dataview
>List
>WHERE done = "0" and !contains(file.path, "Staff")
>```

>[!my] not reviewed
>```dataview
>List
>WHERE reviewed = "0" and !contains(file.path, "Staff")
>```
