import streamlit as st
#das soll gespusht werden


# Seiten-Auswahlmenü in der Seitenleiste
page = st.sidebar.selectbox("Wähle eine Seite", ["Startseite", "Statistik", "Impressum"])

# Eingabe-Speicher initialisieren (z.B. als Session State)
if "inputs" not in st.session_state:
    st.session_state["inputs"] = []

# Startseite
if page == "Startseite":
    st.title("Lustiges Ratespiel")

    # Eingabefeld für Texteingaben
    user_input = st.text_input("Gib deinen Text hier ein:")

    # Speichere die Eingabe in der Sitzung
    if st.button("Speichern"):
        if user_input:
            st.session_state["inputs"].append(user_input)
            st.success("Eingabe gespeichert!")

    # Anzeige der aktuellen Eingaben
    st.write("Bisherige Eingaben:")
    st.write(st.session_state["inputs"])

# Statistik-Seite
elif page == "Statistik":
    st.title("Statistik über deine Eingaben")

    # Berechne einfache Statistiken
    total_inputs = len(st.session_state["inputs"])
    unique_inputs = len(set(st.session_state["inputs"]))

    st.write(f"Anzahl der Eingaben: {total_inputs}")
    st.write(f"Anzahl der einzigartigen Eingaben: {unique_inputs}")

    # Zeige die Liste der Eingaben an
    st.write("Alle gespeicherten Eingaben:")
    st.write(st.session_state["inputs"])

elif page == "Impressum":
    st.title("Impressum")
    
    st.write("Konstantins Coding GMBH")
    st.write("University of Cambridge")
    st.write("49074 Osnabrück")