def hi(name:str = world) -> str:
    return f"hello, {name}"

if __name__ == "__main__":
    import sys 
    hi(sys.argv[1])
