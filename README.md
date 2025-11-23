# 🧹 Hostel Hygiene & Health Monitoring System

A simple *Python Console Application* to report and track hygiene issues in a hostel.  
It allows students to register complaints regarding *water, food, washrooms, mosquitoes, room cleanliness*, and other hygiene problems.  
The system also provides *analytics* to predict possible *health risks* in the hostel.

---

## 🚀 Features

### 🔴 Complaint Management
- Add hygiene-related complaints
- Categories like:
  - Water
  - Food
  - Washroom
  - Room
  - Mosquito
  - Other

### 📋 View All Reports
- Display all recorded complaints with category & description

### 📊 Hygiene Risk Analytics
- Auto-detects frequently reported issues
- Shows possible health hazards:
  - Water issues → Typhoid/jaundice risk
  - Food complaints → Food poisoning
  - Washroom → Skin/fungal infection
  - Mosquito → Dengue/Malaria

---

## 🛠 How to Run

### *Requirements*
- Python 3.x installed

### *Steps*
1. Copy the code into a file named: hostel_hygiene_system.py
2. Open terminal/command prompt
3. Run the program:
   ```bash
   python hostel_hygiene_system.py
## *Sample Output Screens*

### *Main Menu*
------ Hostel Hygiene & Health Monitoring System ------

1. Report a Hygiene Problem
2. View All Reports
3. Hygiene Risk Analytics
4. Exit

Enter your choice (1-4):
### *Report a Complaint*
--- Report a Hygiene Problem ---
Enter category (Water/Food/Washroom/Room/Mosquito/Other): Water
Enter short description of the problem: Yellow water coming from tap

Congratulations! Complaint Added Successfully!
###  *Viewing All Complaints*
--- All Hygiene Complaints ---
Complaint #1
Category    : Water
Description : Yellow water coming from tap
### *Hygiene Risk Analytics Output*
--- Hygiene Risk Analytics ---

Water Issues Reported: 3
High Risk of jaundice/typhoid due to water quality!
