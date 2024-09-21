from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbavaliacoesHLHealthClub(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT DataAvaliacao,NomeProf,Observacao,Idade,Altura,Peso,PesoRef,NomeFormula,Resultado  FROM avaliacoes")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('HLHealthClub - Settings')
        report.start_artifact_report(report_folder, 'HLHealthClub - Avaliações do atleta')
        report.add_script()
        data_headers = ('Data', 'Nome Professor', 'Observação', 'Idade','Altura','Peso','Peso ideal','Medição','Resultado')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('HLHealthClub - Atleta Avaliações data available in report under "HLHealthClub - Avaliações"')
    else:
        logfunc('No HLHealthClub - Atleta Avaliações data available')

__artifacts__ = {
    "HLHealthClubAvaliacoes": (
        "App4_HLHealthClub",
        ('*/data/data/pt.proinf.myhcgym.hlhealthylife/databases/myhcgym.db'),
        get_gymAtletadbavaliacoesHLHealthClub)
}
