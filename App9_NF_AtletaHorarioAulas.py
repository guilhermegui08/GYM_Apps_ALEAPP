from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbgrelhahorarianf(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT Salas_NomeSala,CCAulas_NomeAula,CCAulas_DescricaoAula,Users_Nome  FROM cc_grelhahoraria")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('NF - Settings')
        report.start_artifact_report(report_folder, 'NF - Horários de aulas')
        report.add_script()
        data_headers = ('Nome da Sala', 'Nome da aula', 'Descrição da aula', 'Nome do professor')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('NF - Grelha horária data available in report under "NF - Grelha horária"')
    else:
        logfunc('No NF - Grelha horária de aulas data available')

__artifacts__ = {
    "NFGrelhahoraria": (
        "App9_NF",
        ('*/data/data/pt.proinf.myhcgym.nf/databases/myhcgym.db'),
        get_gymAtletadbgrelhahorarianf)
}
