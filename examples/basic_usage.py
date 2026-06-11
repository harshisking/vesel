from vesel.io import VeselIO
from vesel.models import Header,Version,VeselFile

file = VeselFile(
    header=Header(
        version=Version(0,2,0)
        ),
    payload=b"The First Vesel!"
)

VeselIO.write("examples/the-first.vesel",file)
print("Write Successful")

loaded = VeselIO.read("examples/the-first.vesel")
print("Read and Load Successful\n")

print(loaded.payload.decode("utf-8"))