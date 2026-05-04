import streamlit as st


if "text" not in st.session_state:
    st.session_state.text = ""
    st.session_state.undo_stack = []
    st.session_state.redo_stack = []

st.set_page_config(page_title="Stack App", page_icon="🧠")

st.title("🧠 Stack Application (Undo / Redo)")


new_text = st.text_input("Enter text to add:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("➕ Add"):
        st.session_state.undo_stack.append(st.session_state.text)
        st.session_state.text += new_text
        st.session_state.redo_stack.clear()

with col2:
    if st.button("↩️ Undo"):
        if st.session_state.undo_stack:
            st.session_state.redo_stack.append(st.session_state.text)
            st.session_state.text = st.session_state.undo_stack.pop()
        else:
            st.warning("Nothing to undo")

with col3:
    if st.button("↪️ Redo"):
        if st.session_state.redo_stack:
            st.session_state.undo_stack.append(st.session_state.text)
            st.session_state.text = st.session_state.redo_stack.pop()
        else:
            st.warning("Nothing to redo")

with col4:
    if st.button("🗑️ Clear"):
        st.session_state.text = ""
        st.session_state.undo_stack.clear()
        st.session_state.redo_stack.clear()


st.markdown("### 📄 Current Text")
st.write(st.session_state.text)


