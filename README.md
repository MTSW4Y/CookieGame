Documentatie voor CookieGame

1. Introductie

Dit document biedt uitgebreide documentatie voor het CookieGame-project, een simulatiespel ontwikkeld met Streamlit en SQLite. Het spel simuleert het proces van het produceren en leveren van koekjes, waaronder stroopwafels, princekoeken en pennywafels, aan verschillende klanten zoals Hema, Jumbo en AH. Het project is ontworpen om inzicht te geven in supply chain management en kwaliteitscontrole binnen een productieomgeving.

2. Projectoverzicht

CookieGame is een interactieve simulatie die gebruikers in staat stelt om de operaties van een koekjesfabriek te beheren. Spelers kunnen orders aannemen, voorraden beheren, productieprocessen volgen en kwaliteitscontroles uitvoeren. De simulatie omvat een tijdsmechanisme dat de voortgang van de dag en de leveringsmomenten bijhoudt. Het doel is om efficiënt te produceren en te leveren, terwijl de kwaliteit van de producten wordt gewaarborgd.

2.1. Doelstellingen

•
Simulatie van productieprocessen: Het nabootsen van de stappen die nodig zijn om koekjes te produceren, van grondstoffen tot eindproduct.

•
Supply Chain Management: Het beheren van inkomende orders, voorraden en leveringen.

•
Kwaliteitscontrole: Het implementeren van processen om de kwaliteit van de geproduceerde koekjes te waarborgen en afwijkingen te registreren.

•
Interactieve Gebruikersinterface: Het bieden van een intuïtieve interface via Streamlit voor gebruikersinteractie en monitoring.

2.2. Technologieën

Het CookieGame-project maakt gebruik van de volgende belangrijke technologieën:

•
Python: De primaire programmeertaal voor de gehele applicatie.

•
Streamlit: Een open-source Python-bibliotheek voor het snel bouwen van interactieve webapplicaties. Gebruikt voor de gebruikersinterface van het spel.

•
SQLite: Een lichtgewicht, op bestanden gebaseerd relationeel databasesysteem. Gebruikt voor het opslaan van alle spelgegevens, zoals orders, voorraden en tijdsregistraties.

•
Pandas: Een data-analysebibliotheek die wordt gebruikt voor het verwerken en manipuleren van gegevens die uit de SQLite-database worden opgehaald.

•
streamlit-autorefresh: Een Streamlit-component die automatische verversing van de pagina mogelijk maakt, wat essentieel is voor de real-time voortgang van de simulatie.

3. Installatie en Setup

Om het CookieGame-project lokaal uit te voeren, volgt u de onderstaande stappen.

3.1. Vereisten

Zorg ervoor dat Python 3.x op uw systeem is geïnstalleerd.

3.2. Klonen van de Repository

Open een terminal of command prompt en kloon de GitHub repository:

Bash


git clone https://github.com/MTSW4Y/CookieGame.git
cd CookieGame


3.3. Virtuele Omgeving (Aanbevolen)

Het is sterk aanbevolen om een virtuele omgeving te gebruiken om afhankelijkheden te isoleren:

Bash


python -m venv venv
source venv/bin/activate  # Op Linux/macOS
# of
venv\Scripts\activate  # Op Windows


3.4. Installeren van Afhankelijkheden

Installeer de benodigde Python-pakketten met pip:

Bash


pip install -r requirements.txt


De requirements.txt bevat de volgende pakketten:

•
streamlit-autorefresh

3.5. Database Initialisatie

De database wordt automatisch geïnitialiseerd wanneer app.py voor het eerst wordt uitgevoerd. Er wordt een central_database.db bestand aangemaakt in de projectmap.

3.6. Starten van de Applicatie

Start de Streamlit-applicatie vanuit de hoofdmap van het project:

Bash


streamlit run app.py


De applicatie zal openen in uw standaard webbrowser. Als dit niet automatisch gebeurt, navigeer dan naar http://localhost:8501.

4. Projectstructuur

De projectmap CookieGame heeft de volgende structuur:

Plain Text


CookieGame/
├── README.md
├── app.py
├── database.py
├── orders.py
├── pages/
│   ├── 1_🍪 - openstaande_orders.py
│   ├── 2_👤 - klanten-gereedmelden.py
│   ├── 3_👤 - klanten-kwaliteitscontrole.py
│   ├── 4_🏭 - leveranciers.py
│   ├── 5_🏆 - leaderboard.py
│   ├── 6_💾 - data.py
│   └── app_management.py
└── requirements.txt


5. Module Beschrijvingen

5.1. app.py

Dit is het hoofdbestand van de Streamlit-applicatie. Het initialiseert de SQLite-database en definieert de tabellen die worden gebruikt voor het opslaan van orders, gereedgemelde orders, voorraden en simulatietijd. De init_db() functie zorgt ervoor dat de benodigde tabellen worden aangemaakt als ze nog niet bestaan. Dit bestand is cruciaal voor het opzetten van de database-structuur bij de eerste keer uitvoeren van de applicatie.

5.2. database.py

Deze module bevat alle functies voor interactie met de SQLite-database. Het biedt abstractie voor database-operaties zoals het toevoegen, ophalen, wissen en bijwerken van gegevens in de orders, ready_orders, supplies en time tabellen. Belangrijke functies zijn onder andere:

•
get_connection(): Maakt een verbinding met de central_database.db.

