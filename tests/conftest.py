import pytest
from pathlib import Path
import invoice as m

@pytest.fixture
def stock_file(tmp_path: Path):
    p = tmp_path / "stock.txt"
    p.write_text("pencil,0.15,85\nfolder,1.4,40\n")
    return p

@pytest.fixture
def stock(stock_file):
    return m.loadStock(str(stock_file))

@pytest.fixture
def orders_file(tmp_path: Path):
    p = tmp_path / "orders.txt"
    p.write_text("pencil,15,EUR,0.15,2.25,0.0,0.49,2.75\n")
    return p
