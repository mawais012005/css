import streamlit as st

st.set_page_config(page_title="✍️ CSS Essay Guide Chatbot", page_icon="📘")

st.title("📘 CSS English Essay Guide Chatbot")
st.write("I'm here to guide you on how to write a high-scoring English essay for the CSS exam!")

# Session state for chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Rule-based chatbot logic
def get_css_essay_response(user_input):
    user_input = user_input.lower()

    if "topic" in user_input:
        return (
            "🔍 **Topic Selection Tips:**\n"
            "- Choose a topic you can critically analyze.\n"
            "- Avoid cliché or overly broad topics.\n"
            "- Select one with enough content for 2500–3000 words.\n"
            "- Look for topics that align with current affairs, philosophy, or social issues."
        )
    elif "structure" in user_input or "outline" in user_input:
        return (
            "🧱 **Essay Structure:**\n"
            "1. **Introduction** – Hook + brief intro to the topic + thesis statement\n"
            "2. **Thesis Statement** – Your main argument/position\n"
            "3. **Body Paragraphs** – 5–8 well-organized arguments with evidence\n"
            "4. **Counterarguments** – Acknowledge and refute opposing views\n"
            "5. **Conclusion** – Summarize key points + restate thesis + future outlook"
        )
    elif "thesis" in user_input:
        return (
            "🧠 **Thesis Statement Tips:**\n"
            "- It's your central argument.\n"
            "- Place it at the end of your introduction.\n"
            "- Be clear, assertive, and focused.\n"
            "- Example: *'Education is not the filling of a pail, but the lighting of a fire.'*"
        )
    elif "common mistakes" in user_input:
        return (
            "⚠️ **Common Mistakes to Avoid:**\n"
            "- Weak or vague thesis statement\n"
            "- Repetition and poor transitions\n"
            "- Lack of structure or coherence\n"
            "- Grammar and spelling errors\n"
            "- Going off-topic or being too descriptive"
        )
    elif "length" in user_input or "words" in user_input:
        return (
            "📝 **Essay Length:**\n"
            "- You should aim for **2500–3000 words**.\n"
            "- Avoid being too short (<2000 words) or overly long (>3500)."
        )
    elif "tips" in user_input or "how to write" in user_input:
        return (
            "✨ **General Tips:**\n"
            "- Practice outlines before writing full essays.\n"
            "- Read editorials and opinion columns.\n"
            "- Use quotes, examples, and facts smartly.\n"
            "- Stick to the topic and maintain flow.\n"
            "- Revise and proofread your essay before finalizing."
        )
    elif "conclusion" in user_input:
        return (
            "🔚 **Conclusion Writing Tips:**\n"
            "- Restate your thesis in new words\n"
            "- Summarize your main points\n"
            "- End with a strong, impactful closing thought\n"
            "- Avoid adding new arguments"
        )
    else:
        return (
            "🤖 I can help you with:\n"
            "- Topic selection\n"
            "- Structure & thesis\n"
            "- Common mistakes\n"
            "- Essay length\n"
            "- Writing tips & more\n"
            "Try asking: *'What is the ideal structure of a CSS essay?'*"
        )

# Input from user
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    st.session_state.chat.append(("🧑 You", user_input))
    response = get_css_essay_response(user_input)
    st.session_state.chat.append(("🤖 Bot", response))

# Display chat
for sender, msg in st.session_state.chat:
    st.markdown(f"**{sender}**: {msg}")
