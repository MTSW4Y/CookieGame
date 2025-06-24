# CookieGame

## 1. Introductie

De CookieGame is een simulatiespel ontwikkeld met Streamlit. Het spel simuleert het proces van het produceren en leveren van koekjes, waaronder stroopwafels, princekoeken en pennywafels, aan verschillende klanten zoals Hema, Jumbo en AH. Het project is ontworpen om inzicht te geven in de 'operations' in een productieomgeving. Studenten gaan aan de slag met een fysiek productieomgeving en deze software zorgt voor de administratieve afhandeling. Deze afhandeling wordt gedaan door begeleiders die orders inschieten, grondstoffen leveren en uiteindelijk de kwaliteit controleren.

### 2.1. Doelstellingen

*   **Simulatie van productieprocessen:** Het nabootsen van de stappen die nodig zijn om koekjes te produceren, van grondstoffen tot eindproduct.
*   **Operations:** Het beheren van inkomende orders, voorraden en leveringen.
*   **Kwaliteitscontrole:** Het implementeren van processen om de kwaliteit van de geproduceerde koekjes te waarborgen en afwijkingen te registreren.

### 2.2. Technologieën

Het CookieGame-project maakt gebruik van:

*   **Python:** De primaire programmeertaal voor de gehele applicatie.
*   **Streamlit:** Een open-source Python-bibliotheek voor het snel bouwen van interactieve webapplicaties. Gebruikt voor de gebruikersinterface van het spel.
*   **SQLite:** Een lichtgewicht, op bestanden gebaseerd relationeel databasesysteem. Gebruikt voor het opslaan van alle spelgegevens, zoals orders, voorraden en tijdsregistraties.
*   **Pandas:** Een data-analysebibliotheek die wordt gebruikt voor het verwerken en manipuleren van gegevens die uit de SQLite-database worden opgehaald.

## 3. Projectstructuur

De projectmap `CookieGame` heeft de volgende structuur:

```
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
```

## 4. Module Beschrijvingen

### 5.1. `app.py`

Dit is het hoofdbestand van de Streamlit-applicatie. Het initialiseert de SQLite-database en definieert de tabellen die worden gebruikt voor het opslaan van orders, gereedgemelde orders, voorraden en simulatietijd. De `init_db()` functie zorgt ervoor dat de benodigde tabellen worden aangemaakt als ze nog niet bestaan. Dit bestand is cruciaal voor het opzetten van de database-structuur bij de eerste keer uitvoeren van de applicatie.

### 4.2. `database.py`

Deze module bevat alle functies voor interactie met de SQLite-database. Het biedt abstractie voor database-operaties zoals het toevoegen, ophalen, wissen en bijwerken van gegevens in de `orders`, `ready_orders`, `supplies` en `time` tabellen. Belangrijke functies zijn onder andere:

*   `get_connection()`: Maakt een verbinding met de `central_database.db`.
*   `add_order()`, `get_orders()`, `clear_orders()`, `delete_order_by_id()`: Functies voor het beheren van klantorders.
*   `add_ready_order()`, `get_ready_orders()`, `clear_ready_orders()`, `delete_ready_order_by_id()`: Functies voor het beheren van gereedgemelde orders en kwaliteitscontroles.
*   `add_supply()`, `get_supplies()`, `clear_supplies()`, `delete_supply_by_id()`: Functies voor het beheren van voorraden.
*   `get_simulation_time()`, `upsert_time()`: Functies voor het beheren van de simulatietijd.
*   `registrer_supplies()`: Een helperfunctie om meerdere voorraadtransacties tegelijk te registreren.

### 4.3. `orders.py`

Dit bestand definieert de initiële set van orders en startvoorraden voor de simulatie. Het bevat drie verschillende rondes (`ronde_1`, `ronde_2`, `ronde_3`) van klantorders, elk met specifieke details zoals klantnaam, leveringsdatum en aantallen van elk type koekje. Deze data wordt gebruikt om de simulatie te voeden en verschillende scenario's te testen.

### 4.4. `pages/` Directory

Deze directory bevat de verschillende pagina's van de Streamlit-applicatie. Elke `.py` bestand in deze map vertegenwoordigt een aparte pagina in de navigatie van de Streamlit-app. De namen van de bestanden, zoals `1_🍪 - openstaande_orders.py`, bepalen de volgorde en de weergavenaam in de zijbalk van de Streamlit-applicatie.

