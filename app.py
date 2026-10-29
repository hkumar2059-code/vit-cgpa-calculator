import math
from flask import Flask, render_template, request

app = Flask(__name__)


def get_grade_and_gp(marks, avg, sd):
    """
    Assign a letter grade and grade point using relative grading.
    Falls back to absolute grading when SD is zero (all identical scores).
    """
    if sd == 0:
        if marks >= 90:
            return "S", 10
        elif marks >= 80:
            return "A", 9
        elif marks >= 70:
            return "B", 8
        elif marks >= 60:
            return "C", 7
        elif marks >= 50:
            return "D", 6
        elif marks >= 40:
            return "E", 5
        else:
            return "F", 0

    if marks > avg + 1.5 * sd:
        return "S", 10
    elif marks > avg + 0.5 * sd:
        return "A", 9
    elif marks > avg - 0.5 * sd:
        return "B", 8
    elif marks > avg - 1.0 * sd:
        return "C", 7
    elif marks > avg - 1.5 * sd:
        return "D", 6
    elif marks > avg - 2.0 * sd:
        return "E", 5
    else:
        return "F", 0


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            num_students = int(request.form.get("num_students", 0))
            num_subjects = int(request.form.get("num_subjects", 0))

            if num_students <= 0 or num_subjects <= 0:
                raise ValueError("Number of students and subjects must be at least 1.")

            # --- Collect subject metadata ---
            subject_names = []
            subject_credits = []
            for j in range(num_subjects):
                s_name = (
                    request.form.get(f"sub_name_{j}", f"Subject {j+1}").strip()
                    or f"Subject {j+1}"
                )
                s_credit = float(request.form.get(f"sub_credit_{j}", 1))
                subject_names.append(s_name)
                subject_credits.append(s_credit)

            # --- Collect student marks ---
            students_data = []
            all_total_marks = []  # flat list across every (student, subject) pair

            for i in range(num_students):
                student_name = (
                    request.form.get(f"student_name_{i}", f"Student {i+1}").strip()
                    or f"Student {i+1}"
                )
                student_subjects = []

                for j in range(num_subjects):
                    cat1 = float(request.form.get(f"cat1_{i}_{j}", 0))
                    cat2 = float(request.form.get(f"cat2_{i}_{j}", 0))
                    quiz = float(request.form.get(f"quiz_{i}_{j}", 0))
                    assessment = float(request.form.get(f"assesment_{i}_{j}", 0))
                    fat = float(request.form.get(f"fat_{i}_{j}", 0))

                    # Scale each component
                    con_cat1 = (cat1 / 50.0) * 15.0
                    con_cat2 = (cat2 / 50.0) * 15.0
                    con_quiz = (quiz / 50.0) * 15.0
                    con_assessment = (assessment / 100.0) * 15.0
                    con_fat = (fat / 100.0) * 40.0

                    total_marks = (
                        con_cat1 + con_cat2 + con_quiz + con_assessment + con_fat
                    )
                    all_total_marks.append(total_marks)

                    student_subjects.append(
                        {
                            "sub_name": subject_names[j],
                            "credit": subject_credits[j],
                            "total_marks": round(total_marks, 2),
                        }
                    )

                students_data.append(
                    {"name": student_name, "subjects": student_subjects}
                )

            # --- Compute class-level statistics ---
            n_entries = len(all_total_marks)
            if n_entries > 0:
                avg_marks = sum(all_total_marks) / n_entries
                sq_diff = sum((x - avg_marks) ** 2 for x in all_total_marks)
                sd_marks = math.sqrt(sq_diff / n_entries)
            else:
                avg_marks = 0
                sd_marks = 0

            # --- Assign grades and compute per-student CGPA ---
            all_cgpas = []
            for student in students_data:
                total_gp_credits = 0
                total_credits = 0

                for sub in student["subjects"]:
                    grade, gp = get_grade_and_gp(
                        sub["total_marks"], avg_marks, sd_marks
                    )
                    sub["grade"] = grade
                    sub["gp"] = gp
                    total_gp_credits += gp * sub["credit"]
                    total_credits += sub["credit"]

                student_cgpa = (
                    round(total_gp_credits / total_credits, 2)
                    if total_credits > 0
                    else 0
                )
                student["cgpa"] = student_cgpa
                all_cgpas.append(student_cgpa)

            class_avg_cgpa = (
                round(sum(all_cgpas) / len(all_cgpas), 2) if all_cgpas else 0
            )

            results = {
                "students": students_data,
                "class_avg_marks": round(avg_marks, 2),
                "class_sd_marks": round(sd_marks, 2),
                "class_avg_cgpa": class_avg_cgpa,
            }

            return render_template("index.html", results=results)

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html", results=None)


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


if __name__ == "__main__":
    app.run(debug=True)
