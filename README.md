# Gestió Integral d'Esdeveniments v9.5

## Descripció

Aquesta és una aplicació web autocontinguda (un sol fitxer HTML) dissenyada per gestionar esdeveniments i les assignacions de personal o grups a aquests esdeveniments. La versió 9 introdueix un canvi conceptual important, organitzant la informació en:

1.  **Marcs d'Esdeveniment (Event Frames):** Defineixen l'esdeveniment general (nom, lloc, dates generals, notes generals).
2.  **Assignacions (Assignments):** Vinculen persones o grups específics a un Marc d'Esdeveniment, amb dates concretes (que poden ser un subconjunt de les dates generals del marc), un estat (Pendent, Sí, No) i notes específiques de l'assignació.

L'aplicació està escrita en HTML, CSS i JavaScript (sense frameworks externs, excepte FullCalendar per a la vista de calendari) i està pensada per ser utilitzada directament obrint el fitxer HTML en un navegador web.

**Públic Objectiu:** Dissenyat per a usuaris no programadors que necessiten una eina senzilla per organitzar esdeveniments i la participació de personal.

## Estat Actual del Projecte

*   **Versió:** v9.5
*   **Estat:** Funcional. Permet les operacions bàsiques de creació, lectura, actualització i eliminació (CRUD) per a Marcs d'Esdeveniment, Persones/Grups i Assignacions. Inclou visualitzacions de taula, calendari, exportació CSV filtrada i resums.
*   **Idioma:** Català (interfície i comentaris del codi).

## Característiques Principals

*   **Gestió de Dades:**
    *   **Càrrega/Desa:** Permet carregar i guardar TOTES les dades (Marcs, Assignacions, Persones) en un únic fitxer JSON.
    *   **Càrrega/Desa Selectiva:** Permet carregar i guardar NOMÉS les dades de Persones/Grups en un fitxer JSON separat.
    *   **Avís de Canvis:** Mostra un avís quan hi ha canvis sense desar.
    *   **Sense Desa Automàtica:** **MOLT IMPORTANT:** L'aplicació NO desa les dades automàticament. L'usuari ha de desar manualment les dades utilitzant els botons corresponents.
*   **Marcs d'Esdeveniment:**
    *   Crear, Editar i Eliminar Marcs (nom, lloc, dates generals, notes).
    *   Datalists per autocompletar noms i llocs basats en entrades anteriors.
*   **Persones/Grups:**
    *   Gestionar (Afegir, Editar, Eliminar) persones o grups a través d'un modal.
    *   Emmagatzema nom, rol/tipus, telèfons, email, web i notes.
*   **Assignacions:**
    *   Assignar persones/grups a Marcs d'Esdeveniment existents mitjançant un modal.
    *   Definir dates específiques per a cada assignació (dins del rang del marc).
    *   Establir l'estat de l'assignació (Pendent, Sí, No).
    *   Afegir notes específiques per a l'assignació.
    *   **Detecció de Conflictes:** Avisa visualment en el formulari d'assignació si la persona ja té una altra assignació en les mateixes dates.
