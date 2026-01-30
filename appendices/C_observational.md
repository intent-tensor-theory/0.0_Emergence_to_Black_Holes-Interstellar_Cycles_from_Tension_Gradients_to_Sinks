# Appendix C — Observational Case Studies

---

## C.0 Purpose and Method

This appendix provides **observational support** for the emergence framework. We examine specific astrophysical systems where selection can be evaluated quantitatively.

**Method**:
1. Identify observable proxies for R (retention) and Ṙ (loss rate)
2. Calculate or estimate S for the system
3. Compare S to observed persistence/failure
4. Assign ICHTB class

**Caveat**: These calculations use approximate values. The goal is to demonstrate that S provides **meaningful discrimination** between persisting and failing systems, not to achieve high precision.

---

## C.1 Orion Proplyds

### C.1.1 System Description

The Orion Nebula (M42, d ≈ 400 pc) contains hundreds of **proplyds**—protoplanetary disks around young stars, visible because they are being photoevaporated by UV radiation from the Trapezium cluster.

### C.1.2 Observable Quantities

| Quantity | Symbol | Typical Value | Source |
|----------|--------|---------------|--------|
| Disk mass | M_disk | 0.01–0.1 M☉ | Submm continuum |
| Photoevaporation rate | Ṁ_loss | 10⁻⁷–10⁻⁶ M☉/yr | Hα emission |
| Distance from Trapezium | d | 0.01–0.5 pc | Imaging |
| Stellar age | t_* | 1–3 Myr | HR diagram |

### C.1.3 Selection Number Calculation

$$S_{\text{proplyd}} = \frac{M_{\text{disk}}}{\dot{M}_{\text{loss}} \cdot t_{\text{ref}}}$$

Using t_ref = 1 Myr (typical disk dissipation timescale):

| Proplyd Location | M_disk (M☉) | Ṁ_loss (M☉/yr) | S |
|------------------|-------------|----------------|---|
| Inner (d < 0.03 pc) | 0.01 | 10⁻⁶ | 10 |
| Inner (d < 0.03 pc) | 0.001 | 10⁻⁶ | 1 |
| Outer (d > 0.1 pc) | 0.01 | 10⁻⁸ | 1000 |
| Outer (d > 0.1 pc) | 0.001 | 10⁻⁸ | 100 |

### C.1.4 Interpretation

- **Inner proplyds with low mass**: S ≈ 1 → marginal; many are observed to be failing
- **Inner proplyds with high mass**: S ≈ 10 → survive longer, but still under stress
- **Outer proplyds**: S >> 1 → persist; these are the survivors

The spatial gradient in S matches the observed survival pattern: disk survival probability increases with distance from the Trapezium.

### C.1.5 ICHTB Placement

| Proplyd Type | Axis I | Axis II | Axis III | Class |
|--------------|--------|---------|----------|-------|
| Surviving outer | High | High | High | III |
| Marginal | High | High | Moderate | III (stressed) |
| Failing inner | High | Moderate | Low | II → V |

---

## C.2 Molecular Cloud Filaments

### C.2.1 System Description

Molecular clouds contain **filaments**—elongated dense structures that channel material toward star-forming cores. Herschel observations have shown filaments are ubiquitous in star-forming regions.

### C.2.2 Observable Quantities

| Quantity | Symbol | Typical Value | Source |
|----------|--------|---------------|--------|
| Linear mass density | λ | 10–100 M☉/pc | Dust emission |
| Critical linear density | λ_crit | ~16 M☉/pc | Virial analysis |
| Velocity dispersion | σ_v | 0.2–1 km/s | Spectroscopy |
| Length | L | 1–10 pc | Imaging |

### C.2.3 Selection Analysis

Filaments are **Class I structures**: high directional coherence, low closure.

Their persistence condition is:

$$\lambda > \lambda_{\text{crit}}$$

In selection terms:
- R ∝ λ (linear mass density)
- Ṙ ∝ dispersal rate from turbulence
- S > 1 when λ > λ_crit

### C.2.4 Observations

- **Supercritical filaments** (λ > λ_crit): fragment into cores → star formation
- **Subcritical filaments** (λ < λ_crit): disperse without forming stars

This is selection at the 1D stage: only filaments with sufficient retention proceed to the next stage.

### C.2.5 ICHTB Placement

| Filament Type | Axis I | Axis II | Axis III | Class |
|---------------|--------|---------|----------|-------|
| Supercritical | High | Low-Mod | Low | I → II |
| Subcritical | Moderate | Low | None | I → V |

---

## C.3 Nuclear Stability Band

### C.3.1 System Description

The chart of nuclides shows ~3,000 known isotopes, of which ~250 are stable. The stable isotopes form a narrow band through (N, Z) space.

### C.3.2 Observable Quantities

