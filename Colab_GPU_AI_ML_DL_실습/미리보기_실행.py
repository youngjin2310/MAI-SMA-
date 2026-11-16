"""Run the Colab notebook cells locally and write five CPU-preview figures."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
notebook = root / "Colab_GPU_AI_ML_DL_실습.ipynb"
doc = json.loads(notebook.read_text(encoding="utf-8"))
scope = {"__name__": "__main__"}
for index, cell in enumerate(doc["cells"]):
    if cell["cell_type"] == "code":
        print(f"\n--- Code cell {index + 1} ---", flush=True)
        exec("".join(cell["source"]), scope)
print("\n완료: 그래프 5장과 ZIP 파일을 만들었습니다.")
