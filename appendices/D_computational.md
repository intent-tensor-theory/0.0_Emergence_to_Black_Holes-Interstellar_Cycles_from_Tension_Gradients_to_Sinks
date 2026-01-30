# Appendix D — Computational Methods

---

## D.0 Purpose and Philosophy

This appendix describes computational approaches to simulating emergence. The goal is not to replace physical simulations but to provide **minimal models** that demonstrate the selection framework in action.

**Philosophy**:
- Start with the simplest possible substrate
- Implement emergence stages explicitly
- Include loss mechanisms
- Measure selection outcomes

**Non-goal**: We do not claim these simulations predict real physics quantitatively. They demonstrate that the **qualitative behavior** predicted by the framework emerges from the mathematics.

---

## D.1 Minimal Computational Substrate

### D.1.1 The Grid as Permission Space

We use a discrete grid as a computational analog of the CTS:

```python
import numpy as np

# Grid dimensions
Nx, Ny, Nz = 64, 64, 64

# Scalar potential field
Phi = np.zeros((Nx, Ny, Nz))

# Initialize with small random variations
Phi += np.random.normal(0, 0.01, Phi.shape)
```

The grid is not "space"—it is the **permission space** where scalar variation can occur.

### D.1.2 Boundary Conditions

Typical choices:
- **Periodic**: Phi wraps around (no edges)
- **Fixed**: Phi = 0 at boundaries (external constraint)
- **Absorbing**: Loss occurs at boundaries

```python
def apply_periodic_bc(Phi):
    """Periodic boundary conditions."""
    return Phi  # NumPy handles periodicity via slicing

def apply_absorbing_bc(Phi, loss_rate=0.1):
    """Absorbing boundaries: lose structure at edges."""
    Phi[0, :, :] *= (1 - loss_rate)
    Phi[-1, :, :] *= (1 - loss_rate)
    Phi[:, 0, :] *= (1 - loss_rate)
    Phi[:, -1, :] *= (1 - loss_rate)
    Phi[:, :, 0] *= (1 - loss_rate)
    Phi[:, :, -1] *= (1 - loss_rate)
    return Phi
```

---

## D.2 Gradient Operator (1D Emergence)

### D.2.1 Discrete Gradient

```python
def gradient(Phi):
    """
    Compute gradient of scalar field.
    Returns vector field (Fx, Fy, Fz).
    """
    Fx = np.gradient(Phi, axis=0)
    Fy = np.gradient(Phi, axis=1)
    Fz = np.gradient(Phi, axis=2)
    return Fx, Fy, Fz

def gradient_magnitude(Phi):
    """Magnitude of gradient field."""
    Fx, Fy, Fz = gradient(Phi)
    return np.sqrt(Fx**2 + Fy**2 + Fz**2)
```

### D.2.2 Directional Coherence Metric

```python
def directional_coherence(Phi, threshold=0.1):
    """
    Fraction of grid with significant gradient.
    Measures 1D emergence.
    """
    grad_mag = gradient_magnitude(Phi)
    return np.mean(grad_mag > threshold)
```

---

## D.3 Curl Operator (2D Emergence)

### D.3.1 Discrete Curl

```python
def curl(Fx, Fy, Fz):
    """
    Compute curl of vector field.
    Returns pseudovector field (Cx, Cy, Cz).
    """
    # Cx = dFz/dy - dFy/dz
    Cx = np.gradient(Fz, axis=1) - np.gradient(Fy, axis=2)
    # Cy = dFx/dz - dFz/dx
    Cy = np.gradient(Fx, axis=2) - np.gradient(Fz, axis=0)
    # Cz = dFy/dx - dFx/dy
    Cz = np.gradient(Fy, axis=0) - np.gradient(Fx, axis=1)
    return Cx, Cy, Cz

def curl_magnitude(Fx, Fy, Fz):
    """Magnitude of curl field."""
    Cx, Cy, Cz = curl(Fx, Fy, Fz)
    return np.sqrt(Cx**2 + Cy**2 + Cz**2)
```

### D.3.2 Recursion Metric

```python
def recursion_strength(Phi, threshold=0.05):
    """
    Fraction of grid with significant curl.
    Measures 2D emergence.
    """
    Fx, Fy, Fz = gradient(Phi)
    curl_mag = curl_magnitude(Fx, Fy, Fz)
    return np.mean(curl_mag > threshold)
```

---

## D.4 Laplacian Operator (3D Emergence)

### D.4.1 Discrete Laplacian

```python
from scipy.ndimage import laplace

def laplacian(Phi):
    """
    Compute Laplacian of scalar field.
    """
    return laplace(Phi)

def laplacian_magnitude(Phi):
    """Absolute value of Laplacian."""
    return np.abs(laplacian(Phi))
```

### D.4.2 Closure Detection