| Quantity | Symbol | Range | Source |
|----------|--------|-------|--------|
| Atomic number | Z | 1–118 | Known elements |
| Neutron number | N | 0–177 | Known isotopes |
| Binding energy | B | 0–1800 MeV | Mass spectroscopy |
| Half-life | t_½ | 10⁻²² s – stable | Decay measurements |

### C.3.3 Selection Number Calculation

For nuclear stability:

$$S = \frac{B(Z, N)}{\hbar / \tau_{\min}}$$

where τ_min is the minimum observable timescale.

Using τ_min = 10⁻²² s (strong interaction timescale):

$$\hbar / \tau_{\min} \approx 6.6 \text{ MeV}$$

| Nucleus | B (MeV) | S | Outcome |
|---------|---------|---|---------|
| ⁵⁶Fe | 492 | 75 | Stable |
| ²³⁸U | 1802 | 273 | Long-lived (t_½ = 4.5 Gyr) |
| ⁸Be | 56.5 | 8.6 | Unstable (t_½ = 10⁻¹⁶ s) |
| ⁵He | -0.89 | <0 | Does not exist |

### C.3.4 Interpretation

- **S >> 1**: Stable or very long-lived
- **S > 1 but moderate**: Exists but decays
- **S < 1 or B < 0**: Does not form or decays instantly

The stability band is the **selection basin** in (N, Z) space. Nuclei outside the basin have S < 1 at relevant timescales.

### C.3.5 ICHTB Placement

| Nuclear System | Axis I | Axis II | Axis III | Class |
|----------------|--------|---------|----------|-------|
| Stable nucleus | High | High | High | III |
| Radioactive | High | High | Moderate | III (leaky) |
| Beyond drip line | High | Moderate | Low | II → V |

---

## C.4 Star-Forming Cores

### C.4.1 System Description

**Prestellar cores** are dense clumps within molecular clouds that are gravitationally bound and will form stars. They represent successful 3D closure at cloud scales.

### C.4.2 Observable Quantities

| Quantity | Symbol | Typical Value | Source |
|----------|--------|---------------|--------|
| Core mass | M_core | 0.5–10 M☉ | Dust emission |
| Core radius | R_core | 0.01–0.1 pc | Imaging |
| Virial ratio | α_vir | 0.5–2 | Spectroscopy |
| Free-fall time | t_ff | 10⁵–10⁶ yr | Density |

### C.4.3 Selection Analysis

For gravitationally bound cores:

$$S = \frac{M_{\text{core}}}{\dot{M}_{\text{dispersal}} \cdot t_{\text{ff}}}$$

Bound cores have α_vir < 2, meaning gravitational retention exceeds kinetic loss.

### C.4.4 Observations

- **Bound cores** (α_vir < 1): collapse to form stars
- **Unbound cores** (α_vir > 2): disperse without star formation
- **Marginal cores** (α_vir ≈ 1–2): may or may not collapse

The virial ratio is a proxy for S: low α_vir means high S.

### C.4.5 ICHTB Placement

| Core Type | Axis I | Axis II | Axis III | Class |
|-----------|--------|---------|----------|-------|
| Bound | High | High | High | III (basin) |
| Marginal | High | Moderate | Moderate | II-III |
| Unbound | Moderate | Low | Low | I → V |

---

## C.5 Galactic Disk Persistence

### C.5.1 System Description

The Milky Way disk has persisted for ~10 Gyr while continuously forming stars and losing material to outflows.

### C.5.2 Observable Quantities

| Quantity | Symbol | Value | Source |
|----------|--------|-------|--------|
| Stellar mass | M_* | 6 × 10¹⁰ M☉ | Surveys |
| Gas mass | M_gas | 10¹⁰ M☉ | HI/CO |
| Star formation rate | SFR | 1–2 M☉/yr | Various |
| Outflow rate | Ṁ_out | ~1 M☉/yr | X-ray/UV |
| Age | t_MW | ~10 Gyr | Stellar ages |

### C.5.3 Selection Number Calculation

$$S_{\text{MW}} = \frac{M_{\text{total}}}{\dot{M}_{\text{loss}} \cdot t_{\text{ref}}}$$

Using M_total ≈ 10¹¹ M☉ (baryonic), Ṁ_loss ≈ 2 M☉/yr, t_ref = 10¹⁰ yr:

$$S_{\text{MW}} = \frac{10^{11}}{2 \times 10^{10}} = 5$$

With dark matter halo (M ≈ 10¹² M☉):

$$S_{\text{MW}} \approx 50$$

### C.5.4 Interpretation

S >> 1: The Milky Way is a **strong selection basin**. It has persisted for 10 Gyr and will continue for billions more.

The relatively low S (compared to stable nuclei) reflects the importance of **feedback regulation**: without feedback, S would be higher but the disk would have consumed all gas long ago.

### C.5.5 ICHTB Placement

