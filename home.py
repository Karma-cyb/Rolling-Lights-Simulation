import streamlit as st

with st.container(border = True):
    st.header(":material/info: About")
    st.markdown(
        """
The stochastic bulb wheel game is a Peryahan game that involves a ring or circular series of light bulbs that are lit each on a circular pattern. This is usually done with a wheel and a circuit similar to that of mechanical elevators for displaying the current floor. Prizes are each placed on its own slot with its appropriate light bulb, labelled with a number each. The player can place a bet on a slot with any amount, and must expect their selected light bulb to lit up last.

On this version of the stochastic bulb wheel, prizes are money rewards rather than items so that we can track down the profits gained by the player and the house.
        """
    )

    with st.container(horizontal = True):        
        if st.button("Perform Monte Carlo simulation", icon = ":material/play_circle:", type = "primary"):
            st.switch_page("simulate.py")
        
        if st.button("Play the game!", icon = ":material/sports_esports:", type = "secondary"):
            st.switch_page("play.py")

with st.container(border = True):
    st.header(":material/info: Project Details")
    st.html("<h3>CSEC-413 Modeling and Simulation Final Project</h3>")
    st.markdown(
        """
**Group 9 Members:**
- Carl Cyruz A. Leonador
- John Michael B. Casila
- Mary France B. San Andres

**Course Instructor:** Mr. Allan Ibo Jr.

Powered by Streamlit, Python 3.13.7
        """
    )