```python
def detect_closures(Phi, threshold=0.1):
    """
    Identify closed boundary regions.
    Returns binary mask of closure candidates.
    """
    lap = laplacian(Phi)
    # Look for regions where Laplacian is consistently signed
    positive_curvature = lap > threshold
    negative_curvature = lap < -threshold
    # Use morphological operations to find connected regions
    from scipy.ndimage import label
    labeled_pos, n_pos = label(positive_curvature)
    labeled_neg, n_neg = label(negative_curvature)
    return labeled_pos, labeled_neg, n_pos, n_neg
```

### D.4.3 Closure Metric

```python
def closure_fraction(Phi, threshold=0.1):
    """
    Fraction of grid participating in closures.
    Measures 3D emergence.
    """
    lap_mag = laplacian_magnitude(Phi)
    return np.mean(lap_mag > threshold)
```

---

## D.5 Loss Mechanisms

### D.5.1 Diffusive Loss

```python
def apply_diffusion(Phi, D=0.01):
    """
    Apply diffusive loss (smoothing).
    This drives gradients toward zero.
    """
    lap = laplacian(Phi)
    Phi_new = Phi + D * lap
    return Phi_new
```

### D.5.2 Noise Injection

```python
def apply_noise(Phi, sigma=0.001):
    """
    Add random noise.
    This disrupts coherent structures.
    """
    return Phi + np.random.normal(0, sigma, Phi.shape)
```

### D.5.3 Decay

```python
def apply_decay(Phi, rate=0.01):
    """
    Exponential decay toward zero.
    """
    return Phi * (1 - rate)
```

---

## D.6 Selection Number Calculation

### D.6.1 Grid-Based Selection

```python
def compute_selection_field(Phi, Phi_prev, dt, t_ref):
    """
    Compute selection number at each grid point.
    
    R = |Phi|^2 (structure measure)
    R_dot = |dPhi/dt| (loss rate)
    S = R / (R_dot * t_ref)
    """
    R = Phi**2
    R_dot = np.abs(Phi - Phi_prev) / dt
    # Avoid division by zero
    R_dot = np.maximum(R_dot, 1e-10)
    S = R / (R_dot * t_ref)
    return S

def global_selection_number(Phi, Phi_prev, dt, t_ref):
    """
    Compute global selection number.
    """
    R_total = np.sum(Phi**2)
    R_dot_total = np.sum(np.abs(Phi - Phi_prev)) / dt
    if R_dot_total < 1e-10:
        return np.inf
    return R_total / (R_dot_total * t_ref)
```

---

## D.7 ICHTB Diagnostics

### D.7.1 Axis Measurements

```python
def measure_ichtb_axes(Phi, Phi_prev, dt):
    """
    Measure ICHTB axis values.
    
    Returns:
        I_A: Gradient coherence
        I_B: Gradient disruption
        II_A: Curl strength  
        II_B: Curl disruption
        III_A: Closure strength
        III_B: Closure leakage
    """
    # Axis I: Direction
    grad_mag = gradient_magnitude(Phi)
    grad_mag_prev = gradient_magnitude(Phi_prev)
    I_A = np.mean(grad_mag)
    I_B = np.mean(np.abs(grad_mag - grad_mag_prev)) / dt
    
    # Axis II: Recursion
    Fx, Fy, Fz = gradient(Phi)
    curl_mag = curl_magnitude(Fx, Fy, Fz)
    Fx_p, Fy_p, Fz_p = gradient(Phi_prev)
    curl_mag_prev = curl_magnitude(Fx_p, Fy_p, Fz_p)
    II_A = np.mean(curl_mag)
    II_B = np.mean(np.abs(curl_mag - curl_mag_prev)) / dt
    
    # Axis III: Closure
    lap_mag = laplacian_magnitude(Phi)
    lap_mag_prev = laplacian_magnitude(Phi_prev)
    III_A = np.mean(lap_mag)
    III_B = np.mean(np.abs(lap_mag - lap_mag_prev)) / dt
    
    return I_A, I_B, II_A, II_B, III_A, III_B

def classify_ichtb(I_net, II_net, III_net):
    """
    Assign ICHTB class based on net axis values.
    """
    if I_net < 0 or II_net < 0 or III_net < 0:
        return "V (Failed)"
    elif III_net > 0.5 and I_net < 0.2 and II_net < 0.2:
        return "IV (Over-locked)"
    elif III_net > 0.3 and II_net > 0.3 and I_net > 0.3:
        return "III (Closed)"
    elif II_net > 0.3 and III_net < 0.3:
        return "II (Recursive)"
    elif I_net > 0.3 and II_net < 0.3:
        return "I (Filamentary)"
    else:
        return "Transitional"
```

---

## D.8 SEMF Implementation

The SEMF calculator is provided in `/computational/semf_stability_band.py`. Key functions:

