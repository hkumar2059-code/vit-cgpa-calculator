# VIT Vellore Class CGPA Calculator

A Flask-based web application to calculate and estimate student grades and CGPA using VIT's relative grading system (Mean & Standard Deviation model).

## Features
- **Dynamic Input Grid:** Enter any number of students ($N$) and subjects ($A$) with custom credit weights.
- **Evaluation Weightage Breakdown:**
  - CAT-1 (Max 50) scaled to 15%
  - CAT-2 (Max 50) scaled to 15%
  - Quiz (Max 50) scaled to 15%
  - Assessment (Max 100) scaled to 15%
  - FAT (Max 100) scaled to 40%
- **Relative Grading System:**
  - Computes class average marks ($\mu$) and standard deviation ($\sigma$).
  - Assigns S, A, B, C, D, E, and F letter grades based on deviation thresholds.
  - Generates per-student CGPA and overall class performance statistics.
- **Clean UI:** Built with HTML5, vanilla JavaScript, and Bootstrap 5.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/vit-cgpa-calculator.git
   cd vit-cgpa-calculator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure
```text
vit-cgpa-calculator/
├── app.py                  # Flask backend & grading calculation logic
├── requirements.txt        # Python package dependencies
├── generate_favicon.py     # Favicon generation script
├── static/
│   ├── css/
│   │   └── style.css       # Custom styles
│   └── img/
│       └── favicon.ico     # Application favicon
└── templates/
    ├── index.html          # Main calculator page
    ├── privacy.html        # Privacy policy
    └── terms.html          # Terms and conditions
```
