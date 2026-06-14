# 🖼️ Pixel Manipulation for Image Encryption — PRODIGY_CS_02

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pillow](https://img.shields.io/badge/Pillow-Library-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Internship](https://img.shields.io/badge/Prodigy-InfoTech-purple?style=for-the-badge)

> **Task 02** — Prodigy InfoTech Cyber Security Internship

---

## 📌 Task Description

Develop a simple **image encryption tool** using pixel manipulation. Perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

---

## 🔍 How It Works

Every image is made of **pixels**, and each pixel has 3 values — **R, G, B** (0 to 255).

```
Original Pixel → (200, 150, 100)
XOR with key 123 → (179, 233, 23)   ← Encrypted!
XOR with key 123 → (200, 150, 100)  ← Decrypted back!
```

---

## ✨ Features

- ✅ **3 Encryption Methods** — XOR, ADD, SWAP
- ✅ Encrypt any image (JPG, PNG, BMP)
- ✅ Decrypt image back to original using the same key
- ✅ Saves encrypted/decrypted image automatically
- ✅ Simple menu-driven interface

---

## 🔐 Encryption Methods

| Method | Description | Key Range |
|--------|-------------|-----------|
| **XOR** | XOR each pixel with key value | 0 – 255 |
| **ADD** | Add key to each pixel (mod 256) | 0 – 255 |
| **SWAP** | Shuffle all pixel positions randomly | 0 – 999999 |

> ⚠️ Use the **same method + same key** to decrypt!

---

## 🛠️ Requirements

```bash
pip install pillow numpy
```

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/PRODIGY_CS_02.git

# Navigate to folder
cd PRODIGY_CS_02

# Install dependencies
pip install pillow numpy

# Run the program
python image_encryption.py
```

---

## 💻 Usage Example

```
Main Menu:
  1. Encrypt an image
  2. Decrypt an image
  3. Exit

Enter choice: 1
Enter image file path: photo.jpg
Select method (1/2/3): 1        ← XOR
Enter key (0–255): 123

🔒 Encrypting...
✅ Saved → photo_encrypted.jpg
```

```
Enter choice: 2
Enter image file path: photo_encrypted.jpg
Select method (1/2/3): 1        ← XOR (same method!)
Enter key (0–255): 123          ← same key!

🔓 Decrypting...
✅ Saved → photo_encrypted_decrypted.jpg
```

---

## 🖼️ Visual Result

```
Original Image   →   Encrypt (key=123)   →   Encrypted Image
   😊 Photo                🔑                  🌫️ Random Noise

Encrypted Image  →   Decrypt (key=123)   →   Original Image
  🌫️ Noise                 🔑                    😊 Photo
```

---

## 📂 Project Structure

```
PRODIGY_CS_02/
│
├── image_encryption.py   # Main program
├── sample.jpg            # Sample test image (optional)
└── README.md             # Project documentation
```

---

## 📚 What I Learned

- How **images are stored** as pixel arrays
- **XOR encryption** — a reversible bitwise operation
- Using **NumPy** for fast array manipulation
- **PIL/Pillow** library for image processing
- Basics of **visual cryptography**

---

## 👨‍💻 Author

**Prasad** — Cyber Security Intern @ Prodigy InfoTech

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/prasadsarkate)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/Prasadsarkate)

---

## 🏢 Internship

This project was completed as part of the **Prodigy InfoTech Cyber Security Internship**.

`#ProdigyInfoTech` `#Internship` `#CyberSecurity` `#Python` `#ImageEncryption` `#PixelManipulation`
