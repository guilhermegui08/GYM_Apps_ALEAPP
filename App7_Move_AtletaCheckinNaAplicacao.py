from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbcheckinMove(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT DataCheckin,DataHoraFim,CentroLocal  FROM checkin")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('Move - Settings')
        report.start_artifact_report(report_folder, 'Move - Atleta checkin')
        report.add_script()
        data_headers = ('Data de Entrada', 'Data de Saida', 'Centro')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('Move - Atleta checkin data available in report under "Move - Atleta checkin"')
    else:
        logfunc('No Move - Atleta checkin data available')

__artifacts__ = {
    "MoveCheckin": (
        "App7_Move",
        ('*/data/data/pt.proinf.myhcgym.move/databases/myhcgym.db'),
        get_gymAtletadbcheckinMove)
}
