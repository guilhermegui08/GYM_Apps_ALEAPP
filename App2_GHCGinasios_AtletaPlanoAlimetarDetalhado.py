from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, open_sqlite_db_readonly


def get_gymAtletadbplanoalimentarGHCGinasios(files_found, report_folder, seeker, wrap_text, time_offset):
    db = open_sqlite_db_readonly(files_found[0])
    cursor = db.cursor()
    cursor.execute("SELECT RefPADesc,TxtPA,kCal,HoraSincLinha  FROM PlanoAlimentarLinhas")
    all_rows = cursor.fetchall()
    if len(all_rows) > 0:
        report = ArtifactHtmlReport('GHCGinasios - Settings')
        report.start_artifact_report(report_folder, 'GHCGinasios - Plano alimentar detalhado do atleta')
        report.add_script()
        data_headers = ('Refeição', 'Descrição', 'kCal', 'Hora')
        report.write_artifact_data_table(data_headers, all_rows, files_found[0])
        report.end_artifact_report()
        logfunc('GHCGinasios - Atleta plano alimentar data available in report under "GHCGinasios - plano alimentar detalhado"')
    else:
        logfunc('No GHCGinasios - Atleta plano alimentar detalhado data available')

__artifacts__ = {
    "GHCGinasiosPlanoAlimentarDetalhado": (
        "App2_GHCGinasios",
        ('*/data/data/pt.proinf.myhcgym.ghcginasios/databases/myhcgym.db'),
        get_gymAtletadbplanoalimentarGHCGinasios)
}
