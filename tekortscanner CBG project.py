import matplotlib.pyplot as plt
# Simple AI Risk Assessor voor Medicijntekorten (CBG Concept)

def bereken_tekort_risico(medicijn_naam, aantal_leveranciers, api_monopolie, vraag_stijging_pct):
    print(f"\n--- Analyseren van risicoprofiel voor: {medicijn_naam} ---")
    
    # Basis score berekening op basis van risicofactoren
    risicoscore = 0
    
    # Factor 1: Aantal fabrikanten/leveranciers op de markt
    if aantal_leveranciers == 1:
        risicoscore += 40
    elif aantal_leveranciers <= 3:
        risicoscore += 20
    else:
        risicoscore += 5
        
    # Factor 2: Grondstof (API) afhankelijkheid van één regio/fabriek
    if api_monopolie:
        risicoscore += 35
    else:
        risicoscore += 10
        
    # Factor 3: Verwachte of historische vraagstijging
    if vraag_stijging_pct > 20:
        risicoscore += 25
    elif vraag_stijging_pct > 10:
        risicoscore += 15
    else:
        risicoscore += 5

    # Resultaat & AI Beoordeling
    print(f"Berekende Risicoscore: {risicoscore} / 100")
    
    if risicoscore >= 70:
        status = "KRITIEK RISICO: Onmiddellijk CBG-toezicht en voorraadmonitoring vereist."
    elif risicoscore >= 40:
        status = "MATIG RISICO: Periodieke controle van ketenafhankelijkheid aanbevolen."
    else:
        status = "LAAG RISICO: Voldoende marktspreiding en voorraadveiligheid."
        
    print(f"CBG AI-Advies: {status}\n")

# Testscenario's
bereken_tekort_risico("Amoxicilline 500mg", aantal_leveranciers=2, api_monopolie=True, vraag_stijging_pct=25)
bereken_tekort_risico("Paracetamol 500mg", aantal_leveranciers=8, api_monopolie=False, vraag_stijging_pct=5)
bereken_tekort_risico("Ozempic 1mg", aantal_leveranciers=1, api_monopolie=True, vraag_stijging_pct=30)
bereken_tekort_risico("Salbutamol 100mcg", aantal_leveranciers=3, api_monopolie=False, vraag_stijging_pct=12)

# Data verzamelen van je 4 medicijnen
medicijnen = ["Paracetamol", "Salbutamol", "Amoxicilline", "Ozempic"]
scores = [0, 45, 80, 100]
kleuren = ["green", "orange", "red", "red"]# Live scenario-invoer voor de demo (Meerdere medicijnen vergelijken)
print("\n--- CBG AI Risicoscanner: Live Invoer ---")

# Lege verzamellijsten aanmaken
medicijnen = []
scores = []
kleuren = []

while True:
    naam = input("\nVoer medicijnnaam in: ")
    leveranciers = int(input("Aantal leveranciers (bijv. 1, 2, 5): "))
    api_monopolie = input("Is er sprake van een API-grondstofmonopolie? (ja/nee): ").strip().lower()

    # Risicoscore berekenen
    score = 20
    if leveranciers == 1:
        score += 40
    elif leveranciers <= 3:
        score += 20

    if api_monopolie == "ja":
        score += 40

    score = min(score, 100)

    # Advies en kleur bepalen
    if score >= 70:
        kleur = "red"
        advies = "KRITIEK RISICO: Verplichte 2e API-bron & ketendiversificatie vereist."
    elif score >= 40:
        kleur = "orange"
        advies = "MATIG RISICO: Verplichte ijzeren voorraad (min. 2 maanden) opleggen."
    else:
        kleur = "green"
        advies = "LAAG RISICO: Standaard dossierafhandeling."

    print(f"\n[UITSLAG] Berekende Risicoscore voor {naam}: {score}/100")
    print(f"[ADVIES] {advies}")

    # Waarden opslaan in de verzamellijsten
    medicijnen.append(naam)
    scores.append(score)
    kleuren.append(kleur)

    # Herhaalvraag
    verder = input("\nWilt u nog een medicijn beoordelen? (ja/nee): ").strip().lower()
    if verder != "ja":
        break

# Grafiek genereren en opslaan van ALLE ingevoerde medicijnen samen
plt.figure(figsize=(8, 5))
plt.bar(medicijnen, scores, color=kleuren)
plt.axhline(y=70, color='red', linestyle='--', label='Kritiek risico (70+)')
plt.ylim(0, 110)
plt.ylabel('Risicoscore (0 - 100)')
plt.title('CBG AI Risk Assessment - Vergelijking Medicijnen')
plt.legend()
plt.tight_layout()

plt.savefig('grafiek.png')
print("\nGrafiek met alle medicijnen succesvol geüpdatet als 'grafiek.png'!")

# Grafiek opbouwen
plt.figure(figsize=(7, 4))
plt.bar(medicijnen, scores, color=kleuren)
plt.axhline(y=70, color='red', linestyle='--', label='Kritiek risico (70+)')

# Labels en titel toevoegen
plt.title('CBG AI Risk Assessment - Medicijntekorten')# --- ACTIEPLAN GENEREREN EN OPSLAAN ALS TEKSTBESTAND ---
with open("actieplan.txt", "w", encoding="utf-8") as f:
    f.write("=== CBG AI RISICO-ANALYSE & INTERVENTIEPLAN ===\n")
    f.write("Gegenereerd door Tekortscanner CBG\n")
    f.write("===============================================\n\n")

    for i in range(len(medicijnen)):
        m_naam = medicijnen[i]
        m_score = scores[i]

        if m_score >= 70:
            interventie = (
                "[KRITIEK RISICO]\n"
                "  - Actie: Directe keteninterventie vereist.\n"
                "  - Maatregel 1: Verplichte 2e API-grondstofbron inschakelen.\n"
                "  - Maatregel 2: Landelijke 'ijzeren voorraad' (2-3 maanden) aanspreken.\n"
                "  - Maatregel 3: Automatische melding versturen naar LCG."
            )
        elif m_score >= 40:
            interventie = (
                "[MATIG RISICO]\n"
                "  - Actie: Preventieve voorraadmonitoring.\n"
                "  - Maatregel 1: Opstellen therapeutische alternatievenlijst voor voorschrijvers.\n"
                "  - Maatregel 2: Kwartaal-audit op leveringszekerheid van de fabrikant."
            )
        else:
            interventie = (
                "[LAAG RISICO]\n"
                "  - Actie: Standaard monitoring.\n"
                "  - Maatregel: Geen acute actie vereist. Periodieke herbeoordeling over 6 maanden."
            )

        f.write(f"Medicijn: {m_naam}\n")
        f.write(f"Risicoscore: {m_score}/100\n")
        f.write(f"{interventie}\n")
        f.write("-----------------------------------------------\n\n")

print("Actieplan succesvol geëxporteerd als 'actieplan.txt'!")