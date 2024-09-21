from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbreservaaulasJAFClub(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT DataAula,DataHoraFimAula,nomeAula,NomeSala,Duracao,CentroLocal  FROM ReservaAulas")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('JAFClub - Settings')
        report.start_artifact_report(report_folder, 'JAFClub - Reserva de aulas do atleta')
        report.add_script()
        data_headers = ('Inicio da aula', 'Fim da aula', 'Nome da aula', 'Sala','Duração','Centro')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('JAFClub - Atleta Reserva de aulas data available in report under "JAFClub - Reserva de aulas"')
    else:
        logfunc('No JAFClub - Atleta Reserva de aulas data available')

__artifacts__ = {
    "JAFClubReservaAulas": (
        "App5_JAFClub",
        ('*/data/data/pt.proinf.myhcgym.jafclub/databases/myhcgym.db'),
        get_gymAtletadbreservaaulasJAFClub)
}
