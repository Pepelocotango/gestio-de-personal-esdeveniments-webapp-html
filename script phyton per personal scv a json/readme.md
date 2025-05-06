# Convertidor CSV a JSON de Personal (per a Gestió Esdeveniments v9.x)

Aquest script de Python serveix com a **eina complementària** per a l'aplicació web autònoma **`Gestió de Personal i Esdeveniments v9.x`**.

La seva funció principal és convertir un fitxer CSV, que pot ser fàcilment creat o exportat des d'un full de càlcul (com Excel, Google Sheets, LibreOffice Calc), en un fitxer JSON amb l'estructura **exacta** requerida per la funcionalitat **"Carregar Persones (JSON)"** de l'aplicació web.

Això permet gestionar la llista principal de personal (persones o grups) en un format més familiar com un full de càlcul i després importar-la o actualitzar-la ràpidament a l'aplicació web sense haver d'introduir cada contacte manualment dins de l'aplicació.

**Important:** Aquest script només gestiona la part de **Personal**. No converteix ni gestiona Esdeveniments Marc ni Assignacions, els quals es gestionen directament dins de l'aplicació web.

## Flux de Treball Típic

1.  **Mantenir la Llista:** Manté la teva llista de contactes/personal en un full de càlcul (Excel, Google Sheets, etc.) seguint el format de columnes esperat (veure secció "Format CSV").
2.  **Exportar a CSV:** Exporta el full de càlcul com a fitxer `.csv` (preferiblement amb codificació UTF-8).
3.  **Preparar:** Col·loca el fitxer `.csv` exportat a la mateixa carpeta que l'script `convertir_csvPersonal_a_jsonPersonal.py`. Assegura't que només hi hagi *un* fitxer CSV en aquesta carpeta.
4.  **Executar l'Script:** Obre una terminal a aquesta carpeta i executa: `python3 convertir_csvPersonal_a_jsonPersonal.py`.
5.  **Obtenir el JSON:** L'script generarà un fitxer anomenat `<nom_del_teu_csv>_persones.json`.
6.  **Importar a l'App Web:** Obre l'aplicació `Gestió de Personal i Esdeveniments v9.x` al navegador, vés a la secció "Gestió de Dades" i utilitza el botó **"Carregar Persones (JSON)"**. Selecciona el fitxer JSON que acabes de generar. Això carregarà o sobreescriurà la llista de personal dins de l'aplicació.

## Característiques de l'Script

*   **Detecció Automàtica de CSV:** Troba el primer fitxer `.csv` a la carpeta actual.
*   **Lectura Flexible:** Intenta llegir les columnes necessàries (`name`, `role`, `tel1`, `tlf`, `tel2`, `tlf magatzem`, `empresa`, `Poble`, `correu electrònic`, `web`).
*   **Traducció de Rols:** Expandeix abreviatures de rols definides a `ROLE_MAP` (ex: `TS` -> `TECNIC SO`). Gestiona rols múltiples separats per `/`.
*   **Generació d'ID Únics:** Assigna un ID numèric únic a cada persona, similar al format esperat per l'aplicació.
*   **Agrupació de Notes:** Combina camps opcionals (`empresa`, `Poble`) en el camp `notes` del JSON.
*   **Mapeig de Telèfons:** Assigna els telèfons del CSV als camps `tel1` i `tel2` del JSON, donant prioritat a `tel1`/`tel2` sobre `tlf`/`tlf magatzem`.
*   **Prevenció de Duplicats:** Evita afegir entrades amb noms idèntics (ignorant majúscules/minúscules).
*   **Filtrat Bàsic:** Ignora files buides o sense nom.
*   **Sortida Específica:** Genera un fitxer JSON amb l'estructura `{"people": [...]}` compatible amb la funció "Carregar Persones" de l'app web v9.x.

## Requisits

*   Python 3.x

## Format del Fitxer CSV d'Entrada

L'script espera un fitxer CSV amb una fila de capçalera. Les columnes clau que utilitza són:

*   `name`: **(Obligatori)** Nom de la persona o grup.
*   `role`: Abreviatura(es) del rol (ex: `TS`, `TL/M`). Opcional.
*   `tel1`: Primer telèfon (prioritari). Opcional.
*   `tlf`: Telèfon alternatiu (s'usa per `tel1` si `tel1` està buit). Opcional.
*   `tel2`: Segon telèfon (prioritari). Opcional.
*   `tlf magatzem`: Telèfon alternatiu (s'usa per `tel2` si `tel2` està buit). Opcional.
*   `correu electrònic`: Adreça d'email. Opcional.
*   `web`: Pàgina web. Opcional.
*   `empresa`: Nom de l'empresa (s'afegeix a les notes). Opcional.
*   `Poble`: Població (s'afegeix a les notes, compte amb la majúscula). Opcional.

*Nota:* Exporta el CSV amb codificació **UTF-8**. Si exportes des d'Excel, triar "CSV UTF-8 (delimitado por comas)" sol funcionar bé (genera `utf-8-sig`, que l'script gestiona).

## Format del Fitxer JSON de Sortida

L'script genera un fitxer `<nom_base_csv>_persones.json` amb aquesta estructura, llesta per ser importada a l'aplicació web:

#```json
{
  "people": [
    {
      "id": 1678886400123.456,
      "name": "Nom Exemple Contacte",
      "role": "TECNIC SO / MUNTADOR",
      "tel1": "600111222",
      "tel2": "934445566",
      "email": "exemple@correu.cat",
      "web": "http://www.exemple.com",
      "notes": "Empresa: Nom Empresa\nPoble: Ciutat Exemple"
    },
    // ... més objectes de persona
  ]
}

INSTRUCCIONS:

Com Utilitzar l'Script (Passos Detallats)

Prepara el CSV: Assegura't que el teu fitxer CSV té les columnes necessàries (com a mínim name) i està guardat en format UTF-8.

Col·loca els fitxers: Posa l'script convertir_csvPersonal_a_jsonPersonal.py i el teu fitxer .csv a la mateixa carpeta.

Obre una terminal: Navega fins a aquesta carpeta.

Executa: Escriu python3 convertir_csvPersonal_a_jsonPersonal.py i prem Enter.

Verifica: L'script mostrarà informació sobre el procés. Busca el fitxer .json generat a la mateixa carpeta.

Importa: Utilitza l'opció "Carregar Persones (JSON)" dins de l'aplicació web Gestió de Personal i Esdeveniments v9.x per importar aquest fitxer JSON.

Personalització

Rols: Edita el diccionari ROLE_MAP dins de l'script per afegir o modificar les traduccions d'abreviatures de rol.

Columnes CSV: Si els noms de les teves columnes al CSV són diferents, modifica les crides row.get('nom_columna_csv', '') dins de l'script perquè coincideixin amb els noms del teu fitxer.

Llicència

Aquest script es proporciona tal qual. Pots utilitzar la llicència que consideris oportuna (per exemple, MIT License, com l'aplicació web associada).

![alt text](https://img.shields.io/badge/License-MIT-yellow.svg)