*   **Visualització Principal (Taula Agrupada):**
    *   Mostra els Marcs d'Esdeveniment com a files principals.
    *   **Desplegable:** Cada marc es pot desplegar/replegar per mostrar/ocultar les assignacions associades (obert per defecte).
    *   **Recompte d'Estats:** Mostra icones amb el recompte d'assignacions per estat (Sí, Pendent, No) a la fila del marc.
    *   **Estat Complet:** Permet marcar un marc com a "Personal Complet" amb un checkbox, canviant visualment la fila.
    *   **Filtrat:** Permet filtrar la llista per text (cerca en noms, llocs, notes, persones), per persona assignada, per **esdeveniment (marc)**, per estat d'assignació i per rang de dates.
    *   **Ordenació:** Permet ordenar la taula per diverses columnes (incloent l'estat de "Personal Complet").
    *   **Vista Detall Assignació:** Mostra la persona, dates específiques, estat (amb selector per canviar-lo directament) i notes de l'assignació.
    *   **Accions Ràpides:** Botons per editar/eliminar marcs i assignacions directament des de la taula.
*   **Vista de Calendari:**
    *   Integració amb FullCalendar per mostrar els Marcs d'Esdeveniment visualment.
    *   Vistes disponibles: **6 Mesos (per defecte)**, 3 Mesos, 1 Mes, 1 Setmana, Agenda.
    *   Navegació per fletxes adaptada a cada vista (mensual per vistes multi-mes i mes, setmanal per vistes setmanals).
    *   Clic en un esdeveniment del calendari obre un modal amb els detalls del Marc.
    *   Clic en una data del calendari permet iniciar la creació d'un nou Marc per a aquesta data.
*   **Generació de Llistes / Informes:**
    *   Nova secció (replegada per defecte) per exportar dades.
    *   Botó **"Exportar Vista Filtrada (CSV)"**.
    *   Genera un fitxer CSV basat en els filtres actius a la secció "Filtres i Cerca".
    *   El CSV exporta **només les assignacions** que compleixen els filtres.
    *   El format del CSV és **agrupat per esdeveniment**, mostrant primer les dades del marc, després les assignacions filtrades d'aquest marc i finalment les notes del marc.
*   **Vista de Resums:**
    *   Secció existent (replegada per defecte) que mostra targetes amb dades agrupades per nom d'esdeveniment, data d'inici i persona. (Els botons CSV d'aquesta secció són independents de la nova funcionalitat d'exportació).
*   **Interfície d'Usuari:**
    *   **Responsiva:** S'adapta a diferents mides de pantalla.
    *   **Modals:** Ús de finestres modals per a gestió de persones, assignacions, detalls de marc i confirmacions.
    *   **Seccions Desplegables:** La Llista d'Esdeveniments comença oberta; Generació de Llistes i Resums comencen tancades. Es poden commutar.
    *   **Feedback Visual:** Missatges emergents per informar l'usuari.

## Com Utilitzar

1.  **Obrir el Fitxer:** Desa el fitxer `Gestió de Personal i Esdeveniments v9_5 dev.html` al teu ordinador. Fes doble clic sobre ell per obrir-lo amb el teu navegador web preferit.
2.  **Inici:** Apareixerà una pantalla de benvinguda. Fes clic a "Començar" o utilitza els botons "Carregar" de la secció "Gestió de Dades" si tens fitxers previs.
3.  **Gestionar Persones:** Afegeix/Edita persones des del botó "Gestionar" a "Gestió de Dades".
4.  **Crear Marcs:** Utilitza el formulari "Afegir Marc Esdeveniment".
5.  **Assignar Persones:** A la taula principal, fes clic a la icona verd (+) a la fila del marc per obrir el modal d'assignació.
6.  **Visualitzar:** Explora la Taula (amb assignacions visibles per defecte) o el Calendari.
7.  **Filtrar i Ordenar:** Utilitza els controls de la secció "Filtres i Cerca". Fes clic a les capçaleres de la taula per ordenar.
8.  **Exportar:** Aplica els filtres desitjats. Obre la secció "Generació de Llistes / Informes" i fes clic a "Exportar Vista Filtrada (CSV)" per descarregar un fitxer amb les assignacions filtrades en format agrupat per esdeveniment.
9.  **DESAR:** **Recorda desar les teves dades sovint!** Utilitza els botons "Guardar Tot (JSON)" o "Guardar Persones (JSON)". Si tanques el navegador sense desar, perdràs els canvis.

## Gestió de Dades: Flux de Treball Important (v9.5)

Aquesta aplicació **no té backend ni emmagatzematge automàtic**. Tota la informació es manté a la memòria del navegador durant la sessió.

*   **Per desar el teu treball:** Utilitza **activament** el botó **Guardar Tot (JSON)**. Això generarà un fitxer `.json` que conté tota la informació i que has de desar al teu ordinador.
*   **Per continuar treballant:** Quan tornis a obrir l'aplicació, normalment utilitzaràs **Carregar Tot (JSON)** per restaurar l'estat complet des del fitxer que vas desar.
*   **Avís:** Si no guardes les dades abans de tancar la pàgina, **els canvis es perdran**. Fes desats freqüents! L'aplicació avisa si detecta canvis pendents en tancar.
*   **Incompatibilitat:** Els fitxers JSON de versions anteriors a la v8/v9 no són compatibles.

## Pila Tecnològica

*   HTML5
*   CSS3 (Variables, Flexbox, Grid)
*   JavaScript (ES6+)
*   [FullCalendar](https://fullcalendar.io/) (v6.1.17 - Incrustat)

## Dependències

*   **FullCalendar:** Utilitza la llibreria FullCalendar (v6.1.17 incrustada) per a la vista de calendari. [Llicència MIT](https://github.com/fullcalendar/fullcalendar/blob/main/LICENSE.txt).

## Desenvolupament

Aplicació d'un sol fitxer HTML. Pots editar-lo directament. La lògica principal es troba a l'últim bloc `<script>`.

## Llicència

Aquest projecte està llicenciat sota la Llicència MIT.
(c) 2025 Pepelocotango & Gemini 2.5 Pro

## Agraïments

*   A l'equip de FullCalendar.
*   A les eines d'IA per l'assistència durant el desenvolupament.