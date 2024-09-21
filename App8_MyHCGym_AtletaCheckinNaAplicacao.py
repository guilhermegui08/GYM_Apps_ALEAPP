from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbcheckinMyHCGym(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT DataCheckin,DataHoraFim,CentroLocal  FROM checkin")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('MyHCGym - Settings')
        report.start_artifact_report(report_folder, 'MyHCGym - Atleta checkin')
        report.add_script()
        data_headers = ('Data de Entrada', 'Data de Saida', 'Centro')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('MyHCGym - Atleta checkin data available in report under "MyHCGym - Atleta checkin"')
    else:
        logfunc('No MyHCGym - Atleta checkin data available')

__artifacts__ = {
    "MyHCGymCheckin": (
        "App8_MyHCGym",
        ('*/data/data/pt.proinf.myhcgym.myhcgym/databases/myhcgym.db'),
        get_gymAtletadbcheckinMyHCGym)
}
