import typer

from modules.initialize import initialize
from modules.dataframe import read_settings as rs
from modules.run import run

app = typer.Typer()

@app.command(name="read_settings")
@app.command(name="rs" , hidden=True)
def read_settings(path: str, bit: int = 4, register= True):
    """ExcelファイルからCPUの命令セットを読み取る

    Args:
        path (str): excelファイルのパス
        bit (int, optional): CPUのROMが何ビットで保存されているのか Defaults to 4.
        register (bool, optional): CPUの設定をデータベースに保存するかどうか Defaults to True.
    """
    rs(path, bit, register)

@app.command(name="run")
def run_simulator(name: str, path: str="ROM/ROM.txt", debug: bool=True):
    """CPUシミュレーターを起動する
    """
    run(name, path,debug)

def main():
    initialize()
    app()

if __name__ == "__main__":
    main()
