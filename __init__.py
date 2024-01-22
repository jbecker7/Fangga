from aqt.gui_hooks import editor_did_init_shortcuts
from .transcription_utils import romanizationToManchu, manchuToRomanization


def transcribe_fields(editor):
    """Transcribe Manchu to Romanization or Romanization to Manchu based on which field is empty"""
    if "Manchu" in editor.note and "Romanization" in editor.note:
        if editor.note["Manchu"]:
            editor.note["Romanization"] = (
                manchuToRomanization(editor.note["Manchu"])
            ).lower()
        elif editor.note["Romanization"]:
            editor.note["Manchu"] = romanizationToManchu(editor.note["Romanization"])
        editor.loadNote()


def add_shortcut(shortcuts, editor):
    shortcut = ("Ctrl+Shift+X", lambda: transcribe_fields(editor))
    shortcuts.append(shortcut)


editor_did_init_shortcuts.append(add_shortcut)
