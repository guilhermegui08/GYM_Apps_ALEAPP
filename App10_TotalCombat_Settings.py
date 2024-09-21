#Get DB Settings from GymApp

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, kmlgen, is_platform_windows, open_sqlite_db_readonly, convert_utc_human_to_timezone


def get_gymdbsettingstotalcombat(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    keys = ('appVersionNumber', 'appUpdated', 'externalStoragePath', 'internalStoragePath', 'AndroidID',
            'deviceID', 'GymCodeAppSettings', 'AppID', 'TimeZone', 'servidorWeb',
            'newQRCode','user_name','user_DNasc','user_email', 'user_NumCliente','user_codpin','user_sexo','session')
    placeholders = ','.join(['?'] * len(keys))
    cursor.execute(f"SELECT key, Value, HoraSinc FROM tbl_settings WHERE key IN ({placeholders})", keys)
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('TotalCombat')
        report.start_artifact_report(report_folder, 'TotalCombat - Settings')
        report.add_script()
        data_headers = ('Key', 'Value', 'Hora')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('TotalCombat - Settings data available in report under "TotalCombat - Settings"')
    else:
        logfunc('No TotalCombat - Settings data not available')

__artifacts__ = {
    "TotalCombatSettings": (
        "App10_TotalCombat",
        ('*/data/data/pt.proinf.myhcgym.totalcombat/databases/settings.db'),
        get_gymdbsettingstotalcombat)
}