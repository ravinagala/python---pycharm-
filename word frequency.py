# Accept a string and display word frequency

st = input("Enter a string :")
words = st.split(" ")
for w in sorted(set(words)):
    print(f"{w} - {words.count(w)}")
