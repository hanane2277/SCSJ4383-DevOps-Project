# SCSJ4383 Software Construction - Part B
# Original Code (with Code Smells)
# Code Smell 1: Long Method - process() does 4 things
# Code Smell 2: Duplicate Code - get_grade_label_*() repeated 3 times

class Database:
    def save(self, name, score, grade):
        print(f"[DB] Saved: {name}, {score}, {grade}")

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def process(self):
        """CODE SMELL: Long Method - handles validation, calculation, persistence, and reporting."""
        # 1. Validation
        if not self.name or len(self.name) < 2:
            raise ValueError("Invalid name")
        if not (0 <= self.score <= 100):
            raise ValueError("Invalid score")

        # 2. Grade calculation
        if self.score >= 90:
            grade = 'A'
        elif self.score >= 80:
            grade = 'B'
        elif self.score >= 70:
            grade = 'C'
        elif self.score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        # 3. Save to database
        db = Database()
        db.save(self.name, self.score, grade)

        # 4. Generate report
        print(f"Student: {self.name}")
        print(f"Score:   {self.score}")
        print(f"Grade:   {grade}")


class ReportGenerator:
    """CODE SMELL: Duplicate Code - three identical get_grade_label methods."""

    def get_grade_label_student(self, score):
        if score >= 90: return 'Excellent'
        elif score >= 70: return 'Good'
        elif score >= 50: return 'Pass'
        else: return 'Fail'

    def get_grade_label_transcript(self, score):
        if score >= 90: return 'Excellent'
        elif score >= 70: return 'Good'
        elif score >= 50: return 'Pass'
        else: return 'Fail'

    def get_grade_label_report(self, score):
        if score >= 90: return 'Excellent'
        elif score >= 70: return 'Good'
        elif score >= 50: return 'Pass'
        else: return 'Fail'
