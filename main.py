from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

def main():
    writer(vesel_path("the-first.vesel"),"THE FIRST VESEL IS MADE!")

    data = reader(vesel_path("the-first.vesel"))
    print(data)

def reader(filepath):
    try:
        with open(filepath, "rb") as f:
            magic = f.read(5)
            if magic != b"VESEL":
                raise ValueError("Not a vesel file.")
            
            version = f.read(1)[0]
            if version != 1:
                raise ValueError(
                    f"Unsupported Version: {version}"
                    )
            
            data = (f.read()).decode("utf-8")
        return {'VERSION':version, 'DATA':data}
    except Exception as e:
        print("ERR0R:",e)
        

def writer(filepath,s):
    try:
        with open(filepath, "wb") as f:
            f.write(b"VESEL")
            f.write(bytes([1]))
            f.write(s.encode("utf-8"))
        print("Write Success")
    except Exception as e:
        print("ERR0R:",e)

def vesel_path(filename):
    return f"{DATA_DIR}/{filename}"
    




if __name__=="__main__":
    main()