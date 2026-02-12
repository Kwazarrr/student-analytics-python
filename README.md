# student-analytics-python
# Student Analytics (Pure Python)

Mini data analysis project implemented without external libraries.

## 📌 Project Overview

This project demonstrates:

- CSV file parsing
- Data cleaning
- Data transformation
- Group-by logic using dictionaries
- Aggregations:
  - Count students per group
  - Sum grades per group
  - Average grade per group

The goal was to implement group-by logic manually (without pandas) to deeply understand data structures and aggregation mechanics.

---

## 📂 Dataset

`students.csv`

Format:

name,group,grade
Ann,G1,4
Bob,G2,5
Kate,G1,3
Max,G2,2
Eva,G1,5
John,G2,4
Lisa,G3,5
Mark,G3,3

---

## ⚙️ Functionality

The project includes:

- `load_students()` — CSV parsing into list of dictionaries
- `count_students_by_group()` — count aggregation
- `sum_grades_by_group()` — sum aggregation
- `avg_grade_of_groups()` — average aggregation

---

## ▶️ How to Run

```bash
python main.py
