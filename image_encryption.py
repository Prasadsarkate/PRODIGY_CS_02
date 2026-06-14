"""
Task-02: Pixel Manipulation for Image Encryption
Prodigy Infotech Internship

Operations supported:
  1. XOR  - XOR each pixel channel with a key value (reversible)
  2. ADD  - Add key to each pixel channel (mod 256)  → decrypt by subtracting
  3. SWAP - Swap pixel positions using a seeded shuffle (reversible with same key)
"""

from PIL import Image
import numpy as np
import random
import os


# ──────────────────────────────────────────────
# Core encryption / decryption functions
# ──────────────────────────────────────────────

def xor_encrypt_decrypt(img_array: np.ndarray, key: int) -> np.ndarray:
    """XOR every pixel channel with key. Same function encrypts AND decrypts."""
    return (img_array ^ key).astype(np.uint8)


def add_encrypt(img_array: np.ndarray, key: int) -> np.ndarray:
    """Add key (mod 256) to every pixel channel."""
    return ((img_array.astype(np.int32) + key) % 256).astype(np.uint8)


def add_decrypt(img_array: np.ndarray, key: int) -> np.ndarray:
    """Subtract key (mod 256) from every pixel channel."""
    return ((img_array.astype(np.int32) - key) % 256).astype(np.uint8)


def swap_encrypt(img_array: np.ndarray, key: int) -> np.ndarray:
    """Shuffle pixel positions using a seeded RNG."""
    flat = img_array.reshape(-1, img_array.shape[2]).copy()
    indices = list(range(len(flat)))
    random.seed(key)
    random.shuffle(indices)
    shuffled = flat[indices]
    return shuffled.reshape(img_array.shape)


def swap_decrypt(img_array: np.ndarray, key: int) -> np.ndarray:
    """Reverse the pixel shuffle using the same seed."""
    flat = img_array.reshape(-1, img_array.shape[2]).copy()
    indices = list(range(len(flat)))
    random.seed(key)
    random.shuffle(indices)
    # Build inverse permutation
    inverse = [0] * len(indices)
    for new_pos, old_pos in enumerate(indices):
        inverse[old_pos] = new_pos
    unshuffled = flat[inverse]
    return unshuffled.reshape(img_array.shape)


# ──────────────────────────────────────────────
# Helper utilities
# ──────────────────────────────────────────────

def load_image(path: str) -> tuple[Image.Image, np.ndarray]:
    img = Image.open(path).convert("RGB")
    return img, np.array(img)


def save_image(img_array: np.ndarray, output_path: str):
    Image.fromarray(img_array).save(output_path)
    print(f"  ✅ Saved → {output_path}")


def get_output_path(input_path: str, suffix: str) -> str:
    base, ext = os.path.splitext(input_path)
    return f"{base}_{suffix}{ext}"


def get_int_input(prompt: str, min_val: int = 0, max_val: int = 255) -> int:
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"  ⚠  Enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  ⚠  Invalid input. Please enter an integer.")


# ──────────────────────────────────────────────
# Main menu
# ──────────────────────────────────────────────

def print_banner():
    print("=" * 50)
    print("   🔐 Image Encryption Tool — Pixel Manipulation")
    print("=" * 50)


def choose_operation() -> str:
    print("\nEncryption Method:")
    print("  1. XOR  (fast, key: 0–255)")
    print("  2. ADD  (additive shift, key: 0–255)")
    print("  3. SWAP (pixel shuffle, key: any integer)")
    while True:
        choice = input("Select method (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            return choice
        print("  ⚠  Please enter 1, 2, or 3.")


def main():
    print_banner()

    while True:
        print("\nMain Menu:")
        print("  1. Encrypt an image")
        print("  2. Decrypt an image")
        print("  3. Exit")

        action = input("\nEnter choice (1/2/3): ").strip()

        if action == '3':
            print("\nGoodbye! 👋")
            break

        if action not in ('1', '2'):
            print("  ⚠  Invalid choice.")
            continue

        # Get image path
        img_path = input("Enter image file path: ").strip().strip('"')
        if not os.path.isfile(img_path):
            print(f"  ⚠  File not found: {img_path}")
            continue

        try:
            img, img_array = load_image(img_path)
        except Exception as e:
            print(f"  ⚠  Could not open image: {e}")
            continue

        print(f"  📷 Image loaded: {img.size[0]}×{img.size[1]} px")

        method = choose_operation()

        # Get key
        if method in ('1', '2'):
            key = get_int_input("Enter key (0–255): ", 0, 255)
        else:
            key = get_int_input("Enter key (any integer 0–999999): ", 0, 999999)

        # Perform operation
        if action == '1':   # Encrypt
            if method == '1':
                result = xor_encrypt_decrypt(img_array, key)
            elif method == '2':
                result = add_encrypt(img_array, key)
            else:
                result = swap_encrypt(img_array, key)
            out_path = get_output_path(img_path, "encrypted")
            print("\n🔒 Encrypting...")

        else:               # Decrypt
            if method == '1':
                result = xor_encrypt_decrypt(img_array, key)   # XOR is self-inverse
            elif method == '2':
                result = add_decrypt(img_array, key)
            else:
                result = swap_decrypt(img_array, key)
            out_path = get_output_path(img_path, "decrypted")
            print("\n🔓 Decrypting...")

        save_image(result, out_path)
        print(f"  🗝  Method: {'XOR' if method=='1' else 'ADD' if method=='2' else 'SWAP'} | Key: {key}")


if __name__ == "__main__":
    main()
