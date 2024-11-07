import student # importing our library of test
from student import Student
import pytest

 
@pytest.fixture #test fixture decorator
def student():
  return Student()  #create an instance of student
 
def test_create_student_grades(student):
  assert(student.grades) == []
   
def test_create_student_average(student):
  assert(student.academic_average) == 0
 
def test_add_grades(student):
  student.add_grade(12)
  assert(student.academic_average) == 12
