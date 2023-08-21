import streamlit as st

def main():
    st.title("Task Management App")
    
    num_tasks = st.number_input("Enter the number of tasks:", min_value=1, value=1, step=1)
    tasks = []

    for i in range(num_tasks):
        task = st.text_input(f"Task {i+1}:")
        tasks.append({"task": task, "completed": False})

    for i, task_item in enumerate(tasks):
        task = task_item["task"]
        completed = task_item["completed"]
        checkbox_id = f"task_checkbox_{i}"  # Use a unique identifier
        tasks[i]["completed"] = st.checkbox(
            label=task, value=completed, key=checkbox_id
        )
        
        if tasks[i]["completed"]:
            st.write(f"Task '{task}' has been Completed.")
if __name__ == "__main__":
    main()

