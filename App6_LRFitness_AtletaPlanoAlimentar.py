from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbplanoalimentardetalhadoLRFitness(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT NomePA,ObsPA,NomeTecnico,HoraSincCab  FROM PlanoAlimentarCab")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('LRFitness - Settings')
        report.start_artifact_report(report_folder, 'LRFitness - Plano alimentar do atleta')
        report.add_script()
        data_headers = ('Nome do plano alimentar', 'Observações', 'Nutricionista', 'Hora')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('LRFitness - Atleta plano alimentar data available in report under "LRFitness - Plano alimentar"')
    else:
        logfunc('No LRFitness - Atleta plano alimentar data available')

__artifacts__ = {
    "LRFitnessPlanoAlimentar": (
        "App6_LRFitness",
        ('*/data/data/pt.proinf.myhcgym.lrfitness/databases/myhcgym.db'),
        get_gymAtletadbplanoalimentardetalhadoLRFitness)
}
