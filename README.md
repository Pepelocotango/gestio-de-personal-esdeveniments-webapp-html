# Gestió de Personal i Esdeveniments v9.2 (WebApp HTML)

Aquesta és una aplicació web autònoma (single-file HTML) redissenyada per gestionar esdeveniments (com a "marcs" generals) i les assignacions específiques de personal o grups a aquests marcs. Funciona completament al navegador sense necessitat de backend.

**Versió Actual:** 9.2

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Descripció General (Canvis v8/v9)

Aquesta versió introdueix un canvi fonamental respecte a versions anteriors (v7.x). Ara es diferencia entre:

*   **Esdeveniments Marc:** L'esdeveniment general amb el seu nom, ubicació, rang de dates global i notes generals.
*   **Assignacions:** Vinculen una persona/grup a un Esdeveniment Marc específic, amb les seves pròpies dates (dins del rang del marc), un estat (Pendent, Sí, No) i notes particulars per a aquesta assignació.

Això permet una gestió més detallada quan un mateix esdeveniment implica diverses persones amb possibles disponibilitats o estats diferents. La persistència de dades es continua realitzant manualment mitjançant la càrrega i desat de fitxers JSON.

## Característiques Clau

*   **Gestió d'Esdeveniments Marc:**
    *   Crear, editar i  eliminar marcs d'esdeveniment (nom, ubicació, dates generals, notes generals).
    *   Marcar un marc com a "Personal Complet" directament des de la llista principal.
*   **Gestió d'Assignacions:**
    *   Assignar persones/grups a un esdeveniment marc existent mitjançant un modal dedicat.
    *   Definir dates específiques per a cada assignació (dins del rang del marc).
    *   Establir un estat per a cada assignació (Pendent, Sí, No).
    *   Afegir notes específiques per a cada assignació.
    *   Editar i eliminar assignacions individuals des de la llista.
    *   Detecció de conflictes d'horari per a la persona en afegir/editar una assignació.
*   **Gestió de Persones/Grups:**
    *   Crear, editar i eliminar persones o grups (Nom, Rol/Tipus, Tel1, Tel2, Email, Web, Notes) mitjançant un modal dedicat.
*   **Visualització:**
    *   **Llista Principal (Agrupada):**
        *   Mostra una fila principal per cada Esdeveniment Marc.
        *   Inclou checkbox per marcar "Personal Complet", nom, ubicació, dates generals, recomptes d'estats (Sí/Pendent/No) de les assignacions, notes generals del marc (truncades amb tooltip) i accions del marc (Assignar Persona, Editar Marc).
        *   A sota de cada fila de marc, mostra les files de detall amb les assignacions de personal corresponents.
        *   Les files de detall mostren: Persona/Grup, Dates Assignació, Estat (amb selector directe), Notes Assignació i Accions individuals (Editar/Eliminar Assignació).
        *   El color de fons de les files de detall reflecteix l'estat de l'assignació individual.
    *   **Calendari:**
        *   Vista de calendari integrada (FullCalendar) amb múltiples opcions (4 mesos, 2 mesos (defecte), mes, setmana, agenda).
        *   Mostra els Esdeveniments Marc.
        *   El color de l'esdeveniment al calendari indica si està marcat com a "Personal Complet" (verd) o no (blau).
        *   Fer clic a un esdeveniment del calendari mostra un popup amb els detalls del marc i la llista de persones assignades amb el seu estat.
    *   **Resums:** *(Funcionalitat temporalment desactivada/pendent d'adaptació a la nova estructura)*.
*   **Interactivitat:**
    *   **Filtrat:** Filtra la llista per text (nom esdeveniment, notes marc/assignació, lloc, nom persona), persona assignada, estat d'assignació i rang de dates (comprova intersecció amb dates del marc o de l'assignació).
    *   **Ordenació:** Ordena la llista de marcs fent clic a les capçaleres de columna (Nom Esdeveniment, Ubicació, Dates Generals).
    *   **Actualització Directa:** Canvia l'estat d'una assignació directament des de la taula. Marca/desmarca "Personal Complet" directament des de la taula.
*   **Gestió de Dades:**
    *   **Carregar/Guardar:** Desa i carrega les dades manualment usant fitxers JSON.
    *   Opció per **Guardar/Carregar Tot** (Persones + Marcs + Assignacions) en un sol fitxer.
    *   Opció per **Guardar/Carregar Només Persones** en un fitxer separat.
    *   **AVÍS:** Aquesta versió utilitza una nova estructura de dades. Els fitxers JSON de versions anteriors (v7.x) **NO són compatibles**.