*   **`app_management.py`**: Bevat de logica voor het starten en resetten van de simulatie, het beheren van de simulatietijd en het injecteren van nieuwe orders op basis van de voortgang van de tijd. Het stelt gebruikers ook in staat om spoedbestellingen handmatig toe te voegen en de actieve ronde van orders te selecteren.
*   **`1_🍪 - openstaande_orders.py`**: Toont een overzicht van alle openstaande klantorders die nog moeten worden geproduceerd en geleverd. De data wordt dynamisch opgehaald uit de database en weergegeven in een tabel.
*   **`2_👤 - klanten-gereedmelden.py`**: Biedt een interface voor het gereedmelden van orders. Gebruikers kunnen ordernummers en groepsnummers invoeren om aan te geven dat een order is voltooid.
*   **`3_👤 - klanten-kwaliteitscontrole.py`**: Deze pagina is bedoeld voor kwaliteitscontrole. Gebruikers kunnen de geleverde aantallen en de kwaliteit van de koekjes registreren. Het systeem kan ook feedback van groepen registreren en de redenen voor afkeur vastleggen.
*   **`4_🏭 - leveranciers.py`**: Beheert de uitgifte van materialen aan de productiegroepen. Gebruikers kunnen de aantallen van verschillende ingrediënten (vulling, deeg) en bakjes registreren die aan een specifieke groep zijn geleverd.
*   **`5_🏆 - leaderboard.py`**: Een placeholder-pagina die in de toekomst kan worden uitgebreid om een leaderboard te tonen, mogelijk gebaseerd op de prestaties van verschillende productieteams (bijv. verdiend geld of efficiëntie).
*   **`6_💾 - data.py`**: Biedt functionaliteit voor het bekijken, verwijderen en downloaden van alle gegevens uit de database. Gebruikers kunnen specifieke records verwijderen of een complete JSON-dump van de database downloaden voor analyse of back-updoeleinden.

## 5. Gebruikershandleiding

### 5.1. Starten van een Nieuwe Simulatie

1.  Navigeer naar de `App Management` pagina (via `app_management.py`).
2.  Selecteer de gewenste ronde (bijv. "ronde 1") om de initiële orders te laden.
3.  Klik op de knop `🕒 Start Timer` om de simulatie te starten. De simulatietijd zal beginnen te lopen en orders zullen automatisch worden ingeschoten op basis van de gedefinieerde uren in `orders.py`.

### 5.2. Orders Beheren

*   **Openstaande Orders:** Bekijk de `Openstaande orders` pagina om een overzicht te krijgen van alle actieve orders.
*   **Orders Gereedmelden:** Gebruik de `Klanten - Gereedmelden` pagina om voltooide orders te registreren.
*   **Kwaliteitscontrole:** Op de `Klanten - Kwaliteitscontrole` pagina kunt u de kwaliteit van geleverde producten vastleggen en eventuele afkeurredenen specificeren.

### 5.3. Voorraden Beheren

*   **Materialen Uitgeven:** Gebruik de `Leveranciers` pagina om de uitgifte van grondstoffen (vulling, deeg, bakjes) aan productiegroepen te registreren.

### 5.4. Data Beheren

*   **Data Bekijken en Downloaden:** De `Data` pagina biedt de mogelijkheid om alle databasegegevens te bekijken en te downloaden als een JSON-bestand. Dit is handig voor analyse of het maken van back-ups.
*   **Data Verwijderen:** Op dezelfde `Data` pagina kunt u individuele records (orders, gereedgemelde orders, leveranties) verwijderen.

### 5.5. Simulatie Resetten

Om de simulatie volledig te resetten en alle gegevens te wissen, klikt u op de knop `🔴 Reset Game` op de `App Management` pagina. Dit zal alle orders, gereedgemelde orders en voorraden uit de database verwijderen.

## 6. Ontwikkeling en Bijdragen

Dit project is open-source en bijdragen zijn welkom. Volg de standaard GitHub-workflow:

1.  Fork de repository.
2.  Maak een nieuwe branch voor uw functie (`git checkout -b feature/AmazingFeature`).
3.  Commit uw wijzigingen (`git commit -m 'Add some AmazingFeature'`).
4.  Push naar de branch (`git push origin feature/AmazingFeature`).
5.  Open een Pull Request.
