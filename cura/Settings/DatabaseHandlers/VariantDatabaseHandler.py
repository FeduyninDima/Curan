from UM.Settings.SQLQueryFactory import SQLQueryFactory
from UM.Settings.DatabaseContainerMetadataController import DatabaseMetadataContainerController
from UM.Settings.InstanceContainer import InstanceContainer


class VariantDatabaseHandler(DatabaseMetadataContainerController):
    """The Database handler for Variant containers"""

    def __init__(self):
        super().__init__(SQLQueryFactory(table = "variants",
                                         fields = {
                                             "id": "text",
                                             "name": "text",
                                             "hardware_type": "text",
                                             "definition": "text",
                                             "version": "text",
                                             "setting_version": "text"
                                         }))
        self.container_type = InstanceContainer
