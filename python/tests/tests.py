import sys
sys.path.insert(0,"../")
sys.path.insert(0,"./")

print(sys.path)
import ProcessSegments
def test_import():
    assert not type(ProcessSegments) is None

def test_methods():
    segments = ProcessSegments.process_data()
    assert not type(segments) is None
