from dataclasses import dataclass #used  for decorators

@dataclass
class DataIngestionArtifact:
  trained_file_path:str
  test_file_path:str



