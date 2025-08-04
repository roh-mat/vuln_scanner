from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp

def run_openvas(target):
    connection = UnixSocketConnection()
    with Gmp(connection) as gmp:
        gmp.authenticate('admin', '28758622-8be3-43b4-80d7-c1c3ffea5217')
        # Create target
        target_id = gmp.create_target(name="scan_target", hosts=target)["id"]
        # Create and start task
        task_id = gmp.create_task(name="MyScan", config_id="daba56c8-73ec-11df-a475-002264764cea", target_id=target_id)["id"]
        gmp.start_task(task_id)
        # Wait for completion (polling or async loop)
