from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbgrelhahorariaHLHealthClub(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT Salas_NomeSala,CCAulas_NomeAula,CCAulas_DescricaoAula,Users_Nome  FROM cc_grelhahoraria")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('HLHealthClub - Settings')
        report.start_artifact_report(report_folder, 'HLHealthClub - Horários de aulas')
        report.add_script()
        data_headers = ('Nome da Sala', 'Nome da aula', 'Descrição da aula', 'Nome do professor')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('HLHealthClub - Grelha horária data available in report under "HLHealthClub - Grelha horária"')
    else:
        logfunc('No HLHealthClub - Grelha horária de aulas data available')

__artifacts__ = {
    "HLHealthClubGrelhahoraria": (
        "App4_HLHealthClub",
        ('*/data/data/pt.proinf.myhcgym.hlhealthylife/databases/myhcgym.db'),
        get_gymAtletadbgrelhahorariaHLHealthClub)
}
