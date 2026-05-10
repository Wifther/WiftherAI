import subprocess
import json

tests = [
    ("MutableDefaultArg_list",  {"file": "t.py", "source": "def f(x=[]):\n    return x"}),
    ("MutableDefaultArg_dict",  {"file": "t.py", "source": "def g(opts={}):\n    return opts"}),
    ("BareExceptPass",          {"file": "t.py", "source": "try:\n    x()\nexcept:\n    pass"}),
    ("HardcodedSecret_pass",    {"file": "t.py", "source": 'db_host = "localhost"\npassword = "hunter2"\n'}),
    ("HardcodedSecret_api",     {"file": "t.py", "source": 'api_key = "sk-1234abcd"\n'}),
    ("DangerousEval",           {"file": "t.py", "source": "eval('print(123)')\n"}),
    ("MultiPattern",            {"file": "t.py", "source": 'def f(x=[]):\n    try:\n        pass\n    except:\n        pass\npassword = "bad"\n'}),
    ("CleanCode",               {"file": "t.py", "source": "def add(a, b):\n    return a + b\n"}),
]

all_pass = True
for name, inp in tests:
    r = subprocess.run(
        ["python", "C:/Users/Jenik/Desktop/WiftherAI/wifther.py"],
        input=json.dumps(inp), text=True, capture_output=True
    )
    if r.returncode != 0:
        print(f"FAIL {name}: exit {r.returncode} stderr={r.stderr[:80]}")
        all_pass = False
        continue
    out = json.loads(r.stdout)
    types = [f["type"] for f in out["findings"]]
    recs = [f.get("recommendation", "N/A") for f in out["findings"]]
    print(f"{'OK' if out['status']=='completed' else 'FAIL'} {name}: {out['bug_count']} bug(s) {types}")
    if out["bug_count"] > 0:
        print(f"  Fixes: {recs}")

print("\nAll tests passed!" if all_pass else "\nSome tests FAILED")
