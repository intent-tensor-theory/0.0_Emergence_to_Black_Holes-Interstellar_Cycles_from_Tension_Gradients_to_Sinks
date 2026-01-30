"""
SEMF Stability Band Calculator
==============================

Implements the Semi-Empirical Mass Formula (Bethe-Weizsäcker) to derive
nuclear stability as a selection phenomenon.

Key insight: The periodic table is a survival chart, not a catalog.
The stability band emerges from retention (binding) vs loss (decay) mechanics.

Author: Intent Tensor Theory
License: MIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Tuple, Optional


@dataclass
class SEMFCoefficients:
    """Standard SEMF coefficients (MeV)"""
    a_v: float = 15.8    # Volume term: bulk lock retention
    a_s: float = 18.3    # Surface term: boundary leakage penalty
    a_c: float = 0.714   # Coulomb term: over-centralization stress
    a_a: float = 23.2    # Asymmetry term: shell incompatibility cost
    a_p: float = 12.0    # Pairing term: micro-lock resonance


def pairing_delta(A: int, Z: int, coeffs: SEMFCoefficients) -> float:
    """
    Pairing term δ(A,Z) in MeV.
    
    Even-even: +a_p / sqrt(A)  (bonus)
    Odd-odd:   -a_p / sqrt(A)  (penalty)
    Odd A:     0
    """
    N = A - Z
    if A % 2 == 1:
        return 0.0
    if (Z % 2 == 0) and (N % 2 == 0):
        return +coeffs.a_p / np.sqrt(A)
    if (Z % 2 == 1) and (N % 2 == 1):
        return -coeffs.a_p / np.sqrt(A)
    return 0.0


def binding_energy(A: int, Z: int, coeffs: SEMFCoefficients) -> float:
    """
    SEMF binding energy B(A,Z) in MeV.
    
    B = volume - surface - Coulomb - asymmetry + pairing
    
    ITT interpretation:
    - Volume: retention capacity of core lock
    - Surface: boundary leakage penalty  
    - Coulomb: over-centralization stress
    - Asymmetry: shell incompatibility cost
    - Pairing: micro-lock resonance bonus/penalty
    """
    if A <= 1 or Z < 0 or Z > A:
        return np.nan
    
    vol = coeffs.a_v * A
    surf = coeffs.a_s * (A ** (2/3))
    coul = coeffs.a_c * (Z * (Z - 1)) / (A ** (1/3))
    asym = coeffs.a_a * ((A - 2*Z)**2) / A
    delta = pairing_delta(A, Z, coeffs)
    
    return vol - surf - coul - asym + delta


def separation_energy_neutron(Z: int, N: int, coeffs: SEMFCoefficients) -> float:
    """S_n(Z,N) = B(Z,N) - B(Z,N-1)"""
    A = Z + N
    if N <= 1:
        return np.nan
    B_current = binding_energy(A, Z, coeffs)
    B_prev = binding_energy(A - 1, Z, coeffs)
    return B_current - B_prev


def separation_energy_proton(Z: int, N: int, coeffs: SEMFCoefficients) -> float:
    """S_p(Z,N) = B(Z,N) - B(Z-1,N)"""
    A = Z + N
    if Z <= 1:
        return np.nan
    B_current = binding_energy(A, Z, coeffs)
    B_prev = binding_energy(A - 1, Z - 1, coeffs)
    return B_current - B_prev


def Z_star(A: float, coeffs: SEMFCoefficients) -> float:
    """
    Beta-stability ridge: optimal Z for given A.
    
    Derived from ∂B/∂Z = 0:
    Z*(A) = 2*a_a*A / (4*a_a + a_c*A^(2/3))
    """
    return (2 * coeffs.a_a * A) / (4 * coeffs.a_a + coeffs.a_c * (A ** (2/3)))


def kappa(A: float, coeffs: SEMFCoefficients) -> float:
    """
    Curvature of binding energy surface near ridge.
    κ(A) = 2*a_c/A^(1/3) + 8*a_a/A
    """
    return (2 * coeffs.a_c / (A ** (1/3))) + (8 * coeffs.a_a / A)


def band_half_width(A: float, Delta: float, coeffs: SEMFCoefficients) -> float:
    """
    Half-width of stability band for given persistence margin Δ.
    |Z - Z*(A)| ≤ sqrt(2Δ/κ(A))
    
    Δ encodes "what counts as existing" — the selection timescale knob.
    """
    return np.sqrt((2 * Delta) / kappa(A, coeffs))


def is_bound(Z: int, N: int, coeffs: SEMFCoefficients) -> bool:
    """
    Check if nucleus (Z,N) is bound.
    
    Conditions:
    - S_n > 0 (neutron bound)
    - S_p > 0 (proton bound)  
    - B > 0 (overall positive binding)
    """
    A = Z + N
    B = binding_energy(A, Z, coeffs)
    S_n = separation_energy_neutron(Z, N, coeffs)
    S_p = separation_energy_proton(Z, N, coeffs)
    
    return (S_n > 0) and (S_p > 0) and (B > 0)


def generate_stability_grid(
    Z_max: int = 100,
    N_max: int = 160,
    coeffs: Optional[SEMFCoefficients] = None
) -> pd.DataFrame:
    """
    Generate full grid of nuclear candidates with binding properties.
    """
    if coeffs is None:
        coeffs = SEMFCoefficients()
    
    rows = []
    for Z in range(1, Z_max + 1):
        for N in range(1, N_max + 1):
            A = Z + N
            B = binding_energy(A, Z, coeffs)
            S_n = separation_energy_neutron(Z, N, coeffs)
            S_p = separation_energy_proton(Z, N, coeffs)
            bound = is_bound(Z, N, coeffs)
            
            rows.append({
                'Z': Z,
                'N': N,
                'A': A,
                'B_MeV': B,
                'B_per_A': B / A if not np.isnan(B) else np.nan,
                'S_n': S_n,
                'S_p': S_p,
                'Bound': bound
            })
    
    return pd.DataFrame(rows)


def plot_stability_band(
    df: pd.DataFrame,
    coeffs: Optional[SEMFCoefficients] = None,
    Delta: float = 5.0,
    save_path: Optional[str] = None
):
    """
    Plot the nuclear stability band with ridge and width curves.
    """
    if coeffs is None:
        coeffs = SEMFCoefficients()
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # Plot 1: Bound region in (Z, N) space
    ax1 = axes[0, 0]
    grid = df.pivot(index='N', columns='Z', values='Bound').astype(float)
    im1 = ax1.imshow(
        grid.values, origin='lower', aspect='auto',
        extent=[grid.columns.min(), grid.columns.max(), 
                grid.index.min(), grid.index.max()],
        cmap='Blues'
    )
    ax1.set_xlabel('Z (protons)')
    ax1.set_ylabel('N (neutrons)')
    ax1.set_title('Stability Band: Bound Region (S_n > 0, S_p > 0, B > 0)')
    
    # Plot 2: Binding energy per nucleon
    ax2 = axes[0, 1]
    grid_bpa = df.pivot(index='N', columns='Z', values='B_per_A')
    im2 = ax2.imshow(
        grid_bpa.values, origin='lower', aspect='auto',
        extent=[grid_bpa.columns.min(), grid_bpa.columns.max(),
                grid_bpa.index.min(), grid_bpa.index.max()],
        cmap='viridis'
    )
    ax2.set_xlabel('Z (protons)')
    ax2.set_ylabel('N (neutrons)')
    ax2.set_title('Binding Energy per Nucleon (B/A)')
    plt.colorbar(im2, ax=ax2, label='MeV')
    
    # Plot 3: Ridge + band in (A, Z) space
    ax3 = axes[1, 0]
    A_vals = np.arange(2, 261)
    Z_ridge = [Z_star(A, coeffs) for A in A_vals]
    half_w = [band_half_width(A, Delta, coeffs) for A in A_vals]
    
    ax3.plot(A_vals, Z_ridge, 'k-', linewidth=2, label='Ridge Z*(A)')
    ax3.plot(A_vals, np.array(Z_ridge) + np.array(half_w), 'r--', 
             label=f'Ridge + half-width (Δ={Delta} MeV)')
    ax3.plot(A_vals, np.array(Z_ridge) - np.array(half_w), 'r--',
             label=f'Ridge - half-width')
    ax3.set_xlabel('A = Z + N')
    ax3.set_ylabel('Z')
    ax3.set_title('Beta-Stability Ridge + Selection Band')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Ridge + band in (Z, N) space
    ax4 = axes[1, 1]
    N_ridge = A_vals - np.array(Z_ridge)
    N_upper = A_vals - (np.array(Z_ridge) + np.array(half_w))
    N_lower = A_vals - (np.array(Z_ridge) - np.array(half_w))
    
    ax4.plot(Z_ridge, N_ridge, 'k-', linewidth=2, label='Ridge')
    ax4.plot(np.array(Z_ridge) + np.array(half_w), N_upper, 'r--', label='Band edges')
    ax4.plot(np.array(Z_ridge) - np.array(half_w), N_lower, 'r--')
    ax4.set_xlabel('Z')
    ax4.set_ylabel('N')
    ax4.set_title('Selection Corridor in (Z, N) Space')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def get_best_isotopes_by_Z(df: pd.DataFrame) -> pd.DataFrame:
    """
    For each Z, find the most stable (max B) bound isotope.
    This is the "pre-table frame" — the survival chart.
    """
    bound_df = df[df['Bound']].copy()
    best = (
        bound_df
        .sort_values(['Z', 'B_MeV'], ascending=[True, False])
        .groupby('Z', as_index=False)
        .head(1)
        .loc[:, ['Z', 'N', 'A', 'B_MeV', 'B_per_A', 'S_n', 'S_p']]
        .reset_index(drop=True)
    )
    return best


# =============================================================================
# Selection Number Integration
# =============================================================================

def nuclear_selection_number(
    Z: int, 
    N: int, 
    tau_min: float,  # minimum lifetime in seconds
    coeffs: Optional[SEMFCoefficients] = None
) -> float:
    """
    Selection number for nuclear persistence.
    
    S = B(Z,N) / (ℏ/τ_min)
    
    S > 1: exists at timescale τ_min
    S < 1: cannot persist that long
    
    This makes the stability band contextual:
    - Lab isotopes (microseconds): broad band
    - Natural isotopes (billions of years): narrow band
    """
    if coeffs is None:
        coeffs = SEMFCoefficients()
    
    A = Z + N
    B = binding_energy(A, Z, coeffs)  # MeV
    
    if np.isnan(B) or B <= 0:
        return 0.0
    
    # ℏ in MeV·s
    hbar_MeV_s = 6.582e-22
    
    # Selection number
    S = B / (hbar_MeV_s / tau_min)
    
    return S


# =============================================================================
# Main execution
# =============================================================================

if __name__ == '__main__':
    print("Generating SEMF stability grid...")
    coeffs = SEMFCoefficients()
    df = generate_stability_grid(Z_max=100, N_max=160, coeffs=coeffs)
    
    print(f"Total candidates: {len(df)}")
    print(f"Bound nuclei: {df['Bound'].sum()}")
    
    print("\nGenerating stability band plots...")
    fig = plot_stability_band(df, coeffs, Delta=5.0, save_path='stability_band.png')
    
    print("\nBest isotope per Z (first 20):")
    best = get_best_isotopes_by_Z(df)
    print(best.head(20).to_string(index=False))
    
    # Save data
    df.to_csv('semf_full_grid.csv', index=False)
    best.to_csv('semf_best_by_Z.csv', index=False)
    
    print("\nDone. Files saved:")
    print("  - stability_band.png")
    print("  - semf_full_grid.csv")
    print("  - semf_best_by_Z.csv")
