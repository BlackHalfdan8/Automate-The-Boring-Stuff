#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard with keyboard shortcuts.
# Usage:    py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#           py.exe mcb.pyw list - Loads all keywords to clipboard.
#           py.exe mcb.pyw delete <keyword> - Deletes keyword from the shelf.
#           py.exe mcb.pyw clear - Clears all keywords from the shelf.
#           py.exe mcb.pyw count - Displays total number of keywords.
#           py.exe mcb.pyw search <keyword> - Searches for keyword and copies
#                                             a snippet if found.
#           py.exe mcb.pyw backup - Creates a backup of the current state of the shelf.
#           py.exe mcb.pyw restore - Restores the shelf from the last backup.
#           py.exe mcb.pyw shortcuts - Lists all keyboard shortcuts and their
#                                      assigned keywords.
#           py.exe mcb.pyw setshortcut <shortcut> <keyword> - Assigns a keyword to a
#                                                             keyboard shortcut.
#           py.exe mcb.pyw clearshortcut <shortcut> - Clears the keyword assigned to
#                                                     a keyboard shortcut.
#           py.exe mcb.pyw deleteshortcut <shortcut> - Deletes a keyboard shortcut
#                                                      and its assigned keyword.
#           py.exe mcb.pyw replacshortcut <shortcut> <new_keyword> - Replaces the
#                                                                   keyword assigned to
#                                                                   a keyboard shortcut.
#           py.exe mcb.pyw help - Displays this help message.

import shelve
import pyperclip
import sys
import shutil
import os

mcbShelf = shelve.open("mcb")
backup_dir = "mcb_backups"

# Create backup directory if it doesn't exist
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)


def print_help():
    help_text = (
        "mcb.pyw - Multi-Clipboard Utility\n\n"
        "Usage:\n"
        "  py.exe mcb.pyw save <keyword> - Save clipboard.\n"
        "  py.exe mcb.pyw <keyword> - Load keyword.\n"
        "  py.exe mcb.pyw list - Load all keywords.\n"
        "  py.exe mcb.pyw delete <keyword> - Delete keyword.\n"
        "  py.exe mcb.pyw clear - Clear all keywords.\n"
        "  py.exe mcb.pyw count - Show total keywords.\n"
        "  py.exe mcb.pyw search <keyword> - Search keyword and copy snippet.\n"
        "  py.exe mcb.pyw backup - Create backup.\n"
        "  py.exe mcb.pyw restore - Restore from backup.\n"
        "  py.exe mcb.pyw shortcuts - List shortcuts and keywords.\n"
        "  py.exe mcb.pyw setshortcut <shortcut> <keyword> - Assign shortcut.\n"
        "  py.exe mcb.pyw clearshortcut <shortcut> - Clear shortcut.\n"
        "  py.exe mcb.pyw deleteshortcut <shortcut> - Delete shortcut.\n"
        "  py.exe mcb.pyw replacshortcut <shortcut> <new_keyword> - Replace shortcut.\n"
        "  py.exe mcb.pyw help - Display help.\n"
    )
    pyperclip.copy(help_text.strip())
    print(help_text)


# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == "clear":
        mcbShelf.clear()
    elif sys.argv[1].lower() == "count":
        pyperclip.copy(str(len(mcbShelf)))
    elif sys.argv[1].lower() == "delete":
        keyword = sys.argv[2]
        if keyword in mcbShelf:
            del mcbShelf[keyword]
            pyperclip.copy(f"{keyword} deleted.")
        else:
            pyperclip.copy(f"{keyword} not found.")
    elif sys.argv[1].lower() == "search":
        keyword = sys.argv[2]
        if keyword in mcbShelf:
            content = mcbShelf[keyword]
            snippet = content[:50]  # Adjust the length of the snippet as needed
            pyperclip.copy(f'Snippet for "{keyword}": {snippet}')
        else:
            pyperclip.copy(f"{keyword} not found.")
    elif sys.argv[1].lower() == "backup":
        backup_file = os.path.join(backup_dir, "mcb_backup.db")
        shutil.copy("mcb.dat", backup_file)
        pyperclip.copy(f"Backup created at: {backup_file}")
    elif sys.argv[1].lower() == "restore":
        backup_file = os.path.join(backup_dir, "mcb_backup.db")
        if os.path.exists(backup_file):
            shutil.copy(backup_file, "mcb.dat")
            pyperclip
