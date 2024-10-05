from src.model.model import Model
from src.commands.validations import value_exists_in_dataframes
from src.commands.command_base import CommandArgs, Command
from pydantic.dataclasses import dataclass
from pydantic import model_validator

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.

@dataclass
class ShowColsCommandArgs(CommandArgs):

    model:Model
    alias: str

    @model_validator(mode='after')
    def validate_data_exists(self):
        if not value_exists_in_dataframes(self.model,self.alias):
            raise Exception(f"File {self.alias} not in dataframes")
        return self

    def __repr__(self) -> str:
        return f'Show Cols Command Args: \nalias: {self.alias}'


class ShowColsCommand(Command):

    def execute(self, args: ShowColsCommandArgs):  # type: ignore
        print(args.model.read(args.alias).columns.values)
