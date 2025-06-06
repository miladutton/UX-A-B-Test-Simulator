import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def run_ab_test(n_A, n_B, p_A, p_B, alpha=0.05):
    conversions_A = np.random.binomial(1, p_A, n_A)
    conversions_B = np.random.binomial(1, p_B, n_B)

    obs_p_A = conversions_A.mean()
    obs_p_B = conversions_B.mean()

    pooled_p = (conversions_A.sum() + conversions_B.sum()) / (n_A + n_B)
    std_error = np.sqrt(pooled_p * (1 - pooled_p) * (1/n_A + 1/n_B))

    z = (obs_p_B - obs_p_A) / std_error
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))

    summary = {
        "Observed Conversion A": round(obs_p_A, 4),
        "Observed Conversion B": round(obs_p_B, 4),
        "Z-score": round(z, 4),
        "P-value": round(p_value, 4),
        "Statistically Significant?": "Yes" if p_value < alpha else "No"
    }

    # Plot
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x)
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label='Standard Normal Distribution')
    plt.axvline(z, color='red', linestyle='--', label=f'Z = {z:.2f}')
    plt.fill_between(x, y, where=(x > stats.norm.ppf(1 - alpha/2)), color='red', alpha=0.3)
    plt.fill_between(x, y, where=(x < stats.norm.ppf(alpha/2)), color='red', alpha=0.3)
    plt.title("A/B Test Z-score Visualization")
    plt.xlabel("Z-score")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return summary


# Example usage
if __name__ == "__main__":
    result = run_ab_test(n_A=1000, n_B=1000, p_A=0.12, p_B=0.15)
    for k, v in result.items():
        print(f"{k}: {v}")
