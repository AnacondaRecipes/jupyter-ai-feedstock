import subprocess, sys, re

def get_output(command):
    out = subprocess.check_output(
        [sys.executable, '-m'] + command,
        stderr=subprocess.STDOUT
    ).decode()
    # strip ANSI color codes
    return re.sub(r'\x1b\[[0-9;]*m', '', out)

# check server extensions
server_out = get_output(['jupyter', 'server', 'extension', 'list'])
server_extensions = [
    'jupyter_ai_acp_client',
    'jupyter_ai_chat_commands',
    'jupyter_ai_persona_manager',
    'jupyter_ai_router',
    'jupyter_ai_tools',
    'jupyter_server_documents',
    'jupyter_server_mcp',
    'jupyterlab',
    'jupyterlab_chat',
    'jupyterlab_commands_toolkit',
]
for ext in server_extensions:
    assert ext in server_out and 'OK' in server_out, f'{ext} not found or not OK'
    print(f'OK: {ext}')

# check frontend extensions
lab_out = get_output(['jupyter', 'labextension', 'list'])
lab_extensions = [
    'jupyterlab-notebook-awareness',
]
for ext in lab_extensions:
    assert ext in lab_out and 'enabled OK' in lab_out, f'{ext} not found or not enabled'
    print(f'OK: {ext}')