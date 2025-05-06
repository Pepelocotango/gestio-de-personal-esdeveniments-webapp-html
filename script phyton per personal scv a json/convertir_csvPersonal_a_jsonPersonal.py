#####   execució dins la carpeta : python3 convertir_csvPersonal_a_jsonPersonal.py   #####
import csv
import json
import time
import random
import os
import sys # Importem sys per gestionar millor la sortida d'errors

# --- Configuració ---
# No necessitem noms de fitxer fixos aquí

# --- Llegenda de Rols ---
ROLE_MAP = {
    'TS': 'TECNIC SO',
    'TL': 'TECNIC ILUMINACIÓ',
    'P': 'PRODUCCIÓ',
    'M': 'MUNTADOR',
    'MAQUI': 'MAQUINISTA',
    'AET': 'AET',
    'TP': 'TP',
    # Afegeix més abreviatures i les seves traduccions aquí si cal
    # 'VID': 'VIDEO',
    # 'RIG': 'RIGGER',
}

def translate_role(role_abbr):
    """Tradueix abreviatures de rol, gestionant múltiples rols separats per /."""
    if not role_abbr:
        return ""
    # Separem per '/', netegem espais i convertim a majúscules per buscar al mapa
    parts = [p.strip().upper() for p in role_abbr.split('/')]
    # Tradueix cada part si existeix al mapa, sinó manté la part original (en majúscules)
    translated_parts = [ROLE_MAP.get(part, part) for part in parts if part] # Ignorem parts buides
    # Unim les parts traduïdes
    return " / ".join(translated_parts)

def generate_unique_id():
    """Genera un ID similar al del JavaScript (nombre de coma flotant)."""
    # Multipliquem per 1000 per simular els milisegons i afegim un random per més unicitat
    return time.time() * 1000 + random.random() * 1000

