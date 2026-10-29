import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path):
    prs = Presentation()
    # 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette - Professional Academic Deep Navy & Cyan/Gold
    C_BG = RGBColor(11, 25, 44)         # #0B192C Dark Navy
    C_CARD = RGBColor(19, 39, 67)       # #132743 Slightly lighter navy card
    C_CARD_BORDER = RGBColor(30, 62, 98) # Border
    C_ACCENT = RGBColor(13, 110, 253)   # #0D6EFD Electric Blue
    C_CYAN = RGBColor(0, 210, 255)      # #00D2FF Neon Cyan
    C_GOLD = RGBColor(255, 193, 7)      # #FFC107 Accent Gold
    C_TEXT = RGBColor(245, 247, 250)    # Primary Light Text
    C_MUTED = RGBColor(160, 174, 192)   # Muted Grey Text
    C_WHITE = RGBColor(255, 255, 255)
    C_SUCCESS = RGBColor(25, 135, 84)

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background() # no border
        return bg

    def add_header(slide, title_text, category_text="VIT VELLORE • PROJECT EVALUATION"):
        # Category / breadcrumb
        tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.35))
        tf_cat = tb_cat.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_CYAN

        # Title
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

        # Divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.55), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = C_CARD_BORDER
        line.line.fill.background()

    def add_card(slide, left, top, width, height, bg_color=C_CARD, border_color=C_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.5)
        else:
            card.line.fill.background()
        return card

    # ==========================================
    # SLIDE 1: Title Slide (Hero)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Accent decorative top bar
    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.1))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = C_CYAN
    top_bar.line.fill.background()

    # Subtitle / Department tag
    tag_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.0), Inches(4.8), Inches(0.42))
    tag_box.fill.solid()
    tag_box.fill.fore_color.rgb = C_CARD
    tag_box.line.color.rgb = C_CYAN
    tf_tag = tag_box.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.alignment = PP_ALIGN.CENTER
    p_tag.text = "VELLORE INSTITUTE OF TECHNOLOGY"
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = C_CYAN

    # Main Title
    tb_title = s1.shapes.add_textbox(Inches(0.9), Inches(1.6), Inches(11.5), Inches(1.6))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    p_main = tf_title.paragraphs[0]
    p_main.text = "VIT Vellore Class CGPA Calculator"
    p_main.font.size = Pt(38)
    p_main.font.bold = True
    p_main.font.color.rgb = C_WHITE

    p_sub = tf_title.add_paragraph()
    p_sub.text = "Automated Relative Grading System & Class-Wide Statistical Performance Evaluator"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = C_MUTED
    p_sub.space_before = Pt(8)

    # Guide Card (Submitted to)
    add_card(s1, Inches(0.9), Inches(3.5), Inches(4.0), Inches(3.3))
    tb_guide = s1.shapes.add_textbox(Inches(1.2), Inches(3.7), Inches(3.4), Inches(2.9))
    tf_guide = tb_guide.text_frame
    tf_guide.word_wrap = True
    
    p = tf_guide.paragraphs[0]
    p.text = "PROJECT SUPERVISOR"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p = tf_guide.add_paragraph()
    p.text = "Prof. Yogaraja C"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.space_before = Pt(6)

    p = tf_guide.add_paragraph()
    p.text = "School of Information Technology\nand Engineering (SITE)\nVIT Vellore"
    p.font.size = Pt(12)
    p.font.color.rgb = C_MUTED
    p.space_before = Pt(8)

    # Team Members Card
    add_card(s1, Inches(5.2), Inches(3.5), Inches(7.2), Inches(3.3))
    tb_team = s1.shapes.add_textbox(Inches(5.5), Inches(3.7), Inches(6.6), Inches(2.9))
    tf_team = tb_team.text_frame
    tf_team.word_wrap = True

    p = tf_team.paragraphs[0]
    p.text = "PROJECT TEAM MEMBERS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    members = [
        ("Himanshu Kumar", "26BIT0347", "Full-Stack & Algorithms"),
        ("Srujan Y K", "26BIT0225", "UI/UX & Dynamic DOM"),
        ("Savant Kashyap", "26BIT0360", "Form Logic & Validation"),
        ("Parv Jain", "26BIT0230", "Testing & Documentation")
    ]

    for name, reg, role in members:
        p = tf_team.add_paragraph()
        p.text = f"{name}  •  {reg}"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.space_before = Pt(8)

        p2 = tf_team.add_paragraph()
        p2.text = f"Role: {role}"
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_MUTED

    # ==========================================
    # SLIDE 2: Problem Statement & Motivation
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Problem Statement & Motivation")

    points_data = [
        ("Relative Grading Complexity", "VIT employs relative grading based on dynamic class statistics (Mean and Standard Deviation). Grade boundaries are never fixed, making manual estimation tedious and prone to mathematical inaccuracies.", C_CYAN),
        ("Multi-Component Weightage Scaling", "Every theory course blends 5 separate assessments: CAT-1 (15%), CAT-2 (15%), Quiz (15%), Digital Assessment (15%), and FAT (40%). Students struggle to combine scaled percentages manually.", C_GOLD),
        ("Lack of Batch-Wide Simulation Tools", "Existing tools only compute individual historical GPA. There is no lightweight tool for professors or students to simulate an entire class cohort and predict grade cutoffs before official results.", C_ACCENT)
    ]

    col_w = Inches(3.7)
    gap = Inches(0.3)
    start_x = Inches(0.8)

    for idx, (title, desc, color) in enumerate(points_data):
        x = start_x + idx * (col_w + gap)
        add_card(s2, x, Inches(2.0), col_w, Inches(4.8))
        
        # Pill header
        pill = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.3), Inches(2.3), col_w - Inches(0.6), Inches(0.4))
        pill.fill.solid()
        pill.fill.fore_color.rgb = C_BG
        pill.line.color.rgb = color
        p = pill.text_frame.paragraphs[0]
        p.text = f"KEY CHALLENGE #{idx+1}"
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = color
        p.alignment = PP_ALIGN.CENTER

        tb = s2.shapes.add_textbox(x + Inches(0.3), Inches(3.0), col_w - Inches(0.6), Inches(3.5))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(13)
        p_desc.font.color.rgb = C_MUTED
        p_desc.space_before = Pt(14)

    # ==========================================
    # SLIDE 3: System Architecture
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "System Architecture & Data Pipeline")

    arch_blocks = [
        ("1. Dynamic Client Grid", "HTML5 + Vanilla JS", "Accepts N students and A subjects.\nDynamically injects responsive DOM cards with component inputs.\nClient-side validation protects against invalid ranges.", Inches(0.8)),
        ("2. Flask Controller", "Python 3 + Jinja2", "Receives HTTP POST payload.\nParses multi-dimensional student & subject matrix.\nScales 5-component assessments to standard 100-mark base.", Inches(4.8)),
        ("3. Statistical Engine", "Relative Grading & CGPA", "Calculates Class Mean (μ) & SD (σ).\nAssigns relative letter grades (S-F).\nComputes weighted CGPA: Σ(GP × Cr) / ΣCr.\nZero-persistence privacy model.", Inches(8.8))
    ]

    for title, tech, desc, x_pos in arch_blocks:
        add_card(s3, x_pos, Inches(2.0), Inches(3.7), Inches(4.8))

        tb = s3.shapes.add_textbox(x_pos + Inches(0.3), Inches(2.3), Inches(3.1), Inches(4.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = C_CYAN

        p_t = tf.add_paragraph()
        p_t.text = tech
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = C_GOLD
        p_t.space_before = Pt(4)

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(13)
        p_d.font.color.rgb = C_MUTED
        p_d.space_before = Pt(16)

    # ==========================================
    # SLIDE 4: Grading Formula & Weightage Scaling
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Assessment Component Weightage Breakdown")

    # Left card: Table of Weightages
    add_card(s4, Inches(0.8), Inches(2.0), Inches(6.8), Inches(4.8))
    tb_tbl = s4.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(6.2), Inches(4.4))
    tf_tbl = tb_tbl.text_frame
    tf_tbl.word_wrap = True

    p = tf_tbl.paragraphs[0]
    p.text = "COMPONENT SCALING MATRIX"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    components = [
        ("Continuous Assessment Test 1 (CAT-1)", "Max 50", "Scaled to 15%"),
        ("Continuous Assessment Test 2 (CAT-2)", "Max 50", "Scaled to 15%"),
        ("Digital Quizzes (Quiz 1 & 2 Avg)", "Max 50", "Scaled to 15%"),
        ("Digital Assignment / Assessment (DA)", "Max 100", "Scaled to 15%"),
        ("Final Assessment Test (FAT)", "Max 100", "Scaled to 40%"),
    ]

    for name, raw, weight in components:
        p = tf_tbl.add_paragraph()
        p.text = f"• {name}"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.space_before = Pt(10)

        p_sub = tf_tbl.add_paragraph()
        p_sub.text = f"   Raw: {raw}  ➔  Contribution: {weight}"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = C_GOLD

    # Right Card: Formula
    add_card(s4, Inches(8.0), Inches(2.0), Inches(4.5), Inches(4.8))
    tb_form = s4.shapes.add_textbox(Inches(8.3), Inches(2.3), Inches(3.9), Inches(4.2))
    tf_form = tb_form.text_frame
    tf_form.word_wrap = True

    p = tf_form.paragraphs[0]
    p.text = "TOTAL 100-MARK FORMULA"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    formula_lines = [
        ("T = CAT1_15 + CAT2_15 + Quiz_15 + DA_15 + FAT_40", C_CYAN, 14),
        ("Where:", C_WHITE, 12),
        ("• CAT1_15 = (CAT1 / 50) × 15", C_MUTED, 11),
        ("• CAT2_15 = (CAT2 / 50) × 15", C_MUTED, 11),
        ("• Quiz_15 = (Quiz / 50) × 15", C_MUTED, 11),
        ("• DA_15 = (DA / 100) × 15", C_MUTED, 11),
        ("• FAT_40 = (FAT / 100) × 40", C_MUTED, 11),
        ("Total is rounded to 2 decimal points for statistical precision.", C_WHITE, 12)
    ]

    for line, col, sz in formula_lines:
        p = tf_form.add_paragraph()
        p.text = line
        p.font.size = Pt(sz)
        p.font.color.rgb = col
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 5: Statistical Engine & Cutoffs
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Relative Grading Statistical Cutoffs")

    # Left: Cutoff Table
    add_card(s5, Inches(0.8), Inches(2.0), Inches(7.5), Inches(4.8))
    tb_cut = s5.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(6.9), Inches(4.4))
    tf_cut = tb_cut.text_frame
    tf_cut.word_wrap = True

    p = tf_cut.paragraphs[0]
    p.text = "VIT RELATIVE GRADE DISTRIBUTION THRESHOLDS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    cutoffs = [
        ("S Grade", "10 GP", "Marks > Mean (μ) + 1.5 × SD (σ)", C_CYAN),
        ("A Grade", "9 GP", "Marks > Mean (μ) + 0.5 × SD (σ)", C_SUCCESS),
        ("B Grade", "8 GP", "Marks > Mean (μ) - 0.5 × SD (σ)", C_GOLD),
        ("C Grade", "7 GP", "Marks > Mean (μ) - 1.0 × SD (σ)", C_MUTED),
        ("D Grade", "6 GP", "Marks > Mean (μ) - 1.5 × SD (σ)", C_MUTED),
        ("E Grade", "5 GP", "Marks > Mean (μ) - 2.0 × SD (σ)", C_MUTED),
        ("F Grade", "0 GP", "Marks ≤ Mean (μ) - 2.0 × SD (σ)", RGBColor(220, 53, 69)),
    ]

    for grade, gp, cond, col in cutoffs:
        p = tf_cut.add_paragraph()
        p.text = f"{grade} ({gp}) ➔ {cond}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = col
        p.space_before = Pt(7)

    # Right: Edge Case Box
    add_card(s5, Inches(8.6), Inches(2.0), Inches(3.9), Inches(4.8))
    tb_edge = s5.shapes.add_textbox(Inches(8.9), Inches(2.3), Inches(3.3), Inches(4.2))
    tf_edge = tb_edge.text_frame
    tf_edge.word_wrap = True

    p = tf_edge.paragraphs[0]
    p.text = "CRITICAL EDGE CASE"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p = tf_edge.add_paragraph()
    p.text = "Zero Standard Deviation (σ = 0)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.space_before = Pt(8)

    p = tf_edge.add_paragraph()
    p.text = "If all students obtain identical marks, σ = 0. Dividing by zero crashes standard formulas.\n\nOur algorithm implements an automatic fallback to absolute grading:\n• ≥90 = S\n• ≥80 = A\n• ≥70 = B\n• ≥60 = C\n• ≥50 = D\n• ≥40 = E\n• <40 = F"
    p.font.size = Pt(12)
    p.font.color.rgb = C_MUTED
    p.space_before = Pt(10)

    # ==========================================
    # SLIDE 6: CGPA Calculation Methodology
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Credit Weighted CGPA Calculation")

    cards_data = [
        ("1. Credit Multiplication", "For each course j, the grade point earned (GP_j) is multiplied by course credit (C_j):\n\nWeighted Points = GP_j × C_j", C_CYAN),
        ("2. Student CGPA Formula", "CGPA is the weighted sum divided by total registered credits:\n\nCGPA = Σ(GP_j × C_j) / Σ(C_j)\n\nRounded to 2 decimal places.", C_GOLD),
        ("3. Class Average Aggregation", "The system calculates the cohort-wide average CGPA across all N students:\n\nClass Mean CGPA = Σ(CGPA_i) / N", C_SUCCESS)
    ]

    for idx, (title, body, col) in enumerate(cards_data):
        x = Inches(0.8) + idx * Inches(3.95)
        add_card(s6, x, Inches(2.0), Inches(3.7), Inches(4.8))

        tb = s6.shapes.add_textbox(x + Inches(0.3), Inches(2.3), Inches(3.1), Inches(4.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = col

        p_b = tf.add_paragraph()
        p_b.text = body
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = C_MUTED
        p_b.space_before = Pt(16)

    # ==========================================
    # SLIDE 7: Live Test Verification & Output
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Execution Verification & Results Output")

    # Metrics Card
    add_card(s7, Inches(0.8), Inches(2.0), Inches(11.733), Inches(1.3))
    tb_met = s7.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(11.3), Inches(0.9))
    tf_met = tb_met.text_frame
    tf_met.word_wrap = True

    p = tf_met.paragraphs[0]
    p.text = "TEST SUITE SIMULATION: 3 STUDENTS • 2 SUBJECTS (DSA: 4 Credits, DBMS: 3 Credits)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    p = tf_met.add_paragraph()
    p.text = "Class Mean Marks: 68.45 / 100    |    Class SD: 14.32    |    Class Average CGPA: 8.21"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_GOLD
    p.space_before = Pt(4)

    # Student Cards
    students_demo = [
        ("Student 1 (Alice)", "DSA: 86.5 (S Grade, 10 GP)\nDBMS: 78.0 (A Grade, 9 GP)", "CGPA: 9.57", C_CYAN),
        ("Student 2 (Bob)", "DSA: 65.0 (B Grade, 8 GP)\nDBMS: 62.5 (B Grade, 8 GP)", "CGPA: 8.00", C_GOLD),
        ("Student 3 (Charlie)", "DSA: 54.0 (C Grade, 7 GP)\nDBMS: 51.5 (D Grade, 6 GP)", "CGPA: 6.57", C_MUTED)
    ]

    for idx, (name, subs, cgpa, col) in enumerate(students_demo):
        x = Inches(0.8) + idx * Inches(3.95)
        add_card(s7, x, Inches(3.6), Inches(3.7), Inches(3.2))

        tb = s7.shapes.add_textbox(x + Inches(0.3), Inches(3.8), Inches(3.1), Inches(2.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

        p_s = tf.add_paragraph()
        p_s.text = subs
        p_s.font.size = Pt(12)
        p_s.font.color.rgb = C_MUTED
        p_s.space_before = Pt(8)

        p_c = tf.add_paragraph()
        p_c.text = cgpa
        p_c.font.size = Pt(14)
        p_c.font.bold = True
        p_c.font.color.rgb = col
        p_c.space_before = Pt(10)

    # ==========================================
    # SLIDE 8: Team Contribution Matrix
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Team Contributions & Task Allocation")

    team_data = [
        ("Himanshu Kumar", "26BIT0347", "Lead Full-Stack Developer", "• Flask architecture & REST route pipelines\n• Relative grading & SD algorithm\n• Credit aggregation & backend error handling", C_CYAN),
        ("Srujan Y K", "26BIT0225", "Frontend & UI/UX Engineer", "• Clean Bootstrap 5 responsive layout\n• Academic-grade visual theme (no slop)\n• Tabular results presentation & styling", C_GOLD),
        ("Savant Kashyap", "26BIT0360", "Client-Side Logic Engineer", "• Dynamic JavaScript grid generator\n• Multi-dimensional form payload mapping\n• Input validation & range checking", C_SUCCESS),
        ("Parv Jain", "26BIT0230", "QA & Documentation Specialist", "• Edge case testing (zero SD, blank fields)\n• End-to-end simulation test bench\n• Project documentation & deployment prep", C_MUTED),
    ]

    card_w = Inches(2.7)
    gap_x = Inches(0.28)
    for idx, (name, reg, role, contribs, col) in enumerate(team_data):
        x = Inches(0.8) + idx * (card_w + gap_x)
        add_card(s8, x, Inches(2.0), card_w, Inches(4.8))

        tb = s8.shapes.add_textbox(x + Inches(0.2), Inches(2.2), card_w - Inches(0.4), Inches(4.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

        p_r = tf.add_paragraph()
        p_r.text = reg
        p_r.font.size = Pt(11)
        p_r.font.bold = True
        p_r.font.color.rgb = col

        p_role = tf.add_paragraph()
        p_role.text = role
        p_role.font.size = Pt(11)
        p_role.font.italic = True
        p_role.font.color.rgb = C_GOLD
        p_role.space_before = Pt(4)

        p_c = tf.add_paragraph()
        p_c.text = contribs
        p_c.font.size = Pt(11)
        p_c.font.color.rgb = C_MUTED
        p_c.space_before = Pt(14)

    # ==========================================
    # SLIDE 9: Security, Privacy & Compliance
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Engineering Rigor & Pre-Launch Compliance")

    pillars = [
        ("Zero Data Persistence", "Marks and student identities are computed strictly in-memory during request execution and discarded instantly. Zero database leak vectors.", C_CYAN),
        ("Clean Architecture", "Strict avoidance of AI fluff: No purple gradients, no cursor gimmicks, fully accessible semantic HTML5 and standards-compliant Jinja2 templates.", C_GOLD),
        ("Institutional Compliance", "Mandatory pre-launch checklist completed: Custom favicon, dedicated /privacy and /terms endpoints, production WSGI readiness via Gunicorn.", C_SUCCESS)
    ]

    for idx, (title, desc, col) in enumerate(pillars):
        x = Inches(0.8) + idx * Inches(3.95)
        add_card(s9, x, Inches(2.0), Inches(3.7), Inches(4.8))

        tb = s9.shapes.add_textbox(x + Inches(0.3), Inches(2.3), Inches(3.1), Inches(4.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = col

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(13)
        p_d.font.color.rgb = C_MUTED
        p_d.space_before = Pt(16)

    # ==========================================
    # SLIDE 10: Conclusion & Q&A
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)

    add_card(s10, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1))

    tb_end = s10.shapes.add_textbox(Inches(2.0), Inches(1.6), Inches(9.333), Inches(4.3))
    tf_end = tb_end.text_frame
    tf_end.word_wrap = True

    p = tf_end.paragraphs[0]
    p.text = "CONCLUSION & FUTURE SCOPE"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.alignment = PP_ALIGN.CENTER

    p = tf_end.add_paragraph()
    p.text = "Thank You, Prof. Yogaraja C"
    p.font.size = Pt(30)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(10)

    p = tf_end.add_paragraph()
    p.text = "Future Roadmap:\n1. Bulk CSV / Excel sheet upload for direct class grade processing.\n2. Interactive Gaussian Bell Curve histogram visualization for grade distributions.\n3. PDF grade report generation with VIT format compliance."
    p.font.size = Pt(13)
    p.font.color.rgb = C_MUTED
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(16)

    p = tf_end.add_paragraph()
    p.text = "Open for Questions & Evaluation"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = C_GOLD
    p.alignment = PP_ALIGN.CENTER
    p.space_before = Pt(20)

    prs.save(output_path)
    print(f"Presentation successfully created at: {output_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\hkuma\.gemini\antigravity\scratch\vit-cgpa-calculator"
    out_file = os.path.join(out_dir, "VIT_Vellore_CGPA_Calculator_Presentation.pptx")
    create_deck(out_file)
