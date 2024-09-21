from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbcheckinJAFClub(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT DataCheckin,DataHoraFim,CentroLocal  FROM checkin")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('JAFClub - Settings')
        report.start_artifact_report(report_folder, 'JAFClub - Atleta checkin')
        report.add_script()
        data_headers = ('Data de Entrada', 'Data de Saida', 'Centro')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('JAFClub - Atleta checkin data available in report under "JAFClub - Atleta checkin"')
    else:
        logfunc('No JAFClub - Atleta checkin data available')

__artifacts__ = {
    "JAFClubCheckin": (
        "App5_JAFClub",
        ('*/data/data/pt.proinf.myhcgym.jafclub/databases/myhcgym.db'),
        get_gymAtletadbcheckinJAFClub)
}
