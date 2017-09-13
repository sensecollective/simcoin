from unittest import TestCase
from systemmonitor import CpuTimeSnapshot
from systemmonitor import MemorySnapshot


class TestBash(TestCase):

    def test_cpu_time_snapshot_from_bash(self):
        cpu_time = 'cpu  6993159 247853 1473357 6905504 50921 0 102406 0 0 0'

        snapshot = CpuTimeSnapshot.from_bash(cpu_time)

        self.assertEqual(snapshot.cpu_user, '6993159')
        self.assertEqual(snapshot.cpu_nice, '247853')
        self.assertEqual(snapshot.cpu_system, '1473357')
        self.assertEqual(snapshot.cpu_idle, '6905504')

    def test_memory_snapshot_from_bash(self):
        memory = 'MemTotal:        7577060 kB\nMemFree:         1568016 kB'

        snapshot = MemorySnapshot.from_bash(memory)

        self.assertEqual(snapshot.total_memory, '7577060')
        self.assertEqual(snapshot.free_memory, '1568016')
