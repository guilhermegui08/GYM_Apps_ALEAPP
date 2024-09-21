#Get DB Settings from GymApp

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, kmlgen, is_platform_windows, open_sqlite_db_readonly, convert_utc_human_to_timezone


import base64
import rncryptor
import binascii

def decrypt_data(encrypted_data, password):
    try:
        decoded_data = base64.b64decode(encrypted_data)
        decrypted_data = rncryptor.decrypt(decoded_data, password)
        return decrypted_data
    except (rncryptor.DecryptionError, binascii.Error) as e:
        return f"Error: {e}"


def get_gymdbsettingsencGHCGinasios(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    keys = ('codClienteHC', 'codEntFromSettings', 'mailCliente')
    placeholders = ','.join(['?'] * len(keys))
    cursor.execute(f"SELECT key, Value, HoraSinc FROM tbl_settings WHERE key IN ({placeholders})", keys)
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('GHCGinasios')
        report.start_artifact_report(report_folder, 'GHCGinasios - Settings cifrados')
        report.add_script()

        data_headers = ('Key', 'Valor cifrado', 'Valor decifrado', 'Hora')

        decrypted_rows = []
        for row in all_rows:
            key, encrypted_value, hora_sinc = row
            if key == 'session':
                decrypted_value = encrypted_value
            else:
                decrypted_value = decrypt_data(encrypted_value, '178!819?000!226@184)087&161$196/616')
            decrypted_rows.append((key, encrypted_value, decrypted_value, hora_sinc))

        report.write_artifact_data_table(data_headers, decrypted_rows, files_found[0])
        report.end_artifact_report()
        logfunc('GHCGinasios - Encrypted Settings data available in report under "GHCGinasios - Settings Encrypted"')
    else:
        logfunc('No GHCGinasios - Encrypted Settings data available')


__artifacts__ = {
    "GHCGinasiosSettingsEncrypted": (
        "App2_GHCGinasios",
        ('*/data/data/pt.proinf.myhcgym.ghcginasios/databases/settings.db'),
        get_gymdbsettingsencGHCGinasios)
}
