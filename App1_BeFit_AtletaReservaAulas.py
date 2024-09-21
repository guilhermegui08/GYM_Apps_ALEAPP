from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbreservaaulasbefit(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT DataAula,DataHoraFimAula,nomeAula,NomeSala,Duracao,CentroLocal  FROM ReservaAulas")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('BeFit - Settings')
        report.start_artifact_report(report_folder, 'BeFit - Reserva de aulas do atleta')
        report.add_script()
        data_headers = ('Inicio da aula', 'Fim da aula', 'Nome da aula', 'Sala','Duração','Centro')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('BeFit - Atleta Reserva de aulas data available in report under "BeFit - Reserva de aulas"')
    else:
        logfunc('No BeFit - Atleta Reserva de aulas data available')

__artifacts__ = {
    "BeFitReservaAulas": (
        "App1_BeFit",
        ('*/data/data/pt.proinf.myhcgym.befit/databases/myhcgym1.db'),
        get_gymAtletadbreservaaulasbefit)
}
