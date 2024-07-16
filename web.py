import streamlit as st
import functions

todos = functions.get_todos()


def fresh_todo():
    todo_l = st.session_state['new_todo'] + "\n"
    todos.append(todo_l)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is My Todo App")
st.write("This app is useful for Remaind Your Task")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label='Enter value', placeholder='Add New Todo....',
              on_change=fresh_todo, key='new_todo')

