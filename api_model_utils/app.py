import os
from contextlib import nullcontext

import yappi
from pyinstrument import Profiler


class ManagerProfile:
    @classmethod
    def factory(cls, type_input_data: str):
        """Apply factory pattern design"""
        switch_case = {
            "pyinstrument": ManagerProfilePyinstrument(),
            "yappi": ManagerProfileYappi(),
        }
        msg = (
            f"{cls.__class__.__qualname__}: 'type_input_data' is not a "
            f"valid value. Allowed values: {switch_case.keys()}"
        )
        parser = switch_case.get(type_input_data, msg)
        if parser == msg:
            raise ValueError(msg)
        return parser

    @staticmethod
    def _prepare_output_path(path_profile: str, filename: str):
        if not os.path.exists(path_profile):
            path_profile = os.path.join(os.getcwd(), "output")

            if not os.path.exists(path_profile):
                os.makedirs(path_profile)

        output_path = os.path.join(path_profile, filename)

        return output_path


class ManagerProfilePyinstrument(ManagerProfile):
    def __init__(self):
        self.profiler = Profiler()

    def start(self):
        self.profiler.start()
        return nullcontext()

    def stop_and_write(self, path_profile: str, is_docker: bool, sync: bool):
        self.profiler.stop()
        filename = (
            "pyinstrument_profile_sync.html"
            if sync
            else "pyinstrument_profile_async.html"
        )
        if not is_docker:
            output_html = self.profiler.output_html()
            self._write_output_file(path_profile, output_html, filename=filename)

        print(self.profiler.output_text(unicode=True, color=True))

    def _write_output_file(self, path_profile: str, output_html: str, filename: str):
        output_html_path = self._prepare_output_path(path_profile, filename)
        with open(output_html_path, "w") as file:
            file.write(output_html)


class ManagerProfileYappi(ManagerProfile):
    @staticmethod
    def start():
        yappi.set_clock_type("WALL")
        context_manager = yappi.run()
        return context_manager

    def stop_and_write(self, path_profile: str, is_docker: bool, sync: bool):
        stats = yappi.get_func_stats()
        filename = "yappi_profile_sync.html" if sync else "yappi_profile_async.html"
        if not is_docker:
            self._write_output_file(path_profile, stats, filename=filename)
        stats.print_all()

    def _write_output_file(self, path_profile: str, stats, filename: str):
        output_txt_path = self._prepare_output_path(path_profile, filename)
        with open(output_txt_path, "w") as file:
            stats.print_all(out=file)
