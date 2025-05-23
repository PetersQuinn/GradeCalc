# GPA Tools Suite

This repository provides a collection of Python-based tools designed to help students assess and project academic outcomes. These tools offer insight into final exam requirements, term GPA probabilities, and the effects of new grades on cumulative GPA. The goal is to support informed academic planning through quantitative analysis and visualization.

---

## Contents

### 1. Final Grade Calculator

Calculates the minimum score needed on a final exam to achieve various letter grades, based on the weight of the final and the student's current standing.

* **Inputs:** Current grade (percentage), final exam weight (percentage)
* **Outputs:** Required final exam scores for standard letter grades
* **Interface:** Terminal-based

### 2. Term GPA Predictor

Estimates the likelihood of various term GPA outcomes based on possible grade ranges in each course. Useful for academic planning and benchmarking.

* **Inputs:** Estimated GPA ranges for each new course
* **Outputs:** Frequency and probability distribution of potential term GPAs
* **Visualization:** Histogram and line plot including historical term GPA benchmarks

### 3. Data Science GPA Effect Model

Extends GPA prediction to include cumulative GPA impact, factoring in prior academic performance and simulating realistic grade outcomes.

* **Inputs:** Current cumulative GPA and units, GPA ranges for new units
* **Outputs:** Projected final GPA distributions
* **Visualization:** Histogram, per-course boxplots, summary trends (min/avg/max scenarios)

### 4. GPA Effect Calculator

Provides an interactive tool for visualizing cumulative GPA changes based on new unit performance. Supports between 4 and 6 new units.

* **Inputs:** Current GPA, current units, GPA ranges for new units (entered interactively)
* **Outputs:** Full distribution of potential cumulative GPA outcomes
* **Visualization:** Histogram of outcome distribution

---

## Technologies Used

* Python 3
* NumPy
* Matplotlib
* Seaborn
* itertools
* collections.Counter

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/gpa-tools-suite.git
cd gpa-tools-suite
```

Install required packages:

```bash
pip install numpy matplotlib seaborn
```

---

## Usage

Each script can be run independently from the command line. For example:

```bash
python final_grade_calculator.py
python term_gpa_predictor.py
python data_science_gpa_effect.py
python gpa_effect_calculator.py
```

Note: `gpa_effect_calculator.py` is interactive and prompts for input during execution.

---

## Visual Output

Depending on the script, output visualizations may include:

* GPA distribution histograms
* Probability line charts
* Boxplots for GPA uncertainty by unit
* Benchmark overlays for historical GPA comparisons

---

## Author

**Quinn Peters**
B.S.E. Candidate, Risk, Data, and Financial Engineering
Duke University
