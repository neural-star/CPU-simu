import json
from typing import Any
from rich.progress import track
from rich import print

from tools.search_command import search

def run(cpu_name: str, path: str="ROM/ROM.txt", debug: bool=True):
    with open(rf"databases/{cpu_name}.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    REGISTER: list[int] = [0]*(data["meta"]["register"] + 1)
    
    count = 0
    rows: list = []
    
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            count += 1
            my_list: list[Any] = line.strip().split()
            my_list[1:] = [int(x, 2) for x in my_list[1:]]
            rows.append(my_list)
    
    for PC in track(range(count)):
        ROM: dict = rows[PC]
        EXAMPLE = data["meta"]["example"]
        
        n = EXAMPLE.index("command")
        name: str = data[ROM[n]][n]
        
        name, command = search(name)
        
        if command is None:
            if name == "無条件ジャンプ":
                PC = ROM[data["meta"]["jump_n"]] - 1
            
            continue
        else:
            allowed = {k: REGISTER[ROM[EXAMPLE.index(f"input{i}")]] for i, k in enumerate(["a", "b"], 1)}
            result = eval(command, {}, allowed)
            
            max = 2**data["meta"]["ALU_size"]
            
            if result >= max:
                result %= max
            elif result < 0:
                result = max + result
        
        n = ROM[EXAMPLE.index("output")]
        REGISTER[n] = result
        
        if debug:
            print(f"[bold green]PC: {PC}[/bold green] [bold blue]命令: {name}[/bold blue] [bold yellow]出力: {result}[/bold yellow]")
            print(f"[bold cyan]レジスタの状況: {[format(i, f"0{data["meta"]["bit"]}b") for i in REGISTER]}[/bold cyan]")
    
    if debug:
        print(f"[bold magenta]最終的なレジスタの状況: {[format(i, f"0{data["meta"]["bit"]}b") for i in REGISTER]}[/bold magenta]")