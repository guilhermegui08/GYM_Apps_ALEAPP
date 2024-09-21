from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbsettingsbefit(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute(f"SELECT NomeFuncao,Valor,CentroLocal,HoraSinc FROM atletas_settings")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('BeFit - Settings')
        report.start_artifact_report(report_folder, 'BeFit - Atleta Settings')
        report.add_script()
        data_headers = ('Ação', 'Valor', 'Centro','Data')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('BeFit - Atleta Settings data available in report under "BeFit - Settings"')
    else:
        logfunc('No BeFit - Atleta Settings data available')

__artifacts__ = {
    "BeFitAtleta": (
        "App1_BeFit",
        ('*/data/data/pt.proinf.myhcgym.befit/databases/myhcgym1.db'),
        get_gymAtletadbsettingsbefit)
}
