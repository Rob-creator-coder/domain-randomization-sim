# 🧠 Domain Randomization Simulation

This project demonstrates synthetic data generation using PyBullet and domain randomization techniques. It's designed for training perception or control models that generalize from simulation to real-world environments (Sim2Real transfer).

---

## 🚀 Features

- Synthetic RGB image generation of object-pushing scenarios
- Domain randomization:
  - Object colors
  - Object positions
  - (Extendable: textures, lighting, backgrounds)
- Simulated using PyBullet physics engine
- Saves data to `generated_dataset/` for ML training

---

## 📂 Output

After running the script, you'll find:

- `generated_dataset/img_0000.png`, `img_0001.png`, ..., up to 100 images
- Each image captures a randomized simulation scene

---

## 📦 Dependencies

Install required packages using pip:

```bash
pip install pybullet numpy opencv-python

