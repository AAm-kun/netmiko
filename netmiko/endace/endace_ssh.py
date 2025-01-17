from typing import Optional
from netmiko.cisco_base_connection import CiscoSSHConnection
import re


class EndaceSSH(CiscoSSHConnection):
    def session_preparation(self) -> None:
        self._test_channel_read()
        self.set_base_prompt()
        self.set_terminal_width()
        self.disable_paging(command="no cli session paging enable")

    def enable(
        self,
        cmd: str = "enable",
        pattern: str = "",
        enable_pattern: Optional[str] = None,
        re_flags: int = re.IGNORECASE,
    ) -> str:
        return super().enable(
            cmd=cmd, pattern=pattern, enable_pattern=enable_pattern, re_flags=re_flags
        )

    def check_config_mode(
        self, check_string: str = "(config) #", pattern: str = ""
    ) -> bool:
        return super().check_config_mode(check_string=check_string, pattern=pattern)

    def config_mode(
        self, config_command: str = "conf t", pattern: str = "", re_flags: int = 0
    ) -> str:
        output = ""
        if not self.check_config_mode():
            new_data = self.send_command_timing(
                config_command, strip_command=False, strip_prompt=False
            )
            assert isinstance(new_data, str)
            output += new_data
            if "to enter configuration mode anyway" in output:
                new_data = self.send_command_timing(
                    "YES", strip_command=False, strip_prompt=False
                )
                assert isinstance(new_data, str)
                output += new_data
            if not self.check_config_mode():
                raise ValueError("Failed to enter configuration mode")
        return output

    def exit_config_mode(self, exit_config: str = "exit", pattern: str = "#") -> str:
        return super().exit_config_mode(exit_config=exit_config, pattern=pattern)

    def save_config(
        self,
        cmd: str = "configuration write",
        confirm: bool = False,
        confirm_response: str = "",
    ) -> str:
        self.enable()
        self.config_mode()
        return super().save_config(
            cmd=cmd, confirm=confirm, confirm_response=confirm_response
        )
