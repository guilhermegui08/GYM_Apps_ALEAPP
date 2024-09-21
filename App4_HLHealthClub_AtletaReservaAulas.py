from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbreservaaulasHLHealthClub(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT DataAula,DataHoraFimAula,nomeAula,NomeSala,Duracao,CentroLocal  FROM ReservaAulas")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('HLHealthClub - Settings')
        report.start_artifact_report(report_folder, 'HLHealthClub - Reserva de aulas do atleta')
        report.add_script()
        data_headers = ('Inicio da aula', 'Fim da aula', 'Nome da aula', 'Sala','Duração','Centro')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('HLHealthClub - Atleta Reserva de aulas data available in report under "HLHealthClub - Reserva de aulas"')
    else:
        logfunc('No HLHealthClub - Atleta Reserva de aulas data available')

__artifacts__ = {
    "HLHealthClubReservaAulas": (
        "App4_HLHealthClub",
        ('*/data/data/pt.proinf.myhcgym.hlhealthylife/databases/myhcgym.db'),
        get_gymAtletadbreservaaulasHLHealthClub)
}
