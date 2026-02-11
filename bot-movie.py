import streamlit as st

responses = {
    "hi": "Hi want to know todays special[1] ,Services[2]",
    "1": "Today's special is a [A].Sirai , [B].With love , [C].Bad Boys.",
    "2": "complaint[3] , Queries[4]",
    "3": "Please provide your complaint details.",
    "4": "Please provide your query details.",
    "a1": "Sirai is a thrilling action movie that keeps you on the edge of your seat. [Book - a] to book",
    "b1": "With Love is a heartwarming romantic comedy that will make you laugh and cry. [Book - b] to book",
    "c1": "Bad Boys is an action-packed buddy cop film that delivers non-stop entertainment. [Book - c] to book",
    "book-a": "Your booking has been confirmed - Sirai. Enjoy the movie!",
    "book-b": "Your booking has been confirmed - With Love. Enjoy the movie!",
    "book-c": "Your booking has been confirmed - Bad Boys. Enjoy the movie!",
    "bye": "Goodbye! Have a great day!"
}

st.title("🎬 Movie Booking Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if st.button("Send") and user_input:
    msg = user_input.lower()
    found = False

    for key in responses:
        if key in msg:
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", responses[key]))
            found = True
            break

    if not found:
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(
            ("Bot", "Sorry, I didn't understand that. Please try again.")
        )

for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.write(f"🧑 {message}")
    else:
        st.write(f"🤖 {message}")
