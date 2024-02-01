from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    '''
    Defines types for ingestion valiables imported from text-summarizer/config/config.yaml
    '''
    root_dir: Path # variable from config.yaml
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    '''
    Defines types for validation valiables imported from text-summarizer/config/config.yaml
    '''
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list