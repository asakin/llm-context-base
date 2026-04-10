---
type: decision
summary: We chose PostgreSQL over MongoDB for our primary database because our data is relational, we need ACID transactions, and the team has strong SQL experience.
tags: [decision, engineering, database]
status: complete
owner: Tech Lead
updated: 2026-02-20
---

# Choosing PostgreSQL Over MongoDB

- **Date:** 2026-02-20
- **Decision Status:** Implemented

---

## Context

### The Situation
We're building the data layer for our new service. Need to choose a primary database. The service handles user accounts, transactions, and reporting - all highly relational data.

### What We Knew
- Data model is relational (users → orders → items → payments)
- We need ACID transactions for payment processing
- Team has 3 people with strong PostgreSQL experience, 1 with MongoDB
- Expected data volume: ~10M rows in Year 1
- Need good reporting/analytics query support

---

## Options Considered

### Option A: PostgreSQL - SELECTED

**Description:** Relational database with strong ACID compliance, excellent query optimizer, and mature ecosystem.

**Pros:**
- Natural fit for relational data model
- ACID transactions built-in
- Team expertise (3/4 engineers experienced)
- Excellent for complex queries and reporting
- Mature, well-documented, huge community

**Cons:**
- Schema migrations require planning
- Horizontal scaling is more complex than MongoDB

---

### Option B: MongoDB - REJECTED

**Description:** Document database with flexible schema and easy horizontal scaling.

**Pros:**
- Flexible schema for rapid iteration
- Easy horizontal scaling
- Good for unstructured data

**Cons:**
- Poor fit for relational data (would need denormalization)
- Multi-document transactions are slower and more complex
- Only 1 team member has experience
- Reporting queries are harder to write and optimize

**Why Rejected:** Our data is fundamentally relational. Using MongoDB would mean fighting the database instead of leveraging it.

---

## Decision & Rationale

### The Decision
Use PostgreSQL as our primary database for the new service.

### Why This Approach
The data model is relational. PostgreSQL is purpose-built for relational data. The team knows it. The alternative would require denormalization hacks and give up ACID transactions we need for payments.

### Trade-offs Accepted
- Schema migrations require more upfront planning
- If we need to scale beyond a single node, we'll need to invest in partitioning or read replicas

---

## Implementation

- [x] Set up PostgreSQL 16 on cloud provider
- [x] Create initial schema migration
- [x] Configure connection pooling
- [ ] Set up automated backups and monitoring

---

## Outcome

- **Outcome Status:** succeeded
- **Reviewed:** 2026-04-01

### What Actually Happened
PostgreSQL has handled everything we've thrown at it. Complex reporting queries that would have required MapReduce in MongoDB run in milliseconds. Schema migrations have been painless with a proper migration tool. We're at 2M rows and query performance is excellent.

### What We'd Do Differently
Would have set up read replicas from day one instead of waiting. The reporting queries, while fast, do add load to the primary during business hours.

### Constraints Discovered
- Connection pooling is essential from the start - we hit connection limits in week 2 before adding PgBouncer
- Schema migrations need to be backward-compatible if you deploy with zero downtime (can't just drop columns)

---

## For Future Reference

**When to cite this decision:** When evaluating databases for new services with relational data models.

**Key takeaways:**
- Match the database to the data model, not the hype
- Team expertise matters - a familiar tool used well beats a novel tool used poorly
- Set up read replicas early if you expect reporting workloads
- Connection pooling is not optional - add it before you need it

---

## Change Log

| Date | Change | Author |
|------|--------|--------|
| 2026-02-20 | Initial decision | Tech Lead |
| 2026-03-01 | Updated status to Implemented | Tech Lead |
| 2026-04-01 | Added outcome after 6 weeks in production | Tech Lead |
