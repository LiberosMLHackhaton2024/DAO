from mappoints.dbcontext_mappoints import DatabaseContext
from reportlogs.dbcontext_reportlogs import ReportLogsContext

dbc = DatabaseContext()
rlc = ReportLogsContext()
dbc.reset_and_populate()
rlc.reset_and_populate()