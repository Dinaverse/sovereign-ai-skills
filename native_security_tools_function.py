"""
title: Native Security Tools Executor
description: A function that allows Open WebUI to execute local Kali security tools.
author: Dina
"""

import subprocess
import os

class Tools:
    def __init__(self):
        self.allowed_tools = [
            "nmap", "whois", "theHarvester", "shodan", "dnsrecon", "enum4linux",
            "gobuster", "dirb", "ffuf", "wpscan", "nikto", "openvas", "nuclei",
            "msfconsole", "sqlmap", "xsser", "commix", "hydra", "hashcat", "john",
            "medusa", "aircrack-ng", "bettercap", "mimikatz", "bloodhound",
            "impacket", "dradis", "serpico", "shannon"
        ]

    def run_security_tool(self, tool: str, args: str) -> str:
        """
        Executes a security tool on the host machine.
        :param tool: The name of the security tool.
        :param args: The arguments to pass to the tool.
        """
        if tool not in self.allowed_tools:
            return f"Error: Tool '{tool}' is not in the allowed list."

        try:
            # Execute command directly on the host
            result = subprocess.run(
                f"{tool} {args}", 
                shell=True, 
                capture_output=True, 
                text=True
            )
            return result.stdout if result.stdout else result.stderr
        except Exception as e:
            return f"Error executing {tool}: {str(e)}"
