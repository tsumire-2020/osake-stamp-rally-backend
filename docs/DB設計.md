
```mermaid
erDiagram
  user ||--o{ StampRally: has
  StampRally ||--|{ Stamp: has
  Stamp ||--|{ StampResult: has
  Stamp ||--|{ Alcohol: has
  user ||--o{ StampResult: has

  StampResult {
    bool isStamped
    date stampedDate
  }
```

- アルコールはスクリプトは入れる