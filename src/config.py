from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

ARTIFACTS_DIR = BASE_DIR / "artifacts"

MODEL_PATH = ARTIFACTS_DIR / "catboost_model.pkl"

PREPROCESSOR_PATH = ARTIFACTS_DIR / "preprocessor.pkl"

THRESHOLD_PATH = ARTIFACTS_DIR / "threshold.pkl"