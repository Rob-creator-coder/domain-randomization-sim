import pybullet as p
import pybullet_data
import numpy as np
import cv2
import os
import time
from random import uniform

# Config
OUTPUT_DIR = "generated_dataset"
NUM_SAMPLES = 100
IMAGE_WIDTH, IMAGE_HEIGHT = 640, 480

os.makedirs(OUTPUT_DIR, exist_ok=True)

def random_color():
    return [uniform(0, 1) for _ in range(3)] + [1]

def setup_env():
    p.connect(p.DIRECT)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.resetSimulation()
    p.setGravity(0, 0, -9.8)

    plane_id = p.loadURDF("plane.urdf")
    table_id = p.loadURDF("table/table.urdf", [0.5, 0, 0])

    # Add object with random color
    visual_shape_id = p.createVisualShape(
        shapeType=p.GEOM_BOX,
        halfExtents=[0.05, 0.05, 0.05],
        rgbaColor=random_color()
    )
    collision_shape_id = p.createCollisionShape(
        shapeType=p.GEOM_BOX,
        halfExtents=[0.05, 0.05, 0.05]
    )
    box_id = p.createMultiBody(
        baseMass=1,
        baseCollisionShapeIndex=collision_shape_id,
        baseVisualShapeIndex=visual_shape_id,
        basePosition=[uniform(0.4, 0.6), uniform(-0.1, 0.1), 0.65]
    )

    return box_id

def capture_image(sample_idx):
    cam_target = [0.5, 0, 0.65]
    cam_pos = [0.3, 0, 1.0]
    up_vector = [0, 0, 1]

    view_matrix = p.computeViewMatrix(cam_pos, cam_target, up_vector)
    proj_matrix = p.computeProjectionMatrixFOV(60, IMAGE_WIDTH / IMAGE_HEIGHT, 0.1, 2.0)

    img_arr = p.getCameraImage(IMAGE_WIDTH, IMAGE_HEIGHT, view_matrix, proj_matrix)
    rgb_img = img_arr[2]
    rgb_img = np.reshape(rgb_img, (IMAGE_HEIGHT, IMAGE_WIDTH, 4))[:, :, :3]

    filename = os.path.join(OUTPUT_DIR, f"img_{sample_idx:04d}.png")
    cv2.imwrite(filename, cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR))
    print(f"[INFO] Saved {filename}")

def main():
    for i in range(NUM_SAMPLES):
        setup_env()
        p.stepSimulation()
        time.sleep(0.01)
        capture_image(i)
        p.disconnect()

if __name__ == "__main__":
    main()
