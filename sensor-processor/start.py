import click
from script import SensorProcessor


@click.command()
@click.option("--ping", "ping", is_flag=True, default=False)
@click.option("--path", help="path to be provided as an input")
@click.option("--txt", is_flag=True, help="text input to be provided")
@click.argument("text", required=False)
def start(path, txt, text, ping):
    if path:
        sp = SensorProcessor(file_inp=path)
        outliers = sp.execute()
    if txt:
        text_inp = click.edit(text if text else "Enter your text here...")
        sp = SensorProcessor(text_inp=text_inp)
        outliers = sp.execute()
    if ping:
        print("pong")
    

if __name__ == "__main__":
    start()


# inp = """
# 2 9
# 45 46 47 48 52 60
# S1 34 45 18 20 35 40 50 65 75
# S2 87 89 80 78 90 38 32 45 58
# """
# from pdb import set_trace as bp
#
# sp = SensorProcessor(file_inp="data.txt")
# # bp()
# outliers = sp.execute()
# # print(outliers)
# # a = [[3, 3, 3, 3, 2, 2], [6, 6, 6, 6, 6, 5]]
# # print(a)
# # print(a == outliers)