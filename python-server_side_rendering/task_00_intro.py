import os

def generate_invitations(template, attendees):
    """
    Génère des fichiers d'invitations à partir d'un template et d'une liste de participants.

    Args:
        template (str): Le contenu du template avec des placeholders {name}, {event_title}, {event_date}, {event_location}.
        attendees (list of dict): Liste de dictionnaires contenant les informations des participants.
    """
    # Vérification des types
    if not isinstance(template, str):
        print(f"Error: Invalid template type: {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid attendees type: {type(attendees).__name__}")
        return

    # Gestion des inputs vides
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        invitation = template
        # Remplacer chaque placeholder par la valeur correspondante ou "N/A" si manquante
        invitation = invitation.replace("{name}", str(attendee.get("name") or "N/A"))
        invitation = invitation.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
        invitation = invitation.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
        invitation = invitation.replace("{event_location}", str(attendee.get("event_location") or "N/A"))

        # Nom du fichier
        filename = f"output_{idx}.txt"

        try:
            with open(filename, "w") as f:
                f.write(invitation)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