# --- Funció Principal de Conversió ---
def convert_csv_to_json(csv_path, json_path):
    people_list = []
    processed_names = set() # Per evitar duplicats exactes de nom
    line_count = 0 # Per comptar línies processades (incloent capçalera)
    added_count = 0 # Per comptar persones afegides al JSON
    skipped_count = 0 # Per comptar línies ignorades

    print(f"\n--- Iniciant conversió de '{os.path.basename(csv_path)}' ---")

    try:
        # Utilitzem 'utf-8-sig' per gestionar correctament el possible BOM (Byte Order Mark) d'alguns CSV
        with open(csv_path, mode='r', encoding='utf-8-sig') as csvfile:
            # Llegeix el CSV assumint la primera fila com a capçalera
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            line_count += 1 # Comptem la capçalera

            # Comprova si les columnes clau existeixen
            required_headers = ['name'] # Com a mínim necessitem el nom
            if not all(h in headers for h in required_headers):
                print(f"ERROR: El fitxer CSV '{os.path.basename(csv_path)}' no conté la columna requerida 'name'.")
                return # Atura si no hi ha la columna nom

            print("Columnes detectades:", ", ".join(headers))

            for row in reader:
                line_count += 1
                try:
                    # Neteja i obté dades bàsiques
                    name = row.get('name', '').strip()
                    role_abbr = row.get('role', '').strip()
                    empresa = row.get('empresa', '').strip()
                    poble = row.get('Poble', '').strip() # Compte amb majúscules/minúscules del CSV

                    # --- Filtre Bàsic: Ignora files sense nom o que semblin separadors/comentaris ---
                    if not name or name.startswith(',') or name.startswith('#') or all(not v for v in row.values()):
                        # print(f"  Línia {line_count}: Ignorada (sense nom, separador o buida)")
                        skipped_count += 1
                        continue

                    # --- Evita duplicats exactes de nom (ignorant majúscules/minúscules) ---
                    normalized_name = name.lower()
                    if normalized_name in processed_names:
                         # print(f"  Línia {line_count}: Ignorada (nom duplicat: '{name}')")
                         skipped_count += 1
                         continue
                    processed_names.add(normalized_name)

                    # --- Mapeig de Telèfons (amb prioritat) ---
                    tel1 = row.get('tel1', '').strip() or row.get('tlf', '').strip() or ""
                    tel2 = row.get('tel2', '').strip() or row.get('tlf magatzem', '').strip() or ""

                    # --- Traducció de Rol ---
                    role_translated = translate_role(role_abbr)

                    # --- Construcció de Notes (Afegint empresa i poble si existeixen) ---
                    notes_parts = []
                    if empresa: notes_parts.append(f"Empresa: {empresa}")
                    if poble: notes_parts.append(f"Poble: {poble}")
                    # Podries afegir altres camps aquí, per exemple:
                    # if row.get('AltreCampCSV'): notes_parts.append(f"Altre: {row.get('AltreCampCSV').strip()}")
                    notes = "\n".join(notes_parts)

                    # --- Creació de l'Objecte Persona ---
                    person_obj = {
                        "id": generate_unique_id(),
                        "name": name,
                        "role": role_translated,
                        "tel1": tel1,
                        "tel2": tel2,
                        "email": row.get('correu electrònic', '').strip(), # Compte amb el nom exacte de la columna
                        "web": row.get('web', '').strip(),
                        "notes": notes
                    }
                    people_list.append(person_obj)
                    added_count += 1

                except Exception as e:
                    print(f"ERROR processant línia {line_count}: {row}")
                    print(f"  Detall de l'error: {e}")
                    skipped_count += 1 # Comptem com a saltada si hi ha error

    except FileNotFoundError:
        print(f"ERROR: No s'ha trobat el fitxer CSV '{csv_path}'")
        return
    except Exception as e:
        print(f"ERROR inesperat llegint el CSV: {e}")
        return

    # --- Estructura final del JSON ---
    output_data = {"people": people_list}

    print(f"\n--- Resultat Conversió '{os.path.basename(csv_path)}' ---")
    print(f"  Línies totals llegides (incloent capçalera): {line_count}")
    print(f"  Persones afegides al JSON: {added_count}")
    print(f"  Línies ignorades/saltades: {skipped_count}")
    print(f"  Guardant el fitxer JSON a: '{os.path.basename(json_path)}'")

    # --- Guardar el JSON ---
    try:
        with open(json_path, mode='w', encoding='utf-8') as jsonfile:
            # ensure_ascii=False permet caràcters com accents correctament
            # indent=2 fa que el fitxer sigui llegible per humans
            json.dump(output_data, jsonfile, ensure_ascii=False, indent=2)
        print("  Conversió completada amb èxit!")
    except Exception as e:
        print(f"ERROR inesperat guardant el JSON: {e}")

# --- Executar la conversió ---
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_to_process = None
    json_output_path = None
    found_csv = False

    print(f"Buscant fitxers .csv a la carpeta: {script_dir}")

    # Busca fitxers .csv a la carpeta de l'script
    for filename in os.listdir(script_dir):
        if filename.lower().endswith('.csv'):
            csv_file_to_process = os.path.join(script_dir, filename)
            base_name = os.path.splitext(filename)[0]
            json_output_filename = f"{base_name}_persones.json"
            json_output_path = os.path.join(script_dir, json_output_filename)
            print(f"  -> S'ha trobat: '{filename}'. Es processarà aquest.")
            found_csv = True
            break # Processa només el primer que troba

    if found_csv and csv_file_to_process and json_output_path:
        convert_csv_to_json(csv_file_to_process, json_output_path)
    else:
        print("\nERROR: No s'ha trobat cap fitxer .csv a la carpeta.")
        print("       Assegura't que hi ha un fitxer CSV a la mateixa carpeta que aquest script.")
        sys.exit(1) # Sortim amb codi d'error si no trobem CSV

    print("\n--- Script finalitzat ---")