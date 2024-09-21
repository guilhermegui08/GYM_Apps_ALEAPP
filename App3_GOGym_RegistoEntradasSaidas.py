from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbatividadewebGOGym(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT DataHora,DataHoraFim,Descricao,id_RegistoHC  FROM cc_actividadeweb")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('GOGym - Settings')
        report.start_artifact_report(report_folder, 'GOGym - Entradas ou Saídas do ginásio')
        report.add_script()
        data_headers = ('Data Entrada', 'Data Saída', 'Método de entrada', 'ID do registo')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('GOGym - Atividade Web data available in report under "Entradas/Saídas do ginásio"')
    else:
        logfunc('No GOGym - Atividade Web data available')

__artifacts__ = {
    "GOGymAtividadeWeb": (
        "App3_GOGym",
        ('*/data/data/pt.proinf.myhcgym.gogym/databases/myhcgym.db'),
        get_gymAtletadbatividadewebGOGym)
}
