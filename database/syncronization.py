from database.db_manager import DBManager


def synchronization_from_server_to_db(data, parent):
    db_manager = DBManager()
    sorting = data['sorting']
    notes = data['notes']
    labels = data['labels']
    parent.id_labels_sync = {}

    db_manager.update_sorting(sorting)

    for label in labels:
        db_manager.update_label(label, parent)

    for note in notes:
        db_manager.update_note(note, parent)


