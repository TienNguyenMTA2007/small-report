import numpy as np
import matplotlib.pyplot as plt

f = np.linspace(140, 220, 2000)
# màu đỏ là nước còn màu đen là không khí, sao vẽ thêm 2 cái chú thích vô nhỉ >>>????
def resonance(f, f0, Rmin, sigma_left, sigma_right, R_left, R_right):
    
    R = np.zeros_like(f)

    # Left side of resonance
    left = f < f0
    R[left] = Rmin + (R_left - Rmin) * (
        1 - np.exp(-((f[left] - f0) / sigma_left)**2)
    )

    # Right side of resonance
    right = f >= f0
    R[right] = Rmin + (R_right - Rmin) * (
        1 - np.exp(-((f[right] - f0) / sigma_right)**2)
    )

    return R
R_black = resonance(
    f,
    f0=186.0,
    Rmin=0.005,
    sigma_left=24.0,
    sigma_right=18.0,
    R_left=0.94,
    R_right=0.88
)

R_red = resonance(
    f,
    f0=174.0,
    Rmin=0.045,
    sigma_left=20.0,
    sigma_right=25.0,
    R_left=0.89,
    R_right=0.88
)

plt.figure(figsize=(4.0, 4.8))

plt.plot(
    f,
    R_black,
    color='black',
    linestyle=':',
    linewidth=2.0
)

plt.plot(
    f,
    R_red,
    color='red',
    linestyle=':',
    linewidth=2.0
)

plt.xlim(140, 220)
plt.ylim(0, 1.0)

plt.xticks([140, 160, 180, 200, 220])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

plt.xlabel('Frequency (THz)')
plt.ylabel('Reflectance')

plt.tick_params(
    direction='in',
    length=4,
    width=1
)

plt.tight_layout()
plt.show()