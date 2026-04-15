# 🔒 Online Payments Fraud Detection
> Real-time ML-powered fraud detection for online transactions — built with Python, Flask & Scikit-learn

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat-square&logo=scikit-learn)
![Accuracy](https://img.shields.io/badge/Accuracy-99.5%25-brightgreen?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-6.3M%20Transactions-red?style=flat-square)

---

## 🎯 What It Does

Detects fraudulent online payment transactions in **real-time** using a Decision Tree classifier trained on 6.3 million real mobile money transactions. Enter a transaction → get an instant **FRAUD ⚠️** or **NOT FRAUD ✅** prediction.

---

## 🚀 Demo

| Input | Prediction |
|-------|-----------|
| CASH_OUT · Amount: 5000 · OldBal: 5000 · NewBal: 0 | 🔴 **FRAUD** |
| PAYMENT · Amount: 500 · OldBal: 10000 · NewBal: 9500 | 🟢 **NOT FRAUD** |

---

## 🧠 How It Works

```
User Input → Flask → Feature Engineering → ML Model → Prediction
```

**Key Innovation — Balance Error Feature:**
```python
balanceError = oldbalanceOrg - amount - newbalanceOrig
# If money is missing with no explanation → strong fraud signal
```

**Fraud Pattern the Model Detects:**
```
Account has ₹5000 → CASH_OUT of ₹5000 → Balance = ₹0
        ↑ Complete account drain = FRAUD
```

---

## 📁 Project Structure

```
online-payments-fraud-detection/
│
├── app.py                          # Flask web application
├── train_model.py                  # Model training script
├── model.pkl                       # Trained ML model
├── templates/
│   └── index.html                  # Web UI
└── PS_20174392719_..._log.csv      # Dataset (download separately)
```

---

## ⚙️ Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/your-username/online-payments-fraud-detection.git
cd online-payments-fraud-detection
```

**2. Install dependencies**
```bash
pip install flask scikit-learn pandas numpy
```

**3. Download the dataset**

👉 [Kaggle Dataset](https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset) — place CSV in root folder

**4. Train the model**
```bash
python train_model.py
```

**5. Run the app**
```bash
python app.py
```

Open → `http://127.0.0.1:5000`

---

## 📊 Model Performance

| Model | Test Accuracy |
|-------|--------------|
| XGBoost | 99.79% |
| **Decision Tree ✅ (Selected)** | **~99.5%** |
| Extra Trees | 99.38% |
| Random Forest | 99.58% |
| SVM | 79.01% |

> Decision Tree selected for **interpretability**, **speed**, and superior **class imbalance handling** via `class_weight='balanced'`

---

## 🔬 Features Used

| Feature | Description |
|---------|-------------|
| `type` | Transaction type (encoded: CASH_OUT=1, PAYMENT=2, etc.) |
| `amount` | Transaction amount |
| `oldbalanceOrg` | Origin balance before transaction |
| `newbalanceOrig` | Origin balance after transaction |
| `balanceError` ⭐ | `oldbalanceOrg - amount - newbalanceOrig` (derived) |

---

## ⚠️ Limitations

- Detects **full account-drain fraud only** (CASH_OUT / TRANSFER where balance → 0)
- Does not detect: phishing, small repeated fraud, gradual siphoning
- Static model — does not update with new fraud patterns

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML:** Scikit-learn (DecisionTreeClassifier)
- **Data:** Pandas, NumPy
- **Frontend:** HTML, CSS, Jinja2
- **Dataset:** [Kaggle — Online Payments Fraud Detection](https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset)

---

## 📄 License

MIT License — free to use, modify, and distribute.
