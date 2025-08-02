import nltk
import streamlit as st

from PasswordGenerator import MemorablePasswordGenerator, PinGenerator, RandomPasswordGenerator

st.image("src/image/image.png", width=450)
st.title(" :zap: Password Generator")

st.write("This is a simple password generator app built with Streamlit. You can generate different types of passwords including random passwords, PINs, and memorable passwords.")
option = st.radio("What kind of password would you like to generate?", ["Random Password", "PIN", "Memorable Password"])




if  option == "PIN" :
    length = st.slider("Select the length of the PIN", 4, 12)
    generator = PinGenerator(length=length)

elif option == "Random Password" :
    length = st.slider("Select the length of the Password", 8, 20)
    include_numbers = st.toggle("include numbers")
    include_symbols = st.toggle("include symbols")
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)

else :
    no_of_words = st.slider("How many words you want?", min_value=3, max_value=8, value=3)
    separator = st.text_input("Enter your separator", " - ")
    default_vocabulary = nltk.corpus.words.words()
    vocabulary_input = st.multiselect("Enter you choosen word(leave it and t will generate ranomly)", options=default_vocabulary)
    final_vocab = vocabulary_input if vocabulary_input else default_vocabulary
    capitalize = st.toggle("Capitalization")
    full_words = st.toggle("Use full words", value=True)
    min_letters, max_letters = 2, 5

    if not full_words:
        min_letters = st.number_input("Minimum letters per word", min_value=1, value=2)
        max_letters = st.number_input("Maximum letters per word", min_value=1, value=5)

    generator = MemorablePasswordGenerator(
        no_of_words=no_of_words,
        separator=separator,
        capitalize=capitalize,
        full_words=full_words,
        min_letters=min_letters,
        max_letters=max_letters,
        vocabulary=final_vocab,
    )

if st.button("Generate"):
    password = generator.generate()
    st.write("Your password is:")
    st.header(fr"``` {password} ```")


