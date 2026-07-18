from tools.file_manager import create_file

def initialize():
    create_file("ROM/ROM.txt")
    create_file("databases/CPU.json")
    create_file("commands.yml")
    
    with open("commands.yml", "w", encoding="utf-8") as f:
        f.write("""
                commands:
                    インクリメント: a + 1
                    デクリメント: a - b
                    無条件ジャンプ: null
                """)