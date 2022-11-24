# Decorate a method in a class and still access self:

def track_runtime(func: Callable[..., None]) -> Callable[..., None]:
    def wrapper(self, *args, **kwargs) -> None:  # type: ignore
        before = time.time()
        func(self, *args, **kwargs)
        runtime = time.time() - before
        key = f"outer.{func.__name__}"
        self.runtime_stats.append(f"{key} {runtime}")
    return wrapper

  
class Sample:
    runtime_stats =[]

    @track_runtime
    def begin_check(self):
        pass
      
# -------------------------------------------------------------
