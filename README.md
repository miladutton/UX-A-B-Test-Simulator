# 🧪 A/B Test Simulator for UX Decisions

This Python project simulates the outcome of A/B tests for UX design decisions, like testing different button designs or layouts. It helps you understand statistical significance using a two-proportion z-test.

## 🚀 Features

- Simulate conversion data for two variants
- Perform two-tailed z-test
- Visualize z-distribution and significance thresholds
- Outputs whether the result is statistically significant

## 📥 Inputs

You can customize:
- `n_A`, `n_B`: Sample sizes for groups A and B
- `p_A`, `p_B`: True conversion rates
- `alpha`: Significance level (default = 0.05)

## 🧪 Example Usage

```bash
python ab_test_simulator.py
