# Gestió de Personal i Esdeveniments (WebApp HTML)

Aquesta és una aplicació web autònoma (single-file HTML) dissenyada per gestionar esdeveniments i l'assignació de personal o grups a aquests esdeveniments. Funciona completament al navegador sense necessitat de backend.

**Versió Actual:** 7.95 beta

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Descripció

L'aplicació permet als usuaris crear, editar, visualitzar i gestionar esdeveniments, assignant-los a persones o grups definits dins del sistema. Inclou múltiples vistes (llista, calendari, resums), funcionalitats de filtratge i ordenació, i gestió bàsica de personal. La persistència de dades es realitza manualment mitjançant la importació i exportació de fitxers JSON.

## Característiques Clau

*   **Gestió d'Esdeveniments:**
    *   Crear, editar i eliminar esdeveniments.
    *   Assignar nom, ubicació, dates (inici i fi opcional), persona/grup, estat (Pendent, Sí, No) i notes.
    *   Detecció de conflictes d'horari per a la persona assignada en afegir/editar.
*   **Gestió de Persones/Grups:**
    *   Crear, editar i eliminar persones o grups (nom, rol, contacte, notes) mitjançant un modal dedicat.
*   **Visualització:**
    *   **Llista Principal:** Taula interactiva amb tots els esdeveniments.
    *   **Calendari:** Vista de calendari integrada (FullCalendar) amb múltiples opcions (4 mesos, 2 mesos, mes, setmana, agenda).
    *   **Resums:** Dades agregades per recompte (per data, persona, nom esdeveniment) o llistes agrupades (per nom esdeveniment, data, persona).
*   **Interactivitat:**
    *   **Filtrat:** Filtra la llista d'esdeveniments per text (nom, lloc, notes, persona), persona/grup, estat i rang de dates.
    *   **Ordenació:** Ordena la taula d'esdeveniments fent clic a les capçaleres de columna.
    *   **Actualització d'Estat Directa:** Canvia l'estat d'un esdeveniment directament des de la taula.
*   **Gestió de Dades:**
    *   **Importació/Exportació:** Guarda i carrega dades de persones i esdeveniments manualment usant fitxers JSON. **(Molt important!)**
*   **UI/UX:**
    *   Disseny responsive per adaptar-se a diferents mides de pantalla.
    *   Missatges de feedback per a les accions de l'usuari.
    *   Modals de confirmació i gestió.
    *   Tema personalitzable mitjançant variables CSS.
    *   Interfície en Català.

## Pila Tecnològica

*   HTML5
*   CSS3 (Variables, Flexbox, Grid)
*   JavaScript (ES6+)
*   [FullCalendar](https://fullcalendar.io/) (v6.1.17 - Incrustat)

## Com Utilitzar

1.  **Obrir:** Simplement obre el fitxer `gestio_de_personal_V7_95_beta .html` en un navegador web modern.
2.  **Començar:** A la pantalla inicial, fes clic a "Començar" per iniciar amb llistes buides.
3.  **Importar Dades (Opcional però Recomanat):**
    *   Si ja tens fitxers JSON de persones o esdeveniments d'una sessió anterior, fes servir els botons "Importar Persones (JSON)" o "Importar Esdeveniments (JSON)" a la secció "Gestió de Dades".
4.  **Gestionar:**
    *   Afegeix/Edita persones o grups des del botó "Gestionar" a "Gestió de Dades".
    *   Afegeix/Edita esdeveniments usant el formulari principal.
    *   Visualitza les dades a la llista, calendari o resums.
    *   Filtra i ordena la llista segons necessitis.
5.  **Exportar Dades (Crucial!):**
    *   **REGULARMENT**, fes clic als botons "Exportar Persones (JSON)" i "Exportar Esdeveniments (JSON)" per desar els teus canvis. Com que l'aplicació funciona només al navegador, **les dades NO es guarden automàticament**. Si tanques la pestanya o el navegador sense exportar, perdràs els canvis fets des de l'última importació/exportació.

## Gestió de Dades: Flux de Treball Important

Aquesta aplicació **no té backend ni emmagatzematge automàtic**. Tota la informació (persones i esdeveniments) es manté a la memòria del navegador durant la sessió.

*   **Per desar el teu treball:** Has d'utilitzar **activament** els botons **Exportar Persones (JSON)** i **Exportar Esdeveniments (JSON)**. Això generarà fitxers `.json` que has de desar al teu ordinador.
*   **Per continuar treballant:** Quan tornis a obrir l'aplicació, hauràs d'utilitzar els botons **Importar Persones (JSON)** i **Importar Esdeveniments (JSON)** per carregar els fitxers que vas desar prèviament.
*   **Avís:** Si no exportes les dades abans de tancar la pàgina, **els canvis es perdran**. Fes exportacions freqüents!

## Dependències

*   **FullCalendar:** Aquesta aplicació utilitza la llibreria FullCalendar per a la vista de calendari. FullCalendar està distribuït sota la [Llicència MIT](https://github.com/fullcalendar/fullcalendar/blob/main/LICENSE.txt). La versió incrustada és la 6.1.17.

## Desenvolupament

Com que és una aplicació d'un sol fitxer, no hi ha un procés de *build* complex. Pots editar directament el fitxer HTML.

*   El codi de FullCalendar i la seva localització en català estan incrustats dins d'etiquetes `<script>`.
*   La lògica principal de l'aplicació es troba a l'últim bloc `<script>`.
*   Els estils CSS es troben dins de l'etiqueta `<style>`.

## Llicència

Aquest projecte està llicenciat sota la Llicència MIT. Consulta el fitxer (LICENSE.txt) per a més detalls.

## Agraïments

*   L'equip de FullCalendar per la seva excel·lent llibreria de calendaris.
*   L'assistència de diverses eines d'IA (Gemini, Claude, Perplexity, ChatGPT) i VS Code i  Sublime Text durant el desenvolupament.