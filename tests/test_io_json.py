from cbia_workbench.p2_inference.operators.io_json import dump_json, load_json


def test_dump_json_compact(tmp_path):
    path = tmp_path / "out.json"
    data = {"b": 1, "a": 2}

    dump_json(path, data, compact=True)

    assert path.read_text(encoding="utf-8") == '{"b":1,"a":2}\n'
    assert load_json(path) == data