•
add_order(), get_orders(), clear_orders(), delete_order_by_id(): Functies voor het beheren van klantorders.

•
add_ready_order(), get_ready_orders(), clear_ready_orders(), delete_ready_order_by_id(): Functies voor het beheren van gereedgemelde orders en kwaliteitscontroles.

•
add_supply(), get_supplies(), clear_supplies(), delete_supply_by_id(): Functies voor het beheren van voorraden.

•
get_simulation_time(), upsert_time(): Functies voor het beheren van de simulatietijd.

•
registrer_supplies(): Een helperfunctie om meerdere voorraadtransacties tegelijk te registreren.

5.3. orders.py

Dit bestand definieert de initiële set van orders en startvoorraden voor de simulatie. Het bevat drie verschillende rondes (ronde_1, ronde_2, ronde_3) van klantorders, elk met specifieke details zoals klantnaam, leveringsdatum en aantallen van elk type koekje. Deze data wordt gebruikt om de simulatie te voeden en verschillende scenario's te testen.

5.4. pages/ Directory

Deze directory bevat de verschillende pagina's van de Streamlit-applicatie. Elke .py bestand in deze map vertegenwoordigt een aparte pagina in de navigatie van de Streamlit-app. De namen van de bestanden, zoals 1_🍪 - openstaande_orders.py, bepalen de volgorde en de weergavenaam in de zijbalk van de Streamlit-applicatie.

•
app_management.py: Bevat de logica voor het starten en resetten van de simulatie, het beheren van de simulatietijd en het injecteren van nieuwe orders op basis van de voortgang van de tijd. Het stelt gebruikers ook in staat om spoedbestellingen handmatig toe te voegen en de actieve ronde van orders te selecteren.

•
1_🍪 - openstaande_orders.py: Toont een overzicht van alle openstaande klantorders die nog moeten worden geproduceerd en geleverd. De data wordt dynamisch opgehaald uit de database en weergegeven in een tabel.

•
2_👤 - klanten-gereedmelden.py: Biedt een interface voor het gereedmelden van orders. Gebruikers kunnen ordernummers en groepsnummers invoeren om aan te geven dat een order is voltooid.

•
3_👤 - klanten-kwaliteitscontrole.py: Deze pagina is bedoeld voor kwaliteitscontrole. Gebruikers kunnen de geleverde aantallen en de kwaliteit van de koekjes registreren. Het systeem kan ook feedback van groepen registreren en de redenen voor afkeur vastleggen.

•
4_🏭 - leveranciers.py: Beheert de uitgifte van materialen aan de productiegroepen. Gebruikers kunnen de aantallen van verschillende ingrediënten (vulling, deeg) en bakjes registreren die aan een specifieke groep zijn geleverd.

•
5_🏆 - leaderboard.py: Een placeholder-pagina die in de toekomst kan worden uitgebreid om een leaderboard te tonen, mogelijk gebaseerd op de prestaties van verschillende productieteams (bijv. verdiend geld of efficiëntie).

•
6_💾 - data.py: Biedt functionaliteit voor het bekijken, verwijderen en downloaden van alle gegevens uit de database. Gebruikers kunnen specifieke records verwijderen of een complete JSON-dump van de database downloaden voor analyse of back-updoeleinden.

6. Gebruikershandleiding

6.1. Starten van een Nieuwe Simulatie

1.
Navigeer naar de App Management pagina (via app_management.py).

2.
Selecteer de gewenste ronde (bijv. "ronde 1") om de initiële orders te laden.

3.
Klik op de knop 🕒 Start Timer om de simulatie te starten. De simulatietijd zal beginnen te lopen en orders zullen automatisch worden ingeschoten op basis van de gedefinieerde uren in orders.py.

6.2. Orders Beheren

•
Openstaande Orders: Bekijk de Openstaande orders pagina om een overzicht te krijgen van alle actieve orders.

•
Orders Gereedmelden: Gebruik de Klanten - Gereedmelden pagina om voltooide orders te registreren.

•
Kwaliteitscontrole: Op de Klanten - Kwaliteitscontrole pagina kunt u de kwaliteit van geleverde producten vastleggen en eventuele afkeurredenen specificeren.

6.3. Voorraden Beheren

•
Materialen Uitgeven: Gebruik de Leveranciers pagina om de uitgifte van grondstoffen (vulling, deeg, bakjes) aan productiegroepen te registreren.

6.4. Data Beheren

•
Data Bekijken en Downloaden: De Data pagina biedt de mogelijkheid om alle databasegegevens te bekijken en te downloaden als een JSON-bestand. Dit is handig voor analyse of het maken van back-ups.

•
Data Verwijderen: Op dezelfde Data pagina kunt u individuele records (orders, gereedgemelde orders, leveranties) verwijderen.

6.5. Simulatie Resetten

Om de simulatie volledig te resetten en alle gegevens te wissen, klikt u op de knop 🔴 Reset Game op de App Management pagina. Dit zal alle orders, gereedgemelde orders en voorraden uit de database verwijderen.

7. Ontwikkeling en Bijdragen

Dit project is open-source en bijdragen zijn welkom. Volg de standaard GitHub-workflow:

1.
Fork de repository.

2.
Maak een nieuwe branch voor uw functie (git checkout -b feature/AmazingFeature).

3.
Commit uw wijzigingen (git commit -m 'Add some AmazingFeature').

4.
Push naar de branch (git push origin feature/AmazingFeature).

5.
Open een Pull Request.
