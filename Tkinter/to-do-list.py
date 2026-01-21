import tkinter as tk

def add_task(self, event=None):
    task_text = task_create.get(1.0,tk.END).strip()
    if len(task_text) > 0:
        new_task = tk.Label(root, text=task_text, pady=10)
        task_style_choice = divmod(len(tasks),2)
        print(task_style_choice )
        my_scheme_choice = colour_schemes[task_style_choice[1]]
        new_task.configure(bg=my_scheme_choice["bg"])
        new_task.configure(fg=my_scheme_choice["fg"])
        
        new_task.pack(side=tk.TOP, fill=tk.X)
        tasks.append(new_task)
    task_create.delete(1.0, tk.END)


root = tk.Tk()
tasks=[]

root.title("To-Do-App")
root.geometry("300x400")
todo1 = tk.Label(root, text="--- Add Items Here ---", bg="lightgrey", fg="black",
pady=10)

tasks.append(todo1)
for task in tasks:
    task.pack(side=tk.TOP, fill=tk.X)

task_create = tk.Text(root, height=3, bg="white", fg="black")
task_create.pack(side=tk.BOTTOM, fill=tk.X)
task_create.focus_set()

task_create.bind("<Return>", add_task )

colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

root.mainloop()