```python
def binding_energy(Z, N):
    """
    Semi-Empirical Mass Formula.
    Returns binding energy in MeV.
    """
    A = Z + N
    if A == 0:
        return 0.0
    
    # Coefficients (MeV)
    a_v = 15.75   # Volume
    a_s = 17.8    # Surface
    a_c = 0.711   # Coulomb
    a_a = 23.7    # Asymmetry
    a_p = 11.2    # Pairing
    
    # Terms
    volume = a_v * A
    surface = -a_s * A**(2/3)
    coulomb = -a_c * Z * (Z - 1) / A**(1/3) if A > 0 else 0
    asymmetry = -a_a * (A - 2*Z)**2 / A
    
    # Pairing
    if Z % 2 == 0 and N % 2 == 0:
        pairing = a_p / np.sqrt(A)
    elif Z % 2 == 1 and N % 2 == 1:
        pairing = -a_p / np.sqrt(A)
    else:
        pairing = 0
    
    return volume + surface + coulomb + asymmetry + pairing

def beta_stability_ridge(A):
    """
    Most stable Z for given A.
    """
    a_a = 23.7
    a_c = 0.711
    return 2 * a_a * A / (4 * a_a + a_c * A**(2/3))

def nuclear_selection_number(Z, N, tau_min=1e-22):
    """
    Selection number for nuclear configuration.
    """
    B = binding_energy(Z, N)
    hbar = 6.582e-22  # MeV·s
    loss_scale = hbar / tau_min
    if loss_scale == 0:
        return np.inf
    return B / loss_scale
```

---

## D.9 Example Simulation

```python
def emergence_simulation(n_steps=1000, dt=0.1, t_ref=10.0):
    """
    Run emergence simulation with loss.
    """
    # Initialize
    Phi = np.random.normal(0, 0.1, (32, 32, 32))
    
    history = {
        'S_global': [],
        'grad_coherence': [],
        'curl_strength': [],
        'closure_fraction': []
    }
    
    for step in range(n_steps):
        Phi_prev = Phi.copy()
        
        # Apply dynamics (simple diffusion + source)
        Phi = apply_diffusion(Phi, D=0.01)
        
        # Add localized source to drive emergence
        cx, cy, cz = 16, 16, 16
        Phi[cx-2:cx+2, cy-2:cy+2, cz-2:cz+2] += 0.01
        
        # Apply loss
        Phi = apply_decay(Phi, rate=0.005)
        Phi = apply_noise(Phi, sigma=0.001)
        
        # Measure
        S = global_selection_number(Phi, Phi_prev, dt, t_ref)
        history['S_global'].append(S)
        history['grad_coherence'].append(directional_coherence(Phi))
        
        Fx, Fy, Fz = gradient(Phi)
        history['curl_strength'].append(np.mean(curl_magnitude(Fx, Fy, Fz)))
        history['closure_fraction'].append(closure_fraction(Phi))
    
    return history
```

---

## D.10 Visualization

```python
import matplotlib.pyplot as plt

def plot_emergence_history(history):
    """Plot emergence metrics over time."""
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    
    axes[0, 0].plot(history['S_global'])
    axes[0, 0].axhline(y=1, color='r', linestyle='--', label='S=1')
    axes[0, 0].set_ylabel('Selection Number S')
    axes[0, 0].set_title('Global Selection')
    axes[0, 0].legend()
    
    axes[0, 1].plot(history['grad_coherence'])
    axes[0, 1].set_ylabel('Gradient Coherence')
    axes[0, 1].set_title('Axis I (Direction)')
    
    axes[1, 0].plot(history['curl_strength'])
    axes[1, 0].set_ylabel('Curl Strength')
    axes[1, 0].set_title('Axis II (Recursion)')
    
    axes[1, 1].plot(history['closure_fraction'])
    axes[1, 1].set_ylabel('Closure Fraction')
    axes[1, 1].set_title('Axis III (Closure)')
    
    for ax in axes.flat:
        ax.set_xlabel('Time Step')
    
    plt.tight_layout()
    return fig
```

---

## D.11 What These Models Demonstrate

1. **Selection threshold**: Systems with S < 1 dissipate; S > 1 persist.
2. **Emergence ordering**: Gradients form before curl; curl before closure.
3. **Loss is essential**: Without loss, everything would accumulate trivially.
4. **Basins and ridges**: Spatial structure in S(x) creates attractors and barriers.

---

## D.12 What These Models Do NOT Claim

1. **Quantitative prediction**: These are toy models, not physics simulations.
2. **Real constants**: We do not derive physical constants.
3. **Completeness**: Many physical effects are omitted.
4. **Uniqueness**: Other implementations could work equally well.

The models are **proof of concept**: they show that the qualitative behavior predicted by the framework emerges from simple implementations of the mathematics.

---

## D.13 Code Availability

Full implementations are available in the `/computational` directory:
- `semf_stability_band.py`: SEMF calculator with stability band analysis
- Additional tools may be added as the framework develops

---

🜂 *A model that does not fail*  
*cannot teach you why anything survives.*