| Component | Axis I | Axis II | Axis III | Class |
|-----------|--------|---------|----------|-------|
| Disk | High | High | High | III |
| Bulge | High | High | High | III |
| Halo | Moderate | Moderate | Partial | II-III |
| Spiral arms | High (local) | High | Moderate | II (local) |

---

## C.6 Quasar Lifetimes

### C.6.1 System Description

Quasars are active galactic nuclei powered by accretion onto supermassive black holes. They represent extreme gradient environments.

### C.6.2 Observable Quantities

| Quantity | Symbol | Typical Value | Source |
|----------|--------|---------------|--------|
| Black hole mass | M_BH | 10⁸–10¹⁰ M☉ | Virial estimates |
| Accretion rate | Ṁ_acc | 1–100 M☉/yr | Luminosity |
| Quasar lifetime | t_Q | 10⁷–10⁸ yr | Duty cycle |
| Eddington luminosity | L_Edd | 10⁴⁶–10⁴⁸ erg/s | Theory |

### C.6.3 Selection Analysis

The quasar phase is **transient**: high luminosity but limited fuel.

$$S_{\text{QSO}} = \frac{M_{\text{fuel}}}{\dot{M}_{\text{acc}} \cdot t_{\text{ref}}}$$

With M_fuel ~ 10⁹ M☉ and Ṁ_acc ~ 10 M☉/yr:

$$S_{\text{QSO}} \approx \frac{10^9}{10 \times 10^8} = 1$$

### C.6.4 Interpretation

S ≈ 1: Quasars are **selection ridge objects**. They exist but are not stable long-term. This matches the observed quasar duty cycle (~10⁷–10⁸ yr per episode).

The black hole itself is Class IV (S >> 1), but the quasar phase is Class II-III (marginal).

---

## C.7 Quantum Coherence Systems

### C.7.1 System Description

Laboratory quantum systems (qubits, BECs, SQUIDs) maintain coherence for limited times before decoherence.

### C.7.2 Observable Quantities

| System | T₂ (coherence time) | Temperature | Source |
|--------|---------------------|-------------|--------|
| Superconducting qubit | 10–100 μs | 10 mK | Lab |
| Trapped ion | 1–10 s | μK | Lab |
| NV center | 1 ms | Room temp | Lab |
| BEC | 1–100 s | nK | Lab |

### C.7.3 Selection Analysis

For quantum coherence:
- R = coherence (overlap integral, purity)
- Ṙ = decoherence rate = 1/T₂
- t_ref = operation time (gate time, measurement time)

$$S_{\text{coherence}} = \frac{1}{(1/T_2) \cdot t_{\text{op}}} = \frac{T_2}{t_{\text{op}}}$$

| System | T₂ | t_op | S |
|--------|-----|------|---|
| Superconducting qubit | 100 μs | 10 ns | 10,000 |
| Trapped ion | 1 s | 1 μs | 10⁶ |
| NV center (room T) | 1 ms | 100 ns | 10,000 |

### C.7.4 Interpretation

S >> 1 for these systems **under controlled conditions**. Quantum computing works because engineered environments maintain high S.

In uncontrolled environments, T₂ drops and S approaches 1, leading to decoherence.

### C.7.5 ICHTB Placement

| Coherent System | Axis I | Axis II | Axis III | Class |
|-----------------|--------|---------|----------|-------|
| Isolated qubit | High | High | Low | II |
| Measured qubit | High | Moderate | High | III |
| Decohered | Low | Low | None | V |

---

## C.8 Summary of Observational Support

| System | S Estimate | Outcome | Framework Prediction |
|--------|------------|---------|----------------------|
| Inner Orion proplyd | ~1–10 | Failing/marginal | ✓ Marginal survival |
| Outer Orion proplyd | ~100–1000 | Surviving | ✓ Strong persistence |
| Supercritical filament | >1 | Star formation | ✓ Proceeds to closure |
| Stable nucleus | >>1 | Persists | ✓ Selection basin |
| Radioactive nucleus | >1 (marginal) | Decays | ✓ Leaky closure |
| Milky Way | ~5–50 | 10 Gyr persistence | ✓ Strong basin |
| Quasar phase | ~1 | Transient | ✓ Ridge object |
| Lab qubit | >>1 (controlled) | Coherent | ✓ Engineered basin |

In every case, the selection number S correctly predicts whether the system persists, fails, or is marginal.

---

## C.9 Limitations

1. **Approximate values**: Many quantities are uncertain by factors of 2–10.
2. **Timescale dependence**: S depends on t_ref choice; different questions require different timescales.
3. **Correlation vs. causation**: High S correlates with persistence, but we have not proven S causes persistence.
4. **Selection bias**: We observe survivors; failed systems leave less evidence.

Despite these limitations, the framework provides a **consistent quantitative lens** for interpreting diverse observations.

---

🜂 *Nature does not hide emergence.*  
*It buries it in failed attempts.*
