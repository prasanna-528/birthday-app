import streamlit as st

st.title("🎂 Happy Birthday Akhil Rahul ❤️")

st.write("Initializing Birthday Program...")
st.write("Please Wait...")

# Name Verification
name = st.text_input("Enter your Name :")

if name:
    if name == "Akhil Rahul":
        st.success("Identity Verified ❤️")
        st.write(f"Welcome {name}")

        st.write("Happy Birthday", name)

        st.write("Before I continue...")
        st.write("I want to tell you something.")

        st.write("You told me many times...")
        st.write("'Learn Python' ani.")

        st.write("Every single time...")
        st.write("I said... 'Tomorrow nerchukunta' 😂")

        st.write("But finally...")
        st.write("I listened.")

        st.write("Because I wanted my first Python program to be only for you.")

        st.write("🎉 Happy Birthday Akhil Rahul ❤️")
        st.write("I wish you all the happiness in the world.")
        st.write("Keep smiling 😊")
        st.write("Stay happy.")
        st.write("Take care of yourself 🫂")

        # Love verification
        answer = st.radio("Do you really love me?", ["yes", "no"])

        if answer == "yes":
            st.write("I knew your answer... ❤️")

            st.write("Nuvvu ante naku chala istam.")
            st.write("I Love You So Much ❤️")

            st.write("I'm Sorry... 😂")
            st.write("But it's all because I love you so much.")

            st.write("Please stay with me forever. ❤️")

            st.write("Thank you for coming into my life.")
            st.write("You are one of the best things that ever happened to me.")

            st.success("🎂 Happy Birthday Akhil Rahul ❤️")
            st.write("Stay Happy... Stay Healthy... Stay Mine Forever ❤️")

        else:
            st.warning("Hmm... 😂 Please select yes")

    else:
        st.error("Wrong Name 😂 Try Again")
