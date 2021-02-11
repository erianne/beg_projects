import streamlit as st


def odd_or_even(number):
    try:
        number = int(number)
        if number >= 1 and number <= 1000:
            odd_even = {number % 2 == 0: "Your number is even!",
                        number % 2 != 0: "Your number is odd!"}
            st.write(odd_even[True])
        else:
            st.write("number out of range")
    except:
        st.write("You need a valid number!")


# SITE ###################################################

if __name__ == '__main__':

    st.markdown("# ODD OR EVEN")

    number = st.text_input("Enter a number btw 1 and 1000")

    if st.button("Judge your number!"):
        odd_or_even(number)