*   **UI/UX:**
    *   Disseny responsive que s'adapta a diferents mides de pantalla (incloent vista de "targetes" per a marcs en mòbil).
    *   Missatges de feedback per a les accions de l'usuari.
    *   Modals de confirmació i gestió.
    *   Interfície en Català.
    *   Format de data visualitzat com `dd/mm/aa`.

## Pila Tecnològica

*   HTML5
*   CSS3 (Variables, Flexbox, Grid)
*   JavaScript (ES6+)
*   [FullCalendar](https://fullcalendar.io/) (v6.1.17 - Incrustat)

## Com Utilitzar

1.  **Obrir:** Simplement obre el fitxer `Gestió de Personal i Esdeveniments v9_2.html` en un navegador web modern.
2.  **Començar:** A la pantalla inicial, fes clic a "Començar" per iniciar amb llistes buides.
3.  **Carregar Dades (Opcional però Recomanat):**
    *   Si tens un fitxer JSON amb **totes** les dades (`people`, `eventFrames`, `assignments`) d'una sessió anterior, fes servir "Carregar Tot (JSON)".
    *   Si només vols carregar/actualitzar persones, fes servir "Carregar Persones (JSON)".
4.  **Gestionar Persones:** Afegeix/Edita persones o grups des del botó "Gestionar" a "Gestió de Dades".
5.  **Gestionar Esdeveniments Marc:** Utilitza el formulari principal per "Afegir Esdeveniment Marc" o edita un existent des de la llista (botó llapis a la fila del marc).
6.  **Gestionar Assignacions:** Fes clic al botó verd amb icona de persona (+) a la fila del marc desitjat per obrir el modal i afegir/editar/eliminar assignacions de persones a aquell marc.
7.  **Visualitzar:** Observa les dades a la llista agrupada o al calendari.
8.  **Filtrar i Ordenar:** Utilitza els controls de filtre i fes clic a les capçaleres de la taula per ordenar els marcs.
9.  **Guardar Dades (Crucial!):**
    *   **REGULARMENT**, fes clic a "Guardar Tot (JSON)" per desar l'estat complet (persones, marcs, assignacions).
    *   Opcionalment, utilitza "Guardar Persones (JSON)" si només vols desar la llista de personal.
    *   Com que l'aplicació funciona només al navegador, **les dades NO es guarden automàticament**. Si tanques la pestanya o el navegador sense guardar, perdràs els canvis fets des de l'última càrrega/desat.

## Gestió de Dades: Flux de Treball Important (v9.2)

Aquesta aplicació **no té backend ni emmagatzematge automàtic**. Tota la informació es manté a la memòria del navegador durant la sessió.

*   **Per desar el teu treball:** Utilitza **activament** el botó **Guardar Tot (JSON)**. Això generarà un fitxer `.json` que conté tota la informació i que has de desar al teu ordinador. Pots utilitzar **Guardar Persones (JSON)** per desar només el personal si ho necessites per separat.
*   **Per continuar treballant:** Quan tornis a obrir l'aplicació, normalment utilitzaràs **Carregar Tot (JSON)** per restaurar l'estat complet des del fitxer que vas desar. Pots usar **Carregar Persones (JSON)** si només vols actualitzar la llista de personal.
*   **Avís:** Si no guardes les dades abans de tancar la pàgina, **els canvis es perdran**. Fes desats freqüents!
*   **Incompatibilitat:** Els fitxers JSON de versions anteriors a la v8/v9 no són compatibles amb aquesta estructura de Marcs+Assignacions.

## Dependències

*   **FullCalendar:** Utilitza la llibreria FullCalendar (v6.1.17 incrustada) per a la vista de calendari. [Llicència MIT](https://github.com/fullcalendar/fullcalendar/blob/main/LICENSE.txt).

## Desenvolupament

Aplicació d'un sol fitxer HTML. Pots editar-lo directament.

*   El codi de FullCalendar i la localització estan incrustats.
*   La lògica principal de l'aplicació (v9.2) es troba a l'últim bloc `<script>`, organitzada en objectes (`Utils`, `Render`, `Handlers`, `PeopleManager`).
*   Els estils CSS es troben dins de l'etiqueta `<style>`.

## Llicència

Aquest projecte està llicenciat sota la Llicència MIT.

## Agraïments

*   A l'equip de FullCalendar.
*   A les eines d'IA (Gemini, Claude, etc.) per l'assistència durant el desenvolupament.