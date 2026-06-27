# SCSJ4383 Software Construction - Part B
# Refactored Code (Code Smells Fixed)
# Fix 1: Long Method -> Extract Method + Single Responsibility Principle (SRP)
# Fix 2: Duplicate Code -> Extract Method + DRY Principle

class Database:
    def save(self, name, score, grade):
        print(f"[DB] Saved: {name}, {score}, {grade}")


# FIX 1: Extract Method + SRP
# Each class now has ONE responsibility

class StudentValidator:
    """Responsible for: input validation only."""
    def validate(self, name: str, score: float) -> None:
        if not name or len(name) < 2:
            raise ValueError("Name must be at least 2 characters")
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100")


class GradeCalculator:
    """Responsible for: grade calculation only."""
    def calculate(self, score: float) -> str:
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        elif score >= 60: return 'D'
        else: return 'F'


class StudentRepository:
    """Responsible for: data persistence only."""
    def save(self, name: str, score: float, grade: str) -> None:
        db = Database()
        db.save(name, score, grade)


class StudentService:
    """Orchestrates the workflow, delegates to specialist classes."""
    def __init__(self):
        self.validator  = StudentValidator()
        self.calculator = GradeCalculator()
        self.repository = StudentRepository()

    def process(self, name: str, score: float) -> None:
        self.validator.validate(name, score)
        grade = self.calculator.calculate(score)
        self.repository.save(name, score, grade)
        print(f"Student: {name} | Score: {score} | Grade: {grade}")


# FIX 2: Extract Method + DRY
# Single source of truth for grade label logic

class ReportGenerator:
    """Responsible for: report generation only."""

    def get_grade_label(self, score: float) -> str:
        """Single authoritative method for grade labels. Change logic here only."""
        if score >= 90: return 'Excellent'
        elif score >= 70: return 'Good'
        elif score >= 50: return 'Pass'
        else: return 'Fail'

    def generate_student_report(self, score: float) -> str:
        return f"Student Grade: {self.get_grade_label(score)}"

    def generate_transcript(self, score: float) -> str:
        return f"Transcript Grade: {self.get_grade_label(score)}"

    def generate_report(self, score: float) -> str:
        return f"Report Grade: {self.get_grade_label(score)}"


# Demo
if __name__ == "__main__":
    service = StudentService()
    service.process("Hana", 85)

    rg = ReportGenerator()
    print(rg.generate_student_report(85))
    print(rg.generate_transcript(85))
