import logging

from ruxit.api.base_plugin import BasePlugin

log = logging.getLogger(__name__)


class BasicPlugin(BasePlugin):

    def query(self, **kwargs) -> None:
        pass




