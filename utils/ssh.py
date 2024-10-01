import paramiko


def ssh_connect(username: str, password: str, ip: str, port: int):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)
    return ssh


def ssh_command(ssh, command: str):
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdout.read().decode()