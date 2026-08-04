<div align="center">

# 📈 Halal Capital Growth & Profit-Sharing Models

A dual-script repository implementing ethical, interest-free (Riba-free) investment algorithms to calculate capital growth and Mudarabah-style profit sharing.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bash](https://img.shields.io/badge/Bash-Shell_Script-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)](https://www.gnu.org/software/bash/)
[![Finance](https://img.shields.io/badge/Finance-Islamic_Banking-0052CC?style=for-the-badge&logo=revolut&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)

</div>

---

## 📌 Project Overview

This repository provides two distinct programmatic approaches (Python and Bash) to calculate investment returns based on **Islamic Finance** principles. 

Unlike traditional compound interest models that guarantee a fixed percentage regardless of business performance, these scripts simulate real-world **Mudarabah** (profit-sharing) models. They dynamically calculate investor returns based on actual, realized yearly business profits (or losses), ensuring that capital growth is directly tied to underlying economic activity.

---

## 🕌 Islamic Finance Principles Implemented

* **No Fixed Interest (Riba):** Returns are never guaranteed as a fixed percentage of the capital.
* **Profit and Loss Sharing:** The investor's return fluctuates based on the actual business profit. If the business experiences a loss (negative profit), the capital is adjusted accordingly, reflecting true shared risk.
* **Mudarabah Model:** Clear separation between the capital provider (Investor) and the working business, with profits distributed based on a pre-agreed percentage (`s`).

---

## 🧮 Mathematical Models & Scripts

### 1. Multi-Year Capital Growth (`compound_capitalgrowth.sh.py`)
A Python script designed to track investment compounding over several years based on varying annual profits.

**Inputs:**
* `c`: Initial capital invested.
* `years`: Total duration of the investment.
* `profits`: An array/list of actual profits generated each year (can be negative).
* `s`: The investor's agreed profit-share percentage.

**Growth Formula (Iterative):**
For each year $n$, the new capital is calculated as:
$$C_{n}=C_{n-1}+\left(P_{n}\times\frac{s}{100}\right)$$
*(Where $C$ is Capital, $P$ is the actual business profit for that year, and $s$ is the share percentage).*

---

### 2. Single-Term Profit Sharing (`simple-interestfree.sh`)
A lightweight Bash script for quick, single-term profit distribution calculations.

**Inputs:**
* `c`: Capital invested.
* `p`: Total business profit generated.
* `s`: Investor's profit-share percentage.

**Distribution Formula:**
$$\text{Investor Profit}=p\times\frac{s}{100}$$

---

## 📁 Repository Structure

```text
halal-capital-growth/
├── compound_capitalgrowth.sh.py    # Python logic for multi-year capital compounding
├── simple-interestfree.sh          # Bash script for rapid single-term calculation
└── README.md                       # Project documentation
```
⚙️ Quick Start Usage
Running the Python Model
Ensure you have Python 3 installed. Open your terminal and run:
```text
python3 compound_capitalgrowth.sh.py
```

You will be prompted to enter your initial capital, the number of years, your share percentage, and the specific profit figures for each consecutive year.
Running the Bash Shell Script
Ensure the script has execution permissions, then run it in your terminal:
```text
chmod +x simple-interestfree.sh
./simple-interestfree.sh
```

👤 Author
Hamed Payanda
•	GitHub: @HAMED-PAYANDA
Developed to bridge programmatic logic with ethical, interest-free financial frameworks.
