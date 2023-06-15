"""
Copyright 2023 AITI-KACE
CSD 29.4 Final Project
Group 4
Kwame Asante Owusu-Addo
Grading System

"""


def check_exam_result():
    # Get student information
    full_name = input("Enter student's full name: ")
    department = input("Enter student's department: ")
    course_of_study = input("Enter student's course of study: ")
    has_paid = input("Has the student paid the fees in full? (yes/no): ")
    if has_paid == "yes":
        has_paid = True
    elif has_paid == "no":
        has_paid = False

    # Get exam and assessment scores
    exam_score = int(input("Enter exam score: "))
    assessment_score = int(input("Enter assessment score: "))
    total_score = exam_score + assessment_score

    # Generate student report summary
    print("----- Student Report Summary -----")
    print("Full Name: ", full_name)
    print("Department: ", department)
    print("Course of Study: ", course_of_study)
    print("Final Score: ", total_score)

    # Condoned and failed
    if total_score == 39:
        print("Condoned")
    elif total_score < 39:
        print("Failed and Repeated")
    elif exam_score < 25:
        print("Failed in the exam component, Certificate Not issued")
    elif assessment_score < 15:
        print("Failed in the assessment component, Certificate Not Issued")

    # Check if the student passed both components
    if total_score >= 40 and exam_score >= 25 and assessment_score >= 15 and has_paid is True:
        print("Passed! Congratulations! Certificate Issued")
    elif not has_paid:
        print("Passed, Fees not paid. Certificate Not Issued")


# Run the program
check_exam_result()
