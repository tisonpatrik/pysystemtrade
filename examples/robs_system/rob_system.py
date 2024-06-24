from systems.provided.rob_system.run_system import futures_system
from sysdata.sim.csv_futures_sim_data import csvFuturesSimData

my_data = csvFuturesSimData()

system = futures_system(sim_data=my_data)
system.accounts.portfolio().sharpe()