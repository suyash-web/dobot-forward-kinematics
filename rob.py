import numpy as np
from scipy.spatial.transform import Rotation as R

def compute_transformation():
    a0 = 0
    a1 = 150 - a0
    a2 = 150
    a3 = 90
    
    theta1 = 19.4528
    theta2 = 31.7899
    theta3 = -4.9117
    theta4 = -theta3
    theta3 = -theta2 + theta3
    theta5 = -59.0528
    
    def rotation_matrix(theta):
        theta_rad = np.radians(theta)
        return np.array([
            [np.cos(theta_rad), -np.sin(theta_rad), 0],
            [np.sin(theta_rad), np.cos(theta_rad), 0],
            [0, 0, 1]
        ])
    
    R_1_2 = np.dot(rotation_matrix(theta1), np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])) 
    H_1_2 = np.block([[R_1_2, np.array([[0], [0], [a0]])], [np.zeros((1, 3)), 1]])

    R_2_3 = np.dot(rotation_matrix(theta2), np.eye(3))
    H_2_3 = np.block([[R_2_3, np.array([[a1 * np.sin(np.radians(theta2))], [-a1 * np.cos(np.radians(theta2))], [0]])], [np.zeros((1, 3)), 1]])

    R_3_4 = np.dot(rotation_matrix(theta3), np.eye(3))
    H_3_4 = np.block([[R_3_4, np.array([[a2 * np.cos(np.radians(theta3))], [a2 * np.sin(np.radians(theta3))], [0]])], [np.zeros((1, 3)), 1]])

    R_4_5 = np.dot(rotation_matrix(theta4), np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]))
    H_4_5 = np.block([[R_4_5, np.array([[a3 * np.cos(np.radians(theta4))], [a3 * np.sin(np.radians(theta4))], [0]])], [np.zeros((1, 3)), 1]])
 
    R_5_6 = np.dot(rotation_matrix(theta5), np.eye(3))
    H_5_6 = np.block([[R_5_6, np.array([[0], [0], [0]])], [np.zeros((1, 3)), 1]])

    H_1_6 = np.linalg.multi_dot([H_1_2, H_2_3, H_3_4, H_4_5, H_5_6])
    H_1_6 = np.round(H_1_6, 4)
    print(H_1_6)
    px_new = H_1_6[0, 3]
    py_new = H_1_6[1, 3]
    pz_new = H_1_6[2, 3]
    rotation = theta5 + theta1
    
    
    return px_new, py_new, pz_new, rotation

px_new, py_new, pz_new, rot = compute_transformation()
print(f"px: {px_new}, py: {py_new}, pz: {pz_new}")
print(f"Rotation {rot}")
