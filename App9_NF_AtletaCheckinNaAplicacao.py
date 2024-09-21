from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbcheckinnf(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT DataCheckin,DataHoraFim,CentroLocal  FROM checkin")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('NF - Settings')
        report.start_artifact_report(report_folder, 'NF - Atleta checkin')
        report.add_script()
        data_headers = ('Data de Entrada', 'Data de Saida', 'Centro')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('NF - Atleta checkin data available in report under "NF - Atleta checkin"')
    else:
        logfunc('No NF - Atleta checkin data available')

__artifacts__ = {
    "NFCheckin": (
        "App9_NF",
        ('*/data/data/pt.proinf.myhcgym.nf/databases/myhcgym.db'),
        get_gymAtletadbcheckinnf)
}
