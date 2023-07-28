from .__init__ import CMD_RESULT_FAILED, CMD_RESULT_OK
from unidbg.context import Context
from unidbg.util import parse_init_script
from unidbg.util.cmd_parser import Command, join_args


def cmd_hook_block(ctx: Context, cmd: Command) -> (int, str):
    address, err = cmd.get_addr_arg("addr", 0, -1)
    if err is not None:
        return CMD_RESULT_FAILED, err

    subcommand = cmd.get_subcommand_arg("subcommand", 1, None)
    if err is not None:
        return CMD_RESULT_FAILED, err

    ctx.executor.add_block_hook(address, subcommand)
    if err is not None:
        return CMD_RESULT_FAILED, err
    address_s = ctx.arch.format_address(address)
    print("hook block at %s" % address_s)
    return CMD_RESULT_OK, None


def cmd_hook_code(ctx: Context, cmd: Command) -> (int, str):
    address, err = cmd.get_addr_arg("addr", 0, -1)
    if err is not None:
        return CMD_RESULT_FAILED, err

    subcommand = cmd.get_subcommand_arg("subcommand", 1, None)
    if err is not None:
        return CMD_RESULT_FAILED, err

    ctx.executor.add_code_hook(address, subcommand)
    if err is not None:
        return CMD_RESULT_FAILED, err
    address_s = ctx.arch.format_address(address)
    print("hook code at %s" % address_s)
    return CMD_RESULT_OK, None