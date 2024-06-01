from dbcontext_database import DatabaseContext
from dbcontext_reportlogs import ReportLogsContext

dbc = DatabaseContext()
rlc = ReportLogsContext()
dbc.reset_and_populate()