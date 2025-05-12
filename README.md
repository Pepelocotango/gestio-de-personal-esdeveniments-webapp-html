# Gestió Integral d'Esdeveniments v10.1

## Descripció

Aquesta és una aplicació web autocontinguda (un sol fitxer HTML) dissenyada per gestionar esdeveniments i les assignacions de personal o grups a aquests esdeveniments. La versió 10 continua millorant la usabilitat i les funcionalitats de la versió 9.x, mantenint l'estructura conceptual de:

1.  **Marcs d'Esdeveniment (Event Frames):** Defineixen l'esdeveniment general (nom, lloc, dates generals, notes generals).
2.  **Assignacions (Assignments):** Vinculen persones o grups específics a un Marc d'Esdeveniment, amb dates concretes (que poden ser un subconjunt de les dates generals del marc), un estat (Pendent, Sí, No) i notes específiques de l'assignació.

L'aplicació està escrita en HTML, CSS i JavaScript (sense frameworks externs, excepte FullCalendar per a la vista de calendari) i està pensada per ser utilitzada directament obrint el fitxer HTML en un navegador web.

**Públic Objectiu:** Dissenyat per a usuaris no programadors que necessiten una eina senzilla per organitzar esdeveniments i la participació de personal.

## Estat Actual del Projecte

*   **Versió:** v10.1 
*   **Estat:** Funcional. Permet les operacions bàsiques de creació, lectura, actualització i eliminació (CRUD) per a Marcs d'Esdeveniment, Persones/Grups i Assignacions. Inclou visualitzacions de taula, calendari, exportació CSV filtrada i resums amb exportació CSV detallada.
*   **Idioma:** Català (interfície i comentaris del codi).

## Novetats a la Versió 10.1

*   **Millores als Resums:**
    *   **Ordenació Avançada:** Els resums (agrupats per nom d'esdeveniment, per data d'inici, i per persona) ara tenen una ordenació interna més lògica, prioritzant les dates més recents i després criteris secundaris com noms.
    *   **Exportació CSV Detallada:** Els botons "Exportar CSV" de cada targeta de resum ara generen fitxers CSV amb informació més rica i contextualitzada, incloent detalls del marc de l'esdeveniment associat a cada assignació.
*   **Reorganització de la Interfície:** La secció "Vista de Calendari" ara es mostra abans que la secció "Afegir Marc Esdeveniment" per a un accés més ràpid a la visualització general.
*   **Millora al Modal de Detalls del Marc:** S'ha afegit un botó "Mostrar a la Llista" que filtra la taula principal per mostrar només el marc d'esdeveniment seleccionat i fa scroll fins a ell.
*   **Neteja d'Interfície:** Eliminat un botó de canvi de tema duplicat/no funcional.

## Característiques Principals (v10.1)

*   **Interfície d'Usuari:**
    *   **Canvi de Tema:** Permet seleccionar entre un tema Clar i un tema Fosc (per defecte).
    *   **Ordre de Seccions:** Vista de Calendari primer, seguida pel formulari d'Afegir Marc.
    *   **Responsiva:** S'adapta a diferents mides de pantalla.
    *   **Modals:** Ús de finestres modals per a gestió de persones, assignacions, detalls de marc (amb nou botó "Mostrar a la Llista") i confirmacions.
    *   **Seccions Desplegables:** La Llista d'Esdeveniments comença oberta; Generació de Llistes i Resums comencen tancades.
    *   **Feedback Visual:** Missatges emergents per informar l'usuari.
*   **Gestió de Dades:**
    *   **Càrrega/Desa:** Permet carregar i guardar TOTES les dades (Marcs, Assignacions, Persones) en un únic fitxer JSON.
    *   **Càrrega/Desa Selectiva:** Permet carregar i guardar NOMÉS les dades de Persones/Grups en un fitxer JSON separat.
    *   **Avís de Canvis:** Mostra un avís quan hi ha canvis sense desar.
    *   **Sense Desa Automàtica:** **MOLT IMPORTANT:** L'aplicació NO desa les dades automàticament. L'usuari ha de desar manualment.
*   **Marcs d'Esdeveniment:**
    *   Crear, Editar i Eliminar Marcs.
    *   Datalists per autocompletar noms i llocs.
*   **Persones/Grups:**
    *   Gestionar (Afegir, Editar, Eliminar) persones o grups.
*   **Assignacions:**
    *   Assignar persones/grups a Marcs d'Esdeveniment.
    *   Definir dates específiques, estat i notes per assignació.
    *   **Detecció de Conflictes:** Avisa si la persona ja té una assignació en les mateixes dates.
