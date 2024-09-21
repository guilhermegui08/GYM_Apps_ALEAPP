from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbgrelhahorariabefit(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT Salas_NomeSala,CCAulas_NomeAula,CCAulas_DescricaoAula,Users_Nome  FROM cc_grelhahoraria")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('BeFit - Settings')
        report.start_artifact_report(report_folder, 'BeFit - Horários de aulas')
        report.add_script()
        data_headers = ('Nome da Sala', 'Nome da aula', 'Descrição da aula', 'Nome do professor')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('BeFit - Grelha horária data available in report under "BeFit - Grelha horária"')
    else:
        logfunc('No BeFit - Grelha horária de aulas data available')

__artifacts__ = {
    "BeFitGrelhahoraria": (
        "App1_BeFit",
        ('*/data/data/pt.proinf.myhcgym.befit/databases/myhcgym1.db'),
        get_gymAtletadbgrelhahorariabefit)
}
