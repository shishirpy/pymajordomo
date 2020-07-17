import pytest
from majordomo.pymajordomo.mdcliapi import MajorDomoClient
from majordomo.pymajordomo.mdwrkapi import MajorDomoWorker


def test_client(monkeypatch):
    def mockreturn(*args):
        return [b"4"]

    monkeypatch.setattr(MajorDomoClient, "send", mockreturn)

    client = MajorDomoClient("ipc://test")
    reply = client.send(b"square", "2".encode())

    assert reply[0].decode() == "4"
        

def test_worker(monkeypatch):
    def mockreturn(*args):
        return [b"2"]

    monkeypatch.setattr(MajorDomoWorker, "recv", mockreturn)

    worker = MajorDomoWorker("ipc://test11", "square", False)
    reply = None
    request = worker.recv(reply)
    assert request[0].decode() == "2"