# Database Schema

## PostgreSQL

### users
- id: UUID primary key
- email: varchar
- name: varchar
- role: varchar
- mfa_enabled: boolean
- password_hash: varchar
- created_at: timestamp

### devices
- id: UUID primary key
- user_id: UUID
- hostname: varchar
- os: varchar
- mac_address: varchar
- ip_address: varchar
- browser: varchar
- trust_score: integer
- patch_status: varchar
- antivirus_status: varchar
- disk_encryption: boolean
- firewall_enabled: boolean

### policies
- id: UUID primary key
- name: varchar
- policy_type: varchar
- rules: jsonb
- active: boolean

### incidents
- id: UUID primary key
- title: varchar
- severity: varchar
- source_ip: varchar
- user_id: UUID
- status: varchar
- created_at: timestamp

## MongoDB

### alerts
- _id: ObjectId
- event_id: string
- severity: string
- type: string
- source: string
- payload: object
- timestamp: date

### telemetry
- _id: ObjectId
- device_id: string
- user_id: string
- metric: string
- value: float
- timestamp: date

## Redis

- session tokens
- rate limit counters
- asynchronous job queues
