from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletaAgendadbsettingsGOGym(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute(f"SELECT DataAgendamento,Observacao,CentroLocal FROM agendaweb")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('GOGym - Settings')
        report.start_artifact_report(report_folder, 'GOGym - Dúvidas do Atleta')
        report.add_script()
        data_headers = ('Data', 'Descrição da dúvida', 'Centro')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('GOGym - Atleta Settings data available in report under "GOGym - Dúvidas do Atleta"')
    else:
        logfunc('No GOGym - Dúvidas do atleta available')

__artifacts__ = {
    "GOGymAtletaAgenda": (
        "App3_GOGym",
        ('*/data/data/pt.proinf.myhcgym.gogym/databases/myhcgym.db'),
        get_gymAtletaAgendadbsettingsGOGym)
}
