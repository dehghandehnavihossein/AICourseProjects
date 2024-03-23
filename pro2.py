import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# خواندن داده‌ها از فایل CSV
data = np.genfromtxt(r'C:\Users\VIVAN\Desktop\train.csv', delimiter=',', skip_header=1)

# استخراج متراژ و قیمت از داده‌ها
lot_area = data[:, 0]
sale_price = data[:, 1]

# تعریف تابع Loss (Mean Squared Error)
def calculate_loss(m, b, x, y):
    predictions = m * x + b
    return np.mean((predictions - y) ** 2)

# بازه وزن
m_values = np.linspace(-10, 10, 100)  # مقداردهی اولیه بازه وزن
b_values = np.linspace(-50000, 50000, 100)  # بازه وزن برای متغیر b

# محاسبه Loss بر حسب وزن
loss_values = np.zeros((len(m_values), len(b_values)))
for i, m in enumerate(m_values):
    for j, b in enumerate(b_values):
        loss_values[i, j] = calculate_loss(m, b, lot_area, sale_price)

# نمایش نمودار 3D Loss بر حسب وزن
plt.switch_backend('TkAgg')  # یا plt.switch_backend('Qt5Agg')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
M, B = np.meshgrid(m_values, b_values)
ax.plot_surface(M, B, loss_values.T, cmap='viridis')
ax.set_xlabel('Weight (m)')
ax.set_ylabel('Weight (b)')
ax.set_zlabel('Mean Squared Error (Loss)')
ax.set_title('3D Loss Function for Linear Regression')
plt.show()

# پیدا کردن مقدار بهینه برای وزن
best_indices = np.unravel_index(np.argmin(loss_values), loss_values.shape)
best_m = m_values[best_indices[0]]
best_b = b_values[best_indices[1]]

# نمایش داده‌ها و خط تخمین‌زننده
plt.switch_backend('TkAgg')  # یا plt.switch_backend('Qt5Agg')
plt.scatter(lot_area, sale_price, label='Data', s=0.5)
plt.plot(lot_area, best_m * lot_area + best_b, color='red', label='Best Fit Line')
plt.xlabel('Lot Area')
plt.ylabel('Sale Price')
plt.title('Linear Regression Fit')
plt.legend()
plt.show()
