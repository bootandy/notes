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

# Mock a context manager - Here a sock connection returns a mocked socket
@mock.patch("socket.create_connection")
def test_socket_mocking(con):
    mock_socket = mock.Mock()
    mock_socket.id = "sock"
    con.return_value.__enter__.return_value = mock_socket

    
# Mock a method that is imported directly by other lib that you are testing.
import lib.sublib as testmodule

@patch(f"{testmodule.__name__}.method_name", autospec=True)
def test_rate_break_report_email(method_name,):
    assert method_name.called
    
    