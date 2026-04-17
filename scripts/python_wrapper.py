import subprocess

def run_snap(graph, input_file, output_file):
    cmd = f"gpt {graph} -Pinput={input_file} -Poutput={output_file}"
    subprocess.run(cmd, shell=True)

run_snap("insar_graph.xml", "master.dim", "output.dim")
