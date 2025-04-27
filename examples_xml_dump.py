"""
Example usage of the XML dump functionality with accessibility support.
This example demonstrates how to use the XML dump feature to interact with UI elements.
"""

from oiadb import MyADB
from oiadb.commands import xml_dump
import time

# Initialize ADB
adb = MyADB()

# Start the XML dump server on port 8000
server, server_thread = xml_dump.start_xml_server(port=8000)
print("XML dump server started on port 8000")

# Set up port forwarding
xml_dump.setup_port_forwarding(device_port=8000, host_port=8000)
print("Port forwarding set up")

# Get device IP address
device_ip = xml_dump.get_device_ip()
print(f"Device IP: {device_ip}")

if device_ip:
    print(f"XML dump available at: http://{device_ip}:8000/get_xml")
    print(f"Find elements API: http://{device_ip}:8000/find_elements?id=example_id&value=example_text")
    print(f"Accessibility actions API: http://{device_ip}:8000/accessibility_actions?node_id=example_id")

# Example 1: Get XML dump of current UI
print("\nExample 1: Getting XML dump of current UI")
xml_content = xml_dump.get_xml_dump()
print(f"XML content length: {len(xml_content)} characters")
print(xml_content[:500] + "...")  # Print first 500 characters

# Example 2: Find elements by criteria
print("\nExample 2: Finding elements by criteria")
# Find all buttons
buttons = xml_dump.find_elements_by_criteria({"class": "android.widget.Button"})
print(f"Found {len(buttons)} buttons")
for i, button in enumerate(buttons[:3]):  # Print first 3 buttons
    print(f"Button {i+1}: {button.get('text', 'No text')} - {button.get('resource-id', 'No ID')}")

# Example 3: Perform accessibility action
print("\nExample 3: Performing accessibility action")
# Find and click on a button with text "OK" (with threshold for fuzzy matching)
result = xml_dump.perform_accessibility_action(
    "click", 
    {"value": "OK", "threshold": 0.7}
)
print(f"Click action result: {'Success' if result else 'Failed'}")

# Example 4: Using threshold for fuzzy matching
print("\nExample 4: Using threshold for fuzzy matching")
# Find elements with text similar to "Settings" with 0.7 threshold
settings_elements = xml_dump.find_elements_by_criteria(
    {"value": "Settings", "threshold": 0.7}
)
print(f"Found {len(settings_elements)} elements similar to 'Settings'")
for i, element in enumerate(settings_elements[:3]):  # Print first 3 elements
    print(f"Element {i+1}: {element.get('text', 'No text')} - {element.get('class', 'No class')}")

# Example 5: Get available accessibility actions
print("\nExample 5: Getting available accessibility actions")
# Find an editable text field
text_fields = xml_dump.find_elements_by_criteria({"class": "android.widget.EditText"})
if text_fields:
    text_field_id = text_fields[0].get('resource-id', '')
    actions = xml_dump.get_accessibility_actions(text_field_id)
    print(f"Available actions for text field: {[action['name'] for action in actions]}")
else:
    print("No text fields found")

# Example 6: Set text using accessibility action
print("\nExample 6: Setting text using accessibility action")
if text_fields:
    result = xml_dump.perform_accessibility_action(
        "setText", 
        {"class": "android.widget.EditText"}, 
        "Hello from XML dump!"
    )
    print(f"Set text action result: {'Success' if result else 'Failed'}")

# Wait for a moment to see the results
time.sleep(5)

# Stop the server when done
print("\nStopping XML dump server")
xml_dump.stop_xml_server(server)
print("Server stopped")
