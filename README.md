# rob.py – Forward Kinematics for Dobot Magician Lite

A simple Python script that computes the **forward kinematics** of the **Dobot Magician Lite** robotic arm using homogeneous transformation matrices.

---

## 🧠 What It Does

- Calculates the **end-effector position and orientation** based on given joint parameters.  
- Uses **Denavit–Hartenberg (DH)** transformations for each link.  
- Prints the final **homogeneous transformation matrix** and **pose**.

---

## ⚙️ Requirements

- Python 3.x  
- NumPy  

Install NumPy if needed:
```bash
pip install numpy
```

---

## 🚀 How to Run

1. Download or clone this repository.  
2. Open a terminal in the directory containing `rob.py`.  
3. Run:
   ```bash
   python rob.py
   ```

The script will output the computed transformation matrix and end-effector coordinates.

---

## 🔢 Formula Used

Each joint transformation follows the **DH convention**:

\[
T_i^{i-1} =
\begin{bmatrix}
\cos\theta_i & -\sin\theta_i\cos\alpha_i & \sin\theta_i\sin\alpha_i & a_i\cos\theta_i \\
\sin\theta_i & \cos\theta_i\cos\alpha_i & -\cos\theta_i\sin\alpha_i & a_i\sin\theta_i \\
0 & \sin\alpha_i & \cos\alpha_i & d_i \\
0 & 0 & 0 & 1
\end{bmatrix}
\]

---

## 👨‍💻 Author

Created by:
- **Divya Ganesan**
- **Thayaananthan Kanagaraj**
- **Suyash Dhir**

For educational use in RAS545 – *Robotic Systems 1*.

---

## 📜 License

Free to use for educational and research purposes.
