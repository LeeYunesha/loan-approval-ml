# 🌷 loan_approval_ml

<p align="center">
  <strong>✿ A little machine learning garden for loan approval ✿</strong>
</p>

<p align="center">
  🌱 Data · 🐍 Python · 📊 Machine Learning · 🪽 Experimentation
</p>

---

## 🌸 About the project

This project explores **loan approval prediction** using machine learning.

The goal is simple:

> ✦ Given information about a loan applicant, can we predict whether their loan will be approved?

The project was created as a hands-on journey into **data preprocessing, feature engineering, model training, and evaluation**.

🌷 *A small project, but a lot of learning happened here.*

---

## 🧺 What's inside?

```text
loan_approval_ml/
│
├── 🌱 data/
│   └── loan_approval_dataset.csv
│
├── 🐍 preprocessing.py
├── 🐍 model.py
├── 🐍 model2.py
│
├── 🧸 *.pkl
│   └── saved machine learning objects
│
└── 🌷 README.md
```

---

## 🍃 The workflow

```text
Raw data
   │
   ▼
🌱 Data cleaning
   │
   ▼
🧺 Feature engineering
   │
   ▼
🌸 Data preprocessing
   │
   ▼
🐍 Model training
   │
   ▼
📊 Evaluation
   │
   ▼
🪽 Loan approval prediction
```

---

## 🌼 What I practiced

### 🧹 Data preprocessing

* Cleaning column names
* Handling categorical variables
* Preparing numerical features
* Transforming data into a format suitable for machine learning

### 🌱 Feature engineering

Created additional features from the original dataset to give the model more useful information.

For example:

```python
df["loan_amount_to_term"] = (
    df["loan_amount"] / df["loan_term"]
)
```

This represents the relationship between the **loan amount** and the **loan term**.

### 🐍 Machine Learning

The project uses Python and machine-learning techniques to learn patterns in historical loan applications.

The model then uses those patterns to make predictions for new applicants.

---

## 📊 Project structure

| File                        | Purpose                         |
| --------------------------- | ------------------------------- |
| `preprocessing.py`          | 🌱 Data cleaning & preparation  |
| `model.py`                  | 🐍 Model development            |
| `model2.py`                 | 🌸 Additional model experiments |
| `*.pkl`                     | 🧸 Saved Python/model objects   |
| `loan_approval_dataset.csv` | 🧺 Dataset                      |

---

## 🪻 Technologies

<p align="center">

`Python` · `Pandas` · `NumPy` · `Scikit-learn` · `Pickle`

</p>

---

## 🌷 Why I made this

This repository is part of my journey into **Data Science & Machine Learning**.

Instead of only learning ML theory, I wanted to practice the whole workflow:

**data → preprocessing → features → model → prediction → evaluation**

Every little experiment in this repository helped me understand not only *how* machine learning code works, but also *why* each step is necessary.

---

## 🐇 A tiny note

This project is still growing.

There will probably be:

```text
🌱 new experiments
🌷 new features
🧸 questionable first attempts
✦ better models
🪽 and hopefully fewer bugs
```

That's part of learning.

---

<p align="center">

🌷 ───────────── ✿ ───────────── 🌷

<br>

<em>Made with curiosity, Python, and a little bit of chaos.</em>

<br>

🌱 ✦ 🐇 ✦ 🪽

</p>
