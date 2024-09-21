#Get DB Settings from GymApp

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, kmlgen, is_platform_windows, open_sqlite_db_readonly, convert_utc_human_to_timezone


def get_gymdbsettingsHLHealthClub(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    keys = ('appVersionNumber', 'appUpdated', 'externalStoragePath', 'internalStoragePath', 'AndroidID',
            'deviceID', 'GymCodeAppSettings', 'AppID', 'TimeZone', 'servidorWeb',
            'newQRCode','user_name','user_DNasc','user_email', 'user_NumCliente','user_codpin','user_sexo','session')
    placeholders = ','.join(['?'] * len(keys))
    cursor.execute(f"SELECT key, Value, HoraSinc FROM tbl_settings WHERE key IN ({placeholders})", keys)
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('HLHealthClub')
        report.start_artifact_report(report_folder, 'HLHealthClub - Settings')
        report.add_script()
        data_headers = ('Key', 'Value', 'Hora')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('HLHealthClub - Settings data available in report under "HLHealthClub - Settings"')
    else:
        logfunc('No HLHealthClub - Settings data not available')

__artifacts__ = {
    "HLHealthClubSettings": (
        "App4_HLHealthClub",
        ('*/data/data/pt.proinf.myhcgym.hlhealthylife/databases/settings.db'),
        get_gymdbsettingsHLHealthClub)
}