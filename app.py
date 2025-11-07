from __future__ import annotations

import io
import tempfile
from pathlib import Path
from typing import Iterable, Dict, Any

from flask import Flask, render_template, request, send_file, redirect, url_for, flash

try:
    from converter.formats import (
        load_json,
        dump_json,
        load_yaml,
        dump_yaml,
        load_csv,
        dump_csv,
        load_xlsx_from_path,
        dump_xlsx_to_path,
    )
except ModuleNotFoundError:
    # Allow running as a script: python web/app.py
    # Add project root to sys.path then import
    import sys as _sys
    from pathlib import Path as _Path

    _sys.path.append(str(_Path(__file__).resolve().parents[1]))
    from converter.formats import (  # type: ignore
    load_json,
    dump_json,
    load_yaml,
    dump_yaml,
    load_csv,
    dump_csv,
    load_xlsx_from_path,
    dump_xlsx_to_path,
    )


app = Flask(__name__)
app.secret_key = "dev-secret"


SUPPORTED_INPUTS = {".json", ".yaml", ".yml", ".csv", ".xlsx"}
SUPPORTED_OUTPUTS = {".json", ".yaml", ".yml", ".csv", ".xlsx"}


def _load_data_from_upload(filename: str, content: bytes) -> Any:
    suffix = Path(filename).suffix.lower()
    text = None
    if suffix == ".json":
        text = content.decode("utf-8")
        return load_json(text)
    if suffix in {".yaml", ".yml"}:
        text = content.decode("utf-8")
        return load_yaml(text)
    if suffix == ".csv":
        text = content.decode("utf-8")
        return load_csv(text)
    if suffix == ".xlsx":
        with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=True) as tmp:
            tmp.write(content)
            tmp.flush()
            return load_xlsx_from_path(Path(tmp.name))
    raise ValueError(f"Unsupported input format: {suffix}")


def _serialize_to_target(data: Any, target_suffix: str) -> tuple[io.BytesIO, str]:
    target_suffix = target_suffix.lower()
    if target_suffix == ".json":
        text = dump_json(data, pretty=True)
        return io.BytesIO(text.encode("utf-8")), "application/json"
    if target_suffix in {".yaml", ".yml"}:
        text = dump_yaml(data)
        return io.BytesIO(text.encode("utf-8")), "application/x-yaml"
    if target_suffix == ".csv":
        if isinstance(data, dict):
            data = [data]
        text = dump_csv(data)  # type: ignore[arg-type]
        return io.BytesIO(text.encode("utf-8")), "text/csv"
    if target_suffix == ".xlsx":
        if isinstance(data, dict):
            data = [data]
        with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        try:
            dump_xlsx_to_path(data, tmp_path)  # type: ignore[arg-type]
            buf = io.BytesIO(tmp_path.read_bytes())
            return buf, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        finally:
            try:
                tmp_path.unlink(missing_ok=True)
            except Exception:
                pass
    raise ValueError(f"Unsupported output format: {target_suffix}")


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/convert")
def convert():
    file = request.files.get("file")
    target = request.form.get("target")
    if not file or not file.filename:
        flash("Please choose a file to upload.", "error")
        return redirect(url_for("index"))
    if not target:
        flash("Please select a target format.", "error")
        return redirect(url_for("index"))

    try:
        data = _load_data_from_upload(file.filename, file.read())
        buf, mime = _serialize_to_target(data, target)
        src_name = Path(file.filename).stem
        out_name = f"{src_name}{target}"
        buf.seek(0)
        return send_file(buf, as_attachment=True, download_name=out_name, mimetype=mime)
    except Exception as exc:  # noqa: BLE001
        flash(str(exc), "error")
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


