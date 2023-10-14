import tkinter as tk

def create_welcome_page():
    root = tk.Tk()
    root.title("Welcome to My App")
    root.geometry("400x300")  # Set the size of the window

    # Create a label with a welcome message
    label = tk.Label(root, text="Welcome to My App!", font=("Arial", 20))
    label.pack(pady=50)  # Adjust the padding

    # Run the Tkinter event loop
    root.mainloop()

# Create the welcome page
create_welcome_page()
