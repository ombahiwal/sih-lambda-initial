from openvas_lib import VulnscanManager, VulnscanException

try:
    scanner = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
except VulnscanException as e:
    print("Error:")
    print(e)
