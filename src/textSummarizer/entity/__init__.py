from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    '''
    Controls entity
    '''
    root_dir: Path # variable from config.yaml
    source_URL: str
    local_data_file: Path
    unzip_dir: Path