import os.path
import sys
from prompt_toolkit import prompt

from .__init__ import __version__
from .command import CMD_RESULT_EXIT
from .command.cmd_exit import cmd_exit
from .command.cmd_help import cmd_help
from .command.cmd_load import cmd_load
from .command.cmd_mem import cmd_mem_list, cmd_mem_read
from .common.context import Context
from .util import register_cmd, parse_init_script
from .util.args_parser import parse_arg

g_all_commands = {}
register_cmd(g_all_commands, "exit", ".exit", "exit()", "e", handler=cmd_exit)
register_cmd(g_all_commands, "help", "h", handler=cmd_help)
register_cmd(g_all_commands, "load", "l", handler=cmd_load)
register_cmd(g_all_commands, "mem_list",  "ml", handler=cmd_mem_list)
register_cmd(g_all_commands, "mem_read",  "mr", handler=cmd_mem_read)


def main():
    print('UniDbg %s' % __version__)
    print('Type "help" for more information.')

    init_cmds = []
    if len(sys.argv) >= 2:
        init_script = sys.argv[1]
        if not os.path.exists(init_script):
            print("warning: %s init script file is not exists")
        init_cmds += parse_init_script(init_script)
        print("load init script file `%s`" % init_script)

    context = Context()
    while True:
        if len(init_cmds) > 0:
            line = init_cmds[0]
            del init_cmds[0]
            print(">>> %s" % line)
        else:
            line = prompt('>>> ')
        cmd, sub_args = parse_arg(line)
        if cmd in g_all_commands:
            ret = g_all_commands[cmd](context, sub_args)
            if ret == CMD_RESULT_EXIT:
                break
        else:
            print("unsupported command: `%s`" % line)
