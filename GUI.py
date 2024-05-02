import tkinter as tk
from tkinter import messagebox
import subprocess

class WindowsDesktop:
    def __init__(self, root):
        self.root = root
        self.root.title("SystenBoot")
        self.root.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        self.launch_kernel_button = tk.Button(self.root, text="PythonOS", command=self.launch_kernel)
        self.launch_kernel_button.pack(pady=20)

        self.exit_button = tk.Button(self.root, text="退出", command=self.exit_app)
        self.exit_button.pack(pady=20)

    def launch_kernel(self):
        try:
            subprocess.run(["python3", "kernel.py"])
        except Exception as e:
            messagebox.showerror("错误", f"无法启动 Kernel: {e}")

    def exit_app(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    app = WindowsDesktop(root)
    root.mainloop()

if __name__ == "__main__":
    main()
