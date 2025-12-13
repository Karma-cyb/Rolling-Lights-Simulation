Stochastic Bulb Wheel Game
Option 2: Stochastic Game Simulation (Perya / Casino Game)
----------------------------------------------------------

OVERVIEW
--------
This project is a stochastic casino-style wheel game inspired by Filipino "perya" games.
It models a probabilistic system where outcomes are determined by chance and analyzes how
subtle probability manipulation (house edge) affects long-term player outcomes.

The application includes:
- An interactive bulb wheel game
- A fair probability model
- A tweaked probability model with house edge
- Monte Carlo simulation (10,000 plays)
- Exploratory Data Analysis (EDA)
- House edge computation and comparison

The project demonstrates how games that appear fair can be mathematically biased through
probability weighting.

----------------------------------------------------------

FEATURES
--------
- 12-bulb wheel with fixed prize values
- ₱250 spin cost with balance tracking
- Two game modes:
  - Fair Game (equal probabilities)
  - Tweaked Game (weighted probabilities favoring low prizes)
- Visual wheel animation (for user experience)
- Monte Carlo simulation for long-term analysis
- Outcome distribution charts
- House edge calculation

----------------------------------------------------------

PROJECT STRUCTURE
-----------------
.
├── app.py              # Main Streamlit application
├── README.txt          # Project documentation
├── requirements.txt    # Python dependencies

----------------------------------------------------------

INSTALLATION
------------
1. Make sure Python 3.8 or higher is installed.

2. Clone the repository:
   git clone <your-repo-url>
   cd <project-folder>

3. Install dependencies:
   pip install -r requirements.txt

----------------------------------------------------------

HOW TO RUN
----------
Run the Streamlit application using:

   python -m streamlit run app.py

After running, open the Local URL shown in the terminal (usually http://localhost:8501).

----------------------------------------------------------

GAME MODES
----------
Fair Game:
- All bulbs have equal probability
- Outcomes are evenly distributed over time

Tweaked Game (House Edge):
- Low-value prizes (especially ₱20) occur more frequently
- High-value prizes occur less often
- Produces consistent long-term profit for the house

----------------------------------------------------------

MONTE CARLO SIMULATION
---------------------
The app includes a built-in Monte Carlo simulation that runs 10,000 plays for both game
modes. The results are visualized using bar charts to compare prize distributions and
calculate the house edge.

----------------------------------------------------------

TECHNOLOGIES USED
-----------------
- Python 3
- Streamlit
- NumPy
- Pandas
- Matplotlib

----------------------------------------------------------

AUTHOR
------
Developed as part of a Modeling and Simulation project using Option 2:
Stochastic Game Simulation (Perya / Casino Game).

----------------------------------------------------------
