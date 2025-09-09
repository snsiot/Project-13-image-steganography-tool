import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # EOF marker
    pixels = img.load()

    if img.mode != 'RGB':
        img = img.convert('RGB')

    width, height = img.size
    data_index = 0

    for y in range(height):
        for x in range(width):
            if data_index < len(binary_message):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_message[data_index])
                data_index += 1
                if data_index < len(binary_message):
                    g = (g & ~1) | int(binary_message[data_index])
                    data_index += 1
                if data_index < len(binary_message):
                    b = (b & ~1) | int(binary_message[data_index])
                    data_index += 1
                pixels[x, y] = (r, g, b)
            else:
                break

    img.save(output_path)
    return True

def decode_image(image_path):
    img = Image.open(image_path)
    binary_data = ""
    pixels = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_message = ""
    for byte in all_bytes:
        if byte == '11111110':  # EOF
            break
        decoded_message += chr(int(byte, 2))
    return decoded_message

# --- GUI Part ---
def browse_image(entry):
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

def save_image(entry):
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

def run_encode():
    img_path = img_entry.get()
    message = msg_text.get("1.0", tk.END).strip()
    out_path = out_entry.get()
    if not img_path or not message or not out_path:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        encode_image(img_path, message, out_path)
        messagebox.showinfo("Success", "Message embedded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def run_decode():
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])
    if not img_path:
        return
    try:
        msg = decode_image(img_path)
        messagebox.showinfo("Hidden Message", msg)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- GUI Layout ---
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Original Image Path:").pack(pady=5)
img_entry = tk.Entry(root, width=40)
img_entry.pack()
tk.Button(root, text="Browse", command=lambda: browse_image(img_entry)).pack()

tk.Label(root, text="Message to Hide:").pack(pady=5)
msg_text = tk.Text(root, height=5, width=45)
msg_text.pack()

tk.Label(root, text="Save Output Image As
