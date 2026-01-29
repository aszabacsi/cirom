import inspect

def print_callstack():
  print("Call stack (most recent first):")
    for i, fi in enumerate(inspect.stack()):
        frame = fi.frame
        locals_snapshot = {
            k: frame.f_locals.get(k)
            for k in ("source", "auxiliary", "target", "num_disks")
            if k in frame.f_locals
        }
        print(
            f"#{i} {fi.function} at {fi.filename}:{fi.lineno} locals={locals_snapshot}"
        )
    print("---")
