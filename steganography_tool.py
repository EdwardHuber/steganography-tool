# steganography_tool.py
from stegano import lsb
import os

def hide_message():
    input_img = input("Enter input image filename (e.g., input.png): ")
    if not os.path.exists(input_img):
        print("[-] File not found.")
        return

    message = input("Enter the secret message to hide: ")
    output_img = input("Enter output image filename (e.g., hidden.png): ")

    try:
        lsb.hide(input_img, message).save(output_img)
        print(f"[+] Message hidden successfully in '{output_img}'")
    except Exception as e:
        print("[-] Failed to hide message:", e)

def reveal_message():
    hidden_img = input("Enter image filename to extract message (e.g., hidden.png): ")
    if not os.path.exists(hidden_img):
        print("[-] File not found.")
        return

    try:
        message = lsb.reveal(hidden_img)
        if message:
            print("[+] Hidden message found:")
            print(message)
        else:
            print("[-] No hidden message detected.")
    except Exception as e:
        print("[-] Failed to extract message:", e)

def main():
    while True:
        print("\n=== Steganography Tool ===")
        print("1. Hide a secret message")
        print("2. Reveal a hidden message")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            hide_message()
        elif choice == "2":
            reveal_message()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