*   **Visualització Principal (Taula Agrupada):**
    *   Mostra Marcs d'Esdeveniment i les seves assignacions desplegables.
    *   Recompte d'Estats i opció de marcar "Personal Complet".
    *   Filtrat avançat i ordenació de columnes.
    *   Accions ràpides d'edició/eliminació.
*   **Vista de Calendari:**
    *   Integració amb FullCalendar.
    *   Vistes: 6 Mesos (per defecte), 3 Mesos, 1 Mes, 1 Setmana, Agenda.
    *   Navegació adaptada i interacció per veure detalls o crear esdeveniments.
*   **Generació de Llistes / Informes:**
    *   Secció per exportar dades filtrades de la vista principal a CSV (format agrupat per esdeveniment).
*   **Vista de Resums:**
    *   Targetes amb dades agrupades per nom d'esdeveniment, data d'inici i persona/grup.
    *   **Ordenació millorada** dins de cada resum.
    *   **Exportació CSV detallada** per a cada tipus de resum.

## Com Utilitzar

1.  **Obrir el Fitxer:** Desa el fitxer `Gestió de Personal i Esdeveniments v10_1.html` (o el nom que li hagis donat) al teu ordinador. Fes doble clic sobre ell per obrir-lo amb el teu navegador web preferit.
2.  **Inici:** Apareixerà una pantalla de benvinguda. Fes clic a "Començar" per iniciar una sessió buida. Si tens dades prèvies, pots utilitzar els botons "Carregar Tot (JSON)" o "Carregar Persones (JSON)" de la secció "Gestió de Dades" un cop hagis començat.
3.  **Canviar Tema (Opcional):** Utilitza el botó a la part superior dreta per ajustar el tema visual.
4.  **Visualitzar Calendari:** La vista de calendari ara és la primera secció principal.
5.  **Crear Marcs:** Utilitza el formulari "Afegir Marc Esdeveniment" que ara està sota el calendari.
6.  **Gestionar Persones:** Afegeix/Edita persones des del botó "Gestionar" a "Gestió de Dades > Persones / Grups".
7.  **Assignar Persones:** A la taula principal, fes clic a la icona amb un usuari i un "+" verd a la fila del marc desitjat.
8.  **Filtrar i Ordenar:** Utilitza els controls de la secció "Filtres i Cerca". Fes clic a les capçaleres de la taula per ordenar.
9.  **Exportar:**
    *   **Vista Filtrada Principal:** Aplica filtres, obre "Generació de Llistes / Informes" i clica "Exportar Vista Filtrada (CSV)".
    *   **Resums:** Obre la secció "Resums", i cada targeta tindrà el seu botó "Exportar CSV" que generarà un fitxer detallat.
10. **DESAR:** **Recorda desar les teves dades sovint!** Utilitza els botons "Guardar Tot (JSON)" o "Guardar Persones (JSON)". L'aplicació t'avisarà si intentes tancar la pàgina amb canvis pendents.

## Gestió de Dades: Flux de Treball Important

Aquesta aplicació **no té backend ni emmagatzematge automàtic**. Tota la informació es manté a la memòria del navegador durant la sessió.

*   **Per desar el teu treball:** Utilitza **activament** el botó **Guardar Tot (JSON)**.
*   **Per continuar treballant:** Utilitza **Carregar Tot (JSON)** per restaurar l'estat.
*   **Avís:** Si no guardes les dades abans de tancar la pàgina, **els canvis es perdran**.
*   **Incompatibilitat:** Els fitxers JSON de versions anteriors a la v8/v9 no són compatibles.

## Pila Tecnològica

*   HTML5
*   CSS3 (Variables, Flexbox, Grid)
*   JavaScript (ES6+)
*   [FullCalendar](https://fullcalendar.io/) (v6.1.17 - Incrustat)

## Dependències

*   **FullCalendar:** Utilitza la llibreria FullCalendar (v6.1.17 incrustada). [Llicència MIT](https://github.com/fullcalendar/fullcalendar/blob/main/LICENSE.txt).

## Desenvolupament

Aplicació d'un sol fitxer HTML. Pots editar-lo directament. La lògica principal es troba a l'últim bloc `<script>`.

## Llicència

Aquest projecte està llicenciat sota la Llicència MIT.
(c) 2025 Pepelocotango & Gemini 2.5 Pro

## Agraïments

*   A l'equip de FullCalendar.
*   A les eines d'IA per l'assistència durant el desenvolupament.