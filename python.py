# ---------- Description Notes ----------------
# Callables are Covariant in their returns, but Contravariant in their parameters.
# https://mypy-play.net/?mypy=latest&python=3.11&gist=b9a1485fd8a0f6ea920f579e30ed77ee
#
# Pylint
# Ways to ignore for block or function:
# https://pylint.readthedocs.io/en/latest/user_guide/messages/message_control.html
# pylint: disable=unbalanced-tuple-unpacking
#
# Mock Gotchas:
# https://alexmarandon.com/articles/python_mock_gotchas/

# DECORATE -------------------------------------------------------------

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
    
# MOCK -------------------------------------------------------------

# Mock a context manager - Here a sock connection returns a mocked socket

@mock.patch("socket.create_connection")
def test_socket_mocking(con):
    mock_socket = mock.Mock()
    mock_socket.id = "sock"
    con.return_value.__enter__.return_value = mock_socket
    # Do something
    assert "data" in mock_socket.sendall.call_args_list[0].args[0]

# Mock multiple calls at once:
with (patch("base.someView", mock_tiny_feed),patch("base.otherView", mock_feed)):
    
# Create a Mock that you can call str() on:
Mock(Name=str('my name'), __str__=lambda self: self.Name)

# Mock a method that is imported directly by other lib that you are testing.
import lib.sublib as testmodule
@patch(f"{testmodule.__name__}.method_name", autospec=True)
@patch(f"{testmodule.__name__}.closest_first", autospec=True)
def test_rate_break_report_email(closest_first, method_name):
    # Override using either one of these:
    method_name.return_value = 'To return when called '
    method_name.side_effect = Exception("i am raised when called")
    
    testmodule.do_main_work_that_calls_method_name()
    assert method_name.called
    
# Mock a method used in same file as testing:
# Must import the module to the current namespace like this:
from something import modulename

def test_thing():
    with(mock.patch("something.modulename.class_or_func", mock.Mock())):
        call_thing()

# PYTEST -------------------------------------------------------------   
# Pytest run and see DEBUG logs:
# pytest -o log_cli=true --log-cli-level=DEBUG 
# Global setup / teardown methods:
# https://stackoverflow.com/questions/17801300/how-to-run-a-method-before-all-tests-in-all-classes

# PDB -------------------------------------------------------------   
# Add breakpoint at runtime:
# b <linenumber> (current file)
# b <full_file_path>:<linenumber>
