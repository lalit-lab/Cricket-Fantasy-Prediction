import streamlit as st

def form_index(recent_runs, career_average):
    return recent_runs / career_average if career_average > 0 else 0

def venue_impact(player_avg_at_venue, overall_avg):
    return (player_avg_at_venue - overall_avg) / overall_avg * 100

def h2h_performance(player_avg_vs_team, overall_avg):
    return (player_avg_vs_team - overall_avg) / overall_avg * 100

def first_innings_impact(first_inn_avg):
    return first_inn_avg / 100  

def second_innings_impact(second_inn_avg):
    return second_inn_avg / 100  

def fantasy_efficiency(total_points, matches_played):
    return total_points / matches_played if matches_played > 0 else 0

def pressure_score(avg_in_chase, overall_avg):
    return avg_in_chase / overall_avg if overall_avg > 0 else 0

def weighted_score(fi, vi, h2h, fii, sii, fpm, pp):
    return (fi * 0.20) + (vi * 0.20) + (h2h * 0.15) + (fii * 0.075) + (sii * 0.075) + (fpm * 0.25) + (pp * 0.05)

st.title("🏏 Cricket Fantasy Prediction Model")

recent_runs = st.number_input("Enter runs scored in last 5 matches", min_value=0)
career_avg = st.number_input("Enter career batting average", min_value=0.0)
fi = form_index(recent_runs, career_avg)
st.write(f"**Form Index:** {fi:.2f}")

venue_avg = st.number_input("Enter player's batting average at venue", min_value=0.0)
vi = venue_impact(venue_avg, career_avg)
st.write(f"**Venue Impact:** {vi:.2f}%")

h2h_avg = st.number_input("Enter player's average against opponent", min_value=0.0)
h2h = h2h_performance(h2h_avg, career_avg)
st.write(f"**H2H Performance:** {h2h:.2f}%")

first_inn_avg = st.number_input("Enter player's 1st innings average", min_value=0.0)
fii = first_innings_impact(first_inn_avg)
st.write(f"**1st Innings Impact:** {fii:.2f}")

second_inn_avg = st.number_input("Enter player's 2nd innings average", min_value=0.0)
sii = second_innings_impact(second_inn_avg)
st.write(f"**2nd Innings Impact:** {sii:.2f}")

total_fantasy_points = st.number_input("Enter total fantasy points scored", min_value=0)
matches_played = st.number_input("Enter total matches played", min_value=1)
fpm = fantasy_efficiency(total_fantasy_points, matches_played)
st.write(f"**Fantasy Points Per Match:** {fpm:.2f}")

avg_in_chase = st.number_input("Enter player's average while chasing", min_value=0.0)
pp = pressure_score(avg_in_chase, career_avg)
st.write(f"**Pressure Performance Score:** {pp:.2f}")

final_score = weighted_score(fi, vi, h2h, fii, sii, fpm, pp)
st.subheader(f"🏆 **Overall Weighted Score:** {final_score:.2f}")
