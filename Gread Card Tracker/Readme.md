# Student Grade Tracker
Student Grade Tracker is a simple Python application designed to help educators and students manage and track grades efficiently. It allows users to input grades for various subjects, calculate average grades, and generate a comprehensive grade card as a PDF.

## Features
1. Student Information

Input and manage details such as:
* Student Name
* Roll Number
* Class

2. Subject and Marks Management

* Add subject names and corresponding marks.
* Automatically calculate grades based on the marks entered.

3. Grade Calculations

* View the average marks and grade.
* Get a clear result indicating whether the student passed or failed.

4. Grade Card Generation
* Export the grade card as a PDF file with all the entered details and grades.

5. List Management
* Clear individual subjects from the list.
Clear all grades to start fresh.

## Requirements
Before running the application, ensure you have the following installed:

* Python 3.x
* `tkinter` (usually included with Python)
* `reportlab` (Install via pip install reportlab)

## How to Run
* Clone or download this repository.
* Install the required dependencies:
```
pip install reportlab
```
* Run the script:
```
python main.py
```

## Usage
1. Entering Student Details.
* Fill in the Student Name, Roll Number, and Class fields at the top of the window.

2. Adding Subject and Marks
* Enter the subject name and marks in the respective fields.
* Click Add Marks to save them to the list.

3. Calculate Grades
* Click Calculate Grades to compute the average marks and grade.
4. Generate Grade Card
* Ensure all student details are filled.
* Click Generate Grade Card to save the details and grades as a PDF file.
5. Manage the Grades List
* Use Clear Selected to remove a selected subject from the list.
* Use Clear All to remove all entries.

## Grade Evaluation Criteria

|  Marks Range  |      Grade    |  
| ------------- |:-------------:| 
|  0  - 32      |       F       |   
|  33 - 39    	|       D       | 
|  40 - 49      |   	C       |
|  50 - 59  	|       B       |
|  60 - 69      |   	A-      |
|  70 - 79      |    	A       |
|  80 - 100     |   	A+      |



## Output Example
The Grade Card PDF includes:

* Student Name, Roll Number, and Class.
* List of subjects with marks and grades.
* Average marks and overall grade.
* Result indicating Pass/Fail.