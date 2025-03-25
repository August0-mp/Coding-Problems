from math import comb

chapeaux = {
    "Chapeau 1": {"GER": 3, "ENG": 2, "SPA": 2, "FRA": 1, "ITA": 1},
    "Chapeau 2": {"ITA": 3, "SPA": 2, "GER": 1, "ENG": 1, "BEL": 1, "UKR": 1},
    "Chapeau 3": {"DUT": 2, "POR": 1, "AUS": 1, "SWI": 1, "SCO": 1, "SER": 1, "CRO": 1, "FRA": 1},
    "Chapeau 4": {"FRA": 2, "SLO": 1, "SZR": 1, "ENG": 1, "ITA": 1, "SPA": 1, "GER": 1, "AUS": 1},
}

country_teams = {}

# New dictionary to store filtered chapeaux
filtered_chapeaux = {}

for chapeau, teams in chapeaux.items():
    filtered_teams = {}
    
    for country, count in teams.items():
        # Calculate the new total if we add this chapeau's teams
        new_total = country_teams.get(country, 0) + count

        if count > 2:
            count = 2
        
        # Only add the country if its total won't exceed 2
        if country_teams.get(country, 0) < 2:
            filtered_teams[country] = count
            country_teams[country] = new_total  # Update total teams count
    
    # Save the filtered chapeau
    filtered_chapeaux[chapeau] = filtered_teams

# Print the updated chapeaux
for chapeau, teams in filtered_chapeaux.items():
    print(f"{chapeau}: {teams}")

for chapeau in chapeaux.values():
    for country, count in chapeau.items():
        country_teams[country] = country_teams.get(country, 0) + count

print(country_teams)

def countriesList(chapeaux: dict) -> list:
    countries = set()
    for chapeau in chapeaux:
        for country in chapeaux[chapeau]:
            countries.add(country) 
    return list(countries)

ans = 0

for country in countriesList(chapeaux):
    for chapeau in chapeaux:
        if country in chapeaux[chapeau]:
            ans += comb(9-chapeaux[chapeau][country], 2)
        else:
            ans += comb(9, 2)
print(ans)  
