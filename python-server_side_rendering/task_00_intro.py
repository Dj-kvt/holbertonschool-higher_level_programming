#!/usr/bin/python3
"""Generate personalized invitation files from a template and list of attendees"""

import os


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and list of attendees.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): List of dictionaries with attendee information.

    Returns:
        None
    """

    # Validate input types
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Check for empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders, using "N/A" if missing or None
        content = template
        content = content.replace("{name}", str(attendee.get("name", "N/A") or "N/A"))
        content = content.replace("{event_title}", str(attendee.get("event_title", "N/A") or "N/A"))
        content = content.replace("{event_date}", str(attendee.get("event_date", "N/A") or "N/A"))
        content = content.replace("{event_location}", str(attendee.get("event_location", "N/A") or "N/A"))

        # Generate output file name
        file_name = f"output_{index}.txt"

        # Write to file
        try:
            with open(file_name, "w", encoding="utf-8") as output_file:
                output_file.write(content)
        except Exception as e:
            print(f"Error writing to {file_name}: {e}")
