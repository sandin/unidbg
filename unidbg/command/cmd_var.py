from .__init__ import CMD_RESULT_FAILED, CMD_RESULT_OK
from unidbg.context import Context
from unidbg.util.cmd_parser import Command


def cmd_set(ctx: Context, cmd: Command) -> (int, str):
    name, err = cmd.get_str_arg("name", 0, None)
    if err is not None:
        return CMD_RESULT_FAILED, err

    value, err = cmd.get_str_arg("value", 1, None)
    if err is not None:
        return CMD_RESULT_FAILED, err

    ctx.local_vars[name] = value
    print("set %s = %s" % (name, value))
    return CMD_RESULT_OK, None


def cmd_unset(ctx: Context, cmd: Command) -> (int, str):
    name, err = cmd.get_str_arg("name", 0, None)
    if err is not None:
        return CMD_RESULT_FAILED, err

    if name not in ctx.local_vars:
        return CMD_RESULT_FAILED, "%s is undefined" % name

    value = ctx.local_vars[name]
    del ctx.local_vars[name]
    print("unset %s(%s)" % (name, value))
    return CMD_RESULT_OK, None
