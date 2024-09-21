from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbreservaaulasMove(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT DataAula,DataHoraFimAula,nomeAula,NomeSala,Duracao,CentroLocal  FROM ReservaAulas")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('Move - Settings')
        report.start_artifact_report(report_folder, 'Move - Reserva de aulas do atleta')
        report.add_script()
        data_headers = ('Inicio da aula', 'Fim da aula', 'Nome da aula', 'Sala','Duração','Centro')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('Move - Atleta Reserva de aulas data available in report under "Move - Reserva de aulas"')
    else:
        logfunc('No Move - Atleta Reserva de aulas data available')

__artifacts__ = {
    "MoveReservaAulas": (
        "App7_Move",
        ('*/data/data/pt.proinf.myhcgym.move/databases/myhcgym.db'),
        get_gymAtletadbreservaaulasMove)
}
