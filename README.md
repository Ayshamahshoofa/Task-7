# Task-7

## 🎯 Objective

Use **SQLite + Python** to pull simple sales information and visualize revenue with a bar chart.

This task demonstrates:

* Connecting Python to SQLite
* Running SQL query inside Python
* Loading SQL result into Pandas
* Printing a sales summary
* Plotting a bar chart using Matplotlib

---

## 📂 Project Files

| File              | Description                                           |
| ----------------- | ----------------------------------------------------- |
| `create_db.py`    | Creates SQLite database and inserts sample sales data |
| `task7_script.py` | Runs SQL query, prints result, and plots bar chart    |
| `sales_data.db`   | SQLite database (auto-generated)                      |
| `sales_chart.png` | Revenue bar chart (auto-generated)                    |
| `README.md`       | Project explanation                                   |

---

## 🛠️ Technologies Used

* Python
* SQLite (built-in Python database)
* Pandas
* Matplotlib

---

## 📁 Dataset

Sample sales data created directly inside the script with columns:

* Product
* Quantity
* Price

---

## ▶️ How to Run the Project

### Step-1: Create & Load Database

```
python create_db.py
```

Output:

```
Database created and sample data inserted ✅
```

### Step-2: Run Analysis & Plot Chart

```
python task7_script.py
```

Output:

* Printed sales summary in terminal
* Bar chart displayed
* `sales_chart.png` saved

---

## 📊 Example Output

### Terminal Table

```
✅ Sales Summary:
     product  total_quantity  total_revenue
     Shampoo              XX           XXXX
    Face Wash            XX           XXXX
  Moisturizer            XX           XXXX
```

### Bar Chart

A bar chart comparing total revenue by product.

---

## ✅ Summary

This task successfully:

* Created a small sales database
* Executed SQL query in Python
* Printed sales results
* Visualized revenue data
* Saved chart output

---


* ✅ GitHub commit message
* ✅ Folder structure screenshot sample
* ✅ PPT for this task

Just tell me!
