from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletaAgendadbsettingsbefit(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute(f"SELECT DataAgendamento,Observacao,CentroLocal FROM agendaweb")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('BeFit - Settings')
        report.start_artifact_report(report_folder, 'BeFit - Dúvidas do Atleta')
        report.add_script()
        data_headers = ('Data', 'Descrição da dúvida', 'Centro')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('BeFit - Atleta Settings data available in report under "BeFit - Dúvidas do Atleta"')
    else:
        logfunc('No NF - Dúvidas do atleta available')

__artifacts__ = {
    "BeFitAtletaAgenda": (
        "App1_BeFit",
        ('*/data/data/pt.proinf.myhcgym.befit/databases/myhcgym1.db'),
        get_gymAtletaAgendadbsettingsbefit)
}
